# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'supplier_dialog.ui'
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
    QDialogButtonBox, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_SupplierDialog(object):
    def setupUi(self, SupplierDialog):
        if not SupplierDialog.objectName():
            SupplierDialog.setObjectName(u"SupplierDialog")
        SupplierDialog.resize(680, 522)
        self.mainVerticalLayout = QVBoxLayout(SupplierDialog)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        self.groupSupplierDetails = QGroupBox(SupplierDialog)
        self.groupSupplierDetails.setObjectName(u"groupSupplierDetails")
        self.groupSupplierDetails.setFlat(True)
        self.supplierDetailsLayout = QVBoxLayout(self.groupSupplierDetails)
        self.supplierDetailsLayout.setObjectName(u"supplierDetailsLayout")
        self.groupSupplierInformation = QGroupBox(self.groupSupplierDetails)
        self.groupSupplierInformation.setObjectName(u"groupSupplierInformation")
        self.groupSupplierInformation.setFlat(True)
        self.formSupplierInfo = QFormLayout(self.groupSupplierInformation)
        self.formSupplierInfo.setObjectName(u"formSupplierInfo")
        self.labelSupplierCode = QLabel(self.groupSupplierInformation)
        self.labelSupplierCode.setObjectName(u"labelSupplierCode")

        self.formSupplierInfo.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelSupplierCode)

        self.txtSupplierCode = QLineEdit(self.groupSupplierInformation)
        self.txtSupplierCode.setObjectName(u"txtSupplierCode")
        self.txtSupplierCode.setReadOnly(True)

        self.formSupplierInfo.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtSupplierCode)

        self.labelSupplierName = QLabel(self.groupSupplierInformation)
        self.labelSupplierName.setObjectName(u"labelSupplierName")

        self.formSupplierInfo.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelSupplierName)

        self.txtSupplierName = QLineEdit(self.groupSupplierInformation)
        self.txtSupplierName.setObjectName(u"txtSupplierName")

        self.formSupplierInfo.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtSupplierName)

        self.labelContactPerson = QLabel(self.groupSupplierInformation)
        self.labelContactPerson.setObjectName(u"labelContactPerson")

        self.formSupplierInfo.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelContactPerson)

        self.txtContactPerson = QLineEdit(self.groupSupplierInformation)
        self.txtContactPerson.setObjectName(u"txtContactPerson")

        self.formSupplierInfo.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtContactPerson)

        self.labelPhone = QLabel(self.groupSupplierInformation)
        self.labelPhone.setObjectName(u"labelPhone")

        self.formSupplierInfo.setWidget(3, QFormLayout.ItemRole.LabelRole, self.labelPhone)

        self.txtPhone = QLineEdit(self.groupSupplierInformation)
        self.txtPhone.setObjectName(u"txtPhone")

        self.formSupplierInfo.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtPhone)

        self.labelEmail = QLabel(self.groupSupplierInformation)
        self.labelEmail.setObjectName(u"labelEmail")

        self.formSupplierInfo.setWidget(4, QFormLayout.ItemRole.LabelRole, self.labelEmail)

        self.txtEmail = QLineEdit(self.groupSupplierInformation)
        self.txtEmail.setObjectName(u"txtEmail")

        self.formSupplierInfo.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtEmail)

        self.txtAddress = QPlainTextEdit(self.groupSupplierInformation)
        self.txtAddress.setObjectName(u"txtAddress")
        self.txtAddress.setMaximumSize(QSize(16777215, 70))

        self.formSupplierInfo.setWidget(5, QFormLayout.ItemRole.FieldRole, self.txtAddress)

        self.labelAddress = QLabel(self.groupSupplierInformation)
        self.labelAddress.setObjectName(u"labelAddress")

        self.formSupplierInfo.setWidget(5, QFormLayout.ItemRole.LabelRole, self.labelAddress)


        self.supplierDetailsLayout.addWidget(self.groupSupplierInformation)

        self.groupStatus = QGroupBox(self.groupSupplierDetails)
        self.groupStatus.setObjectName(u"groupStatus")
        self.groupStatus.setFlat(True)
        self.statusLayout = QHBoxLayout(self.groupStatus)
        self.statusLayout.setObjectName(u"statusLayout")
        self.labelStatus = QLabel(self.groupStatus)
        self.labelStatus.setObjectName(u"labelStatus")

        self.statusLayout.addWidget(self.labelStatus)

        self.cmbStatus = QComboBox(self.groupStatus)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.statusLayout.addWidget(self.cmbStatus)


        self.supplierDetailsLayout.addWidget(self.groupStatus)

        self.groupNotes = QGroupBox(self.groupSupplierDetails)
        self.groupNotes.setObjectName(u"groupNotes")
        self.groupNotes.setFlat(True)
        self.notesLayout = QVBoxLayout(self.groupNotes)
        self.notesLayout.setObjectName(u"notesLayout")

        self.supplierDetailsLayout.addWidget(self.groupNotes)

        self.txtNotes = QPlainTextEdit(self.groupSupplierDetails)
        self.txtNotes.setObjectName(u"txtNotes")
        self.txtNotes.setMaximumSize(QSize(16777215, 70))

        self.supplierDetailsLayout.addWidget(self.txtNotes)

        self.buttonBox = QDialogButtonBox(self.groupSupplierDetails)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.supplierDetailsLayout.addWidget(self.buttonBox)


        self.mainVerticalLayout.addWidget(self.groupSupplierDetails)


        self.retranslateUi(SupplierDialog)

        QMetaObject.connectSlotsByName(SupplierDialog)
    # setupUi

    def retranslateUi(self, SupplierDialog):
        SupplierDialog.setWindowTitle(QCoreApplication.translate("SupplierDialog", u"Supplier Details", None))
        self.groupSupplierDetails.setTitle(QCoreApplication.translate("SupplierDialog", u"Supplier Details", None))
        self.groupSupplierInformation.setTitle(QCoreApplication.translate("SupplierDialog", u"Supplier Information", None))
        self.labelSupplierCode.setText(QCoreApplication.translate("SupplierDialog", u"Supplier Code:", None))
        self.labelSupplierName.setText(QCoreApplication.translate("SupplierDialog", u"Supplier Name:", None))
        self.labelContactPerson.setText(QCoreApplication.translate("SupplierDialog", u"Contact Person:", None))
        self.labelPhone.setText(QCoreApplication.translate("SupplierDialog", u"Phone:", None))
        self.labelEmail.setText(QCoreApplication.translate("SupplierDialog", u"Email:", None))
        self.labelAddress.setText(QCoreApplication.translate("SupplierDialog", u"Address:", None))
        self.groupStatus.setTitle(QCoreApplication.translate("SupplierDialog", u"Status", None))
        self.labelStatus.setText(QCoreApplication.translate("SupplierDialog", u"Status:", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("SupplierDialog", u"Active", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("SupplierDialog", u"Inactive", None))

        self.groupNotes.setTitle(QCoreApplication.translate("SupplierDialog", u"Notes", None))
    # retranslateUi

