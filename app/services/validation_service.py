import re

from app.services.message_service import MessageService


class ValidationService:

    """
    Central validation service
    """

    @staticmethod
    def required(value, field_name):

        if value is None or str(value).strip() == "":
            return False, f"{field_name} is required"

        return True, ""

    @staticmethod
    def max_length(value, length, field_name):

        if value is None:
            return True, ""

        if len(str(value)) > length:
            return False, f"{field_name} may not exceed {length} characters."

        return True, ""

    @staticmethod
    def min_length(value, length, field_name):

        if value is None or len(str(value)) < length:
            return False, f"{field_name} must be at least {length} characters."

        return True, ""

    @staticmethod
    def email(email):

        if not email:
            return True, ""

        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        if re.fullmatch(pattern, email):
            return True, ""

        return False, "Invalid email address."
                

        

    @staticmethod
    def phone(phone):

        if not phone:
            return True, ""

        pattern = r"^[0-9+\-() ]+$"

        if re.fullmatch(pattern, phone):
            return True, ""

        return False, "Invalid phone number."

    @staticmethod
    def positive_number(value, field_name):

        try:
            if float(value) >= 0:
                return True, ""
        

        except (TypeError, ValueError):
            pass

        return False, f"{field_name} must be zero or greater." 

    @staticmethod
    def integer(value, field_name):

        try:
            int(value)
            return True, ""
        except (TypeError, ValueError):
            return False, f"{field_name} must be a integer."

    @staticmethod
    def check(parent, result):

        valid, message = result

        if not valid:
            MessageService.warning(parent, "Validation", message)

            return False

        return True