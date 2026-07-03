import bcrypt

from app.models.user_model import UserModel


class AuthService:

    @staticmethod
    def login(username, password):

        user = UserModel.get_by_username(username)

        if user is None:
            return None

        (
            user_id,
            username,
            password_hash,
            fullname,
            role,
            active
        ) = user

        if active == 0:
            return None

        if bcrypt.checkpw(
            password.encode(),
            password_hash.encode()
        ):

            return {
                "id": user_id,
                "username": username,
                "fullname": fullname,
                "role": role
            }

        return None