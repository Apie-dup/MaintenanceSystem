from app.database.connection import Database

class LookupModel:

    TABLES = {
        "Trades": ("trades", "trade_name"),
        "Departments": ("departments", "department_name"),
        "Priorities": ("priorities", "priority_name"),
        "Statuses": ("statuses", "status_name"),

        "Asset Categories": ("asset_categories", "category_name"),
        "Asset Locations": ("asset_locations", "location_name"),
        "Manufacturers": ("manufacturers", "manufacturer_name"),

        "Inventory Categories": ("inventory_categories", "category_name"),
        "Units of Measure": ("units_of_measure", "unit_name")
    }

    @staticmethod
    def get_all(lookup_type):
        table, field = LookupModel.TABLES[lookup_type]

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(f"""
            SELECT
                id,
                {field}
            FROM {table}
            ORDER BY {field}
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows
    
    @staticmethod
    def insert(lookup_type, value):
        table, field = LookupModel.TABLES[lookup_type]

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            f"INSERT INTO {table} ({field}) VALUES (?)",
            (value,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def update(lookup_type, lookup_id, value):
        table, field = LookupModel.TABLES[lookup_type]

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            f"""
            UPDATE {table}
            SET {field} = ?
            WHERE id = ?
            """,
            (value, lookup_id)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def delete(lookup_type, lookup_id):
        table, _ = LookupModel.TABLES[lookup_type]

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            f"DELETE FROM {table} WHERE id = ?",
            (lookup_id,)
        )

        conn.commit()
        conn.close()



      