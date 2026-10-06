# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehicle_sop_inspection_page.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_VehicleSopInspectionPage(object):
    def setupUi(self, VehicleSopInspectionPage):
        if not VehicleSopInspectionPage.objectName():
            VehicleSopInspectionPage.setObjectName(u"VehicleSopInspectionPage")
        VehicleSopInspectionPage.resize(795, 475)
        self.verticalLayout = QVBoxLayout(VehicleSopInspectionPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(VehicleSopInspectionPage)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSearch = QLabel(VehicleSopInspectionPage)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(VehicleSopInspectionPage)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblInspections = QTableWidget(VehicleSopInspectionPage)
        if (self.tblInspections.columnCount() < 8):
            self.tblInspections.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblInspections.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblInspections.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblInspections.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblInspections.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblInspections.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblInspections.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblInspections.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblInspections.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tblInspections.setObjectName(u"tblInspections")
        self.tblInspections.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.tblInspections)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnNew = QPushButton(VehicleSopInspectionPage)
        self.btnNew.setObjectName(u"btnNew")

        self.horizontalLayout_2.addWidget(self.btnNew)

        self.btnOpen = QPushButton(VehicleSopInspectionPage)
        self.btnOpen.setObjectName(u"btnOpen")

        self.horizontalLayout_2.addWidget(self.btnOpen)

        self.btnPrint = QPushButton(VehicleSopInspectionPage)
        self.btnPrint.setObjectName(u"btnPrint")

        self.horizontalLayout_2.addWidget(self.btnPrint)

        self.btnDelete = QPushButton(VehicleSopInspectionPage)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.btnRefresh = QPushButton(VehicleSopInspectionPage)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(VehicleSopInspectionPage)

        QMetaObject.connectSlotsByName(VehicleSopInspectionPage)
    # setupUi

    def retranslateUi(self, VehicleSopInspectionPage):
        VehicleSopInspectionPage.setWindowTitle(QCoreApplication.translate("VehicleSopInspectionPage", u"Vehicle SOP Inspections Page", None))
        self.lblTitle.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"SOP Inspections", None))
        self.lblSearch.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("VehicleSopInspectionPage", u"Search inspections...", None))
        ___qtablewidgetitem = self.tblInspections.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"Inspection No.", None))
        ___qtablewidgetitem1 = self.tblInspections.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"Date", None))
        ___qtablewidgetitem2 = self.tblInspections.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"New Column", None))
        ___qtablewidgetitem3 = self.tblInspections.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"Vehicle ? Asset", None))
        ___qtablewidgetitem4 = self.tblInspections.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"SOP", None))
        ___qtablewidgetitem5 = self.tblInspections.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"Frequency", None))
        ___qtablewidgetitem6 = self.tblInspections.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"Operator", None))
        ___qtablewidgetitem7 = self.tblInspections.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"Status", None))
        self.btnNew.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"New Inspection", None))
        self.btnOpen.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"Open / View", None))
        self.btnPrint.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"Print Completed Inspection", None))
        self.btnDelete.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"Delete", None))
        self.btnRefresh.setText(QCoreApplication.translate("VehicleSopInspectionPage", u"Refresh", None))
    # retranslateUi

