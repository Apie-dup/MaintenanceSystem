# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehicle_logbook_page.ui'
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

class Ui_VehicleLogbookPage(object):
    def setupUi(self, VehicleLogbookPage):
        if not VehicleLogbookPage.objectName():
            VehicleLogbookPage.setObjectName(u"VehicleLogbookPage")
        VehicleLogbookPage.resize(1125, 597)
        self.verticalLayout = QVBoxLayout(VehicleLogbookPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(VehicleLogbookPage)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSearch = QLabel(VehicleLogbookPage)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(VehicleLogbookPage)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblLogbook = QTableWidget(VehicleLogbookPage)
        if (self.tblLogbook.columnCount() < 13):
            self.tblLogbook.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblLogbook.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblLogbook.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblLogbook.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblLogbook.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblLogbook.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblLogbook.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblLogbook.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblLogbook.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblLogbook.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblLogbook.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblLogbook.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tblLogbook.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tblLogbook.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.tblLogbook.setObjectName(u"tblLogbook")

        self.verticalLayout.addWidget(self.tblLogbook)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(VehicleLogbookPage)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(VehicleLogbookPage)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnRefresh = QPushButton(VehicleLogbookPage)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.btnCreateWorkOrder = QPushButton(VehicleLogbookPage)
        self.btnCreateWorkOrder.setObjectName(u"btnCreateWorkOrder")

        self.horizontalLayout_2.addWidget(self.btnCreateWorkOrder)

        self.btnOpenWorkOrder = QPushButton(VehicleLogbookPage)
        self.btnOpenWorkOrder.setObjectName(u"btnOpenWorkOrder")

        self.horizontalLayout_2.addWidget(self.btnOpenWorkOrder)

        self.btnDelete = QPushButton(VehicleLogbookPage)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.horizontalSpacer = QSpacerItem(1045, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnPrint = QPushButton(VehicleLogbookPage)
        self.btnPrint.setObjectName(u"btnPrint")

        self.horizontalLayout_2.addWidget(self.btnPrint)

        self.btnPrintBlank = QPushButton(VehicleLogbookPage)
        self.btnPrintBlank.setObjectName(u"btnPrintBlank")

        self.horizontalLayout_2.addWidget(self.btnPrintBlank)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(VehicleLogbookPage)

        QMetaObject.connectSlotsByName(VehicleLogbookPage)
    # setupUi

    def retranslateUi(self, VehicleLogbookPage):
        VehicleLogbookPage.setWindowTitle(QCoreApplication.translate("VehicleLogbookPage", u"Vehicle Logbook", None))
        self.lblTitle.setText(QCoreApplication.translate("VehicleLogbookPage", u"Vehicle Logbook", None))
        self.lblSearch.setText(QCoreApplication.translate("VehicleLogbookPage", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("VehicleLogbookPage", u"Search vehicle, driver, destination or purpose...", None))
        ___qtablewidgetitem = self.tblLogbook.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VehicleLogbookPage", u"Date", None))
        ___qtablewidgetitem1 = self.tblLogbook.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VehicleLogbookPage", u"Asset No.", None))
        ___qtablewidgetitem2 = self.tblLogbook.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VehicleLogbookPage", u"Vehicle", None))
        ___qtablewidgetitem3 = self.tblLogbook.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VehicleLogbookPage", u"Driver", None))
        ___qtablewidgetitem4 = self.tblLogbook.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VehicleLogbookPage", u"From", None))
        ___qtablewidgetitem5 = self.tblLogbook.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VehicleLogbookPage", u"To", None))
        ___qtablewidgetitem6 = self.tblLogbook.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("VehicleLogbookPage", u"Start km", None))
        ___qtablewidgetitem7 = self.tblLogbook.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("VehicleLogbookPage", u"End km", None))
        ___qtablewidgetitem8 = self.tblLogbook.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("VehicleLogbookPage", u"Distance", None))
        ___qtablewidgetitem9 = self.tblLogbook.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("VehicleLogbookPage", u"Puspose", None))
        ___qtablewidgetitem10 = self.tblLogbook.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("VehicleLogbookPage", u"Defect / Fault", None))
        ___qtablewidgetitem11 = self.tblLogbook.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("VehicleLogbookPage", u"Fuel", None))
        ___qtablewidgetitem12 = self.tblLogbook.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("VehicleLogbookPage", u"Work Order", None))
        self.btnAdd.setText(QCoreApplication.translate("VehicleLogbookPage", u"Add Entry", None))
        self.btnEdit.setText(QCoreApplication.translate("VehicleLogbookPage", u"Edit", None))
        self.btnRefresh.setText(QCoreApplication.translate("VehicleLogbookPage", u"Refresh", None))
        self.btnCreateWorkOrder.setText(QCoreApplication.translate("VehicleLogbookPage", u"Create Work Order", None))
        self.btnOpenWorkOrder.setText(QCoreApplication.translate("VehicleLogbookPage", u"Open Work Order", None))
        self.btnDelete.setText(QCoreApplication.translate("VehicleLogbookPage", u"Delete", None))
        self.btnPrint.setText(QCoreApplication.translate("VehicleLogbookPage", u"Print Logbook", None))
        self.btnPrintBlank.setText(QCoreApplication.translate("VehicleLogbookPage", u"Print Blank Logbook", None))
    # retranslateUi

