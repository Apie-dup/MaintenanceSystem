from app.database.connection import Database
from app.database.schema import DatabaseSchema
from app.database.seed import DatabaseSeeder
from app.database.migrations import MigrationManager

class DatabaseSetup:

    @staticmethod
    def initialize():

        print("=" * 50)
        print("Maintenance Management System")
        print("Database Initializer")
        print("=" * 50)

        # Create database file if necessary
        Database.connect().close()

        # Create tables
        DatabaseSchema.create_tables()

        # Run Migration
        MigrationManager.run()

        # Seed default data
        DatabaseSeeder.seed()

        print("Database initialized succssesfully.")

    @staticmethod
    def rebuild():

        print("=" * 50)
        print("Rebuild Database")
        print("=" * 50)

        DatabaseSeeder.rebuild_database()

        print("Database rebuild complete.")