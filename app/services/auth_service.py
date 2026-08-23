import bcrypt

from app.models.user_model import UserModel


class AuthService:

    @staticmethod
    def login(username, password):

        user = UserModel.get_by_username(
            username
        )

        if user is None:
            return None

        if not user["active"]:
            return None

        password_hash = (
            user["password_hash"]
        )

        if bcrypt.checkpw(
            password.encode(),
            password_hash.encode()
        ):

            return {
                "id": user["id"],
                "username": user["username"],
                "fullname": user["fullname"],
                "role": user["role"],
            }

        return None