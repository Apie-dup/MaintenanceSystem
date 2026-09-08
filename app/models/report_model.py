from app.database.connection import Database


class ReportModel:

    @staticmethod
    def get_work_orders(
        from_date=None,
        to_date=None,
        status=None,
        asset_number=None,
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        query = """
            SELECT
                work_orders.id,
                work_orders.work_order_number,
                assets.asset_number,
                assets.asset_name,

                CASE
                    WHEN technicians.id IS NULL
                        THEN 'Unassigned'
                    ELSE
                        technicians.employee_number
                        || ' - '
                        || technicians.first_name
                        || ' '
                        || technicians.last_name
                END AS technician_display,

                work_orders.priority,
                work_orders.status,
                work_orders.date_created,
                work_orders.due_date,
                work_orders.completed_date,
                work_orders.labour_hours,
                work_orders.estimated_cost,
                work_orders.actual_cost

            FROM work_orders

            LEFT JOIN assets
                ON work_orders.asset_id = assets.id

            LEFT JOIN technicians
                ON work_orders.technician_id
                = technicians.id

            WHERE 1 = 1
        """

        parameters = []

        if from_date:
            query += """
                AND work_orders.date_created >= ?
            """
            parameters.append(from_date)

        if to_date:
            query += """
                AND work_orders.date_created <= ?
            """
            parameters.append(to_date)

        if status:
            query += """
                AND work_orders.status = ?
            """
            parameters.append(status)

        if asset_number:
            query += """
                AND assets.asset_number = ?
            """
            parameters.append(asset_number)

        query += """
            ORDER BY
                work_orders.date_created DESC,
                work_orders.id DESC
        """

        cursor.execute(
            query,
            parameters
        )

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def get_maintenance_costs(
        from_date=None,
        to_date=None,
        status=None,
        asset_number=None,
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        query = """
            SELECT
                assets.id AS id,
                assets.asset_number AS asset_number,
                assets.asset_name AS asset_name,

                COUNT(work_orders.id)
                    AS work_order_count,

                COALESCE(
                    SUM(work_orders.labour_hours),
                    0
                ) AS labour_hours,

                COALESCE(
                    SUM(
                        COALESCE(work_orders.labour_hours, 0)
                        *
                        COALESCE(technicians.hourly_rate, 0)
                    ),
                    0
                ) AS labour_cost,

                COALESCE(
                    SUM(
                        COALESCE(parts.material_cost, 0)
                    ),
                    0
                ) AS material_cost,

                COALESCE(
                    SUM(
                        (
                            COALESCE(work_orders.labour_hours, 0)
                            *
                            COALESCE(technicians.hourly_rate, 0)
                        )
                        +
                        COALESCE(parts.material_cost, 0)
                    ),
                    0
                ) AS total_cost

            FROM work_orders

            INNER JOIN assets
                ON work_orders.asset_id = assets.id

            LEFT JOIN technicians
                ON work_orders.technician_id = technicians.id

            LEFT JOIN (
                SELECT
                    work_order_id,
                    SUM(total_cost) AS material_cost
                FROM work_order_parts
                GROUP BY work_order_id
            ) AS parts
                ON parts.work_order_id = work_orders.id

            WHERE 1 = 1
        """

        parameters = []

        if from_date:
            query += """
                AND work_orders.date_created >= ?
            """
            parameters.append(from_date)

        if to_date:
            query += """
                AND work_orders.date_created <= ?
            """
            parameters.append(to_date)

        if status:
            query += """
                AND work_orders.status = ?
            """
            parameters.append(status)

        if asset_number:
            query += """
                AND assets.asset_number = ?
            """
            parameters.append(asset_number)

        query += """
            GROUP BY
                assets.id,
                assets.asset_number,
                assets.asset_name

            ORDER BY
                total_cost DESC,
                assets.asset_number
        """

        cursor.execute(
            query,
            parameters
        )

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def get_inventory_stock():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                inventory.id AS id,
                inventory.part_number AS part_number,
                inventory.part_name AS part_name,
                inventory.category AS category,

                COALESCE(
                    suppliers.supplier_name,
                    'No Supplier'
                ) AS supplier_name,

                inventory.quantity AS quantity,
                inventory.minimum_quantity AS minimum_quantity,
                inventory.reorder_quantity AS reorder_quantity,
                inventory.unit_cost AS unit_cost,

                (
                    COALESCE(inventory.quantity, 0)
                    *
                    COALESCE(inventory.unit_cost, 0)
                ) AS stock_value,

                inventory.location AS location,
                inventory.status AS status,

                CASE
                    WHEN inventory.quantity
                         <= inventory.minimum_quantity
                        THEN 'Low Stock'
                    ELSE 'OK'
                END AS stock_level

            FROM inventory

            LEFT JOIN suppliers
                ON inventory.supplier_id = suppliers.id

            ORDER BY
                CASE
                    WHEN inventory.quantity
                         <= inventory.minimum_quantity
                        THEN 0
                    ELSE 1
                END,
                inventory.part_number
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def get_preventive_maintenance():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                preventive_maintenance.id AS id,
                preventive_maintenance.pm_number AS pm_number,

                assets.asset_number AS asset_number,
                assets.asset_name AS asset_name,

                preventive_maintenance.task AS task,

                preventive_maintenance.frequency_type
                    AS frequency_type,

                preventive_maintenance.frequency_value
                    AS frequency_value,

                preventive_maintenance.last_service_date
                    AS last_service_date,

                preventive_maintenance.next_due_date
                    AS next_due_date,

                preventive_maintenance.priority
                    AS priority,

                CASE
                    WHEN preventive_maintenance.active = 0
                        THEN 'Inactive'

                    WHEN preventive_maintenance.next_due_date
                         < DATE('now')
                        THEN 'Overdue'

                    WHEN preventive_maintenance.next_due_date
                         = DATE('now')
                        THEN 'Due Today'

                    WHEN preventive_maintenance.next_due_date
                         <= DATE('now', '+7 days')
                        THEN 'Due Soon'

                    ELSE 'Scheduled'
                END AS due_status

            FROM preventive_maintenance

            INNER JOIN assets
                ON preventive_maintenance.asset_id
                = assets.id

            ORDER BY
                preventive_maintenance.next_due_date,
                preventive_maintenance.pm_number
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def get_technician_performance(
        from_date=None,
        to_date=None
    ):

        conn = Database.connect()
        cursor = conn.cursor()

        query = """
            SELECT
                technicians.id AS id,

                technicians.employee_number
                    AS employee_number,

                (
                    technicians.first_name
                    || ' '
                    || technicians.last_name
                ) AS technician_name,

                technicians.trade AS trade,

                COUNT(work_orders.id)
                    AS work_order_count,

                SUM(
                    CASE
                        WHEN work_orders.status
                            IN ('Completed', 'Closed')
                        THEN 1
                        ELSE 0
                    END
                ) AS completed_count,

                CASE
                    WHEN COUNT(work_orders.id) = 0
                        THEN 0
                    ELSE
                        (
                            SUM(
                                CASE
                                    WHEN work_orders.status
                                        IN ('Completed', 'Closed')
                                    THEN 1
                                    ELSE 0
                                END
                            )
                            * 100.0
                            / COUNT(work_orders.id)
                        )
                END AS completion_rate,

                COALESCE(
                    SUM(work_orders.labour_hours),
                    0
                ) AS labour_hours,

                COALESCE(
                    SUM(
                        COALESCE(work_orders.labour_hours, 0)
                        *
                        COALESCE(technicians.hourly_rate, 0)
                    ),
                    0
                ) AS labour_cost

            FROM technicians

            LEFT JOIN work_orders
                ON work_orders.technician_id
                = technicians.id
        """

        parameters = []

        date_conditions = []

        if from_date:
            date_conditions.append(
                "work_orders.date_created >= ?"
            )
            parameters.append(from_date)

        if to_date:
            date_conditions.append(
                "work_orders.date_created <= ?"
            )
            parameters.append(to_date)

        if date_conditions:
            query += """
                AND
            """ + " AND ".join(
                date_conditions
            )

        query += """
            GROUP BY
                technicians.id,
                technicians.employee_number,
                technicians.first_name,
                technicians.last_name,
                technicians.trade,
                technicians.hourly_rate

            ORDER BY
                completed_count DESC,
                labour_hours DESC,
                technician_name
        """

        cursor.execute(
            query,
            parameters
        )

        rows = cursor.fetchall()

        conn.close()

        return rows