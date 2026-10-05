# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 690)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.navigationFrame = QFrame(self.centralwidget)
        self.navigationFrame.setObjectName(u"navigationFrame")
        self.navigationFrame.setMinimumSize(QSize(220, 0))
        self.navigationFrame.setMaximumSize(QSize(220, 16777215))
        self.navigationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.navigationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.navigationFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblLogo = QLabel(self.navigationFrame)
        self.lblLogo.setObjectName(u"lblLogo")

        self.verticalLayout.addWidget(self.lblLogo)

        self.lblCompany = QLabel(self.navigationFrame)
        self.lblCompany.setObjectName(u"lblCompany")

        self.verticalLayout.addWidget(self.lblCompany)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btnDashboard = QPushButton(self.navigationFrame)
        self.btnDashboard.setObjectName(u"btnDashboard")
        self.btnDashboard.setCheckable(False)

        self.verticalLayout.addWidget(self.btnDashboard)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnAssets = QPushButton(self.navigationFrame)
        self.btnAssets.setObjectName(u"btnAssets")
        self.btnAssets.setCheckable(False)

        self.verticalLayout.addWidget(self.btnAssets)

        self.btnWorkOrders = QPushButton(self.navigationFrame)
        self.btnWorkOrders.setObjectName(u"btnWorkOrders")
        self.btnWorkOrders.setCheckable(False)

        self.verticalLayout.addWidget(self.btnWorkOrders)

        self.btnPM = QPushButton(self.navigationFrame)
        self.btnPM.setObjectName(u"btnPM")
        self.btnPM.setCheckable(False)

        self.verticalLayout.addWidget(self.btnPM)

        self.btnVehicleLogbook = QPushButton(self.navigationFrame)
        self.btnVehicleLogbook.setObjectName(u"btnVehicleLogbook")

        self.verticalLayout.addWidget(self.btnVehicleLogbook)

        self.btnVehicleSops = QPushButton(self.navigationFrame)
        self.btnVehicleSops.setObjectName(u"btnVehicleSops")

        self.verticalLayout.addWidget(self.btnVehicleSops)

        self.btnSopInspections = QPushButton(self.navigationFrame)
        self.btnSopInspections.setObjectName(u"btnSopInspections")

        self.verticalLayout.addWidget(self.btnSopInspections)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.btnTechnicians = QPushButton(self.navigationFrame)
        self.btnTechnicians.setObjectName(u"btnTechnicians")
        self.btnTechnicians.setCheckable(False)

        self.verticalLayout.addWidget(self.btnTechnicians)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_10)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.btnInventory = QPushButton(self.navigationFrame)
        self.btnInventory.setObjectName(u"btnInventory")
        self.btnInventory.setCheckable(False)

        self.verticalLayout.addWidget(self.btnInventory)

        self.btnPurchaseOrders = QPushButton(self.navigationFrame)
        self.btnPurchaseOrders.setObjectName(u"btnPurchaseOrders")

        self.verticalLayout.addWidget(self.btnPurchaseOrders)

        self.btnSuppliers = QPushButton(self.navigationFrame)
        self.btnSuppliers.setObjectName(u"btnSuppliers")
        self.btnSuppliers.setCheckable(False)

        self.verticalLayout.addWidget(self.btnSuppliers)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_11)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.btnReports = QPushButton(self.navigationFrame)
        self.btnReports.setObjectName(u"btnReports")
        self.btnReports.setCheckable(False)

        self.verticalLayout.addWidget(self.btnReports)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.btnUsers = QPushButton(self.navigationFrame)
        self.btnUsers.setObjectName(u"btnUsers")

        self.verticalLayout.addWidget(self.btnUsers)

        self.btnSettings = QPushButton(self.navigationFrame)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setCheckable(False)

        self.verticalLayout.addWidget(self.btnSettings)

        self.btnAbout = QPushButton(self.navigationFrame)
        self.btnAbout.setObjectName(u"btnAbout")

        self.verticalLayout.addWidget(self.btnAbout)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.btnLogout = QPushButton(self.navigationFrame)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setCheckable(False)

        self.verticalLayout.addWidget(self.btnLogout)


        self.horizontalLayout.addWidget(self.navigationFrame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageDashboard = QWidget()
        self.pageDashboard.setObjectName(u"pageDashboard")
        self.stackedWidget.addWidget(self.pageDashboard)
        self.pageAssets = QWidget()
        self.pageAssets.setObjectName(u"pageAssets")
        self.stackedWidget.addWidget(self.pageAssets)
        self.pageWorkOrders = QWidget()
        self.pageWorkOrders.setObjectName(u"pageWorkOrders")
        self.stackedWidget.addWidget(self.pageWorkOrders)
        self.pageVehicleLogbook = QWidget()
        self.pageVehicleLogbook.setObjectName(u"pageVehicleLogbook")
        self.stackedWidget.addWidget(self.pageVehicleLogbook)
        self.pagePM = QWidget()
        self.pagePM.setObjectName(u"pagePM")
        self.stackedWidget.addWidget(self.pagePM)
        self.pageTechnicians = QWidget()
        self.pageTechnicians.setObjectName(u"pageTechnicians")
        self.stackedWidget.addWidget(self.pageTechnicians)
        self.pageInventory = QWidget()
        self.pageInventory.setObjectName(u"pageInventory")
        self.stackedWidget.addWidget(self.pageInventory)
        self.pageSuppliers = QWidget()
        self.pageSuppliers.setObjectName(u"pageSuppliers")
        self.stackedWidget.addWidget(self.pageSuppliers)
        self.pageReports = QWidget()
        self.pageReports.setObjectName(u"pageReports")
        self.stackedWidget.addWidget(self.pageReports)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.stackedWidget.addWidget(self.pageSettings)
        self.pageUsers = QWidget()
        self.pageUsers.setObjectName(u"pageUsers")
        self.stackedWidget.addWidget(self.pageUsers)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.pagePurchaseOrders = QWidget()
        self.pagePurchaseOrders.setObjectName(u"pagePurchaseOrders")
        self.stackedWidget.addWidget(self.pagePurchaseOrders)
        self.pageVehicleSops = QWidget()
        self.pageVehicleSops.setObjectName(u"pageVehicleSops")
        self.stackedWidget.addWidget(self.pageVehicleSops)
        self.pageSopInspections = QWidget()
        self.pageSopInspections.setObjectName(u"pageSopInspections")
        self.stackedWidget.addWidget(self.pageSopInspections)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(14)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblLogo.setText("")
        self.lblCompany.setText("")
        self.btnDashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btnAssets.setText(QCoreApplication.translate("MainWindow", u"Assets", None))
        self.btnWorkOrders.setText(QCoreApplication.translate("MainWindow", u"Work Orders", None))
        self.btnPM.setText(QCoreApplication.translate("MainWindow", u"Preventive Maintenance", None))
        self.btnVehicleLogbook.setText(QCoreApplication.translate("MainWindow", u"Vehicle Logbook", None))
        self.btnVehicleSops.setText(QCoreApplication.translate("MainWindow", u"Vehicle SOPs", None))
        self.btnSopInspections.setText(QCoreApplication.translate("MainWindow", u" SOP Inspections", None))
        self.btnTechnicians.setText(QCoreApplication.translate("MainWindow", u"Technicians", None))
        self.btnInventory.setText(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.btnPurchaseOrders.setText(QCoreApplication.translate("MainWindow", u"Purchase Orders", None))
        self.btnSuppliers.setText(QCoreApplication.translate("MainWindow", u"Suppliers", None))
        self.btnReports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.btnUsers.setText(QCoreApplication.translate("MainWindow", u"Users", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btnAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.btnLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

