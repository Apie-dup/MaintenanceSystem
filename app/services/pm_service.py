from app.models.pm_model import PMModel


class PMService:

    @staticmethod
    def get_all():
        return PMModel.get_all()

    @staticmethod
    def get(record_id):
        return PMModel.get(record_id)

    @staticmethod
    def add(record):
        PMModel.add(record)

    @staticmethod
    def update(record):
        PMModel.update(record)

    @staticmethod
    def delete(record_id):
        PMModel.delete(record_id)

    @staticmethod
    def search(text):
        return PMModel.search(text)

    @staticmethod
    def get_next_pm_number():
        return PMModel.get_next_pm_number()