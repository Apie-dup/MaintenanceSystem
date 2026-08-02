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
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QGroupBox,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AddTechnicianDialog(object):
    def setupUi(self, AddTechnicianDialog):
        if not AddTechnicianDialog.objectName():
            AddTechnicianDialog.setObjectName(u"AddTechnicianDialog")
        AddTechnicianDialog.resize(680, 520)
        self.mainLayout = QVBoxLayout(AddTechnicianDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.groupPersonalInfo = QGroupBox(AddTechnicianDialog)
        self.groupPersonalInfo.setObjectName(u"groupPersonalInfo")
        self.groupPersonalInfo.setFlat(True)
        self.formPersonalInfo = QFormLayout(self.groupPersonalInfo)
        self.formPersonalInfo.setObjectName(u"formPersonalInfo")
        self.lblEmployeeNumber = QLabel(self.groupPersonalInfo)
        self.lblEmployeeNumber.setObjectName(u"lblEmployeeNumber")

        self.formPersonalInfo.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblEmployeeNumber)

        self.txtEmployeeNumber = QLineEdit(self.groupPersonalInfo)
        self.txtEmployeeNumber.setObjectName(u"txtEmployeeNumber")
        self.txtEmployeeNumber.setReadOnly(True)

        self.formPersonalInfo.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtEmployeeNumber)

        self.lblFirstName = QLabel(self.groupPersonalInfo)
        self.lblFirstName.setObjectName(u"lblFirstName")

        self.formPersonalInfo.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblFirstName)

        self.txtFirstName = QLineEdit(self.groupPersonalInfo)
        self.txtFirstName.setObjectName(u"txtFirstName")

        self.formPersonalInfo.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtFirstName)

        self.lblLastName = QLabel(self.groupPersonalInfo)
        self.lblLastName.setObjectName(u"lblLastName")

        self.formPersonalInfo.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblLastName)

        self.txtLastName = QLineEdit(self.groupPersonalInfo)
        self.txtLastName.setObjectName(u"txtLastName")

        self.formPersonalInfo.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtLastName)

        self.lblPhone = QLabel(self.groupPersonalInfo)
        self.lblPhone.setObjectName(u"lblPhone")

        self.formPersonalInfo.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblPhone)

        self.txtPhone = QLineEdit(self.groupPersonalInfo)
        self.txtPhone.setObjectName(u"txtPhone")

        self.formPersonalInfo.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtPhone)

        self.lblEmail = QLabel(self.groupPersonalInfo)
        self.lblEmail.setObjectName(u"lblEmail")

        self.formPersonalInfo.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblEmail)

        self.txtEmail = QLineEdit(self.groupPersonalInfo)
        self.txtEmail.setObjectName(u"txtEmail")

        self.formPersonalInfo.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtEmail)


        self.mainLayout.addWidget(self.groupPersonalInfo)

        self.groupEmploymentInfo = QGroupBox(AddTechnicianDialog)
        self.groupEmploymentInfo.setObjectName(u"groupEmploymentInfo")
        self.groupEmploymentInfo.setFlat(True)
        self.formEmploymentInfo = QFormLayout(self.groupEmploymentInfo)
        self.formEmploymentInfo.setObjectName(u"formEmploymentInfo")
        self.lblTrade = QLabel(self.groupEmploymentInfo)
        self.lblTrade.setObjectName(u"lblTrade")

        self.formEmploymentInfo.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblTrade)

        self.cmbTrade = QComboBox(self.groupEmploymentInfo)
        self.cmbTrade.setObjectName(u"cmbTrade")

        self.formEmploymentInfo.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbTrade)

        self.lblDepartment = QLabel(self.groupEmploymentInfo)
        self.lblDepartment.setObjectName(u"lblDepartment")

        self.formEmploymentInfo.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblDepartment)

        self.cmbDepartment = QComboBox(self.groupEmploymentInfo)
        self.cmbDepartment.setObjectName(u"cmbDepartment")

        self.formEmploymentInfo.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbDepartment)

        self.lblHourlyRate = QLabel(self.groupEmploymentInfo)
        self.lblHourlyRate.setObjectName(u"lblHourlyRate")

        self.formEmploymentInfo.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblHourlyRate)

        self.dsbHourlyRate = QDoubleSpinBox(self.groupEmploymentInfo)
        self.dsbHourlyRate.setObjectName(u"dsbHourlyRate")
        self.dsbHourlyRate.setDecimals(2)
        self.dsbHourlyRate.setMaximum(999999.989999999990687)

        self.formEmploymentInfo.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dsbHourlyRate)

        self.lblStatus = QLabel(self.groupEmploymentInfo)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formEmploymentInfo.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.cmbStatus = QComboBox(self.groupEmploymentInfo)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.formEmploymentInfo.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbStatus)


        self.mainLayout.addWidget(self.groupEmploymentInfo)

        self.buttonBox = QDialogButtonBox(AddTechnicianDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.mainLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddTechnicianDialog)

        QMetaObject.connectSlotsByName(AddTechnicianDialog)
    # setupUi

    def retranslateUi(self, AddTechnicianDialog):
        AddTechnicianDialog.setWindowTitle(QCoreApplication.translate("AddTechnicianDialog", u"Add Technician", None))
        self.groupPersonalInfo.setTitle(QCoreApplication.translate("AddTechnicianDialog", u"Personal Information", None))
        self.lblEmployeeNumber.setText(QCoreApplication.translate("AddTechnicianDialog", u"Employee No:", None))
        self.lblFirstName.setText(QCoreApplication.translate("AddTechnicianDialog", u"First Name:", None))
        self.lblLastName.setText(QCoreApplication.translate("AddTechnicianDialog", u"Last Name:", None))
        self.lblPhone.setText(QCoreApplication.translate("AddTechnicianDialog", u"Phone:", None))
        self.lblEmail.setText(QCoreApplication.translate("AddTechnicianDialog", u"Email:", None))
        self.groupEmploymentInfo.setTitle(QCoreApplication.translate("AddTechnicianDialog", u"Employment Information", None))
        self.lblTrade.setText(QCoreApplication.translate("AddTechnicianDialog", u"Trade:", None))
        self.lblDepartment.setText(QCoreApplication.translate("AddTechnicianDialog", u"Department:", None))
        self.lblHourlyRate.setText(QCoreApplication.translate("AddTechnicianDialog", u"Hourly Rate:", None))
        self.dsbHourlyRate.setPrefix("")
        self.lblStatus.setText(QCoreApplication.translate("AddTechnicianDialog", u"Status:", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("AddTechnicianDialog", u"Active", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("AddTechnicianDialog", u"Inactive", None))

    # retranslateUi

