from database import Database


class DashboardService:

    @staticmethod
    def get_statistics():

        conn = Database.connect()
        cursor = conn.cursor()

        stats = {
            "assets": 0,
            "work_orders": 0,
            "pm_due": 0,
            "low_stock": 0,
        }

        # Assets
        try:
            cursor.execute("SELECT COUNT(*) FROM assets")
            stats["assets"] = cursor.fetchone()[0]
        except Exception:
            pass

        # Open Work Orders
        try:
            cursor.execute("""
                SELECT COUNT(*)
                FROM work_orders
                WHERE status='Open'
            """)
            stats["work_orders"] = cursor.fetchone()[0]
        except Exception:
            pass

        # PM Due
        try:
            cursor.execute("""
                SELECT COUNT(*)
                FROM preventive_maintenance
            """)
            stats["pm_due"] = cursor.fetchone()[0]
        except Exception:
            pass

        # Low Stock
        try:
            cursor.execute("""
                SELECT COUNT(*)
                FROM inventory
                WHERE quantity <= minimum_quantity
            """)
            stats["low_stock"] = cursor.fetchone()[0]
        except Exception:
            pass

        conn.close()

        return stats