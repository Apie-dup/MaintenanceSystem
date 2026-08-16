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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_ReportsPage(object):
    def setupUi(self, ReportsPage):
        if not ReportsPage.objectName():
            ReportsPage.setObjectName(u"ReportsPage")
        ReportsPage.resize(777, 614)
        self.verticalLayout_2 = QVBoxLayout(ReportsPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupReportsOption = QGroupBox(ReportsPage)
        self.groupReportsOption.setObjectName(u"groupReportsOption")
        self.formLayout = QFormLayout(self.groupReportsOption)
        self.formLayout.setObjectName(u"formLayout")
        self.lblReportType = QLabel(self.groupReportsOption)
        self.lblReportType.setObjectName(u"lblReportType")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblReportType)

        self.cmbReportType = QComboBox(self.groupReportsOption)
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.setObjectName(u"cmbReportType")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbReportType)

        self.lblFromDate = QLabel(self.groupReportsOption)
        self.lblFromDate.setObjectName(u"lblFromDate")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblFromDate)

        self.dtFromDate = QDateEdit(self.groupReportsOption)
        self.dtFromDate.setObjectName(u"dtFromDate")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dtFromDate)

        self.lblToDate = QLabel(self.groupReportsOption)
        self.lblToDate.setObjectName(u"lblToDate")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblToDate)

        self.dtToDate = QDateEdit(self.groupReportsOption)
        self.dtToDate.setObjectName(u"dtToDate")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dtToDate)

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


        self.formLayout.setLayout(3, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupReportsOption)

        self.groupReportsResult = QGroupBox(ReportsPage)
        self.groupReportsResult.setObjectName(u"groupReportsResult")
        self.verticalLayout = QVBoxLayout(self.groupReportsResult)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tblReport = QTableWidget(self.groupReportsResult)
        self.tblReport.setObjectName(u"tblReport")

        self.verticalLayout.addWidget(self.tblReport)


        self.verticalLayout_2.addWidget(self.groupReportsResult)

        self.lblStatus = QLabel(ReportsPage)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout_2.addWidget(self.lblStatus)


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
        self.cmbReportType.setItemText(3, QCoreApplication.translate("ReportsPage", u"Preventive Maintenance", None))
        self.cmbReportType.setItemText(4, QCoreApplication.translate("ReportsPage", u"Technician Performance", None))

        self.lblFromDate.setText(QCoreApplication.translate("ReportsPage", u"From Date:", None))
        self.lblToDate.setText(QCoreApplication.translate("ReportsPage", u"To Date:", None))
        self.btnGenerate.setText(QCoreApplication.translate("ReportsPage", u"Generate Report", None))
        self.btnExport.setText(QCoreApplication.translate("ReportsPage", u"Export", None))
        self.btnClear.setText(QCoreApplication.translate("ReportsPage", u"Clear Filters", None))
        self.groupReportsResult.setTitle(QCoreApplication.translate("ReportsPage", u"Reports Result ", None))
        self.lblStatus.setText(QCoreApplication.translate("ReportsPage", u"Showing  0 Records ", None))
    # retranslateUi

