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
                AND DATE(work_orders.date_created)
                    >= DATE(?)
            """
            parameters.append(from_date)

        if to_date:
            query += """
                AND DATE(work_orders.date_created)
                    <= DATE(?)
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
                    SUM(
                        CASE
                            WHEN labour.entry_count > 0
                            THEN labour.labour_hours
                            ELSE COALESCE(
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
                            WHEN labour.entry_count > 0
                            THEN labour.labour_cost
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
                ) AS labour_cost,

                COALESCE(
                    SUM(
                        COALESCE(
                            parts.material_cost,
                            0
                        )
                    ),
                    0
                ) AS material_cost,

                COALESCE(
                    SUM(
                        CASE
                            WHEN labour.entry_count > 0
                            THEN labour.labour_cost
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
                        +
                        COALESCE(
                            parts.material_cost,
                            0
                        )
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
                    COUNT(id) AS entry_count,
                    SUM(hours) AS labour_hours,
                    SUM(labour_cost) AS labour_cost
                FROM work_order_labour
                GROUP BY work_order_id
            ) AS labour
                ON labour.work_order_id
                = work_orders.id

            LEFT JOIN (
                SELECT
                    work_order_id,
                    SUM(total_cost) AS material_cost
                FROM work_order_parts
                GROUP BY work_order_id
            ) AS parts
                ON parts.work_order_id
                = work_orders.id

            WHERE 1 = 1
        """

        parameters = []

        if from_date:
            query += """
                AND DATE(work_orders.date_created)
                    >= DATE(?)
            """
            parameters.append(from_date)

        if to_date:
            query += """
                AND DATE(work_orders.date_created)
                    <= DATE(?)
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

        try:

            cursor.execute("""
                SELECT
                    preventive_maintenance.id
                        AS id,

                    preventive_maintenance.pm_number
                        AS pm_number,

                    preventive_maintenance.asset_id
                        AS asset_id,

                    assets.asset_number
                        AS asset_number,

                    assets.asset_name
                        AS asset_name,

                    preventive_maintenance.task
                        AS task,

                    preventive_maintenance.frequency_type
                        AS frequency_type,

                    preventive_maintenance.frequency_value
                        AS frequency_value,

                    preventive_maintenance.last_service_date
                        AS last_service_date,

                    preventive_maintenance.next_due_date
                        AS next_due_date,

                    preventive_maintenance.last_service_meter
                        AS last_service_meter,

                    preventive_maintenance.next_due_meter
                        AS next_due_meter,

                    preventive_maintenance.priority
                        AS priority,

                    preventive_maintenance.active
                        AS active

                FROM preventive_maintenance

                INNER JOIN assets
                    ON preventive_maintenance.asset_id
                    = assets.id

                ORDER BY
                    preventive_maintenance.pm_number
            """)

            return cursor.fetchall()

        finally:
            conn.close()

    @staticmethod
    def get_technician_performance(
        from_date=None,
        to_date=None
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        query = """
            WITH detailed_labour AS (
                SELECT
                    work_order_id,
                    technician_id,
                    SUM(hours) AS labour_hours,
                    SUM(labour_cost) AS labour_cost
                FROM work_order_labour
                GROUP BY
                    work_order_id,
                    technician_id
            ),

            work_order_has_labour AS (
                SELECT DISTINCT
                    work_order_id
                FROM work_order_labour
            ),

            technician_work AS (
                -- -----------------------------------------
                -- Detailed labour
                -- -----------------------------------------

                SELECT
                    dl.technician_id,
                    wo.id AS work_order_id,
                    wo.status,
                    dl.labour_hours,
                    dl.labour_cost
                FROM detailed_labour AS dl

                INNER JOIN work_orders AS wo
                    ON wo.id = dl.work_order_id

                WHERE 1 = 1
        """

        parameters = []

        if from_date:
            query += """
                AND DATE(wo.date_created)
                    >= DATE(?)
            """
            parameters.append(from_date)

        if to_date:
            query += """
                AND DATE(wo.date_created)
                    <= DATE(?)
            """
            parameters.append(to_date)

        query += """

                UNION ALL

                -- -----------------------------------------
                -- Legacy labour
                -- Only when no detailed labour exists
                -- -----------------------------------------

                SELECT
                    wo.technician_id,
                    wo.id AS work_order_id,
                    wo.status,

                    COALESCE(
                        wo.labour_hours,
                        0
                    ) AS labour_hours,

                    (
                        COALESCE(
                            wo.labour_hours,
                            0
                        )
                        *
                        COALESCE(
                            t.hourly_rate,
                            0
                        )
                    ) AS labour_cost

                FROM work_orders AS wo

                INNER JOIN technicians AS t
                    ON t.id = wo.technician_id

                LEFT JOIN work_order_has_labour AS whl
                    ON whl.work_order_id = wo.id

                WHERE whl.work_order_id IS NULL
        """

        if from_date:
            query += """
                AND DATE(wo.date_created)
                    >= DATE(?)
            """
            parameters.append(from_date)

        if to_date:
            query += """
                AND DATE(wo.date_created)
                    <= DATE(?)
            """
            parameters.append(to_date)

        query += """
            )

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

                COUNT(
                    technician_work.work_order_id
                ) AS work_order_count,

                COALESCE(
                    SUM(
                        CASE
                            WHEN technician_work.status
                                IN (
                                    'Completed',
                                    'Closed'
                                )
                            THEN 1
                            ELSE 0
                        END
                    ),
                    0
                ) AS completed_count,

                COALESCE(
                    SUM(
                        CASE
                            WHEN technician_work.status
                                NOT IN (
                                    'Completed',
                                    'Closed',
                                    'Cancelled'
                                )
                            THEN 1
                            ELSE 0
                        END
                    ),
                    0
                ) AS open_count,

                CASE
                    WHEN COUNT(
                        technician_work.work_order_id
                    ) = 0
                    THEN 0

                    ELSE
                        (
                            SUM(
                                CASE
                                    WHEN technician_work.status
                                        IN (
                                            'Completed',
                                            'Closed'
                                        )
                                    THEN 1
                                    ELSE 0
                                END
                            )
                            * 100.0
                            /
                            COUNT(
                                technician_work.work_order_id
                            )
                        )
                END AS completion_rate,

                COALESCE(
                    SUM(
                        technician_work.labour_hours
                    ),
                    0
                ) AS labour_hours,

                COALESCE(
                    SUM(
                        technician_work.labour_cost
                    ),
                    0
                ) AS labour_cost

            FROM technicians

            LEFT JOIN technician_work
                ON technician_work.technician_id
                = technicians.id

            GROUP BY
                technicians.id,
                technicians.employee_number,
                technicians.first_name,
                technicians.last_name,
                technicians.trade

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

    @staticmethod
    def get_inventory_transactions(
        from_date,
        to_date
    ):

        conn = Database.connect()
        cursor = conn.cursor()

        try:

            cursor.execute("""
                SELECT
                    inventory_transactions.id,
                    inventory_transactions.created_at,

                    inventory.part_number,
                    inventory.part_name,

                    inventory_transactions.transaction_type,
                    inventory_transactions.quantity_change,
                    inventory_transactions.previous_quantity,
                    inventory_transactions.new_quantity,
                    inventory_transactions.unit_cost,

                    work_orders.work_order_number,

                    inventory_transactions.reference,
                    inventory_transactions.username,
                    inventory_transactions.notes

                FROM inventory_transactions

                LEFT JOIN inventory
                    ON inventory_transactions.inventory_id
                    = inventory.id

                LEFT JOIN work_orders
                    ON inventory_transactions.work_order_id
                    = work_orders.id

                WHERE DATE(
                    inventory_transactions.created_at
                ) BETWEEN ? AND ?

                ORDER BY
                    inventory_transactions.created_at DESC,
                    inventory_transactions.id DESC
            """, (
                from_date,
                to_date,
            ))

            return cursor.fetchall()

        finally:
            conn.close()

    @staticmethod
    def get_low_stock_reorder():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                inventory.id,
                inventory.part_number,
                inventory.part_name,
                inventory.category,

                COALESCE(
                    suppliers.supplier_name,
                    'No Supplier'
                ) AS supplier_name,

                inventory.quantity,
                inventory.minimum_quantity,
                inventory.reorder_quantity,
                inventory.unit_cost,
                inventory.location,
                inventory.status,

                (
                    inventory.reorder_quantity
                    * inventory.unit_cost
                ) AS reorder_cost

            FROM inventory

            LEFT JOIN suppliers
                ON inventory.supplier_id
                = suppliers.id

            WHERE
                inventory.quantity
                <= inventory.minimum_quantity

            ORDER BY
                inventory.quantity ASC,
                inventory.part_number ASC
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def get_asset_maintenance_history(
        from_date=None,
        to_date=None,
        status=None,
        asset_number=None,
    ):

        conn = Database.connect()
        cursor = conn.cursor()

        try:

            query = """
                SELECT
                    work_orders.id,
                    work_orders.work_order_number,

                    assets.asset_number,
                    assets.asset_name,

                    technicians.employee_number,

                    (
                        technicians.first_name
                        || ' '
                        || technicians.last_name
                    ) AS technician_name,

                    work_orders.title,
                    work_orders.priority,
                    work_orders.status,

                    work_orders.date_created,
                    work_orders.due_date,

                    work_orders.completed_date
                        AS completed_date,

                    work_orders.labour_hours,
                    work_orders.estimated_cost,
                    work_orders.actual_cost

                FROM work_orders

                INNER JOIN assets
                    ON work_orders.asset_id
                    = assets.id

                LEFT JOIN technicians
                    ON work_orders.technician_id
                    = technicians.id

                WHERE 1 = 1
            """

            parameters = []

            if from_date:
                query += """
                    AND DATE(work_orders.date_created)
                        >= DATE(?)
                """
                parameters.append(from_date)

            if to_date:
                query += """
                    AND DATE(work_orders.date_created)
                        <= DATE(?)
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

            return cursor.fetchall()

        finally:
            conn.close()

    @staticmethod
    def get_technician_work_history(
        from_date=None,
        to_date=None,
        status=None,
        technician_id=None,
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        try:

            query = """
                WITH detailed_labour AS (
                    SELECT
                        work_order_id,
                        technician_id,
                        SUM(hours) AS labour_hours,
                        SUM(labour_cost) AS labour_cost
                    FROM work_order_labour
                    GROUP BY
                        work_order_id,
                        technician_id
                ),

                work_order_has_labour AS (
                    SELECT DISTINCT
                        work_order_id
                    FROM work_order_labour
                ),

                technician_work AS (

                    -- -------------------------------------
                    -- Detailed labour
                    -- -------------------------------------

                    SELECT
                        dl.technician_id,
                        wo.id AS work_order_id,
                        dl.labour_hours,
                        dl.labour_cost

                    FROM detailed_labour AS dl

                    INNER JOIN work_orders AS wo
                        ON wo.id = dl.work_order_id

                    WHERE 1 = 1

                    UNION ALL

                    -- -------------------------------------
                    -- Legacy labour
                    -- Only when no detailed labour exists
                    -- -------------------------------------

                    SELECT
                        wo.technician_id,
                        wo.id AS work_order_id,

                        COALESCE(
                            wo.labour_hours,
                            0
                        ) AS labour_hours,

                        (
                            COALESCE(
                                wo.labour_hours,
                                0
                            )
                            *
                            COALESCE(
                                t.hourly_rate,
                                0
                            )
                        ) AS labour_cost

                    FROM work_orders AS wo

                    INNER JOIN technicians AS t
                        ON t.id = wo.technician_id

                    LEFT JOIN work_order_has_labour AS whl
                        ON whl.work_order_id = wo.id

                    WHERE whl.work_order_id IS NULL
                )

                SELECT
                    work_orders.id,
                    work_orders.work_order_number,

                    technicians.id
                        AS technician_id,

                    technicians.employee_number,

                    (
                        technicians.first_name
                        || ' '
                        || technicians.last_name
                    ) AS technician_name,

                    technicians.trade,

                    assets.asset_number,
                    assets.asset_name,

                    work_orders.title,
                    work_orders.priority,
                    work_orders.status,

                    work_orders.date_created,
                    work_orders.due_date,
                    work_orders.completed_date,

                    technician_work.labour_hours,

                    technician_work.labour_cost
                        AS actual_cost

                FROM technician_work

                INNER JOIN work_orders
                    ON work_orders.id
                    = technician_work.work_order_id

                INNER JOIN technicians
                    ON technicians.id
                    = technician_work.technician_id

                LEFT JOIN assets
                    ON work_orders.asset_id
                    = assets.id

                WHERE 1 = 1
            """

            parameters = []

            if from_date:
                query += """
                    AND DATE(work_orders.date_created)
                        >= DATE(?)
                """
                parameters.append(from_date)

            if to_date:
                query += """
                    AND DATE(work_orders.date_created)
                        <= DATE(?)
                """
                parameters.append(to_date)

            if status:
                query += """
                    AND work_orders.status = ?
                """
                parameters.append(status)

            if technician_id is not None:
                query += """
                    AND technicians.id = ?
                """
                parameters.append(
                    technician_id
                )

            query += """
                ORDER BY
                    technicians.employee_number,
                    work_orders.date_created DESC,
                    work_orders.id DESC
            """

            cursor.execute(
                query,
                parameters
            )

            return cursor.fetchall()

        finally:
            conn.close()