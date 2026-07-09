from app.database.connection import Database


class MigrationManager:

    @staticmethod
    def get_database_version():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT value
            FROM app_settings
            WHERE key='database_version'
        """)

        row = cursor.fetchone()

        conn.close()

        if row:
            return int(row[0])

        return 1

    @staticmethod
    def set_database_version(version):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE app_settings
            SET value=?
            WHERE key='database_version'
        """, (str(version),))

        conn.commit()
        conn.close()

    @staticmethod
    def run():

        version = MigrationManager.get_database_version()

        print("=" * 50)
        print("Database Migration Manager")
        print(f"Current Database Version : {version}")
        print("=" * 50)

        # Future migrations go here

        print("Database is up to date.")
