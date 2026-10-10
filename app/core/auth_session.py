from app.models.user_model import UserModel
from app.core.permissions import Permissions


class AuthSession:

    _user_id = None

    @classmethod
    def start(cls, user):
        """
        Start a session using the user returned
        by successful authentication.
        """
        if not isinstance(user, dict):
            raise ValueError(
                "Invalid authenticated user."
            )

        user_id = user.get("id")

        if not isinstance(user_id, int) or isinstance(user_id, bool):
            raise ValueError(
                "Invalid authenticated user ID."
            )

        record = UserModel.get_by_id(user_id)

        if record is None or not record["active"]:
            raise PermissionError(
                "User account is not active."
            )

        cls._user_id = user_id

    @classmethod
    def current_user(cls):
        """
        Retrieve the current user from the database.
        """
        if cls._user_id is None:
            return None

        user = UserModel.get_by_id(cls._user_id)

        if user is None or not user["active"]:
            return None

        return {
            "id": user["id"],
            "username": user["username"],
            "fullname": user["fullname"],
            "role": user["role"],
        }

    @classmethod
    def has_permission(cls, permission):
        """
        Check the current user's database role.
        """
        user = cls.current_user()

        if user is None:
            return False

        return Permissions.has_permission(
            user["role"],
            permission,
        )

    @classmethod
    def require_permission(cls, permission):
        """
        Raise an error if permission is denied.
        """
        if not cls.has_permission(permission):
            raise PermissionError(
                "You do not have permission "
                "to perform this operation."
            )

    @classmethod
    def clear(cls):
        """
        End the current session.
        """
        cls._user_id = None