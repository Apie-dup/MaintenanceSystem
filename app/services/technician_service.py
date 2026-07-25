from app.models.technician_model import TechnicianModel


class TechnicianService:

    @staticmethod
    def get_all():
        return TechnicianModel.get_all()

    @staticmethod
    def get(record_id):
        return TechnicianModel.get_by_id(record_id)

    @staticmethod
    def add(record):
        TechnicianModel.insert(record)

    @staticmethod
    def update(record):
        TechnicianModel.update(record)

    @staticmethod
    def delete(record_id):
        TechnicianModel.delete(record_id)

    @staticmethod
    def search(text):
        return TechnicianModel.search(text)

    @staticmethod
    def get_next_employee_number():
        return TechnicianModel.get_next_employee_number()