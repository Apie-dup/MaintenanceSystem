from app.database.connection import Database

conn = Database.connect()
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS preventive_maintenance")

conn.commit()
conn.close()

print("preventive_maintenance table dropped successfully.")