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
    QStackedWidget, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
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

        self.btnDashboard = QPushButton(self.navigationFrame)
        self.btnDashboard.setObjectName(u"btnDashboard")
        self.btnDashboard.setCheckable(False)

        self.verticalLayout.addWidget(self.btnDashboard)

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

        self.btnTechnicians = QPushButton(self.navigationFrame)
        self.btnTechnicians.setObjectName(u"btnTechnicians")
        self.btnTechnicians.setCheckable(False)

        self.verticalLayout.addWidget(self.btnTechnicians)

        self.btnInventory = QPushButton(self.navigationFrame)
        self.btnInventory.setObjectName(u"btnInventory")
        self.btnInventory.setCheckable(False)

        self.verticalLayout.addWidget(self.btnInventory)

        self.btnSuppliers = QPushButton(self.navigationFrame)
        self.btnSuppliers.setObjectName(u"btnSuppliers")
        self.btnSuppliers.setCheckable(False)

        self.verticalLayout.addWidget(self.btnSuppliers)

        self.btnReports = QPushButton(self.navigationFrame)
        self.btnReports.setObjectName(u"btnReports")
        self.btnReports.setCheckable(False)

        self.verticalLayout.addWidget(self.btnReports)

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

        self.stackedWidget.setCurrentIndex(9)


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
        self.btnTechnicians.setText(QCoreApplication.translate("MainWindow", u"Technicians", None))
        self.btnInventory.setText(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.btnSuppliers.setText(QCoreApplication.translate("MainWindow", u"Suppliers", None))
        self.btnReports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.btnUsers.setText(QCoreApplication.translate("MainWindow", u"Users", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btnAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.btnLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

