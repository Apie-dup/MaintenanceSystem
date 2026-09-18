# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reports_page.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ReportsPage(object):
    def setupUi(self, ReportsPage):
        if not ReportsPage.objectName():
            ReportsPage.setObjectName(u"ReportsPage")
        ReportsPage.resize(781, 622)
        self.verticalLayout_3 = QVBoxLayout(ReportsPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupReportsOption = QGroupBox(ReportsPage)
        self.groupReportsOption.setObjectName(u"groupReportsOption")
        self.verticalLayout_2 = QVBoxLayout(self.groupReportsOption)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblReportType = QLabel(self.groupReportsOption)
        self.lblReportType.setObjectName(u"lblReportType")

        self.horizontalLayout_3.addWidget(self.lblReportType)

        self.cmbReportType = QComboBox(self.groupReportsOption)
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.setObjectName(u"cmbReportType")

        self.horizontalLayout_3.addWidget(self.cmbReportType)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblFromDate = QLabel(self.groupReportsOption)
        self.lblFromDate.setObjectName(u"lblFromDate")

        self.horizontalLayout_4.addWidget(self.lblFromDate)

        self.dtFromDate = QDateEdit(self.groupReportsOption)
        self.dtFromDate.setObjectName(u"dtFromDate")
        self.dtFromDate.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dtFromDate)

        self.lblToDate = QLabel(self.groupReportsOption)
        self.lblToDate.setObjectName(u"lblToDate")

        self.horizontalLayout_4.addWidget(self.lblToDate)

        self.dtToDate = QDateEdit(self.groupReportsOption)
        self.dtToDate.setObjectName(u"dtToDate")
        self.dtToDate.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dtToDate)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblStatus_2 = QLabel(self.groupReportsOption)
        self.lblStatus_2.setObjectName(u"lblStatus_2")

        self.horizontalLayout_5.addWidget(self.lblStatus_2)

        self.cmbStatus = QComboBox(self.groupReportsOption)
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.horizontalLayout_5.addWidget(self.cmbStatus)

        self.lblAsset = QLabel(self.groupReportsOption)
        self.lblAsset.setObjectName(u"lblAsset")

        self.horizontalLayout_5.addWidget(self.lblAsset)

        self.cmbAsset = QComboBox(self.groupReportsOption)
        self.cmbAsset.setObjectName(u"cmbAsset")

        self.horizontalLayout_5.addWidget(self.cmbAsset)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnGenerate = QPushButton(self.groupReportsOption)
        self.btnGenerate.setObjectName(u"btnGenerate")

        self.horizontalLayout.addWidget(self.btnGenerate)

        self.btnExport = QPushButton(self.groupReportsOption)
        self.btnExport.setObjectName(u"btnExport")

        self.horizontalLayout.addWidget(self.btnExport)

        self.btnClear = QPushButton(self.groupReportsOption)
        self.btnClear.setObjectName(u"btnClear")

        self.horizontalLayout.addWidget(self.btnClear)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.groupReportsOption)

        self.groupBox = QGroupBox(ReportsPage)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblTotal = QLabel(self.frame)
        self.lblTotal.setObjectName(u"lblTotal")

        self.gridLayout.addWidget(self.lblTotal, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lblTotalValue = QLabel(self.frame)
        self.lblTotalValue.setObjectName(u"lblTotalValue")

        self.gridLayout.addWidget(self.lblTotalValue, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblOpen = QLabel(self.frame_2)
        self.lblOpen.setObjectName(u"lblOpen")

        self.gridLayout_2.addWidget(self.lblOpen, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lblOpenValue = QLabel(self.frame_2)
        self.lblOpenValue.setObjectName(u"lblOpenValue")

        self.gridLayout_2.addWidget(self.lblOpenValue, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lblCompleted = QLabel(self.frame_3)
        self.lblCompleted.setObjectName(u"lblCompleted")

        self.gridLayout_3.addWidget(self.lblCompleted, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lblCompletedValue = QLabel(self.frame_3)
        self.lblCompletedValue.setObjectName(u"lblCompletedValue")

        self.gridLayout_3.addWidget(self.lblCompletedValue, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lblTotalCost = QLabel(self.frame_4)
        self.lblTotalCost.setObjectName(u"lblTotalCost")

        self.gridLayout_4.addWidget(self.lblTotalCost, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lblTotalCostValue = QLabel(self.frame_4)
        self.lblTotalCostValue.setObjectName(u"lblTotalCostValue")

        self.gridLayout_4.addWidget(self.lblTotalCostValue, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupReportsResult = QGroupBox(ReportsPage)
        self.groupReportsResult.setObjectName(u"groupReportsResult")
        self.verticalLayout = QVBoxLayout(self.groupReportsResult)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tblReport = QTableWidget(self.groupReportsResult)
        self.tblReport.setObjectName(u"tblReport")

        self.verticalLayout.addWidget(self.tblReport)


        self.verticalLayout_3.addWidget(self.groupReportsResult)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblStatus = QLabel(ReportsPage)
        self.lblStatus.setObjectName(u"lblStatus")

        self.horizontalLayout_6.addWidget(self.lblStatus)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.btnPrint = QPushButton(ReportsPage)
        self.btnPrint.setObjectName(u"btnPrint")

        self.horizontalLayout_6.addWidget(self.btnPrint)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.retranslateUi(ReportsPage)

        QMetaObject.connectSlotsByName(ReportsPage)
    # setupUi

    def retranslateUi(self, ReportsPage):
        ReportsPage.setWindowTitle(QCoreApplication.translate("ReportsPage", u"Reports Page", None))
        self.groupReportsOption.setTitle(QCoreApplication.translate("ReportsPage", u"Reports Option", None))
        self.lblReportType.setText(QCoreApplication.translate("ReportsPage", u"Report Type:", None))
        self.cmbReportType.setItemText(0, QCoreApplication.translate("ReportsPage", u"Work Orders", None))
        self.cmbReportType.setItemText(1, QCoreApplication.translate("ReportsPage", u"Maintenance Costs", None))
        self.cmbReportType.setItemText(2, QCoreApplication.translate("ReportsPage", u"Inventory Stock", None))
        self.cmbReportType.setItemText(3, QCoreApplication.translate("ReportsPage", u"Inventory Transactions", None))
        self.cmbReportType.setItemText(4, QCoreApplication.translate("ReportsPage", u"Preventive Maintenance", None))
        self.cmbReportType.setItemText(5, QCoreApplication.translate("ReportsPage", u"Technician Performance", None))
        self.cmbReportType.setItemText(6, QCoreApplication.translate("ReportsPage", u"Low Stock / Reorder", None))
        self.cmbReportType.setItemText(7, QCoreApplication.translate("ReportsPage", u"Asset Maintenance History", None))
        self.cmbReportType.setItemText(8, QCoreApplication.translate("ReportsPage", u"Technician Work History", None))

        self.lblFromDate.setText(QCoreApplication.translate("ReportsPage", u"From Date:", None))
        self.lblToDate.setText(QCoreApplication.translate("ReportsPage", u"To Date:", None))
        self.lblStatus_2.setText(QCoreApplication.translate("ReportsPage", u"Status:", None))
        self.lblAsset.setText(QCoreApplication.translate("ReportsPage", u"Asset:", None))
        self.btnGenerate.setText(QCoreApplication.translate("ReportsPage", u"Generate Report", None))
        self.btnExport.setText(QCoreApplication.translate("ReportsPage", u"Export", None))
        self.btnClear.setText(QCoreApplication.translate("ReportsPage", u"Clear Filters", None))
        self.groupBox.setTitle(QCoreApplication.translate("ReportsPage", u"Report Summary", None))
        self.lblTotal.setText(QCoreApplication.translate("ReportsPage", u"Total", None))
        self.lblTotalValue.setText(QCoreApplication.translate("ReportsPage", u"0", None))
        self.lblOpen.setText(QCoreApplication.translate("ReportsPage", u"Open", None))
        self.lblOpenValue.setText(QCoreApplication.translate("ReportsPage", u"0", None))
        self.lblCompleted.setText(QCoreApplication.translate("ReportsPage", u"Completed", None))
        self.lblCompletedValue.setText(QCoreApplication.translate("ReportsPage", u"0", None))
        self.lblTotalCost.setText(QCoreApplication.translate("ReportsPage", u"Total Cost", None))
        self.lblTotalCostValue.setText(QCoreApplication.translate("ReportsPage", u"0.00", None))
        self.groupReportsResult.setTitle(QCoreApplication.translate("ReportsPage", u"Reports Result ", None))
        self.lblStatus.setText(QCoreApplication.translate("ReportsPage", u"Showing  0 Records ", None))
        self.btnPrint.setText(QCoreApplication.translate("ReportsPage", u"Print", None))
    # retranslateUi

