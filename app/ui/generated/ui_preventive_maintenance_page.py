# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preventive_maintenance_page.ui'
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

class Ui_PMWindow(object):
    def setupUi(self, PMWindow):
        if not PMWindow.objectName():
            PMWindow.setObjectName(u"PMWindow")
        PMWindow.resize(827, 523)
        self.verticalLayout = QVBoxLayout(PMWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblPMTitle = QLabel(PMWindow)
        self.lblPMTitle.setObjectName(u"lblPMTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblPMTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblPMTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSearch = QLabel(PMWindow)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(PMWindow)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblPM = QTableWidget(PMWindow)
        if (self.tblPM.columnCount() < 15):
            self.tblPM.setColumnCount(15)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tblPM.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        self.tblPM.setObjectName(u"tblPM")
        self.tblPM.setWordWrap(False)
        self.tblPM.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tblPM)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(PMWindow)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(PMWindow)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnRefresh = QPushButton(PMWindow)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.btnGenerateWorkOrder = QPushButton(PMWindow)
        self.btnGenerateWorkOrder.setObjectName(u"btnGenerateWorkOrder")

        self.horizontalLayout_2.addWidget(self.btnGenerateWorkOrder)

        self.btnDelete = QPushButton(PMWindow)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lblStatus = QLabel(PMWindow)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout.addWidget(self.lblStatus)


        self.retranslateUi(PMWindow)

        QMetaObject.connectSlotsByName(PMWindow)
    # setupUi

    def retranslateUi(self, PMWindow):
        PMWindow.setWindowTitle(QCoreApplication.translate("PMWindow", u"Preventive Maintenance Window", None))
        self.lblPMTitle.setText(QCoreApplication.translate("PMWindow", u"Preventive Maintenance", None))
        self.lblSearch.setText(QCoreApplication.translate("PMWindow", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("PMWindow", u"Search preventive maintenance.....", None))
        ___qtablewidgetitem = self.tblPM.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PMWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tblPM.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PMWindow", u"PM Number", None))
        ___qtablewidgetitem2 = self.tblPM.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PMWindow", u"Asset Id", None))
        ___qtablewidgetitem3 = self.tblPM.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PMWindow", u"Task", None))
        ___qtablewidgetitem4 = self.tblPM.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PMWindow", u"Description", None))
        ___qtablewidgetitem5 = self.tblPM.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PMWindow", u"Frequency Type", None))
        ___qtablewidgetitem6 = self.tblPM.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PMWindow", u"Frequency Value", None))
        ___qtablewidgetitem7 = self.tblPM.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PMWindow", u"Last Service Date", None))
        ___qtablewidgetitem8 = self.tblPM.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("PMWindow", u"Next Due Date", None))
        ___qtablewidgetitem9 = self.tblPM.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("PMWindow", u"Estimated Hours", None))
        ___qtablewidgetitem10 = self.tblPM.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("PMWindow", u"Estimated Cost", None))
        ___qtablewidgetitem11 = self.tblPM.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("PMWindow", u"Priority", None))
        ___qtablewidgetitem12 = self.tblPM.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("PMWindow", u"Active", None))
        ___qtablewidgetitem13 = self.tblPM.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("PMWindow", u"Notes", None))
        ___qtablewidgetitem14 = self.tblPM.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("PMWindow", u"Created At", None))
        self.btnAdd.setText(QCoreApplication.translate("PMWindow", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("PMWindow", u"Edit", None))
        self.btnRefresh.setText(QCoreApplication.translate("PMWindow", u"Refresh", None))
        self.btnGenerateWorkOrder.setText(QCoreApplication.translate("PMWindow", u"Generate Work Order", None))
        self.btnDelete.setText(QCoreApplication.translate("PMWindow", u"Delete", None))
        self.lblStatus.setText(QCoreApplication.translate("PMWindow", u"Status", None))
    # retranslateUi

