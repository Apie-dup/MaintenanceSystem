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
    QSpacerItem, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)

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

        self.btnPM = QPushButton(self.frameNavigation)
        self.btnPM.setObjectName(u"btnPM")

        self.verticalLayout.addWidget(self.btnPM)

        self.btnInventory = QPushButton(self.frameNavigation)
        self.btnInventory.setObjectName(u"btnInventory")

        self.verticalLayout.addWidget(self.btnInventory)

        self.btnReports = QPushButton(self.frameNavigation)
        self.btnReports.setObjectName(u"btnReports")

        self.verticalLayout.addWidget(self.btnReports)

        self.btnSettings = QPushButton(self.frameNavigation)
        self.btnSettings.setObjectName(u"btnSettings")

        self.verticalLayout.addWidget(self.btnSettings)

        self.btnThecnicians = QPushButton(self.frameNavigation)
        self.btnThecnicians.setObjectName(u"btnThecnicians")

        self.verticalLayout.addWidget(self.btnThecnicians)

        self.btnSuppliers = QPushButton(self.frameNavigation)
        self.btnSuppliers.setObjectName(u"btnSuppliers")

        self.verticalLayout.addWidget(self.btnSuppliers)

        self.btnLookups = QPushButton(self.frameNavigation)
        self.btnLookups.setObjectName(u"btnLookups")

        self.verticalLayout.addWidget(self.btnLookups)

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
        self.frameAssets = QFrame(self.frameContent)
        self.frameAssets.setObjectName(u"frameAssets")
        self.frameAssets.setMinimumSize(QSize(0, 0))
        self.frameAssets.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameAssets.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frameAssets)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lblAssetsValue = QLabel(self.frameAssets)
        self.lblAssetsValue.setObjectName(u"lblAssetsValue")
        font = QFont()
        font.setPointSize(24)
        self.lblAssetsValue.setFont(font)

        self.gridLayout_3.addWidget(self.lblAssetsValue, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lblAssetsTitle = QLabel(self.frameAssets)
        self.lblAssetsTitle.setObjectName(u"lblAssetsTitle")

        self.gridLayout_3.addWidget(self.lblAssetsTitle, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frameAssets, 1, 0, 1, 1)

        self.lblTitle = QLabel(self.frameContent)
        self.lblTitle.setObjectName(u"lblTitle")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.lblTitle.setFont(font1)

        self.gridLayout_2.addWidget(self.lblTitle, 0, 1, 1, 1)

        self.framePMDue = QFrame(self.frameContent)
        self.framePMDue.setObjectName(u"framePMDue")
        self.framePMDue.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePMDue.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.framePMDue)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lblPMDueTitle = QLabel(self.framePMDue)
        self.lblPMDueTitle.setObjectName(u"lblPMDueTitle")

        self.gridLayout_5.addWidget(self.lblPMDueTitle, 0, 0, 1, 1)

        self.lblPMDueValue = QLabel(self.framePMDue)
        self.lblPMDueValue.setObjectName(u"lblPMDueValue")
        self.lblPMDueValue.setFont(font)

        self.gridLayout_5.addWidget(self.lblPMDueValue, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.framePMDue, 2, 0, 1, 1)

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


        self.gridLayout_2.addWidget(self.frameLowStock, 1, 2, 1, 1)

        self.frame = QFrame(self.frameContent)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lblTechnisiansTitle = QLabel(self.frame)
        self.lblTechnisiansTitle.setObjectName(u"lblTechnisiansTitle")

        self.gridLayout_7.addWidget(self.lblTechnisiansTitle, 0, 0, 1, 1)

        self.lblTechniciansValue = QLabel(self.frame)
        self.lblTechniciansValue.setObjectName(u"lblTechniciansValue")
        self.lblTechniciansValue.setFont(font)

        self.gridLayout_7.addWidget(self.lblTechniciansValue, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame, 2, 1, 1, 1)

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


        self.gridLayout_2.addWidget(self.frameOpenWorkOrders, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.frameContent)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lblSuppliersTitle = QLabel(self.frame_2)
        self.lblSuppliersTitle.setObjectName(u"lblSuppliersTitle")

        self.gridLayout_8.addWidget(self.lblSuppliersTitle, 0, 0, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_8.addWidget(self.label, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_2, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.frameContent, 0, 1, 1, 1)

        DashboardWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DashboardWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
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
        self.btnDashboard.setText(QCoreApplication.translate("DashboardWindow", u"Dashboard", None))
        self.btnAssets.setText(QCoreApplication.translate("DashboardWindow", u"Assets", None))
        self.btnWorkOrders.setText(QCoreApplication.translate("DashboardWindow", u"Work Orders", None))
        self.btnPM.setText(QCoreApplication.translate("DashboardWindow", u"Preventive Maitenance", None))
        self.btnInventory.setText(QCoreApplication.translate("DashboardWindow", u"Inventory", None))
        self.btnReports.setText(QCoreApplication.translate("DashboardWindow", u"Reports", None))
        self.btnSettings.setText(QCoreApplication.translate("DashboardWindow", u"Settings", None))
        self.btnThecnicians.setText(QCoreApplication.translate("DashboardWindow", u"Technicians", None))
        self.btnSuppliers.setText(QCoreApplication.translate("DashboardWindow", u"Suppliers", None))
        self.btnLookups.setText(QCoreApplication.translate("DashboardWindow", u"Lookup Management", None))
        self.btnLogout.setText(QCoreApplication.translate("DashboardWindow", u"Logout", None))
        self.lblAssetsValue.setText(QCoreApplication.translate("DashboardWindow", u"123", None))
        self.lblAssetsTitle.setText(QCoreApplication.translate("DashboardWindow", u"Assets", None))
        self.lblTitle.setText(QCoreApplication.translate("DashboardWindow", u"Dashboard", None))
        self.lblPMDueTitle.setText(QCoreApplication.translate("DashboardWindow", u"PM Due", None))
        self.lblPMDueValue.setText(QCoreApplication.translate("DashboardWindow", u"123", None))
        self.lblLowStockTitle.setText(QCoreApplication.translate("DashboardWindow", u"Low Stock", None))
        self.lblLowStockValue.setText(QCoreApplication.translate("DashboardWindow", u"123", None))
        self.lblTechnisiansTitle.setText(QCoreApplication.translate("DashboardWindow", u"Technisians", None))
        self.lblTechniciansValue.setText(QCoreApplication.translate("DashboardWindow", u"123", None))
        self.lblOpenWorkOrdersValue.setText(QCoreApplication.translate("DashboardWindow", u"123", None))
        self.lblOpenWorkOrdersTitle.setText(QCoreApplication.translate("DashboardWindow", u"Open Work Orders", None))
        self.lblSuppliersTitle.setText(QCoreApplication.translate("DashboardWindow", u"Suppliers", None))
        self.label.setText(QCoreApplication.translate("DashboardWindow", u"123", None))
        self.mainToolBar.setWindowTitle(QCoreApplication.translate("DashboardWindow", u"toolBar", None))
    # retranslateUi

