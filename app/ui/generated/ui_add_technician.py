# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_technician.ui'
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
    QDialogButtonBox, QDoubleSpinBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddTechnicianDialog(object):
    def setupUi(self, AddTechnicianDialog):
        if not AddTechnicianDialog.objectName():
            AddTechnicianDialog.setObjectName(u"AddTechnicianDialog")
        AddTechnicianDialog.resize(876, 703)
        self.verticalLayout = QVBoxLayout(AddTechnicianDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblEmployeeNo = QLabel(AddTechnicianDialog)
        self.lblEmployeeNo.setObjectName(u"lblEmployeeNo")

        self.horizontalLayout.addWidget(self.lblEmployeeNo)

        self.txtEmployeeNumber = QLineEdit(AddTechnicianDialog)
        self.txtEmployeeNumber.setObjectName(u"txtEmployeeNumber")

        self.horizontalLayout.addWidget(self.txtEmployeeNumber)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblFirstName = QLabel(AddTechnicianDialog)
        self.lblFirstName.setObjectName(u"lblFirstName")

        self.horizontalLayout_2.addWidget(self.lblFirstName)

        self.txtFirstName = QLineEdit(AddTechnicianDialog)
        self.txtFirstName.setObjectName(u"txtFirstName")

        self.horizontalLayout_2.addWidget(self.txtFirstName)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblLastName = QLabel(AddTechnicianDialog)
        self.lblLastName.setObjectName(u"lblLastName")

        self.horizontalLayout_3.addWidget(self.lblLastName)

        self.txtLastName = QLineEdit(AddTechnicianDialog)
        self.txtLastName.setObjectName(u"txtLastName")

        self.horizontalLayout_3.addWidget(self.txtLastName)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblPhone = QLabel(AddTechnicianDialog)
        self.lblPhone.setObjectName(u"lblPhone")

        self.horizontalLayout_4.addWidget(self.lblPhone)

        self.txtPhone = QLineEdit(AddTechnicianDialog)
        self.txtPhone.setObjectName(u"txtPhone")

        self.horizontalLayout_4.addWidget(self.txtPhone)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblEmail = QLabel(AddTechnicianDialog)
        self.lblEmail.setObjectName(u"lblEmail")

        self.horizontalLayout_5.addWidget(self.lblEmail)

        self.txtEmail = QLineEdit(AddTechnicianDialog)
        self.txtEmail.setObjectName(u"txtEmail")

        self.horizontalLayout_5.addWidget(self.txtEmail)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblTrade = QLabel(AddTechnicianDialog)
        self.lblTrade.setObjectName(u"lblTrade")

        self.horizontalLayout_6.addWidget(self.lblTrade)

        self.cmbTrade = QComboBox(AddTechnicianDialog)
        self.cmbTrade.setObjectName(u"cmbTrade")

        self.horizontalLayout_6.addWidget(self.cmbTrade)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lblDepartment = QLabel(AddTechnicianDialog)
        self.lblDepartment.setObjectName(u"lblDepartment")

        self.horizontalLayout_7.addWidget(self.lblDepartment)

        self.cmbDepartment = QComboBox(AddTechnicianDialog)
        self.cmbDepartment.setObjectName(u"cmbDepartment")

        self.horizontalLayout_7.addWidget(self.cmbDepartment)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblHourlyRate = QLabel(AddTechnicianDialog)
        self.lblHourlyRate.setObjectName(u"lblHourlyRate")

        self.horizontalLayout_8.addWidget(self.lblHourlyRate)

        self.dsbHourlyRate = QDoubleSpinBox(AddTechnicianDialog)
        self.dsbHourlyRate.setObjectName(u"dsbHourlyRate")

        self.horizontalLayout_8.addWidget(self.dsbHourlyRate, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lblStatus = QLabel(AddTechnicianDialog)
        self.lblStatus.setObjectName(u"lblStatus")

        self.horizontalLayout_9.addWidget(self.lblStatus)

        self.cmbStatus = QComboBox(AddTechnicianDialog)
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.horizontalLayout_9.addWidget(self.cmbStatus)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.buttonBox = QDialogButtonBox(AddTechnicianDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddTechnicianDialog)
        self.buttonBox.accepted.connect(AddTechnicianDialog.accept)
        self.buttonBox.rejected.connect(AddTechnicianDialog.reject)

        QMetaObject.connectSlotsByName(AddTechnicianDialog)
    # setupUi

    def retranslateUi(self, AddTechnicianDialog):
        AddTechnicianDialog.setWindowTitle(QCoreApplication.translate("AddTechnicianDialog", u"Add Technician", None))
        self.lblEmployeeNo.setText(QCoreApplication.translate("AddTechnicianDialog", u"Employee No", None))
        self.lblFirstName.setText(QCoreApplication.translate("AddTechnicianDialog", u"First Name", None))
        self.lblLastName.setText(QCoreApplication.translate("AddTechnicianDialog", u"Last Name", None))
        self.lblPhone.setText(QCoreApplication.translate("AddTechnicianDialog", u"Phone", None))
        self.lblEmail.setText(QCoreApplication.translate("AddTechnicianDialog", u"Email", None))
        self.lblTrade.setText(QCoreApplication.translate("AddTechnicianDialog", u"Trade", None))
        self.lblDepartment.setText(QCoreApplication.translate("AddTechnicianDialog", u"Department", None))
        self.lblHourlyRate.setText(QCoreApplication.translate("AddTechnicianDialog", u"Hourly Rate", None))
        self.lblStatus.setText(QCoreApplication.translate("AddTechnicianDialog", u"Status", None))
    # retranslateUi

