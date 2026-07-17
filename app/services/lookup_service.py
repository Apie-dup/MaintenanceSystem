from app.models.lookup_model import LookupModel


class LookupService:

    @staticmethod
    def get_lookup_values(lookup_type):
        return LookupModel.get_all(lookup_type)

    @staticmethod
    def load_trades(combo):
        combo.clear()

        for row in LookupModel.get_all("Trades"):
            combo.addItem(row[1], row[0])

    @staticmethod
    def load_departments(combo):
        combo.clear()

        for row in LookupModel.get_all("Departments"):
            combo.addItem(row[1], row[0])

    @staticmethod
    def load_statuses(combo):
        combo.clear()

        for row in LookupModel.get_all("Statuses"):
            combo.addItem(row[1], row[0])

    @staticmethod
    def add_lookup_value(lookup_type, value):
        LookupModel.insert(lookup_type, value)

    @staticmethod
    def update_lookup_value(lookup_type, lookup_id, value):
        LookupModel.update(lookup_type, lookup_id, value)

    @staticmethod
    def delete_lookup_value(lookup_type, lookup_id):
        LookupModel.delete(lookup_type, lookup_id)