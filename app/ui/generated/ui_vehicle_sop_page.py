# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehicle_sop_page.ui'
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

class Ui_VehicleSopPage(object):
    def setupUi(self, VehicleSopPage):
        if not VehicleSopPage.objectName():
            VehicleSopPage.setObjectName(u"VehicleSopPage")
        VehicleSopPage.resize(650, 378)
        self.verticalLayout = QVBoxLayout(VehicleSopPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(VehicleSopPage)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSearch = QLabel(VehicleSopPage)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(VehicleSopPage)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblVehicleSops = QTableWidget(VehicleSopPage)
        if (self.tblVehicleSops.columnCount() < 6):
            self.tblVehicleSops.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblVehicleSops.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblVehicleSops.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblVehicleSops.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblVehicleSops.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblVehicleSops.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblVehicleSops.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblVehicleSops.setObjectName(u"tblVehicleSops")

        self.verticalLayout.addWidget(self.tblVehicleSops)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(VehicleSopPage)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(VehicleSopPage)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(VehicleSopPage)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.btnChecklist = QPushButton(VehicleSopPage)
        self.btnChecklist.setObjectName(u"btnChecklist")

        self.horizontalLayout_2.addWidget(self.btnChecklist)

        self.btnPrintInspectionForm = QPushButton(VehicleSopPage)
        self.btnPrintInspectionForm.setObjectName(u"btnPrintInspectionForm")

        self.horizontalLayout_2.addWidget(self.btnPrintInspectionForm)

        self.btnRefresh = QPushButton(VehicleSopPage)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(VehicleSopPage)

        QMetaObject.connectSlotsByName(VehicleSopPage)
    # setupUi

    def retranslateUi(self, VehicleSopPage):
        VehicleSopPage.setWindowTitle(QCoreApplication.translate("VehicleSopPage", u"Vehicle SOPs", None))
        self.lblTitle.setText(QCoreApplication.translate("VehicleSopPage", u"Vehicle SOPs", None))
        self.lblSearch.setText(QCoreApplication.translate("VehicleSopPage", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("VehicleSopPage", u"Search SOPs...", None))
        ___qtablewidgetitem = self.tblVehicleSops.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VehicleSopPage", u"SOP Number", None))
        ___qtablewidgetitem1 = self.tblVehicleSops.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VehicleSopPage", u"Asset No.", None))
        ___qtablewidgetitem2 = self.tblVehicleSops.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VehicleSopPage", u"Vehicle / Asset", None))
        ___qtablewidgetitem3 = self.tblVehicleSops.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VehicleSopPage", u"SOP Name", None))
        ___qtablewidgetitem4 = self.tblVehicleSops.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VehicleSopPage", u"Frequency", None))
        ___qtablewidgetitem5 = self.tblVehicleSops.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VehicleSopPage", u"Active", None))
        self.btnAdd.setText(QCoreApplication.translate("VehicleSopPage", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("VehicleSopPage", u"Edit", None))
        self.btnDelete.setText(QCoreApplication.translate("VehicleSopPage", u"Delete", None))
        self.btnChecklist.setText(QCoreApplication.translate("VehicleSopPage", u"Checklist", None))
        self.btnPrintInspectionForm.setText(QCoreApplication.translate("VehicleSopPage", u"Print Inspection Form", None))
        self.btnRefresh.setText(QCoreApplication.translate("VehicleSopPage", u"Refresh", None))
    # retranslateUi

