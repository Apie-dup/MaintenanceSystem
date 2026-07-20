from app.models.pm_model import PMModel


class PMService:

    @staticmethod
    def get_all():
        return PMModel.get_all()

    @staticmethod
    def get_pm(pm_id):
        return PMModel.get_by_id(pm_id)

    @staticmethod
    def add(record):
        PMModel.insert(record)

    @staticmethod
    def update(record):
        PMModel.update(record)

    @staticmethod
    def delete_pm(pm_id):
        PMModel.delete(pm_id)

    @staticmethod
    def search(text):
        return PMModel.search(text)

    @staticmethod
    def get_next_pm_number():
        return PMModel.get_next_pm_number()