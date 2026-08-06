from app.database.connection import Database
from app.core.logger import logger


class MigrationManager:

    LATEST_VERSION = 4

    # ---------------------------------------------------------
    # Database version
    # ---------------------------------------------------------

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

        return int(row["version"]) if row else 0

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

    # ---------------------------------------------------------
    # Run migrations
    # ---------------------------------------------------------

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

            elif version == 2:
                MigrationManager.migrate_to_v3()
                version = 3

            elif version == 3:
                MigrationManager.migrate_to_v4()
                version = 4

            else:
                raise RuntimeError(
                    f"No migration path exists from version {version}."
                )

            MigrationManager.set_database_version(
                version
            )

        logger.info("Database is up to date.")

    # ---------------------------------------------------------
    # Version 2
    # Add created_at to inventory
    # ---------------------------------------------------------

    @staticmethod
    def migrate_to_v2():
        conn = Database.connect()
        cursor = conn.cursor()

        try:
            logger.info(
                "Migrating database to Version 2..."
            )

            if not MigrationManager.column_exists(
                cursor,
                "inventory",
                "created_at"
            ):
                cursor.execute("""
                    ALTER TABLE inventory
                    ADD COLUMN created_at TEXT
                    DEFAULT CURRENT_TIMESTAMP
                """)

                logger.info(
                    "Added created_at column to inventory."
                )
            else:
                logger.info(
                    "inventory.created_at already exists."
                )

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    # ---------------------------------------------------------
    # Version 3
    # Add pm_id to work_orders
    # ---------------------------------------------------------

    @staticmethod
    def migrate_to_v3():
        conn = Database.connect()
        cursor = conn.cursor()

        try:
            logger.info(
                "Migrating database to Version 3..."
            )

            if not MigrationManager.column_exists(
                cursor,
                "work_orders",
                "pm_id"
            ):
                cursor.execute("""
                    ALTER TABLE work_orders
                    ADD COLUMN pm_id INTEGER
                """)

                logger.info(
                    "Added pm_id column to work_orders."
                )
            else:
                logger.info(
                    "work_orders.pm_id already exists."
                )

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    # ---------------------------------------------------------
    # Version 4
    # Add notes to assets
    # ---------------------------------------------------------

    @staticmethod
    def migrate_to_v4():
        conn = Database.connect()
        cursor = conn.cursor()

        try:
            logger.info(
                "Migrating database to Version 4..."
            )

            if not MigrationManager.column_exists(
                cursor,
                "assets",
                "notes"
            ):
                cursor.execute("""
                    ALTER TABLE assets
                    ADD COLUMN notes TEXT
                """)

                logger.info(
                    "Added notes column to assets."
                )
            else:
                logger.info(
                    "assets.notes already exists."
                )

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    # ---------------------------------------------------------
    # Column check
    # ---------------------------------------------------------

    @staticmethod
    def column_exists(
        cursor,
        table_name,
        column_name
    ):
        cursor.execute(
            f"PRAGMA table_info({table_name})"
        )

        columns = cursor.fetchall()

        return any(
            column["name"] == column_name
            for column in columns
        )