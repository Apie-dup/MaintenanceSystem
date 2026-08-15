from app.models.technician_model import TechnicianModel


class TechnicianService:

    # ---------------------------------------------------------
    # Read
    # ---------------------------------------------------------

    @staticmethod
    def get_all():
        return TechnicianModel.get_all()

    @staticmethod
    def get_by_id(record_id):
        return TechnicianModel.get_by_id(
            record_id
        )

    @staticmethod
    def search(search_text):
        return TechnicianModel.search(
            search_text
        )

    @staticmethod
    def get_active_technicians():
        return TechnicianModel.get_active_technicians()

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    @staticmethod
    def get_next_employee_number():
        return TechnicianModel.get_next_employee_number()

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    @staticmethod
    def validate(data):

        if not data["employee_number"].strip():
            raise ValueError(
                "Employee Number is required."
            )

        if not data["first_name"].strip():
            raise ValueError(
                "First Name is required."
            )

        if not data["last_name"].strip():
            raise ValueError(
                "Last Name is required."
            )

        if data["hourly_rate"] < 0:
            raise ValueError(
                "Hourly Rate cannot be negative."
            )

    # ---------------------------------------------------------
    # Create
    # ---------------------------------------------------------

    @staticmethod
    def create(data):

        TechnicianService.validate(data)

        if TechnicianModel.employee_number_exists(
            data["employee_number"]
        ):
            raise ValueError(
                "Employee Number already exists."
            )

        return TechnicianModel.insert(data)

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(record_id, data):

        TechnicianService.validate(data)

        if TechnicianModel.employee_number_exists(
            data["employee_number"],
            exclude_id=record_id,
        ):
            raise ValueError(
                "Employee Number already exists."
            )

        TechnicianModel.update(
            record_id,
            data
        )

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    @staticmethod
    def delete(record_id):

        if TechnicianModel.is_used_in_work_orders(
            record_id
        ):
            raise ValueError(
                "This technician is linked to one or more "
                "work orders and cannot be deleted. "
                "Set the technician to Inactive instead."
            )

        TechnicianModel.delete(record_id)