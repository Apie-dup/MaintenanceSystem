# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pm_page.ui'
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
        PMWindow.resize(827, 700)
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
        if (self.tblPM.columnCount() < 8):
            self.tblPM.setColumnCount(8)
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
        self.tblPM.setObjectName(u"tblPM")
        self.tblPM.setAlternatingRowColors(True)
        self.tblPM.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tblPM)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(PMWindow)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(PMWindow)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnRefresh = QPushButton(PMWindow)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.btnDelete = QPushButton(PMWindow)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(PMWindow)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnClose)


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
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PMWindow", u"Asset", None))
        ___qtablewidgetitem3 = self.tblPM.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PMWindow", u"Task", None))
        ___qtablewidgetitem4 = self.tblPM.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PMWindow", u"Frequency", None))
        ___qtablewidgetitem5 = self.tblPM.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PMWindow", u"Next Due", None))
        ___qtablewidgetitem6 = self.tblPM.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PMWindow", u"Priority", None))
        ___qtablewidgetitem7 = self.tblPM.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PMWindow", u"Status", None))
        self.btnAdd.setText(QCoreApplication.translate("PMWindow", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("PMWindow", u"Edit", None))
        self.btnRefresh.setText(QCoreApplication.translate("PMWindow", u"Refresh", None))
        self.btnDelete.setText(QCoreApplication.translate("PMWindow", u"Delete", None))
        self.btnClose.setText(QCoreApplication.translate("PMWindow", u"Close", None))
        self.lblStatus.setText(QCoreApplication.translate("PMWindow", u"Status", None))
    # retranslateUi

