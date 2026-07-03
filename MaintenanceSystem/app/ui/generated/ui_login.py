# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(800, 600)
        LoginWindow.setMinimumSize(QSize(520, 340))
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(self.centralwidget)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.lblUsername = QLabel(self.centralwidget)
        self.lblUsername.setObjectName(u"lblUsername")
        font1 = QFont()
        font1.setBold(True)
        self.lblUsername.setFont(font1)

        self.verticalLayout.addWidget(self.lblUsername)

        self.txtUsername = QLineEdit(self.centralwidget)
        self.txtUsername.setObjectName(u"txtUsername")

        self.verticalLayout.addWidget(self.txtUsername)

        self.lblPassword = QLabel(self.centralwidget)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setFont(font1)

        self.verticalLayout.addWidget(self.lblPassword)

        self.txtPassword = QLineEdit(self.centralwidget)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.txtPassword)

        self.chkRememberMe = QCheckBox(self.centralwidget)
        self.chkRememberMe.setObjectName(u"chkRememberMe")

        self.verticalLayout.addWidget(self.chkRememberMe)

        self.btnLogin = QPushButton(self.centralwidget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setFont(font1)

        self.verticalLayout.addWidget(self.btnLogin)

        self.btnExit = QPushButton(self.centralwidget)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setFont(font1)

        self.verticalLayout.addWidget(self.btnExit)

        self.lblVersion = QLabel(self.centralwidget)
        self.lblVersion.setObjectName(u"lblVersion")

        self.verticalLayout.addWidget(self.lblVersion)

        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LoginWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Maintenance Management System - Login", None))
        self.lblTitle.setText(QCoreApplication.translate("LoginWindow", u"Maintenace Management System", None))
        self.lblUsername.setText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.txtUsername.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Enter username", None))
        self.lblPassword.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Enter Password", None))
        self.chkRememberMe.setText(QCoreApplication.translate("LoginWindow", u"Remember Me", None))
        self.btnLogin.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.btnExit.setText(QCoreApplication.translate("LoginWindow", u"Exit", None))
        self.lblVersion.setText(QCoreApplication.translate("LoginWindow", u"Version 1.0", None))
    # retranslateUi

