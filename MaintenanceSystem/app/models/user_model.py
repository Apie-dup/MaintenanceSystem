from database import Database


class UserModel:

    @staticmethod
    def get_by_username(username):

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                username,
                password_hash,
                fullname,
                role,
                active
            FROM users
            WHERE username = ?
        """, (username,))

        row = cursor.fetchone()

        conn.close()

        return row