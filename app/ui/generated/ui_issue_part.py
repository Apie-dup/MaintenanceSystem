# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'issue_part.ui'
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
    QLabel, QLineEdit, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_IssuePartDialog(object):
    def setupUi(self, IssuePartDialog):
        if not IssuePartDialog.objectName():
            IssuePartDialog.setObjectName(u"IssuePartDialog")
        IssuePartDialog.resize(537, 551)
        self.mainLayout = QVBoxLayout(IssuePartDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.groupPart = QGroupBox(IssuePartDialog)
        self.groupPart.setObjectName(u"groupPart")
        self.groupPart.setFlat(True)
        self.formPart = QFormLayout(self.groupPart)
        self.formPart.setObjectName(u"formPart")
        self.lblPart = QLabel(self.groupPart)
        self.lblPart.setObjectName(u"lblPart")

        self.formPart.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblPart)

        self.cmbPart = QComboBox(self.groupPart)
        self.cmbPart.setObjectName(u"cmbPart")

        self.formPart.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbPart)


        self.mainLayout.addWidget(self.groupPart)

        self.groupAvailableQty = QGroupBox(IssuePartDialog)
        self.groupAvailableQty.setObjectName(u"groupAvailableQty")
        self.groupAvailableQty.setFlat(True)
        self.formAvailableQty = QFormLayout(self.groupAvailableQty)
        self.formAvailableQty.setObjectName(u"formAvailableQty")
        self.lblAvailableQuantity = QLabel(self.groupAvailableQty)
        self.lblAvailableQuantity.setObjectName(u"lblAvailableQuantity")

        self.formAvailableQty.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblAvailableQuantity)

        self.txtAvailable = QLineEdit(self.groupAvailableQty)
        self.txtAvailable.setObjectName(u"txtAvailable")
        self.txtAvailable.setReadOnly(True)

        self.formAvailableQty.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtAvailable)


        self.mainLayout.addWidget(self.groupAvailableQty)

        self.groupQtyIssue = QGroupBox(IssuePartDialog)
        self.groupQtyIssue.setObjectName(u"groupQtyIssue")
        self.groupQtyIssue.setFlat(True)
        self.formQtyIssue = QFormLayout(self.groupQtyIssue)
        self.formQtyIssue.setObjectName(u"formQtyIssue")
        self.lblQuantityToIssue = QLabel(self.groupQtyIssue)
        self.lblQuantityToIssue.setObjectName(u"lblQuantityToIssue")

        self.formQtyIssue.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblQuantityToIssue)

        self.spnQuantity = QDoubleSpinBox(self.groupQtyIssue)
        self.spnQuantity.setObjectName(u"spnQuantity")
        self.spnQuantity.setMinimum(0.010000000000000)
        self.spnQuantity.setMaximum(999999.000000000000000)

        self.formQtyIssue.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spnQuantity)


        self.mainLayout.addWidget(self.groupQtyIssue)

        self.groupUnitCost = QGroupBox(IssuePartDialog)
        self.groupUnitCost.setObjectName(u"groupUnitCost")
        self.groupUnitCost.setFlat(True)
        self.formUnitCost = QFormLayout(self.groupUnitCost)
        self.formUnitCost.setObjectName(u"formUnitCost")
        self.lblUnitCost = QLabel(self.groupUnitCost)
        self.lblUnitCost.setObjectName(u"lblUnitCost")

        self.formUnitCost.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblUnitCost)

        self.txtUnitCost = QLineEdit(self.groupUnitCost)
        self.txtUnitCost.setObjectName(u"txtUnitCost")
        self.txtUnitCost.setReadOnly(True)

        self.formUnitCost.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtUnitCost)


        self.mainLayout.addWidget(self.groupUnitCost)

        self.groupTotalCost = QGroupBox(IssuePartDialog)
        self.groupTotalCost.setObjectName(u"groupTotalCost")
        self.groupTotalCost.setFlat(True)
        self.formTotalCost = QFormLayout(self.groupTotalCost)
        self.formTotalCost.setObjectName(u"formTotalCost")
        self.lblTotalCost = QLabel(self.groupTotalCost)
        self.lblTotalCost.setObjectName(u"lblTotalCost")

        self.formTotalCost.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblTotalCost)

        self.txtTotalCost = QLineEdit(self.groupTotalCost)
        self.txtTotalCost.setObjectName(u"txtTotalCost")
        self.txtTotalCost.setReadOnly(True)

        self.formTotalCost.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtTotalCost)


        self.mainLayout.addWidget(self.groupTotalCost)

        self.groupNotes = QGroupBox(IssuePartDialog)
        self.groupNotes.setObjectName(u"groupNotes")
        self.groupNotes.setFlat(True)
        self.layoutNotes = QVBoxLayout(self.groupNotes)
        self.layoutNotes.setObjectName(u"layoutNotes")
        self.txtNotes = QTextEdit(self.groupNotes)
        self.txtNotes.setObjectName(u"txtNotes")

        self.layoutNotes.addWidget(self.txtNotes)


        self.mainLayout.addWidget(self.groupNotes)

        self.buttonBox = QDialogButtonBox(IssuePartDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.mainLayout.addWidget(self.buttonBox)


        self.retranslateUi(IssuePartDialog)

        QMetaObject.connectSlotsByName(IssuePartDialog)
    # setupUi

    def retranslateUi(self, IssuePartDialog):
        IssuePartDialog.setWindowTitle(QCoreApplication.translate("IssuePartDialog", u"Issue Part Dialog", None))
        self.groupPart.setTitle(QCoreApplication.translate("IssuePartDialog", u"Part", None))
        self.lblPart.setText(QCoreApplication.translate("IssuePartDialog", u"Part:", None))
        self.groupAvailableQty.setTitle(QCoreApplication.translate("IssuePartDialog", u"Available Quantity", None))
        self.lblAvailableQuantity.setText(QCoreApplication.translate("IssuePartDialog", u"Available Quantity:", None))
        self.groupQtyIssue.setTitle(QCoreApplication.translate("IssuePartDialog", u"Quantity to Issue", None))
        self.lblQuantityToIssue.setText(QCoreApplication.translate("IssuePartDialog", u"Quantity to Issue:", None))
        self.groupUnitCost.setTitle(QCoreApplication.translate("IssuePartDialog", u"Unit Cost", None))
        self.lblUnitCost.setText(QCoreApplication.translate("IssuePartDialog", u"Unit Cost:", None))
        self.groupTotalCost.setTitle(QCoreApplication.translate("IssuePartDialog", u"Total Cost", None))
        self.lblTotalCost.setText(QCoreApplication.translate("IssuePartDialog", u"Total Cost:", None))
        self.groupNotes.setTitle(QCoreApplication.translate("IssuePartDialog", u"Notes", None))
    # retranslateUi

