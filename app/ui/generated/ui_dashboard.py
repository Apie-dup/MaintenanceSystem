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
    QSpacerItem, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)

class Ui_DashboardWindow(object):
    def setupUi(self, DashboardWindow):
        if not DashboardWindow.objectName():
            DashboardWindow.setObjectName(u"DashboardWindow")
        DashboardWindow.resize(1119, 651)
        self.centralwidget = QWidget(DashboardWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.frameNavigation = QFrame(self.centralwidget)
        self.frameNavigation.setObjectName(u"frameNavigation")
        self.frameNavigation.setMinimumSize(QSize(220, 0))
        self.frameNavigation.setMaximumSize(QSize(220, 16777215))
        self.frameNavigation.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameNavigation.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frameNavigation)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblLogo = QLabel(self.frameNavigation)
        self.lblLogo.setObjectName(u"lblLogo")

        self.verticalLayout.addWidget(self.lblLogo)

        self.lblCompany = QLabel(self.frameNavigation)
        self.lblCompany.setObjectName(u"lblCompany")

        self.verticalLayout.addWidget(self.lblCompany)

        self.lblMaintenaceManagementSysytem = QLabel(self.frameNavigation)
        self.lblMaintenaceManagementSysytem.setObjectName(u"lblMaintenaceManagementSysytem")

        self.verticalLayout.addWidget(self.lblMaintenaceManagementSysytem)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.btnDashboard = QPushButton(self.frameNavigation)
        self.btnDashboard.setObjectName(u"btnDashboard")

        self.verticalLayout.addWidget(self.btnDashboard, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer_6 = QSpacerItem(20, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.btnAssets = QPushButton(self.frameNavigation)
        self.btnAssets.setObjectName(u"btnAssets")

        self.verticalLayout.addWidget(self.btnAssets, 0, Qt.AlignmentFlag.AlignLeft)

        self.btnWorkOrders = QPushButton(self.frameNavigation)
        self.btnWorkOrders.setObjectName(u"btnWorkOrders")

        self.verticalLayout.addWidget(self.btnWorkOrders, 0, Qt.AlignmentFlag.AlignLeft)

        self.btnPM = QPushButton(self.frameNavigation)
        self.btnPM.setObjectName(u"btnPM")

        self.verticalLayout.addWidget(self.btnPM, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer_5 = QSpacerItem(20, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.btnThecnicians = QPushButton(self.frameNavigation)
        self.btnThecnicians.setObjectName(u"btnThecnicians")

        self.verticalLayout.addWidget(self.btnThecnicians, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.btnInventory = QPushButton(self.frameNavigation)
        self.btnInventory.setObjectName(u"btnInventory")

        self.verticalLayout.addWidget(self.btnInventory, 0, Qt.AlignmentFlag.AlignLeft)

        self.btnSuppliers = QPushButton(self.frameNavigation)
        self.btnSuppliers.setObjectName(u"btnSuppliers")

        self.verticalLayout.addWidget(self.btnSuppliers, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer_3 = QSpacerItem(20, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.btnReports = QPushButton(self.frameNavigation)
        self.btnReports.setObjectName(u"btnReports")

        self.verticalLayout.addWidget(self.btnReports, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer_2 = QSpacerItem(20, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btnLookups = QPushButton(self.frameNavigation)
        self.btnLookups.setObjectName(u"btnLookups")

        self.verticalLayout.addWidget(self.btnLookups, 0, Qt.AlignmentFlag.AlignLeft)

        self.btnSettings = QPushButton(self.frameNavigation)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout.addWidget(self.btnSettings, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnLogout = QPushButton(self.frameNavigation)
        self.btnLogout.setObjectName(u"btnLogout")

        self.verticalLayout.addWidget(self.btnLogout)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.frameNavigation)

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

