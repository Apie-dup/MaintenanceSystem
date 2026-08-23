from app.database.connection import Database
from app.database.schema import DatabaseSchema
from app.database.seed import DatabaseSeeder
from app.database.migrations import MigrationManager
from app.core.logger import logger
from app.core.version import APP_NAME

class DatabaseSetup:

    @staticmethod
    def initialize():

        logger.info("%s", "=" * 50)
        logger.info(APP_NAME)
        logger.info("Database Initializer")
        logger.info("%s", "=" * 50)

        # Create database file if necessary
        Database.connect().close()

        # Create tables
        DatabaseSchema.create_tables()

        # Run Migration
        MigrationManager.run()

        # Seed default data
        DatabaseSeeder.seed()

        logger.info("Database initialized successfully.")

    @staticmethod
    def rebuild():

        logger.info("%s", "=" * 50)
        logger.info("Rebuild Database")
        logger.info("%s", "=" * 50)

        DatabaseSeeder.rebuild_database()

        logger.info("Database rebuild complete.")