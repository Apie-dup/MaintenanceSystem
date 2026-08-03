from app.database.connection import Database
from app.core.logger import logger


class MigrationManager:

    LATEST_VERSION = 3

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

        logger.info(
            "Database file: %s",
            Database.database_path()
        )

        version = MigrationManager.get_database_version()

        logger.info("%s", "=" * 50)
        logger.info("Database Migration Manager")
        logger.info(
            "Current Database Version : %s",
            version
        )
        logger.info(
            "Latest Database Version  : %s",
            MigrationManager.LATEST_VERSION
        )
        logger.info("%s", "=" * 50)

        while version < MigrationManager.LATEST_VERSION:

            if version == 1:
                MigrationManager.migrate_to_v2()
                version = 2
                MigrationManager.set_database_version(version)

            elif version == 2:
                MigrationManager.migrate_to_v3()
                version = 3
                MigrationManager.set_database_version(version)


        logger.info("Database is up to date.")

    @staticmethod
    def migrate_to_v2():

        conn = Database.connect()
        cursor = conn.cursor()

        logger.info("Migrating database to Version 2...")

        # Check existing columns
        cursor.execute("PRAGMA table_info(inventory)")
        columns = [row["name"] for row in cursor.fetchall()]

        # Only add the column if it doesn't already exist
        if "created_at" not in columns:
            cursor.execute("""
                ALTER TABLE inventory
                ADD COLUMN created_at TEXT DEFAULT CURRENT_TIMESTAMP
            """)

            logger.info("Added created_at column.")

        else:

            logger.info("created_at column already exists.")

        MigrationManager.set_database_version (2)

        conn.commit()
        conn.close()

    @staticmethod
    def migrate_to_v3():
        pass