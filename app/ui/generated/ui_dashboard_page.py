# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_DashboardPage(object):
    def setupUi(self, DashboardPage):
        if not DashboardPage.objectName():
            DashboardPage.setObjectName(u"DashboardPage")
        DashboardPage.resize(930, 572)
        self.frameContent = QFrame(DashboardPage)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setGeometry(QRect(9, 9, 948, 795))
        self.frameContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameContent.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frameContent)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.dashboardSubtitle = QLabel(self.frameContent)
        self.dashboardSubtitle.setObjectName(u"dashboardSubtitle")
        self.dashboardSubtitle.setStyleSheet(u"font-size: 16px;")

        self.gridLayout_2.addWidget(self.dashboardSubtitle, 2, 0, 1, 1)

        self.dashboardSection_2 = QGroupBox(self.frameContent)
        self.dashboardSection_2.setObjectName(u"dashboardSection_2")
        self.dashboardSection_2.setFlat(True)
        self.gridLayout_4 = QGridLayout(self.dashboardSection_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tblPMDue = QTableWidget(self.dashboardSection_2)
        if (self.tblPMDue.columnCount() < 5):
            self.tblPMDue.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblPMDue.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblPMDue.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblPMDue.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblPMDue.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblPMDue.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblPMDue.setObjectName(u"tblPMDue")

        self.gridLayout_4.addWidget(self.tblPMDue, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.dashboardSection_2, 5, 0, 1, 1)

        self.dashboardSection = QGroupBox(self.frameContent)
        self.dashboardSection.setObjectName(u"dashboardSection")
        self.dashboardSection.setFlat(True)
        self.gridLayout_3 = QGridLayout(self.dashboardSection)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tblUrgentWorkOrders = QTableWidget(self.dashboardSection)
        if (self.tblUrgentWorkOrders.columnCount() < 5):
            self.tblUrgentWorkOrders.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblUrgentWorkOrders.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblUrgentWorkOrders.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblUrgentWorkOrders.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblUrgentWorkOrders.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblUrgentWorkOrders.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tblUrgentWorkOrders.setObjectName(u"tblUrgentWorkOrders")

        self.gridLayout_3.addWidget(self.tblUrgentWorkOrders, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.dashboardSection, 4, 0, 1, 1)

        self.overviewCardsLayout = QGridLayout()
        self.overviewCardsLayout.setObjectName(u"overviewCardsLayout")
        self.cardLowStock = QFrame(self.frameContent)
        self.cardLowStock.setObjectName(u"cardLowStock")
        self.cardLowStock.setMinimumSize(QSize(180, 115))
        self.cardLowStock.setFrameShape(QFrame.Shape.StyledPanel)
        self._6 = QVBoxLayout(self.cardLowStock)
        self._6.setObjectName(u"_6")
        self.lbLowStockTitle = QLabel(self.cardLowStock)
        self.lbLowStockTitle.setObjectName(u"lbLowStockTitle")

        self._6.addWidget(self.lbLowStockTitle)

        self.lblLowStockValue = QLabel(self.cardLowStock)
        self.lblLowStockValue.setObjectName(u"lblLowStockValue")
        font = QFont()
        font.setPointSize(18)
        self.lblLowStockValue.setFont(font)
        self.lblLowStockValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._6.addWidget(self.lblLowStockValue)

        self.lblLowStockHint = QLabel(self.cardLowStock)
        self.lblLowStockHint.setObjectName(u"lblLowStockHint")

        self._6.addWidget(self.lblLowStockHint)


        self.overviewCardsLayout.addWidget(self.cardLowStock, 1, 1, 1, 1)

        self.cardAssets = QFrame(self.frameContent)
        self.cardAssets.setObjectName(u"cardAssets")
        self.cardAssets.setMinimumSize(QSize(180, 115))
        self.cardAssets.setFrameShape(QFrame.Shape.StyledPanel)
        self.gridLayout = QGridLayout(self.cardAssets)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblAssetsValue = QLabel(self.cardAssets)
        self.lblAssetsValue.setObjectName(u"lblAssetsValue")
        self.lblAssetsValue.setFont(font)
        self.lblAssetsValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lblAssetsValue, 1, 0, 1, 1)

        self.labelAssetsTitle = QLabel(self.cardAssets)
        self.labelAssetsTitle.setObjectName(u"labelAssetsTitle")

        self.gridLayout.addWidget(self.labelAssetsTitle, 0, 0, 1, 1)

        self.lblAssetsHint = QLabel(self.cardAssets)
        self.lblAssetsHint.setObjectName(u"lblAssetsHint")

        self.gridLayout.addWidget(self.lblAssetsHint, 2, 0, 1, 1)


        self.overviewCardsLayout.addWidget(self.cardAssets, 0, 0, 1, 1)

        self.cardNext7Days = QFrame(self.frameContent)
        self.cardNext7Days.setObjectName(u"cardNext7Days")
        self.cardNext7Days.setMinimumSize(QSize(180, 115))
        self.cardNext7Days.setFrameShape(QFrame.Shape.StyledPanel)
        self._5 = QVBoxLayout(self.cardNext7Days)
        self._5.setObjectName(u"_5")
        self.lblPMDueWeekTitle_2 = QLabel(self.cardNext7Days)
        self.lblPMDueWeekTitle_2.setObjectName(u"lblPMDueWeekTitle_2")

        self._5.addWidget(self.lblPMDueWeekTitle_2)

        self.lblPMDueWeekValue_2 = QLabel(self.cardNext7Days)
        self.lblPMDueWeekValue_2.setObjectName(u"lblPMDueWeekValue_2")
        self.lblPMDueWeekValue_2.setFont(font)
        self.lblPMDueWeekValue_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._5.addWidget(self.lblPMDueWeekValue_2)

        self.lblPMDueWeekHint_2 = QLabel(self.cardNext7Days)
        self.lblPMDueWeekHint_2.setObjectName(u"lblPMDueWeekHint_2")

        self._5.addWidget(self.lblPMDueWeekHint_2)


        self.overviewCardsLayout.addWidget(self.cardNext7Days, 1, 0, 1, 1)

        self.cardPMOverdue = QFrame(self.frameContent)
        self.cardPMOverdue.setObjectName(u"cardPMOverdue")
        self.cardPMOverdue.setMinimumSize(QSize(180, 115))
        self.cardPMOverdue.setFrameShape(QFrame.Shape.StyledPanel)
        self._4 = QVBoxLayout(self.cardPMOverdue)
        self._4.setObjectName(u"_4")
        self.dashboardCard_4 = QLabel(self.cardPMOverdue)
        self.dashboardCard_4.setObjectName(u"dashboardCard_4")

        self._4.addWidget(self.dashboardCard_4)

        self.lblPMOverdueValue = QLabel(self.cardPMOverdue)
        self.lblPMOverdueValue.setObjectName(u"lblPMOverdueValue")
        self.lblPMOverdueValue.setFont(font)
        self.lblPMOverdueValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._4.addWidget(self.lblPMOverdueValue)

        self.lblPMOverDueHint = QLabel(self.cardPMOverdue)
        self.lblPMOverDueHint.setObjectName(u"lblPMOverDueHint")

        self._4.addWidget(self.lblPMOverDueHint)


        self.overviewCardsLayout.addWidget(self.cardPMOverdue, 0, 4, 1, 1)

        self.cardTechnicians = QFrame(self.frameContent)
        self.cardTechnicians.setObjectName(u"cardTechnicians")
        self.cardTechnicians.setMinimumSize(QSize(180, 115))
        self.cardTechnicians.setFrameShape(QFrame.Shape.StyledPanel)
        self._7 = QVBoxLayout(self.cardTechnicians)
        self._7.setObjectName(u"_7")
        self.lblTechniciansTitle = QLabel(self.cardTechnicians)
        self.lblTechniciansTitle.setObjectName(u"lblTechniciansTitle")

        self._7.addWidget(self.lblTechniciansTitle)

        self.lblTechniciansValue = QLabel(self.cardTechnicians)
        self.lblTechniciansValue.setObjectName(u"lblTechniciansValue")
        self.lblTechniciansValue.setFont(font)
        self.lblTechniciansValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._7.addWidget(self.lblTechniciansValue)

        self.lblTechniciansHint = QLabel(self.cardTechnicians)
        self.lblTechniciansHint.setObjectName(u"lblTechniciansHint")

        self._7.addWidget(self.lblTechniciansHint)


        self.overviewCardsLayout.addWidget(self.cardTechnicians, 1, 2, 1, 1)

        self.cardOpenWOs = QFrame(self.frameContent)
        self.cardOpenWOs.setObjectName(u"cardOpenWOs")
        self.cardOpenWOs.setMinimumSize(QSize(180, 115))
        self.cardOpenWOs.setFrameShape(QFrame.Shape.StyledPanel)
        self._2 = QVBoxLayout(self.cardOpenWOs)
        self._2.setObjectName(u"_2")
        self.lblOpenWorkOrdersTitle = QLabel(self.cardOpenWOs)
        self.lblOpenWorkOrdersTitle.setObjectName(u"lblOpenWorkOrdersTitle")

        self._2.addWidget(self.lblOpenWorkOrdersTitle)

        self.lblOpenWorkOrdersValue = QLabel(self.cardOpenWOs)
        self.lblOpenWorkOrdersValue.setObjectName(u"lblOpenWorkOrdersValue")
        self.lblOpenWorkOrdersValue.setFont(font)
        self.lblOpenWorkOrdersValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._2.addWidget(self.lblOpenWorkOrdersValue)

        self.lblOpenWorkOrdersHint = QLabel(self.cardOpenWOs)
        self.lblOpenWorkOrdersHint.setObjectName(u"lblOpenWorkOrdersHint")

        self._2.addWidget(self.lblOpenWorkOrdersHint)


        self.overviewCardsLayout.addWidget(self.cardOpenWOs, 0, 1, 1, 1)

        self.cardPMDueToday = QFrame(self.frameContent)
        self.cardPMDueToday.setObjectName(u"cardPMDueToday")
        self.cardPMDueToday.setMinimumSize(QSize(180, 115))
        self.cardPMDueToday.setFrameShape(QFrame.Shape.StyledPanel)
        self._3 = QVBoxLayout(self.cardPMDueToday)
        self._3.setObjectName(u"_3")
        self.lblPMDueWeekTitle = QLabel(self.cardPMDueToday)
        self.lblPMDueWeekTitle.setObjectName(u"lblPMDueWeekTitle")

        self._3.addWidget(self.lblPMDueWeekTitle)

        self.lblPMDueWeekValue = QLabel(self.cardPMDueToday)
        self.lblPMDueWeekValue.setObjectName(u"lblPMDueWeekValue")
        self.lblPMDueWeekValue.setFont(font)
        self.lblPMDueWeekValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._3.addWidget(self.lblPMDueWeekValue)

        self.lblPMDueWeekHint = QLabel(self.cardPMDueToday)
        self.lblPMDueWeekHint.setObjectName(u"lblPMDueWeekHint")

        self._3.addWidget(self.lblPMDueWeekHint)


        self.overviewCardsLayout.addWidget(self.cardPMDueToday, 0, 2, 1, 1)

        self.cardVehicleDefects = QFrame(self.frameContent)
        self.cardVehicleDefects.setObjectName(u"cardVehicleDefects")
        self.cardVehicleDefects.setFrameShape(QFrame.Shape.StyledPanel)
        self.cardVehicleDefects.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.cardVehicleDefects)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lblVehicleDefectsTitle = QLabel(self.cardVehicleDefects)
        self.lblVehicleDefectsTitle.setObjectName(u"lblVehicleDefectsTitle")

        self.gridLayout_5.addWidget(self.lblVehicleDefectsTitle, 0, 0, 1, 1)

        self.lblVehicleDefectsValue = QLabel(self.cardVehicleDefects)
        self.lblVehicleDefectsValue.setObjectName(u"lblVehicleDefectsValue")
        self.lblVehicleDefectsValue.setFont(font)

        self.gridLayout_5.addWidget(self.lblVehicleDefectsValue, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btnVehicleDefects = QPushButton(self.cardVehicleDefects)
        self.btnVehicleDefects.setObjectName(u"btnVehicleDefects")
        self.btnVehicleDefects.setFlat(True)

        self.gridLayout_5.addWidget(self.btnVehicleDefects, 2, 0, 1, 1)


        self.overviewCardsLayout.addWidget(self.cardVehicleDefects, 0, 3, 1, 1)

        self.cardInventoryValue = QFrame(self.frameContent)
        self.cardInventoryValue.setObjectName(u"cardInventoryValue")
        self.cardInventoryValue.setMinimumSize(QSize(180, 115))
        self.cardInventoryValue.setFrameShape(QFrame.Shape.StyledPanel)
        self._8 = QVBoxLayout(self.cardInventoryValue)
        self._8.setObjectName(u"_8")
        self.lblInventoryValueTitle = QLabel(self.cardInventoryValue)
        self.lblInventoryValueTitle.setObjectName(u"lblInventoryValueTitle")

        self._8.addWidget(self.lblInventoryValueTitle)

        self.lblInventoryValueValue = QLabel(self.cardInventoryValue)
        self.lblInventoryValueValue.setObjectName(u"lblInventoryValueValue")
        self.lblInventoryValueValue.setFont(font)

        self._8.addWidget(self.lblInventoryValueValue)

        self.lblInvetoryValueHint = QLabel(self.cardInventoryValue)
        self.lblInvetoryValueHint.setObjectName(u"lblInvetoryValueHint")

        self._8.addWidget(self.lblInvetoryValueHint)


        self.overviewCardsLayout.addWidget(self.cardInventoryValue, 1, 3, 1, 1)


        self.gridLayout_2.addLayout(self.overviewCardsLayout, 3, 0, 1, 1)

        self.dashboardTitle = QLabel(self.frameContent)
        self.dashboardTitle.setObjectName(u"dashboardTitle")
        self.dashboardTitle.setStyleSheet(u"font-size: 22px; font-weight: bold;")

        self.gridLayout_2.addWidget(self.dashboardTitle, 1, 0, 1, 1)


        self.retranslateUi(DashboardPage)

        QMetaObject.connectSlotsByName(DashboardPage)
    # setupUi

    def retranslateUi(self, DashboardPage):
        DashboardPage.setWindowTitle(QCoreApplication.translate("DashboardPage", u"Dash Board Page", None))
        self.dashboardSubtitle.setText(QCoreApplication.translate("DashboardPage", u"Maintenance overview for 02 August 2026", None))
        self.dashboardSection_2.setTitle(QCoreApplication.translate("DashboardPage", u"PM Due", None))
        ___qtablewidgetitem = self.tblPMDue.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DashboardPage", u"PM Number", None))
        ___qtablewidgetitem1 = self.tblPMDue.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DashboardPage", u"Asset", None))
        ___qtablewidgetitem2 = self.tblPMDue.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DashboardPage", u"Task", None))
        ___qtablewidgetitem3 = self.tblPMDue.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DashboardPage", u"Next Due", None))
        ___qtablewidgetitem4 = self.tblPMDue.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DashboardPage", u"Status", None))
        self.dashboardSection.setTitle(QCoreApplication.translate("DashboardPage", u"Urgent Work Orders", None))
        ___qtablewidgetitem5 = self.tblUrgentWorkOrders.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DashboardPage", u"Work Order", None))
        ___qtablewidgetitem6 = self.tblUrgentWorkOrders.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DashboardPage", u"Asset", None))
        ___qtablewidgetitem7 = self.tblUrgentWorkOrders.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DashboardPage", u"Priority", None))
        ___qtablewidgetitem8 = self.tblUrgentWorkOrders.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DashboardPage", u"Due", None))
        ___qtablewidgetitem9 = self.tblUrgentWorkOrders.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DashboardPage", u"Status", None))
        self.lbLowStockTitle.setText(QCoreApplication.translate("DashboardPage", u"Low Stock", None))
        self.lblLowStockValue.setText(QCoreApplication.translate("DashboardPage", u"123", None))
        self.lblLowStockHint.setText(QCoreApplication.translate("DashboardPage", u"Stock running low", None))
        self.lblAssetsValue.setText(QCoreApplication.translate("DashboardPage", u"123", None))
        self.labelAssetsTitle.setText(QCoreApplication.translate("DashboardPage", u"Assets", None))
        self.lblAssetsHint.setText(QCoreApplication.translate("DashboardPage", u"Registered", None))
        self.lblPMDueWeekTitle_2.setText(QCoreApplication.translate("DashboardPage", u"Next 7 Days", None))
        self.lblPMDueWeekValue_2.setText(QCoreApplication.translate("DashboardPage", u"123", None))
        self.lblPMDueWeekHint_2.setText(QCoreApplication.translate("DashboardPage", u"Upcomming PM", None))
        self.dashboardCard_4.setText(QCoreApplication.translate("DashboardPage", u"PM Overdue", None))
        self.lblPMOverdueValue.setText(QCoreApplication.translate("DashboardPage", u"123", None))
        self.lblPMOverDueHint.setText(QCoreApplication.translate("DashboardPage", u"Past due date", None))
        self.lblTechniciansTitle.setText(QCoreApplication.translate("DashboardPage", u"Technicians", None))
        self.lblTechniciansValue.setText(QCoreApplication.translate("DashboardPage", u"123", None))
        self.lblTechniciansHint.setText(QCoreApplication.translate("DashboardPage", u"Active technicians", None))
        self.lblOpenWorkOrdersTitle.setText(QCoreApplication.translate("DashboardPage", u"Open WOs", None))
        self.lblOpenWorkOrdersValue.setText(QCoreApplication.translate("DashboardPage", u"123", None))
        self.lblOpenWorkOrdersHint.setText(QCoreApplication.translate("DashboardPage", u"Currently open", None))
        self.lblPMDueWeekTitle.setText(QCoreApplication.translate("DashboardPage", u"PM Due Today", None))
        self.lblPMDueWeekValue.setText(QCoreApplication.translate("DashboardPage", u"123", None))
        self.lblPMDueWeekHint.setText(QCoreApplication.translate("DashboardPage", u"Due today", None))
        self.lblVehicleDefectsTitle.setText(QCoreApplication.translate("DashboardPage", u"Unresolved Vehicle Defects", None))
        self.lblVehicleDefectsValue.setText(QCoreApplication.translate("DashboardPage", u"123", None))
        self.btnVehicleDefects.setText(QCoreApplication.translate("DashboardPage", u"View Defects", None))
        self.lblInventoryValueTitle.setText(QCoreApplication.translate("DashboardPage", u"Inventory Value", None))
        self.lblInventoryValueValue.setText(QCoreApplication.translate("DashboardPage", u"N$ 248,500.00", None))
        self.lblInvetoryValueHint.setText(QCoreApplication.translate("DashboardPage", u"Current stock value", None))
        self.dashboardTitle.setText(QCoreApplication.translate("DashboardPage", u"Dashboard", None))
    # retranslateUi

