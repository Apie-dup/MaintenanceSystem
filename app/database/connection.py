import sqlite3
from pathlib import Path


DATABASE = Path("database") / "maintenance.db"

# Ensure the database folder exists
DATABASE.parent.mkdir(exist_ok=True)


from pathlib import Path
import sqlite3


class Database:
    """
    Central database connection manager.
    """

    DB_FOLDER = Path("database")
    DB_FILE = DB_FOLDER / "maintenance.db"

    @classmethod
    def connect(cls):
        """
        Returns a SQLite connection.
        """

        cls.DB_FOLDER.mkdir(exist_ok=True)

        connection = sqlite3.connect(cls.DB_FILE)

        # Access columns by name if needed
        connection.row_factory = sqlite3.Row

        # Enable Foreign Keys
        connection.execute("PRAGMA foreign_keys = ON;")

        return connection

    @classmethod
    def database_exists(cls):
        return cls.DB_FILE.exists()

    @classmethod
    def database_path(cls):
        return str(cls.DB_FILE.resolve())