from app.database.connection import Database


class AssetHistoryModel:

    @staticmethod
    def get_history(asset_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                event_date,
                event_type,
                reference,
                description,
                status,
                meter,
                source_type,
                source_id

            FROM
            (
                -- -----------------------------------------
                -- Work Orders
                -- -----------------------------------------

                SELECT
                    work_orders.date_created
                        AS event_date,

                    'Work Order'
                        AS event_type,

                    work_orders.work_order_number
                        AS reference,

                    work_orders.title
                        AS description,

                    work_orders.status
                        AS status,

                    NULL
                        AS meter,

                    'work_order'
                        AS source_type,

                    work_orders.id
                        AS source_id

                FROM work_orders

                WHERE work_orders.asset_id = ?

                UNION ALL

                -- -----------------------------------------
                -- Completed Preventive Maintenance
                -- -----------------------------------------

                SELECT
                    pm_service_history.service_date
                        As event_date,

                    'Preventive Maintenance'
                        AS event_type,

                    preventive_maintenance.pm_number
                        || ' / ' ||
                        COALESCE(
                            work_orders.work_order_number,
                            ''
                        )
                        AS reference,

                    preventive_maintenance.task
                        AS description,

                    'Completed'
                        AS status,

                    pm_service_history.meter_reading
                        AS meter,

                    'work_order'
                        AS source_type,

                    pm_service_history.work_order_id
                        AS source_id

                FROM pm_service_history

                INNER JOIN preventive_maintenance
                    ON pm_service_history.pm_id
                        = preventive_maintenance.id

                LEFT JOIN work_orders
                    ON pm_service_history.work_order_id
                        = work_orders.id

                WHERE pm_service_history.asset_id = ?

                UNION ALL

                -- -----------------------------------------
                -- Vehicle Logbook
                -- -----------------------------------------

                SELECT
                    vehicle_logbook.log_date
                        AS event_date,

                    'Vehicle Logbook'
                        AS event_type,

                    'LOG-' || vehicle_logbook.id
                        AS reference,

                    CASE
                        WHEN TRIM(
                            COALESCE(
                                vehicle_logbook.defect_reported,
                                ''
                            )
                        ) <> ''
                        THEN vehicle_logbook.defect_reported

                        ELSE
                            COALESCE(
                                vehicle_logbook.purpose,
                                'Vehicle logbook entry'
                            )
                    END
                        AS description,

                    CASE
                        WHEN vehicle_logbook.work_order_id IS NOT NULL
                        THEN 'Work Order Linked'
                        ELSE ''
                    END
                        AS status,

                    vehicle_logbook.end_meter
                        AS meter,

                    'vehicle_logbook'
                        AS source_type,

                    vehicle_logbook.id
                        AS source_id

                FROM vehicle_logbook

                WHERE vehicle_logbook.asset_id = ?

                UNION ALL

                -- -----------------------------------------
                -- Meter Readings
                -- -----------------------------------------

                SELECT
                    asset_meter_readings.reading_date
                        AS event_date,

                    'Meter Reading'
                        AS event_type,

                    asset_meter_readings.source_type
                        AS reference,

                    asset_meter_readings.meter_type
                        AS description,

                    ''
                        AS status,

                    asset_meter_readings.reading
                        AS meter,

                    'meter_reading'
                        AS source_type,

                    asset_meter_readings.id
                        AS source_id

                FROM asset_meter_readings

                WHERE asset_meter_readings.asset_id = ?
            )

            ORDER BY
                event_date DESC,
                event_type
        """, (
            asset_id,
            asset_id,
            asset_id,
            asset_id,
        ))

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def get_summary(asset_id):

        conn = Database.connect()
        cursor = conn.cursor()

        try:

            # -------------------------------------------------
            # Completed maintenance
            # -------------------------------------------------

            cursor.execute("""
                SELECT
                    COUNT(*) AS work_order_count,

                    COALESCE(
                        SUM(actual_cost),
                        0
                    ) AS maintenance_cost,

                    MAX(completed_date)
                        AS last_maintenance_date

                FROM work_orders

                WHERE asset_id = ?
                  AND status IN (
                      'Completed',
                      'Closed'
                  )
            """, (
                asset_id,
            ))

            work_order_row = cursor.fetchone()

            # -------------------------------------------------
            # Labour hours and cost
            #
            # Use detailed labour entries where available.
            # Otherwise fall back to the legacy Work Order
            # labour_hours and technician hourly rate.
            # -------------------------------------------------

            cursor.execute("""
                SELECT
                    COALESCE(
                        SUM(
                            CASE

                                WHEN EXISTS (
                                    SELECT 1
                                    FROM work_order_labour
                                    WHERE work_order_labour.work_order_id
                                        = work_orders.id
                                )
                                THEN (
                                    SELECT COALESCE(
                                        SUM(work_order_labour.hours),
                                        0
                                    )
                                    FROM work_order_labour
                                    WHERE work_order_labour.work_order_id
                                        = work_orders.id
                                )

                                ELSE
                                    COALESCE(
                                        work_orders.labour_hours,
                                        0
                                    )

                            END
                        ),
                        0
                    ) AS labour_hours,

                    COALESCE(
                        SUM(
                            CASE

                                WHEN EXISTS (
                                    SELECT 1
                                    FROM work_order_labour
                                    WHERE work_order_labour.work_order_id
                                        = work_orders.id
                                )
                                THEN (
                                    SELECT COALESCE(
                                        SUM(work_order_labour.labour_cost),
                                        0
                                    )
                                    FROM work_order_labour
                                    WHERE work_order_labour.work_order_id
                                        = work_orders.id
                                )

                                ELSE
                                    COALESCE(
                                        work_orders.labour_hours,
                                        0
                                    )
                                    *
                                    COALESCE(
                                        technicians.hourly_rate,
                                        0
                                    )

                            END
                        ),
                        0
                    ) AS labour_cost

                FROM work_orders

                LEFT JOIN technicians
                    ON work_orders.technician_id
                        = technicians.id

                WHERE work_orders.asset_id = ?
                  AND work_orders.status IN (
                      'Completed',
                      'Closed'
                  )
            """, (
                asset_id,
            ))

            labour_row = cursor.fetchone()

            # -------------------------------------------------
            # Detailed parts cost
            # -------------------------------------------------

            cursor.execute("""
                SELECT
                    COALESCE(
                        SUM(work_order_parts.total_cost),
                        0
                    ) AS parts_cost

                FROM work_order_parts

                INNER JOIN work_orders
                    ON work_order_parts.work_order_id
                        = work_orders.id

                WHERE work_orders.asset_id = ?
                  AND work_orders.status IN (
                      'Completed',
                      'Closed'
                  )
            """, (
                asset_id,
            ))

            parts_row = cursor.fetchone()

            # -------------------------------------------------
            # Open Work Orders
            # -------------------------------------------------

            cursor.execute("""
                SELECT
                    COUNT(*) AS open_work_order_count

                FROM work_orders

                WHERE asset_id = ?
                  AND status NOT IN (
                      'Completed',
                      'Closed',
                      'Cancelled'
                  )
            """, (
                asset_id,
            ))

            open_row = cursor.fetchone()

            return {
                "work_order_count": int(
                    work_order_row[
                        "work_order_count"
                    ] or 0
                ),

                "open_work_order_count": int(
                    open_row[
                        "open_work_order_count"
                    ] or 0
                ),

                "labour_hours": float(
                    labour_row[
                        "labour_hours"
                    ] or 0
                ),

                "labour_cost": float(
                    labour_row[
                        "labour_cost"
                    ] or 0
                ),

                "parts_cost": float(
                    parts_row[
                        "parts_cost"
                    ] or 0
                ),

                "maintenance_cost": float(
                    work_order_row[
                        "maintenance_cost"
                    ] or 0
                ),

                "last_maintenance_date":
                    work_order_row[
                        "last_maintenance_date"
                    ],
            }

        finally:
            conn.close()