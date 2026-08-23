# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'users_page.ui'
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

class Ui_UsersPage(object):
    def setupUi(self, UsersPage):
        if not UsersPage.objectName():
            UsersPage.setObjectName(u"UsersPage")
        UsersPage.resize(550, 372)
        self.verticalLayout = QVBoxLayout(UsersPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(UsersPage)
        self.lblTitle.setObjectName(u"lblTitle")

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblSearch = QLabel(UsersPage)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout_2.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(UsersPage)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout_2.addWidget(self.txtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tblUsers = QTableWidget(UsersPage)
        if (self.tblUsers.columnCount() < 5):
            self.tblUsers.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblUsers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblUsers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblUsers.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblUsers.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblUsers.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblUsers.setObjectName(u"tblUsers")

        self.verticalLayout.addWidget(self.tblUsers)

        self.lblStatus = QLabel(UsersPage)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout.addWidget(self.lblStatus)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnAdd = QPushButton(UsersPage)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(UsersPage)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout.addWidget(self.btnEdit)

        self.btnDeactivate = QPushButton(UsersPage)
        self.btnDeactivate.setObjectName(u"btnDeactivate")

        self.horizontalLayout.addWidget(self.btnDeactivate)

        self.btnRefresh = QPushButton(UsersPage)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout.addWidget(self.btnRefresh)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(UsersPage)

        QMetaObject.connectSlotsByName(UsersPage)
    # setupUi

    def retranslateUi(self, UsersPage):
        UsersPage.setWindowTitle(QCoreApplication.translate("UsersPage", u"Users", None))
        self.lblTitle.setText(QCoreApplication.translate("UsersPage", u"User Management", None))
        self.lblSearch.setText(QCoreApplication.translate("UsersPage", u"Search:", None))
        ___qtablewidgetitem = self.tblUsers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("UsersPage", u"Username", None))
        ___qtablewidgetitem1 = self.tblUsers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("UsersPage", u"Full Name", None))
        ___qtablewidgetitem2 = self.tblUsers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("UsersPage", u"Role", None))
        ___qtablewidgetitem3 = self.tblUsers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("UsersPage", u"Status", None))
        ___qtablewidgetitem4 = self.tblUsers.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("UsersPage", u"Created At", None))
        self.lblStatus.setText(QCoreApplication.translate("UsersPage", u"Status:", None))
        self.btnAdd.setText(QCoreApplication.translate("UsersPage", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("UsersPage", u"Edit", None))
        self.btnDeactivate.setText(QCoreApplication.translate("UsersPage", u"Deactivate", None))
        self.btnRefresh.setText(QCoreApplication.translate("UsersPage", u"Refresh", None))
    # retranslateUi

