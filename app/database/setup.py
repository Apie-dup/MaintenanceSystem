from app.database.connection import Database
from app.database.schema import DatabaseSchema
from app.database.seed import DatabaseSeeder

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

        # Seed default data
        DatabaseSeeder.seed()

        print("Database initialized succssesfully.")