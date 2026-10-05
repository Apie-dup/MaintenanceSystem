from app.database.connection import Database


class VehicleSopInspectionModel:

    # ---------------------------------------------------------
    # Get all
    # ---------------------------------------------------------

    @staticmethod
    def get_all():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                vehicle_sop_inspections.*,
                assets.asset_number,
                assets.asset_name
            FROM vehicle_sop_inspections
            LEFT JOIN assets
                ON vehicle_sop_inspections.asset_id = assets.id
            ORDER BY
                vehicle_sop_inspections.inspection_date DESC,
                vehicle_sop_inspections.inspection_number DESC
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    # ---------------------------------------------------------
    # Get by ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(inspection_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                vehicle_sop_inspections.*,
                assets.asset_number,
                assets.asset_name
            FROM vehicle_sop_inspections
            LEFT JOIN assets
                ON vehicle_sop_inspections.asset_id = assets.id
            WHERE vehicle_sop_inspections.id = ?
        """, (inspection_id,))

        row = cursor.fetchone()
        conn.close()

        return row

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    @staticmethod
    def search(text):

        conn = Database.connect()
        cursor = conn.cursor()

        search_text = f"%{text}%"

        cursor.execute("""
            SELECT
                vehicle_sop_inspections.*,
                assets.asset_number,
                assets.asset_name
            FROM vehicle_sop_inspections
            LEFT JOIN assets
                ON vehicle_sop_inspections.asset_id = assets.id
            WHERE
                vehicle_sop_inspections.inspection_number LIKE ?
                OR vehicle_sop_inspections.sop_number LIKE ?
                OR vehicle_sop_inspections.sop_name LIKE ?
                OR vehicle_sop_inspections.frequency LIKE ?
                OR vehicle_sop_inspections.inspection_date LIKE ?
                OR vehicle_sop_inspections.operator_name LIKE ?
                OR vehicle_sop_inspections.status LIKE ?
                OR assets.asset_number LIKE ?
                OR assets.asset_name LIKE ?
            ORDER BY
                vehicle_sop_inspections.inspection_date DESC,
                vehicle_sop_inspections.inspection_number DESC
        """, (
            search_text,
            search_text,
            search_text,
            search_text,
            search_text,
            search_text,
            search_text,
            search_text,
            search_text,
        ))

        rows = cursor.fetchall()
        conn.close()

        return rows

    # ---------------------------------------------------------
    # Next inspection number
    # ---------------------------------------------------------

    @staticmethod
    def get_next_inspection_number():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT MAX(
                CAST(
                    SUBSTR(
                        inspection_number,
                        5
                    ) AS INTEGER
                )
            )
            FROM vehicle_sop_inspections
            WHERE inspection_number
                GLOB 'INS-[0-9]*'
        """)

        row = cursor.fetchone()
        conn.close()

        last_number = (
            row[0]
            if row and row[0] is not None
            else 0
        )

        return (
            f"INS-{last_number + 1:06d}"
        )

    # ---------------------------------------------------------
    # Create
    # ---------------------------------------------------------

    @staticmethod
    def create(data):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO vehicle_sop_inspections (
                inspection_number,
                sop_id,
                asset_id,
                sop_number,
                sop_name,
                frequency,
                inspection_date,
                operator_name,
                meter_type,
                meter_reading,
                status,
                comments
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["inspection_number"],
            data["sop_id"],
            data["asset_id"],
            data["sop_number"],
            data["sop_name"],
            data["frequency"],
            data["inspection_date"],
            data.get("operator_name"),
            data.get("meter_type"),
            data.get("meter_reading"),
            data.get(
                "status",
                "In Progress"
            ),
            data.get("comments"),
        ))

        inspection_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return inspection_id

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(data, conn=None):

        owns_connection = conn is None

        if owns_connection:
            conn = Database.connect()

        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE vehicle_sop_inspections
                SET
                    inspection_date = ?,
                    operator_name = ?,
                    meter_type = ?,
                    meter_reading = ?,
                    status = ?,
                    comments = ?
                WHERE id = ?
            """, (
                data["inspection_date"],
                data.get("operator_name"),
                data.get("meter_type"),
                data.get("meter_reading"),
                data["status"],
                data.get("comments"),
                data["id"],
            ))

            if owns_connection:
                conn.commit()

        except Exception:

            if owns_connection:
                conn.rollback()

            raise

        finally:

            if owns_connection:
                conn.close()

    @staticmethod
    def create_with_items(
        inspection_data,
        items   
    ):

        conn = Database.connect()
        cursor = conn.cursor()

        try:

            cursor.execute("""
                INSERT INTO vehicle_sop_inspections (
                    inspection_number,
                    sop_id,
                    asset_id,
                    sop_number,
                    sop_name,
                    frequency,
                    inspection_date,
                    operator_name,
                    meter_type,
                    meter_reading,
                    status,
                    comments
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                inspection_data["inspection_number"],
                inspection_data["sop_id"],
                inspection_data["asset_id"],
                inspection_data["sop_number"],
                inspection_data["sop_name"],
                inspection_data["frequency"],
                inspection_data["inspection_date"],
                inspection_data.get("operator_name"),
                inspection_data.get("meter_type"),
                inspection_data.get("meter_reading"),
                inspection_data.get(
                    "status",
                    "In Progress"
                ),
                inspection_data.get("comments"),
            ))

            inspection_id = cursor.lastrowid

            for item in items:

                cursor.execute("""
                    INSERT INTO vehicle_sop_inspection_items (
                        inspection_id,
                        sop_item_id,
                        sequence,
                        check_description,
                        required,
                        result,
                        comments
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    inspection_id,
                    item.get("sop_item_id"),
                    item["sequence"],
                    item["check_description"],
                    item.get("required", 1),
                    item.get("result"),
                    item.get("comments"),
                ))

            conn.commit()

            return inspection_id

        except Exception:

            conn.rollback()
            raise

        finally:

            conn.close()

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    @staticmethod
    def delete(inspection_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM vehicle_sop_inspections
            WHERE id = ?
        """, (inspection_id,))

        conn.commit()
        conn.close()