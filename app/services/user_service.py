import bcrypt

from app.models.user_model import UserModel


class UserService:

    ROLES = [
        "Administrator",
        "Maintenance Manager",
        "Technician",
        "Viewer",
    ]

    # -------------------------------------------------
    # Queries
    # -------------------------------------------------

    @staticmethod
    def get_all():
        return UserModel.get_all()

    @staticmethod
    def get_by_id(record_id):
        return UserModel.get_by_id(
            record_id
        )

    @staticmethod
    def username_exists(
        username,
        exclude_id=None
    ):
        return UserModel.username_exists(
            username,
            exclude_id
        )

    # -------------------------------------------------
    # Password
    # -------------------------------------------------

    @staticmethod
    def hash_password(password):

        if not password:
            raise ValueError(
                "Password is required."
            )

        password_hash = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        return password_hash.decode()

    # -------------------------------------------------
    # Create
    # -------------------------------------------------

    @staticmethod
    def create(data):

        username = (
            data["username"]
            .strip()
        )

        fullname = (
            data["fullname"]
            .strip()
        )

        role = data["role"]
        password = data["password"]

        if not username:
            raise ValueError(
                "Username is required."
            )

        if not fullname:
            raise ValueError(
                "Full Name is required."
            )

        if role not in UserService.ROLES:
            raise ValueError(
                "Please select a valid role."
            )

        if UserModel.username_exists(
            username
        ):
            raise ValueError(
                "That username already exists."
            )

        password_hash = (
            UserService.hash_password(
                password
            )
        )

        model_data = {
            "username": username,
            "password_hash": password_hash,
            "fullname": fullname,
            "role": role,
            "active": (
                1
                if data.get("active", True)
                else 0
            ),
        }

        return UserModel.create(
            model_data
        )

    # -------------------------------------------------
    # Update
    # -------------------------------------------------

    @staticmethod
    def update(record_id, data):

        username = (
            data["username"]
            .strip()
        )

        fullname = (
            data["fullname"]
            .strip()
        )

        role = data["role"]

        if not username:
            raise ValueError(
                "Username is required."
            )

        if not fullname:
            raise ValueError(
                "Full Name is required."
            )

        if role not in UserService.ROLES:
            raise ValueError(
                "Please select a valid role."
            )

        if UserModel.username_exists(
            username,
            exclude_id=record_id
        ):
            raise ValueError(
                "That username already exists."
            )

        model_data = {
            "username": username,
            "fullname": fullname,
            "role": role,
            "active": (
                1
                if data.get("active", True)
                else 0
            ),
        }

        UserModel.update(
            record_id,
            model_data
        )

        # A blank password means:
        # keep the existing password.
        password = (
            data.get("password", "")
            .strip()
        )

        if password:

            password_hash = (
                UserService.hash_password(
                    password
                )
            )

            UserModel.update_password(
                record_id,
                password_hash
            )

    @staticmethod
    def set_active(record_id, active):

        user = UserModel.get_by_id(
            record_id
        )

        if user is None:
            raise ValueError(
                "User could not be found."
            )

        # Protect the last active Administrator.
        if (
            not active
            and user["role"] == "Administrator"
            and user["active"]
            and UserModel.count_active_administrators() <= 1
        ):
            raise ValueError(
                "The last active Administrator "
                "cannot be deactivated."
            )

        UserModel.set_active(
            record_id,
            active
        )