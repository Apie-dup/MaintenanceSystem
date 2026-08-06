from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QComboBox,
    QDateEdit,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QSpinBox,
    QTextEdit,
    QWidget,
)


class FormHelper:
    """
    Applies shared form standards to dialogs and form widgets.
    """

    LABEL_WIDTH = 130
    CONTROL_HEIGHT = 34
    TEXT_AREA_MIN_HEIGHT = 110

    @classmethod
    def apply(cls, form: QWidget):
        """
        Apply standard control sizing and behavior to a form.
        """

        cls.configure_labels(form)
        cls.configure_line_edits(form)
        cls.configure_combo_boxes(form)
        cls.configure_date_edits(form)
        cls.configure_spin_boxes(form)
        cls.configure_text_areas(form)

    # ---------------------------------------------------------
    # Labels
    # ---------------------------------------------------------

    @classmethod
    def configure_labels(cls, form: QWidget):
        for label in form.findChildren(QLabel):
            text = label.text().strip()

            # Only treat labels ending in ":" as field labels.
            if not text.endswith(":"):
                continue

            label.setMinimumWidth(cls.LABEL_WIDTH)
            label.setMaximumWidth(cls.LABEL_WIDTH)
            label.setAlignment(
                Qt.AlignmentFlag.AlignRight
                | Qt.AlignmentFlag.AlignVCenter
            )

    # ---------------------------------------------------------
    # Line edits
    # ---------------------------------------------------------

    @classmethod
    def configure_line_edits(cls, form: QWidget):
        for control in form.findChildren(QLineEdit):
            control.setMinimumHeight(cls.CONTROL_HEIGHT)

    # ---------------------------------------------------------
    # Combo boxes
    # ---------------------------------------------------------

    @classmethod
    def configure_combo_boxes(cls, form: QWidget):
        for control in form.findChildren(QComboBox):
            control.setMinimumHeight(cls.CONTROL_HEIGHT)

    # ---------------------------------------------------------
    # Date edits
    # ---------------------------------------------------------

    @classmethod
    def configure_date_edits(cls, form: QWidget):
        for control in form.findChildren(QDateEdit):
            control.setMinimumHeight(cls.CONTROL_HEIGHT)
            control.setCalendarPopup(True)

    # ---------------------------------------------------------
    # Spin boxes
    # ---------------------------------------------------------

    @classmethod
    def configure_spin_boxes(cls, form: QWidget):
        spin_boxes = (
            form.findChildren(QSpinBox)
            + form.findChildren(QDoubleSpinBox)
        )

        for control in spin_boxes:
            control.setMinimumHeight(cls.CONTROL_HEIGHT)
            control.setButtonSymbols(
                QAbstractSpinBox.ButtonSymbols.UpDownArrows
            )

    # ---------------------------------------------------------
    # Text areas
    # ---------------------------------------------------------

    @classmethod
    def configure_text_areas(cls, form: QWidget):
        text_areas = (
            form.findChildren(QTextEdit)
            + form.findChildren(QPlainTextEdit)
        )

        for control in text_areas:
            # Do not force small description boxes to become very tall.
            if control.minimumHeight() < cls.TEXT_AREA_MIN_HEIGHT:
                control.setMinimumHeight(
                    cls.TEXT_AREA_MIN_HEIGHT
                )

    # ---------------------------------------------------------
    # Focus
    # ---------------------------------------------------------

    @staticmethod
    def focus_first(*widgets):
        """
        Focus the first enabled and editable widget supplied.
        """

        for widget in widgets:
            if not widget.isEnabled():
                continue

            if hasattr(widget, "isReadOnly"):
                if widget.isReadOnly():
                    continue

            widget.setFocus()

            if hasattr(widget, "selectAll"):
                widget.selectAll()

            return