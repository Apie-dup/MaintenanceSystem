from PySide6.QtWidgets import QApplication, QGraphicsBlurEffect


class AppTheme:
    """
    Enhanced Fluent-inspired theme for PySide6.
    Includes:
    - Light mode
    - Dark mode
    - High-contrast accessibility mode
    - Dynamic accent color
    - Acrylic blur support
    """

    MODE_LIGHT = "light"
    MODE_DARK = "dark"
    MODE_HIGH_CONTRAST = "high_contrast"

    current_mode = MODE_LIGHT

    FONT_FAMILY = "Segoe UI"
    FONT_SIZE = 13

    # Accent color can be changed dynamically
    ACCENT_COLOR = "#0f6cbd"
    ACCENT_COLOR_HOVER = "#115ea3"

    # Light theme colors
    LIGHT_BG = "#f7f7f7"
    LIGHT_SURFACE = "#ffffff"
    LIGHT_SURFACE_ALT = "#f3f3f3"
    LIGHT_TEXT = "#1f1f1f"
    LIGHT_SUBTEXT = "#616161"
    LIGHT_BORDER = "#e1e1e1"
    LIGHT_SELECTION = "#cfe8ff"

    # Dark theme colors
    DARK_BG = "#202020"
    DARK_SURFACE = "#2b2b2b"
    DARK_SURFACE_ALT = "#323232"
    DARK_TEXT = "#ffffff"
    DARK_SUBTEXT = "#c8c8c8"
    DARK_BORDER = "#444444"
    DARK_SELECTION = "#264f78"

    # High contrast theme
    HC_BG = "#000000"
    HC_SURFACE = "#000000"
    HC_TEXT = "#ffffff"
    HC_BORDER = "#ffffff"
    HC_SELECTION = "#ffff00"

    # ---------------------------------------------------------
    # Acrylic blur helper
    # ---------------------------------------------------------

    @staticmethod
    def apply_acrylic(widget, radius=20):
        effect = QGraphicsBlurEffect()
        effect.setBlurRadius(radius)
        widget.setGraphicsEffect(effect)

    # ---------------------------------------------------------
    # Apply theme
    # ---------------------------------------------------------

    @classmethod
    def apply(cls, app: QApplication, mode=None):
        if mode is not None:
            cls.current_mode = mode

        if cls.current_mode == cls.MODE_DARK:
            app.setStyleSheet(cls.dark_qss())

        elif cls.current_mode == cls.MODE_HIGH_CONTRAST:
            app.setStyleSheet(cls.high_contrast_qss())

        else:
            app.setStyleSheet(cls.light_qss())

    @classmethod
    def toggle_mode(cls, app: QApplication):
        if cls.current_mode == cls.MODE_LIGHT:
            cls.current_mode = cls.MODE_DARK
        elif cls.current_mode == cls.MODE_DARK:
            cls.current_mode = cls.MODE_HIGH_CONTRAST
        else:
            cls.current_mode = cls.MODE_LIGHT

        cls.apply(app)


    @classmethod
    def light_qss(cls):
        return f"""
        * {{
            font-family: "{cls.FONT_FAMILY}";
            font-size: {cls.FONT_SIZE}px;
        }}

        QWidget {{
            background-color: {cls.LIGHT_BG};
            color: {cls.LIGHT_TEXT};
        }}

        QMainWindow,
        QDialog {{
            background-color: {cls.LIGHT_BG};
        }}

        QLabel {{
            background: transparent;
            color: {cls.LIGHT_TEXT};
        }}

        QLabel[subtext="true"] {{
            color: {cls.LIGHT_SUBTEXT};
            font-size: 12px;
        }}

        QLabel#lblTitle,
        QLabel#dashboardTitle {{
            font-size: 24px;
            font-weight: 600;
            color: {cls.LIGHT_TEXT};
        }}

        QLabel#lblDashboardSubtitle,
        QLabel#dashboardSubtitle {{
            color: {cls.LIGHT_SUBTEXT};
            font-size: 14px;
        }}

        /* --------------------------------
           Sidebar
        -------------------------------- */

        #sidebar,
        #navigationFrame,
        #frameNavigation {{
            background-color: #202020;
            border: none;
        }}

        #sidebar QLabel,
        #navigationFrame QLabel,
        #frameNavigation QLabel {{
            color: #ffffff;
            background: transparent;
        }}

        #sidebar QPushButton,
        #navigationFrame QPushButton,
        #frameNavigation QPushButton {{
            background: transparent;
            color: #f2f2f2;
            border: none;
            border-radius: 4px;
            padding: 9px 12px;
            text-align: left;
            min-height: 24px;
        }}

        #sidebar QPushButton:hover,
        #navigationFrame QPushButton:hover,
        #frameNavigation QPushButton:hover {{
            background-color: #2d2d2d;
        }}

        #sidebar QPushButton:checked,
        #navigationFrame QPushButton:checked,
        #frameNavigation QPushButton:checked {{
            background-color: #333333;
            border-left: 3px solid {cls.ACCENT_COLOR};
            font-weight: 600;
        }}

        /* --------------------------------
           Buttons
        -------------------------------- */

        QPushButton {{
            background-color: {cls.LIGHT_SURFACE};
            color: {cls.LIGHT_TEXT};
            border: 1px solid {cls.LIGHT_BORDER};
            border-radius: 4px;
            padding: 8px 16px;
            min-height: 30px;
        }}

        QPushButton:hover {{
            background-color: {cls.LIGHT_SURFACE_ALT};
            border-color: #c8c8c8;
        }}

        QPushButton:pressed {{
            background-color: #e9e9e9;
        }}

        QPushButton:disabled {{
            color: #9a9a9a;
            background-color: #f2f2f2;
            border-color: #e5e5e5;
        }}

        QPushButton[accent="true"] {{
            background-color: {cls.ACCENT_COLOR};
            color: white;
            border: none;
        }}

        QPushButton[accent="true"]:hover {{
            background-color: {cls.ACCENT_COLOR_HOVER};
        }}

        /* --------------------------------
           Inputs
        -------------------------------- */

        QLineEdit,
        QComboBox,
        QSpinBox,
        QDoubleSpinBox,
        QDateEdit,
        QTextEdit,
        QPlainTextEdit {{
            background-color: {cls.LIGHT_SURFACE};
            color: {cls.LIGHT_TEXT};
            border: 1px solid #cfcfcf;
            border-radius: 4px;
            padding: 6px 10px;
            selection-background-color: {cls.LIGHT_SELECTION};
        }}

        QLineEdit:focus,
        QComboBox:focus,
        QSpinBox:focus,
        QDoubleSpinBox:focus,
        QDateEdit:focus,
        QTextEdit:focus,
        QPlainTextEdit:focus {{
            border: 1px solid {cls.ACCENT_COLOR};
        }}

        QLineEdit:read-only {{
            background-color: #f4f4f4;
            color: #5f5f5f;
        }}

        QComboBox QAbstractItemView {{
            background-color: {cls.LIGHT_SURFACE};
            color: {cls.LIGHT_TEXT};
            border: 1px solid {cls.LIGHT_BORDER};
            border-radius: 4px;
            selection-background-color: {cls.LIGHT_SELECTION};
            selection-color: {cls.LIGHT_TEXT};
            outline: none;
            padding: 4px;
        }}

        QComboBox QAbstractItemView::item {{
            min-height: 28px;
            padding: 4px 8px;
        }}

        QComboBox QAbstractItemView::item:hover {{
            background-color: #e8f2fc;
        }}

        QComboBox QAbstractItemView::item:selected {{
            background-color: {cls.LIGHT_SELECTION};
        }}

        /* --------------------------------
           Group boxes
        -------------------------------- */

        QGroupBox {{
            background: transparent;
            border: none;
            border-top: 1px solid #bdbdbd;
            margin-top: 14px;
            padding-top: 10px;
            font-weight: 500;
        }}

        QGroupBox::title {{
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0 6px;
            color: {cls.LIGHT_TEXT};
            background-color: {cls.LIGHT_BG};
        }}

        /* --------------------------------
           Cards (fixed)
        -------------------------------- */

        QFrame[card="true"],
        .dashboardCard,
        QFrame#cardAssets,
        QFrame#cardOpenWOs,
        QFrame#cardPMDueToday,
        QFrame#cardPMOverdue,
        QFrame#cardNext7Days,
        QFrame#cardLowStock,
        QFrame#cardTechnicians,
        QFrame#cardInventoryValue {{
            background-color: {cls.LIGHT_SURFACE};
            border: 1px solid {cls.LIGHT_BORDER};
            border-radius: 6px;
        }}

        /* --------------------------------
           Tables
        -------------------------------- */

        QTableWidget,
        QTableView {{
            background-color: {cls.LIGHT_SURFACE};
            alternate-background-color: #fafafa;
            color: {cls.LIGHT_TEXT};
            border: 1px solid {cls.LIGHT_BORDER};
            border-radius: 4px;
            gridline-color: #ededed;
            selection-background-color: {cls.LIGHT_SELECTION};
        }}

        QHeaderView::section {{
            background-color: #f5f5f5;
            color: {cls.LIGHT_TEXT};
            border: none;
            border-bottom: 1px solid {cls.LIGHT_BORDER};
            padding: 8px 10px;
            font-weight: 600;
        }}

        QTableCornerButton::section {{
            background-color: #f5f5f5;
            border: none;
            border-bottom: 1px solid {cls.LIGHT_BORDER};
        }}

        /* --------------------------------
           Scrollbars
        -------------------------------- */

        QScrollBar:vertical {{
            background: transparent;
            width: 12px;
        }}

        QScrollBar::handle:vertical {{
            background: #c4c4c4;
            min-height: 28px;
            border-radius: 6px;
        }}

        QScrollBar::handle:vertical:hover {{
            background: #a8a8a8;
        }}

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {{
            height: 0;
        }}

        QScrollBar:horizontal {{
            background: transparent;
            height: 12px;
        }}

        QScrollBar::handle:horizontal {{
            background: #c4c4c4;
            min-width: 28px;
            border-radius: 6px;
        }}

        QScrollBar::add-line:horizontal,
        QScrollBar::sub-line:horizontal {{
            width: 0;
        }}

        /* --------------------------------
           Dialog buttons
        -------------------------------- */

        QDialogButtonBox QPushButton {{
            min-width: 80px;
        }}

        QCheckBox {{
            spacing: 7px;
        }}

        QToolTip {{
            background-color: #2b2b2b;
            color: white;
            border: none;
            padding: 5px;
        }}
        """

    @classmethod
    def dark_qss(cls):
        return f"""
        * {{
            font-family: "{cls.FONT_FAMILY}";
            font-size: {cls.FONT_SIZE}px;
        }}

        QWidget {{
            background-color: {cls.DARK_BG};
            color: {cls.DARK_TEXT};
        }}

        QMainWindow,
        QDialog {{
            background-color: {cls.DARK_BG};
        }}

        QLabel {{
            background: transparent;
            color: {cls.DARK_TEXT};
        }}

        QLabel[subtext="true"] {{
            color: {cls.DARK_SUBTEXT};
        }}

        QLabel#lblTitle,
        QLabel#dashboardTitle {{
            font-size: 24px;
            font-weight: 600;
        }}

        /* --------------------------------
           Sidebar
        -------------------------------- */

        #sidebar,
        #navigationFrame,
        #frameNavigation {{
            background-color: #181818;
            border: none;
        }}

        #sidebar QPushButton,
        #navigationFrame QPushButton,
        #frameNavigation QPushButton {{
            background: transparent;
            color: #f2f2f2;
            border: none;
            border-radius: 4px;
            padding: 9px 12px;
            text-align: left;
        }}

        #sidebar QPushButton:hover,
        #navigationFrame QPushButton:hover,
        #frameNavigation QPushButton:hover {{
            background-color: #2b2b2b;
        }}

        #sidebar QPushButton:checked,
        #navigationFrame QPushButton:checked,
        #frameNavigation QPushButton:checked {{
            background-color: #313131;
            border-left: 3px solid {cls.ACCENT_COLOR};
            font-weight: 600;
        }}

        /* --------------------------------
           Buttons
        -------------------------------- */

        QPushButton {{
            background-color: {cls.DARK_SURFACE_ALT};
            color: {cls.DARK_TEXT};
            border: 1px solid {cls.DARK_BORDER};
            border-radius: 4px;
            padding: 8px 16px;
            min-height: 30px;
        }}

        QPushButton:hover {{
            background-color: #3a3a3a;
        }}

        QPushButton[accent="true"] {{
            background-color: {cls.ACCENT_COLOR};
            color: #101010;
            border: none;
        }}

        /* --------------------------------
           Inputs
        -------------------------------- */

        QLineEdit,
        QComboBox,
        QSpinBox,
        QDoubleSpinBox,
        QDateEdit,
        QTextEdit,
        QPlainTextEdit {{
            background-color: {cls.DARK_SURFACE};
            color: {cls.DARK_TEXT};
            border: 1px solid {cls.DARK_BORDER};
            border-radius: 4px;
            padding: 6px 10px;
            selection-background-color: {cls.DARK_SELECTION};
        }}

        QLineEdit:focus,
        QComboBox:focus,
        QSpinBox:focus,
        QDoubleSpinBox:focus,
        QDateEdit:focus,
        QTextEdit:focus {{
            border: 1px solid {cls.ACCENT_COLOR};
        }}

        /* --------------------------------
           Group boxes
        -------------------------------- */

        QGroupBox {{
            background: transparent;
            border: none;
            border-top: 1px solid #555555;
            margin-top: 14px;
            padding-top: 10px;
            font-weight: 500;
        }}

        QGroupBox::title {{
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0 6px;
            background-color: {cls.DARK_BG};
        }}

        /* --------------------------------
           Cards (fixed)
        -------------------------------- */

        QFrame[card="true"],
        .dashboardCard,
        QFrame#cardAssets,
        QFrame#cardOpenWOs,
        QFrame#cardPMDueToday,
        QFrame#cardPMOverdue,
        QFrame#cardNext7Days,
        QFrame#cardLowStock,
        QFrame#cardTechnicians,
        QFrame#cardInventoryValue {{
            background-color: {cls.DARK_SURFACE};
            border: 1px solid {cls.DARK_BORDER};
            border-radius: 6px;
        }}

        /* --------------------------------
           Tables
        -------------------------------- */

        QTableWidget,
        QTableView {{
            background-color: {cls.DARK_SURFACE};
            alternate-background-color: #303030;
            color: {cls.DARK_TEXT};
            border: 1px solid {cls.DARK_BORDER};
            border-radius: 4px;
            gridline-color: #3b3b3b;
            selection-background-color: {cls.DARK_SELECTION};
        }}

        QHeaderView::section {{
            background-color: #333333;
            color: {cls.DARK_TEXT};
            border: none;
            border-bottom: 1px solid {cls.DARK_BORDER};
            padding: 8px 10px;
            font-weight: 600;
        }}
        """

