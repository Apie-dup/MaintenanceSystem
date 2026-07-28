from PySide6.QtWidgets import QComboBox


class LookupHelper:
    """
    Helper methods for populating combo boxes.
    """

    @staticmethod
    def fill_combo(combo: QComboBox,
                   items,
                   include_blank=False):

        combo.clear()

        if include_blank:
            combo.addItem("")

        combo.addItems(items)

    @staticmethod
    def fill_combo_data(combo, rows):

        combo.clear()

        for record_id, text in rows:

            combo.addItem(text, record_id)

    @staticmethod
    def current_id(combo):

        return combo.currentData()