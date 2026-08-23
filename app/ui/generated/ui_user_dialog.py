# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_UserDialog(object):
    def setupUi(self, UserDialog):
        if not UserDialog.objectName():
            UserDialog.setObjectName(u"UserDialog")
        UserDialog.resize(524, 602)
        self.verticalLayout = QVBoxLayout(UserDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(UserDialog)
        self.lblTitle.setObjectName(u"lblTitle")

        self.verticalLayout.addWidget(self.lblTitle)

        self.verticalSpacer = QSpacerItem(20, 74, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblUsername = QLabel(UserDialog)
        self.lblUsername.setObjectName(u"lblUsername")

        self.horizontalLayout.addWidget(self.lblUsername)

        self.txtUsername = QLineEdit(UserDialog)
        self.txtUsername.setObjectName(u"txtUsername")

        self.horizontalLayout.addWidget(self.txtUsername)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblFullName = QLabel(UserDialog)
        self.lblFullName.setObjectName(u"lblFullName")

        self.horizontalLayout_2.addWidget(self.lblFullName)

        self.txtFullName = QLineEdit(UserDialog)
        self.txtFullName.setObjectName(u"txtFullName")

        self.horizontalLayout_2.addWidget(self.txtFullName)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblRole = QLabel(UserDialog)
        self.lblRole.setObjectName(u"lblRole")

        self.horizontalLayout_3.addWidget(self.lblRole)

        self.cmbRole = QComboBox(UserDialog)
        self.cmbRole.setObjectName(u"cmbRole")

        self.horizontalLayout_3.addWidget(self.cmbRole)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblStatus = QLabel(UserDialog)
        self.lblStatus.setObjectName(u"lblStatus")

        self.horizontalLayout_4.addWidget(self.lblStatus)

        self.cmbStatus = QComboBox(UserDialog)
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.horizontalLayout_4.addWidget(self.cmbStatus)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 75, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblPassword = QLabel(UserDialog)
        self.lblPassword.setObjectName(u"lblPassword")

        self.horizontalLayout_5.addWidget(self.lblPassword)

        self.txtPassword = QLineEdit(UserDialog)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_5.addWidget(self.txtPassword)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblConfirmPassword = QLabel(UserDialog)
        self.lblConfirmPassword.setObjectName(u"lblConfirmPassword")

        self.horizontalLayout_6.addWidget(self.lblConfirmPassword)

        self.txtConfirmPassword = QLineEdit(UserDialog)
        self.txtConfirmPassword.setObjectName(u"txtConfirmPassword")
        self.txtConfirmPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_6.addWidget(self.txtConfirmPassword)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 74, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.lblPasswordHint = QLabel(UserDialog)
        self.lblPasswordHint.setObjectName(u"lblPasswordHint")

        self.verticalLayout.addWidget(self.lblPasswordHint)

        self.verticalSpacer_4 = QSpacerItem(20, 51, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.buttonBox = QDialogButtonBox(UserDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(UserDialog)
        self.buttonBox.accepted.connect(UserDialog.accept)
        self.buttonBox.rejected.connect(UserDialog.reject)

        QMetaObject.connectSlotsByName(UserDialog)
    # setupUi

    def retranslateUi(self, UserDialog):
        UserDialog.setWindowTitle(QCoreApplication.translate("UserDialog", u"User Dialog", None))
        self.lblTitle.setText(QCoreApplication.translate("UserDialog", u"User", None))
        self.lblUsername.setText(QCoreApplication.translate("UserDialog", u"Username:", None))
        self.lblFullName.setText(QCoreApplication.translate("UserDialog", u"Full Name:", None))
        self.lblRole.setText(QCoreApplication.translate("UserDialog", u"Role:", None))
        self.lblStatus.setText(QCoreApplication.translate("UserDialog", u"Status:", None))
        self.lblPassword.setText(QCoreApplication.translate("UserDialog", u"Password:", None))
        self.lblConfirmPassword.setText(QCoreApplication.translate("UserDialog", u"Confirm Password:", None))
        self.lblPasswordHint.setText(QCoreApplication.translate("UserDialog", u"Password information:", None))
    # retranslateUi

