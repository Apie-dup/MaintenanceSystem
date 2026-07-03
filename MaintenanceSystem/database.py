import sqlite3
from pathlib import Path

DATABASE = Path("database") / "maintenance.db"


class Database:

    @staticmethod
    def connect():
        return sqlite3.connect(DATABASE)