import sqlite3

def get_assets():
    conn = sqlite3.connect("database/maintenance.db")
    cursor = conn.cursor()

    query = """
    SELECT id, asset_number, asset_name
    FROM assets;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()
    return rows


# Example usage
assets = get_assets()
for asset in assets:
    print(asset)
