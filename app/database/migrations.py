from app.database.connection import Database


class MigrationManager:

    LATEST_VERSION = 2

    @staticmethod
    def get_database_version():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT version
            FROM schema_version
            LIMIT 1
        """)

        row = cursor.fetchone()

        conn.close()

        return row[0] if row else 0

    @staticmethod
    def set_database_version(version):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE schema_version
            SET version = ?
        """, (version,))

        conn.commit()
        conn.close()

    @staticmethod
    def run():

        print("Database file:", Database.database_path())

        version = MigrationManager.get_database_version()

        print("=" * 50)
        print("Database Migration Manager")
        print(f"Current Database Version : {version}")
        print(f"Latest Database Version  : {MigrationManager.LATEST_VERSION}")
        print("=" * 50)

        while version < MigrationManager.LATEST_VERSION:

            if version == 1:
                MigrationManager.migrate_to_v2()
                version = 2
                MigrationManager.set_database_version(version)

            elif version == 2:
                MigrationManager.migrate_to_v3()
                version = 3
                MigrationManager.set_database_version(version)


        print("Database is up to date.")

    @staticmethod
    def migrate_to_v2():

        conn = Database.connect()
        cursor = conn.cursor()

        print("Migrating database to Version 2...")

        # Check existing columns
        cursor.execute("PRAGMA table_info(inventory)")
        columns = [row["name"] for row in cursor.fetchall()]

        # Only add the column if it doesn't already exist
        if "created_at" not in columns:
            cursor.execute("""
                ALTER TABLE inventory
                ADD COLUMN created_at TEXT DEFAULT CURRENT_TIMESTAMP
            """)

            print("✓ Added created_at column.")

        else:

            print("✓ created_at column already exists.")

        MigrationManager.set_database_version (2)

        conn.commit()
        conn.close()

    @staticmethod
    def migrate_to_v3():
        pass