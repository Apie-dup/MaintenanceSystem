from app.services.lookup_service import LookupService


class LookupManager:

    @staticmethod
    def load(combo, lookup_type, defaults=None):

        combo.clear()

        rows = LookupService.get_all(lookup_type)

        if rows:
            for lookup_id, value in rows:
                if value is None:
                    continue
                combo.addItem(str(value), lookup_id)
        elif defaults:
            combo.addItems(defaults)

        if combo.count() == 0 and defaults:
            combo.addItems(defaults) 