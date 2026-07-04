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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_DashboardWindow(object):
    def setupUi(self, DashboardWindow):
        if not DashboardWindow.objectName():
            DashboardWindow.setObjectName(u"DashboardWindow")
        DashboardWindow.resize(800, 600)
        self.centralwidget = QWidget(DashboardWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
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

        self.btnDashboard = QPushButton(self.frameNavigation)
        self.btnDashboard.setObjectName(u"btnDashboard")

        self.verticalLayout.addWidget(self.btnDashboard)

        self.btnAssets = QPushButton(self.frameNavigation)
        self.btnAssets.setObjectName(u"btnAssets")

        self.verticalLayout.addWidget(self.btnAssets)

        self.btnWorkOrders = QPushButton(self.frameNavigation)
        self.btnWorkOrders.setObjectName(u"btnWorkOrders")

        self.verticalLayout.addWidget(self.btnWorkOrders)

        self.btnPreventive = QPushButton(self.frameNavigation)
        self.btnPreventive.setObjectName(u"btnPreventive")

        self.verticalLayout.addWidget(self.btnPreventive)

        self.btnInventory = QPushButton(self.frameNavigation)
        self.btnInventory.setObjectName(u"btnInventory")

        self.verticalLayout.addWidget(self.btnInventory)

        self.btnReports = QPushButton(self.frameNavigation)
        self.btnReports.setObjectName(u"btnReports")

        self.verticalLayout.addWidget(self.btnReports)

        self.btnSettings = QPushButton(self.frameNavigation)
        self.btnSettings.setObjectName(u"btnSettings")

        self.verticalLayout.addWidget(self.btnSettings)

        self.verticalSpacer = QSpacerItem(20, 203, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnLogout = QPushButton(self.frameNavigation)
        self.btnLogout.setObjectName(u"btnLogout")

        self.verticalLayout.addWidget(self.btnLogout)


        self.gridLayout.addWidget(self.frameNavigation, 0, 0, 1, 1)

        self.frameContent = QFrame(self.centralwidget)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameContent.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frameContent)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.framePMDue = QFrame(self.frameContent)
        self.framePMDue.setObjectName(u"framePMDue")
        self.framePMDue.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePMDue.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.framePMDue)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lblPMDueTitle = QLabel(self.framePMDue)
        self.lblPMDueTitle.setObjectName(u"lblPMDueTitle")

        self.gridLayout_5.addWidget(self.lblPMDueTitle, 0, 0, 1, 1)

        self.lblPMDUEValue = QLabel(self.framePMDue)
        self.lblPMDUEValue.setObjectName(u"lblPMDUEValue")
        font = QFont()
        font.setPointSize(24)
        self.lblPMDUEValue.setFont(font)

        self.gridLayout_5.addWidget(self.lblPMDUEValue, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.framePMDue, 2, 0, 1, 1)

        self.lblTitle = QLabel(self.frameContent)
        self.lblTitle.setObjectName(u"lblTitle")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.lblTitle.setFont(font1)

        self.gridLayout_2.addWidget(self.lblTitle, 0, 1, 1, 1)

        self.frameAssets = QFrame(self.frameContent)
        self.frameAssets.setObjectName(u"frameAssets")
        self.frameAssets.setMinimumSize(QSize(0, 0))
        self.frameAssets.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameAssets.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frameAssets)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lblAssetsTitle = QLabel(self.frameAssets)
        self.lblAssetsTitle.setObjectName(u"lblAssetsTitle")

        self.gridLayout_3.addWidget(self.lblAssetsTitle, 0, 0, 1, 1)

        self.lblAssetsValue = QLabel(self.frameAssets)
        self.lblAssetsValue.setObjectName(u"lblAssetsValue")
        self.lblAssetsValue.setFont(font)

        self.gridLayout_3.addWidget(self.lblAssetsValue, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.frameAssets, 1, 0, 1, 1)

        self.frameLowStock = QFrame(self.frameContent)
        self.frameLowStock.setObjectName(u"frameLowStock")
        self.frameLowStock.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLowStock.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frameLowStock)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lblLowStockTitle = QLabel(self.frameLowStock)
        self.lblLowStockTitle.setObjectName(u"lblLowStockTitle")

        self.gridLayout_6.addWidget(self.lblLowStockTitle, 0, 0, 1, 1)

        self.lblLowStockValue = QLabel(self.frameLowStock)
        self.lblLowStockValue.setObjectName(u"lblLowStockValue")
        self.lblLowStockValue.setFont(font)

        self.gridLayout_6.addWidget(self.lblLowStockValue, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.frameLowStock, 2, 2, 1, 1)

        self.frameOpenWorkOrders = QFrame(self.frameContent)
        self.frameOpenWorkOrders.setObjectName(u"frameOpenWorkOrders")
        self.frameOpenWorkOrders.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameOpenWorkOrders.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frameOpenWorkOrders)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lblOpenWorkOrdersValue = QLabel(self.frameOpenWorkOrders)
        self.lblOpenWorkOrdersValue.setObjectName(u"lblOpenWorkOrdersValue")
        self.lblOpenWorkOrdersValue.setFont(font)

        self.gridLayout_4.addWidget(self.lblOpenWorkOrdersValue, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lblOpenWorkOrdersTitle = QLabel(self.frameOpenWorkOrders)
        self.lblOpenWorkOrdersTitle.setObjectName(u"lblOpenWorkOrdersTitle")

        self.gridLayout_4.addWidget(self.lblOpenWorkOrdersTitle, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frameOpenWorkOrders, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.frameContent, 0, 1, 1, 1)

        DashboardWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DashboardWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        DashboardWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DashboardWindow)
        self.statusbar.setObjectName(u"statusbar")
        DashboardWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DashboardWindow)

        QMetaObject.connectSlotsByName(DashboardWindow)
    # setupUi

    def retranslateUi(self, DashboardWindow):
        DashboardWindow.setWindowTitle(QCoreApplication.translate("DashboardWindow", u"Mantenance Management System", None))
        self.lblLogo.setText("")
        self.lblCompany.setText(QCoreApplication.translate("DashboardWindow", u"Your Organization", None))
        self.btnDashboard.setText(QCoreApplication.translate("DashboardWindow", u"Dashboard", None))
        self.btnAssets.setText(QCoreApplication.translate("DashboardWindow", u"Assets", None))
        self.btnWorkOrders.setText(QCoreApplication.translate("DashboardWindow", u"Work Orders", None))
        self.btnPreventive.setText(QCoreApplication.translate("DashboardWindow", u"Preventive Maitenance", None))
        self.btnInventory.setText(QCoreApplication.translate("DashboardWindow", u"Inventory", None))
        self.btnReports.setText(QCoreApplication.translate("DashboardWindow", u"Reports", None))
        self.btnSettings.setText(QCoreApplication.translate("DashboardWindow", u"Settings", None))
        self.btnLogout.setText(QCoreApplication.translate("DashboardWindow", u"Logout", None))
        self.lblPMDueTitle.setText(QCoreApplication.translate("DashboardWindow", u"PM Due", None))
        self.lblPMDUEValue.setText(QCoreApplication.translate("DashboardWindow", u"123", None))
        self.lblTitle.setText(QCoreApplication.translate("DashboardWindow", u"Dashboard", None))
        self.lblAssetsTitle.setText(QCoreApplication.translate("DashboardWindow", u"Assets", None))
        self.lblAssetsValue.setText(QCoreApplication.translate("DashboardWindow", u"123", None))
        self.lblLowStockTitle.setText(QCoreApplication.translate("DashboardWindow", u"Low Stock", None))
        self.lblLowStockValue.setText(QCoreApplication.translate("DashboardWindow", u"123", None))
        self.lblOpenWorkOrdersValue.setText(QCoreApplication.translate("DashboardWindow", u"123", None))
        self.lblOpenWorkOrdersTitle.setText(QCoreApplication.translate("DashboardWindow", u"Open Work Orders", None))
    # retranslateUi

