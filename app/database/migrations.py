from app.database.connection import Database
from app.core.logger import logger


class MigrationManager:

    LATEST_VERSION = 14

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

            elif version == 4:
                MigrationManager.migrate_to_v5()
                version = 5

            elif version == 5:
                MigrationManager.migrate_to_v6()
                version = 6

            elif version == 6:
                MigrationManager.migrate_to_v7()
                version = 7

            elif version == 7:
                MigrationManager.migrate_to_v8()
                version = 8

            elif version == 8:
                MigrationManager.migrate_to_v9()
                version = 9

            elif version == 9:
                MigrationManager.migrate_to_v10()
                version = 10

            elif version == 10:
                MigrationManager.migrate_to_v11()
                version = 11

            elif version == 11:
                MigrationManager.migrate_to_v12()
                version = 12

            elif version == 12:
                MigrationManager.migrate_to_v13()
                version = 13

            elif version == 13:
                MigrationManager.migrate_to_v14()
                version = 14

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

    # -----------------------------------------------------
    # Version 5
    # Work Order completion tracking
    # -----------------------------------------------------

    @staticmethod
    def migrate_to_v5():

        conn = Database.connect()
        cursor = conn.cursor()

        logger.info(
            "Migrating database to Version 5..."
        )

        cursor.execute(
            "PRAGMA table_info(work_orders)"
        )

        columns = [
            row["name"]
            for row in cursor.fetchall()
        ]

        if "completed_date" not in columns:

            cursor.execute("""
                ALTER TABLE work_orders
                ADD COLUMN completed_date TEXT
            """)

            logger.info(
                "completed_date column added."
            )

        else:

            logger.info(
                "completed_date already exists."
            )

        if "closed_date" not in columns:

            cursor.execute("""
                ALTER TABLE work_orders
                ADD COLUMN closed_date TEXT
            """)

            logger.info(
                "closed_date column added."
            )

        else:

            logger.info(
                "closed_date already exists."
            )

        conn.commit()
        conn.close()

    @staticmethod
    def migrate_to_v6():

        conn = Database.connect()
        cursor = conn.cursor()

        try:
            logger.info(
                "Migrating database to Version 6..."
            )

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS work_order_history
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    work_order_id INTEGER NOT NULL,
                    action TEXT NOT NULL,
                    field_name TEXT,
                    old_value TEXT,
                    new_value TEXT,
                    notes TEXT,
                    created_at TEXT
                        DEFAULT CURRENT_TIMESTAMP,

                    FOREIGN KEY(work_order_id)
                        REFERENCES work_orders(id)
                        ON DELETE CASCADE
                )
            """)

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def migrate_to_v7():

        conn = Database.connect()
        cursor = conn.cursor()

        logger.info(
            "Migrating database to Version 7..."
        )

        cursor.execute(
            "PRAGMA table_info(assets)"
        )

        columns = [
            row["name"]
            for row in cursor.fetchall()
        ]

        if "purchase_cost" not in columns:

            cursor.execute("""
                ALTER TABLE assets
                ADD COLUMN purchase_cost REAL DEFAULT 0
            """)

            logger.info(
                "Added purchase_cost column to assets."
            )

        else:
            logger.info(
                "purchase_cost column already exists in assets."
            )

        conn.commit()
        conn.close()

    # -----------------------------------------------------
    # Version 8
    # Application settings
    # -----------------------------------------------------

    @staticmethod
    def migrate_to_v8():

        conn = Database.connect()
        cursor = conn.cursor()

        try:
            logger.info(
                "Migrating database to Version 8..."
            )

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS app_settings
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    key TEXT NOT NULL UNIQUE,

                    value TEXT,

                    description TEXT,

                    updated_at TEXT
                        DEFAULT CURRENT_TIMESTAMP
                )
            """)

            settings = [
                (
                    "organization_name",
                    "Your Organization",
                    "Organization name used in reports and exports."
                ),
                (
                    "system_name",
                    "Maintenance Management System",
                    "Application/system display name."
                ),
                (
                    "currency_symbol",
                    "N$",
                    "Currency symbol used throughout the system."
                ),
                (
                    "currency_code",
                    "NAD",
                    "ISO currency code."
                ),
                (
                    "date_format",
                    "dd-MMM-yyyy",
                    "Default display date format."
                ),
            ]

            cursor.executemany("""
                INSERT OR IGNORE INTO app_settings
                (
                    key,
                    value,
                    description
                )
                VALUES (?, ?, ?)
            """, settings)

            conn.commit()

            logger.info(
                "Application settings table created and seeded."
            )

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def migrate_to_v9():

        conn = Database.connect()
        cursor = conn.cursor()

        try:
            logger.info(
                "Migrating database to Version 9..."
            )

            cursor.execute("""
                INSERT OR IGNORE INTO app_settings
                (
                    key,
                    value,
                    description
                )
                VALUES (?, ?, ?)
            """, (
                "theme_mode",
                "light",
                "Application theme: light or dark."
            ))

            conn.commit()

            logger.info(
                "Added theme_mode application setting."
            )

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def migrate_to_v10():

        conn = Database.connect()
        cursor = conn.cursor()

        try:
            logger.info(
                "Migrating database to Version 10..."
            )

            #---------------------------------------------
            # user_id
            #---------------------------------------------

            if not MigrationManager.column_exists(
                cursor,
                "work_order_history",
                "user_id"
            ):
                cursor.execute("""
                    ALTER TABLE work_order_history
                    ADD COLUMN user_id INTEGER
                    REFERENCES users(id)
                """)

                logger.info(
                    "Added user_id to work_order_history."
                )

            else:
                logger.info(
                    "work_order_history.user_id "
                    "already exists."
                )

            #--------------------------------------------
            # username
            #---------------------------------------------

            if not MigrationManager.column_exists(
                cursor,
                "work_order_history",
                "username"
            ):
                cursor.execute("""
                    ALTER TABLE work_order_history
                    ADD COLUMN username TEXT
                """)

                logger.info(
                    "Added username to work_order_history."
                )

            #--------------------------------------------
            # Index
            #---------------------------------------------

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS
                    idx_work_order_history_user_id
                ON work_order_history(user_id)
            """)

            conn.commit()

            logger.info(
                "Work Order audit user tracking added."
            )

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def migrate_to_v11():

        conn = Database.connect()
        cursor = conn.cursor()

        try:
            logger.info(
                "Migrating database to Version 11..."
            )

            if not MigrationManager.column_exists(
                cursor,
                "work_orders",
                "estimated_hours"
            ):
                cursor.execute("""
                    ALTER TABLE work_orders
                    ADD COLUMN estimated_hours REAL
                    DEFAULT 0
                """)

                logger.info(
                    "Added estimated_hours to work_orders."
                )

            else:
                logger.info(
                    "work_orders.estimated_hours "
                    "already exists."
                )

            conn.commit()

            logger.info(
                "Work Order estimated labour tracking added."
            )

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def migrate_to_v12():

        conn = Database.connect()
        cursor = conn.cursor()

        try:
            logger.info(
                "Migrating database to Version 12..."
            )

            # ---------------------------------------------
            # meter_type
            # ---------------------------------------------

            if not MigrationManager.column_exists(
                cursor,
                "preventive_maintenance",
                "meter_type"
            ):
                cursor.execute("""
                    ALTER TABLE preventive_maintenance
                    ADD COLUMN meter_type TEXT
                """)

                logger.info(
                    "Added meter_type to preventive_maintenance."
                )

            # ---------------------------------------------
            # last_service_meter
            # ---------------------------------------------

            if not MigrationManager.column_exists(
                cursor,
                "preventive_maintenance",
                "last_service_meter"
            ):
                cursor.execute("""
                    ALTER TABLE preventive_maintenance
                    ADD COLUMN last_service_meter REAL
                """)

                logger.info(
                    "Added last_service_meter "
                    "to preventive_maintenance."
                )

            # ---------------------------------------------
            # next_due_meter
            # ---------------------------------------------

            if not MigrationManager.column_exists(
                cursor,
                "preventive_maintenance",
                "next_due_meter"
            ):
                cursor.execute("""
                    ALTER TABLE preventive_maintenance
                    ADD COLUMN next_due_meter REAL
                """)

                logger.info(
                    "Added next_due_meter "
                    "to preventive_maintenance."
                )

            conn.commit()

            logger.info(
                "Preventive Maintenance meter tracking added."
            )

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def migrate_to_v13():

        conn = Database.connect()
        cursor = conn.cursor()

        try:
            logger.info(
                "Migrating database to Version 13..."
            )

        # -------------------------------------------------
        # Asset meter readings
        # -------------------------------------------------

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS asset_meter_readings
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    asset_id INTEGER NOT NULL,

                    meter_type TEXT NOT NULL,

                    reading REAL NOT NULL,

                    reading_date TEXT NOT NULL,

                    notes TEXT,

                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,

                    FOREIGN KEY (asset_id)
                        REFERENCES assets(id)
                        ON DELETE CASCADE
                )
            """)

            logger.info(
                "Created asset_meter_readings table."
            )

        # -------------------------------------------------
        # Asset index
        # -------------------------------------------------

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS
                    idx_asset_meter_readings_asset_id
                ON asset_meter_readings(asset_id)
            """)

        # -------------------------------------------------
        # Asset + meter type index
        # -------------------------------------------------

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS
                    idx_asset_meter_readings_asset_meter
                ON asset_meter_readings(
                    asset_id,
                    meter_type
                )
            """)

            conn.commit()

            logger.info(
                "Asset meter reading tracking added."
            )

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def migrate_to_v14():

        conn = Database.connect()
        cursor = conn.cursor()

        try:
            logger.info(
                "Migrating database to Version 14..."
            )

            if not MigrationManager.column_exists(
                cursor,
                "work_orders",
                "meter_reading"
            ):
                cursor.execute("""
                    ALTER TABLE work_orders
                    ADD COLUMN meter_reading REAL
                """)

                logger.info(
                    "Added meter_reading to work_orders."
            )

            else:
                logger.info(
                    "work_orders.meter_reading "
                    "already exists."
                )

            conn.commit()

            logger.info(
                "Work Order meter reading tracking added."
            )

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()