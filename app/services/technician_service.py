from app.models.technician_model import TechnicianModel


class TechnicianService:

    @staticmethod
    def get_technicians():
        return TechnicianModel.get_all()

    @staticmethod
    def get_technician(technician_id):
        return TechnicianModel.get_by_id(technician_id)

    @staticmethod
    def add_technician(technician):
        TechnicianModel.insert(technician)

    @staticmethod
    def update_technician(technician):
        TechnicianModel.update(technician)

    @staticmethod
    def delete_technician(technician_id):
        TechnicianModel.delete(technician_id)

    @staticmethod
    def search_technicians(search_text):
        return TechnicianModel.search(search_text)

    @staticmethod
    def get_next_employee_number():
        return TechnicianModel.get_next_employee_number()