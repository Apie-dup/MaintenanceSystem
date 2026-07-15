from app.models.pm_model import PMModel


class PMService:

    @staticmethod
    def get_pm_schedules():
        return PMModel.get_all()

    @staticmethod
    def get_pm(pm_id):
        return PMModel.get_by_id(pm_id)

    @staticmethod
    def add_pm(pm):
        PMModel.insert(pm)

    @staticmethod
    def update_pm(pm):
        PMModel.update(pm)

    @staticmethod
    def delete_pm(pm_id):
        PMModel.delete(pm_id)

    @staticmethod
    def search_pm(search_text):
        return PMModel.search(search_text)

    @staticmethod
    def get_next_pm_number():
        return PMModel.get_next_pm_number()