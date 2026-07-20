from app.database.connection import Database

conn = Database.connect()
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(inventory)")

for column in cursor.fetchall():
    print(column)

conn.close()
