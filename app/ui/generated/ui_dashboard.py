# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QToolBar, QWidget)

class Ui_DashboardWindow(object):
    def setupUi(self, DashboardWindow):
        if not DashboardWindow.objectName():
            DashboardWindow.setObjectName(u"DashboardWindow")
        DashboardWindow.resize(1119, 651)
        self.centralwidget = QWidget(DashboardWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(220, 0))
        self.sidebar.setMaximumSize(QSize(220, 16777215))
        self.sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.sidebar)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lblLogo = QLabel(self.sidebar)
        self.lblLogo.setObjectName(u"lblLogo")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblLogo)

        self.lblCompany = QLabel(self.sidebar)
        self.lblCompany.setObjectName(u"lblCompany")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblCompany)

        self.lblMaintenaceManagementSysytem = QLabel(self.sidebar)
        self.lblMaintenaceManagementSysytem.setObjectName(u"lblMaintenaceManagementSysytem")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblMaintenaceManagementSysytem)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(3, QFormLayout.ItemRole.LabelRole, self.verticalSpacer_7)

        self.btnDashboard = QPushButton(self.sidebar)
        self.btnDashboard.setObjectName(u"btnDashboard")
        icon = QIcon()
        icon.addFile(u"../../resources/icons/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnDashboard.setIcon(icon)
        self.btnDashboard.setCheckable(True)
        self.btnDashboard.setAutoExclusive(True)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.btnDashboard)

        self.verticalSpacer_6 = QSpacerItem(20, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(5, QFormLayout.ItemRole.LabelRole, self.verticalSpacer_6)

        self.btnAssets = QPushButton(self.sidebar)
        self.btnAssets.setObjectName(u"btnAssets")
        icon1 = QIcon()
        icon1.addFile(u"../../resources/icons/assets.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAssets.setIcon(icon1)
        self.btnAssets.setCheckable(True)
        self.btnAssets.setAutoExclusive(True)

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.LabelRole, self.btnAssets)

        self.btnWorkOrders = QPushButton(self.sidebar)
        self.btnWorkOrders.setObjectName(u"btnWorkOrders")
        icon2 = QIcon()
        icon2.addFile(u"../../resources/icons/workorders.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnWorkOrders.setIcon(icon2)
        self.btnWorkOrders.setCheckable(True)
        self.btnWorkOrders.setAutoExclusive(True)

        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.LabelRole, self.btnWorkOrders)

        self.btnPM = QPushButton(self.sidebar)
        self.btnPM.setObjectName(u"btnPM")
        icon3 = QIcon()
        icon3.addFile(u"../../resources/icons/pm.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnPM.setIcon(icon3)
        self.btnPM.setCheckable(True)
        self.btnPM.setAutoExclusive(True)

        self.formLayout_2.setWidget(8, QFormLayout.ItemRole.LabelRole, self.btnPM)

        self.verticalSpacer_5 = QSpacerItem(20, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(9, QFormLayout.ItemRole.LabelRole, self.verticalSpacer_5)

        self.btnThecnicians = QPushButton(self.sidebar)
        self.btnThecnicians.setObjectName(u"btnThecnicians")
        icon4 = QIcon()
        icon4.addFile(u"../../resources/icons/technicians.png.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnThecnicians.setIcon(icon4)
        self.btnThecnicians.setCheckable(True)
        self.btnThecnicians.setAutoExclusive(True)

        self.formLayout_2.setWidget(10, QFormLayout.ItemRole.LabelRole, self.btnThecnicians)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(11, QFormLayout.ItemRole.LabelRole, self.verticalSpacer_4)

        self.btnInventory = QPushButton(self.sidebar)
        self.btnInventory.setObjectName(u"btnInventory")
        icon5 = QIcon()
        icon5.addFile(u"../../resources/icons/inventory.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnInventory.setIcon(icon5)
        self.btnInventory.setCheckable(True)
        self.btnInventory.setAutoExclusive(True)

        self.formLayout_2.setWidget(12, QFormLayout.ItemRole.LabelRole, self.btnInventory)

        self.btnSuppliers = QPushButton(self.sidebar)
        self.btnSuppliers.setObjectName(u"btnSuppliers")
        icon6 = QIcon()
        icon6.addFile(u"../../resources/icons/suppliers.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnSuppliers.setIcon(icon6)
        self.btnSuppliers.setCheckable(True)
        self.btnSuppliers.setAutoExclusive(True)

        self.formLayout_2.setWidget(13, QFormLayout.ItemRole.LabelRole, self.btnSuppliers)

        self.verticalSpacer_3 = QSpacerItem(20, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(14, QFormLayout.ItemRole.LabelRole, self.verticalSpacer_3)

        self.btnReports = QPushButton(self.sidebar)
        self.btnReports.setObjectName(u"btnReports")
        icon7 = QIcon()
        icon7.addFile(u"../../resources/icons/reports.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnReports.setIcon(icon7)
        self.btnReports.setCheckable(True)
        self.btnReports.setAutoExclusive(True)

        self.formLayout_2.setWidget(15, QFormLayout.ItemRole.LabelRole, self.btnReports)

        self.verticalSpacer_2 = QSpacerItem(20, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(16, QFormLayout.ItemRole.LabelRole, self.verticalSpacer_2)

        self.btnLookups = QPushButton(self.sidebar)
        self.btnLookups.setObjectName(u"btnLookups")
        icon8 = QIcon()
        icon8.addFile(u"../../resources/icons/lookup.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLookups.setIcon(icon8)
        self.btnLookups.setCheckable(True)
        self.btnLookups.setAutoExclusive(True)

        self.formLayout_2.setWidget(17, QFormLayout.ItemRole.LabelRole, self.btnLookups)

        self.btnSettings = QPushButton(self.sidebar)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon9 = QIcon()
        icon9.addFile(u"../../resources/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnSettings.setIcon(icon9)
        self.btnSettings.setCheckable(True)
        self.btnSettings.setAutoExclusive(True)

        self.formLayout_2.setWidget(18, QFormLayout.ItemRole.LabelRole, self.btnSettings)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(19, QFormLayout.ItemRole.LabelRole, self.verticalSpacer)

        self.btnLogout = QPushButton(self.sidebar)
        self.btnLogout.setObjectName(u"btnLogout")
        icon10 = QIcon()
        icon10.addFile(u"../../resources/icons/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnLogout.setIcon(icon10)
        self.btnLogout.setCheckable(True)
        self.btnLogout.setAutoExclusive(True)

        self.formLayout_2.setWidget(20, QFormLayout.ItemRole.LabelRole, self.btnLogout)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.sidebar)

        DashboardWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DashboardWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1119, 33))
        DashboardWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(DashboardWindow)
        self.statusBar.setObjectName(u"statusBar")
        DashboardWindow.setStatusBar(self.statusBar)
        self.mainToolBar = QToolBar(DashboardWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setIconSize(QSize(32, 32))
        self.mainToolBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.mainToolBar.setFloatable(False)
        DashboardWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(DashboardWindow)

        QMetaObject.connectSlotsByName(DashboardWindow)
    # setupUi

    def retranslateUi(self, DashboardWindow):
        DashboardWindow.setWindowTitle(QCoreApplication.translate("DashboardWindow", u"Mantenance Management System", None))
        self.lblLogo.setText("")
        self.lblCompany.setText(QCoreApplication.translate("DashboardWindow", u"Your Organization", None))
        self.lblMaintenaceManagementSysytem.setText(QCoreApplication.translate("DashboardWindow", u"Maintenance Management System", None))
        self.btnDashboard.setText(QCoreApplication.translate("DashboardWindow", u"Dashboard", None))
        self.btnAssets.setText(QCoreApplication.translate("DashboardWindow", u"Assets", None))
        self.btnWorkOrders.setText(QCoreApplication.translate("DashboardWindow", u"Work Orders", None))
        self.btnPM.setText(QCoreApplication.translate("DashboardWindow", u"Preventive Maitenance", None))
        self.btnThecnicians.setText(QCoreApplication.translate("DashboardWindow", u"Technicians", None))
        self.btnInventory.setText(QCoreApplication.translate("DashboardWindow", u"Inventory", None))
        self.btnSuppliers.setText(QCoreApplication.translate("DashboardWindow", u"Suppliers", None))
        self.btnReports.setText(QCoreApplication.translate("DashboardWindow", u"Reports", None))
        self.btnLookups.setText(QCoreApplication.translate("DashboardWindow", u"Lookup Management", None))
        self.btnSettings.setText(QCoreApplication.translate("DashboardWindow", u"Settings", None))
        self.btnLogout.setText(QCoreApplication.translate("DashboardWindow", u"Logout", None))
        self.mainToolBar.setWindowTitle(QCoreApplication.translate("DashboardWindow", u"toolBar", None))
    # retranslateUi

