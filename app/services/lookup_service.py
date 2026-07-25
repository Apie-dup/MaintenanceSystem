from app.models.lookup_model import LookupModel

class LookupService:

    @staticmethod
    def get_all(lookup_type):
        return LookupModel.get_all(lookup_type)
    
    @staticmethod
    def get(record_id):
        return LookupModel.get(record_id)
    
    @staticmethod
    def add(record):
        LookupModel.insert(record)

    @staticmethod
    def update(record):
        LookupModel.update(record)

    @staticmethod
    def delete(recor_id):
        LookupModel.delete(recor_id)

    @staticmethod
    def search(lookup_type, text):
        return LookupModel.search(lookup_type, text)
