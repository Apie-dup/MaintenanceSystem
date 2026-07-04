from database import Database


class DashboardService:

    @staticmethod
    def get_statistics():

        conn = Database.connect()
        cursor = conn.cursor()

        stats = {}

        tables = {
            "assets": "assets",
            "work_orders": "work_orders",
            "inventory": "inventory"
        }

        for key, table in tables.items():

            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                stats[key] = cursor.fetchone()[0]

            except Exception:
                stats[key] = 0

        conn.close()

        return stats