from PySide6.QtWidgets import QMessageBox


class Validator:

    @staticmethod
    def required(parent, value, field):

        if not value.strip():

            QMessageBox.warning(
                parent,
                "Validation",
                f"{field} is required."
            )

            return False

        return True