from app.database.connection import Database


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
                active,
                created_at
            FROM users
            WHERE username = ?
        """, (username,))

        row = cursor.fetchone()
        conn.close()

        return row

    @staticmethod
    def get_by_id(record_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                username,
                password_hash,
                fullname,
                role,
                active,
                created_at
            FROM users
            WHERE id = ?
        """, (record_id,))

        row = cursor.fetchone()
        conn.close()

        return row

    @staticmethod
    def get_all():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                username,
                fullname,
                role,
                active,
                created_at
            FROM users
            ORDER BY username
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def username_exists(
        username,
        exclude_id=None
    ):

        conn = Database.connect()
        cursor = conn.cursor()

        if exclude_id is None:
            cursor.execute("""
                SELECT 1
                FROM users
                WHERE username = ?
                LIMIT 1
            """, (username,))
        else:
            cursor.execute("""
                SELECT 1
                FROM users
                WHERE username = ?
                AND id != ?
                LIMIT 1
            """, (
                username,
                exclude_id,
            ))

        row = cursor.fetchone()
        conn.close()

        return row is not None

    @staticmethod
    def create(data):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users
            (
                username,
                password_hash,
                fullname,
                role,
                active
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            data["username"],
            data["password_hash"],
            data["fullname"],
            data["role"],
            data["active"],
        ))

        record_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return record_id

    @staticmethod
    def update(record_id, data):

        existing = UserModel.get_by_id(
            record_id
        )

        if existing is None:
            raise ValueError(
                "User could not be found."
            )

        new_role = data["role"]
        new_active = bool(
            data["active"]
        )

        was_active_administrator = (
            existing["role"] == "Administrator"
            and bool(existing["active"])
        )

        will_be_active_administrator = (
            new_role == "Administrator"
            and new_active
        )

        if (
            was_active_administrator
            and not will_be_active_administrator
            and UserModel.count_active_administrators() <= 1
        ):
            raise ValueError(
                "The last active Administrator "
                "cannot be demoted or deactivated."
            )

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE users
            SET
                username = ?,
                fullname = ?,
                role = ?,
                active = ?
            WHERE id = ?
        """, (
            data["username"],
            data["fullname"],
            data["role"],
            data["active"],
            record_id,
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def update_password(
        record_id,
        password_hash
    ):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE users
            SET password_hash = ?
            WHERE id = ?
        """, (
            password_hash,
            record_id,
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def set_active(
        record_id,
        active
    ):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE users
            SET active = ?
            WHERE id = ?
        """, (
            1 if active else 0,
            record_id,
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def count_active_administrators():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM users
            WHERE role = 'Administrator'
              AND active = 1
        """)

        count = cursor.fetchone()[0]

        conn.close()

        return count