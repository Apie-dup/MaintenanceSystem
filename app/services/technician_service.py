from app.models.technician_model import TechnicianModel


class TechnicianService:

    # ---------------------------------------------------------
    # Get all technicians
    # ---------------------------------------------------------

    @staticmethod
    def get_all():
        return TechnicianModel.get_all()

    # ---------------------------------------------------------
    # Get technician by ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(record_id):
        return TechnicianModel.get_by_id(record_id)

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    @staticmethod
    def search(search_text):
        return TechnicianModel.search(search_text)

    # ---------------------------------------------------------
    # Next employee number
    # ---------------------------------------------------------

    @staticmethod
    def get_next_employee_number():
        return TechnicianModel.get_next_employee_number()

    # ---------------------------------------------------------
    # Create
    # ---------------------------------------------------------

    @staticmethod
    def create(data):

        if not data["first_name"].strip():
            raise ValueError(
                "First Name is required."
            )

        if not data["last_name"].strip():
            raise ValueError(
                "Last Name is required."
            )

        if not data["employee_number"].strip():
            raise ValueError(
                "Employee Number is required."
            )

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

        if not data["first_name"].strip():
            raise ValueError(
                "First Name is required."
            )

        if not data["last_name"].strip():
            raise ValueError(
                "Last Name is required."
            )

        if not data["employee_number"].strip():
            raise ValueError(
                "Employee Number is required."
            )

        if TechnicianModel.employee_number_exists(
            data["employee_number"],
            exclude_id=record_id
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
        TechnicianModel.delete(record_id)

    @staticmethod
    def get_active_technicians():
        return TechnicianModel.get_active_technicians()