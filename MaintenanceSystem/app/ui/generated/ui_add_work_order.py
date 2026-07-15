# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_work_order.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_AddWorkOrderDialog(object):
    def setupUi(self, AddWorkOrderDialog):
        if not AddWorkOrderDialog.objectName():
            AddWorkOrderDialog.setObjectName(u"AddWorkOrderDialog")
        AddWorkOrderDialog.resize(877, 720)
        self.verticalLayout = QVBoxLayout(AddWorkOrderDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblWorkOrderNumber = QLabel(AddWorkOrderDialog)
        self.lblWorkOrderNumber.setObjectName(u"lblWorkOrderNumber")

        self.horizontalLayout.addWidget(self.lblWorkOrderNumber)

        self.txtWorkOrderNumber = QLineEdit(AddWorkOrderDialog)
        self.txtWorkOrderNumber.setObjectName(u"txtWorkOrderNumber")
        self.txtWorkOrderNumber.setReadOnly(True)

        self.horizontalLayout.addWidget(self.txtWorkOrderNumber)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Asset = QLabel(AddWorkOrderDialog)
        self.Asset.setObjectName(u"Asset")

        self.horizontalLayout_2.addWidget(self.Asset)

        self.cmbAsset = QComboBox(AddWorkOrderDialog)
        self.cmbAsset.setObjectName(u"cmbAsset")

        self.horizontalLayout_2.addWidget(self.cmbAsset)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblTitle = QLabel(AddWorkOrderDialog)
        self.lblTitle.setObjectName(u"lblTitle")

        self.horizontalLayout_3.addWidget(self.lblTitle)

        self.txtTitle = QLineEdit(AddWorkOrderDialog)
        self.txtTitle.setObjectName(u"txtTitle")

        self.horizontalLayout_3.addWidget(self.txtTitle)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblDescription = QLabel(AddWorkOrderDialog)
        self.lblDescription.setObjectName(u"lblDescription")

        self.horizontalLayout_4.addWidget(self.lblDescription)

        self.teDescription = QTextEdit(AddWorkOrderDialog)
        self.teDescription.setObjectName(u"teDescription")

        self.horizontalLayout_4.addWidget(self.teDescription)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblPriority = QLabel(AddWorkOrderDialog)
        self.lblPriority.setObjectName(u"lblPriority")

        self.horizontalLayout_5.addWidget(self.lblPriority)

        self.cmbPriority = QComboBox(AddWorkOrderDialog)
        self.cmbPriority.setObjectName(u"cmbPriority")

        self.horizontalLayout_5.addWidget(self.cmbPriority)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblStatus = QLabel(AddWorkOrderDialog)
        self.lblStatus.setObjectName(u"lblStatus")

        self.horizontalLayout_6.addWidget(self.lblStatus)

        self.cmbStatus = QComboBox(AddWorkOrderDialog)
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.horizontalLayout_6.addWidget(self.cmbStatus)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lblTechnician = QLabel(AddWorkOrderDialog)
        self.lblTechnician.setObjectName(u"lblTechnician")

        self.horizontalLayout_7.addWidget(self.lblTechnician)

        self.cmbTechnician = QComboBox(AddWorkOrderDialog)
        self.cmbTechnician.setObjectName(u"cmbTechnician")

        self.horizontalLayout_7.addWidget(self.cmbTechnician)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblRequestedBy = QLabel(AddWorkOrderDialog)
        self.lblRequestedBy.setObjectName(u"lblRequestedBy")

        self.horizontalLayout_8.addWidget(self.lblRequestedBy)

        self.txtRequestedBy = QLineEdit(AddWorkOrderDialog)
        self.txtRequestedBy.setObjectName(u"txtRequestedBy")

        self.horizontalLayout_8.addWidget(self.txtRequestedBy)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lblDateCreated = QLabel(AddWorkOrderDialog)
        self.lblDateCreated.setObjectName(u"lblDateCreated")

        self.horizontalLayout_9.addWidget(self.lblDateCreated)

        self.dtDateCreated = QDateEdit(AddWorkOrderDialog)
        self.dtDateCreated.setObjectName(u"dtDateCreated")
        self.dtDateCreated.setCalendarPopup(True)

        self.horizontalLayout_9.addWidget(self.dtDateCreated, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lblDueDate = QLabel(AddWorkOrderDialog)
        self.lblDueDate.setObjectName(u"lblDueDate")

        self.horizontalLayout_10.addWidget(self.lblDueDate)

        self.dtDueDate = QDateEdit(AddWorkOrderDialog)
        self.dtDueDate.setObjectName(u"dtDueDate")
        self.dtDueDate.setCalendarPopup(True)

        self.horizontalLayout_10.addWidget(self.dtDueDate, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lblEstimatedCost = QLabel(AddWorkOrderDialog)
        self.lblEstimatedCost.setObjectName(u"lblEstimatedCost")

        self.horizontalLayout_11.addWidget(self.lblEstimatedCost)

        self.dsbEstimatedCost = QDoubleSpinBox(AddWorkOrderDialog)
        self.dsbEstimatedCost.setObjectName(u"dsbEstimatedCost")
        self.dsbEstimatedCost.setMaximum(9999999.990000000223517)
        self.dsbEstimatedCost.setSingleStep(10.000000000000000)

        self.horizontalLayout_11.addWidget(self.dsbEstimatedCost, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lblActualCost = QLabel(AddWorkOrderDialog)
        self.lblActualCost.setObjectName(u"lblActualCost")

        self.horizontalLayout_12.addWidget(self.lblActualCost)

        self.dsbActualCost = QDoubleSpinBox(AddWorkOrderDialog)
        self.dsbActualCost.setObjectName(u"dsbActualCost")
        self.dsbActualCost.setMaximum(9999999.990000000223517)
        self.dsbActualCost.setSingleStep(10.000000000000000)

        self.horizontalLayout_12.addWidget(self.dsbActualCost, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lblLabourHours = QLabel(AddWorkOrderDialog)
        self.lblLabourHours.setObjectName(u"lblLabourHours")

        self.horizontalLayout_13.addWidget(self.lblLabourHours)

        self.dsbLabourHours = QDoubleSpinBox(AddWorkOrderDialog)
        self.dsbLabourHours.setObjectName(u"dsbLabourHours")
        self.dsbLabourHours.setMaximum(1000.000000000000000)
        self.dsbLabourHours.setSingleStep(0.250000000000000)

        self.horizontalLayout_13.addWidget(self.dsbLabourHours, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lblNotes = QLabel(AddWorkOrderDialog)
        self.lblNotes.setObjectName(u"lblNotes")

        self.horizontalLayout_14.addWidget(self.lblNotes)

        self.teNotes = QTextEdit(AddWorkOrderDialog)
        self.teNotes.setObjectName(u"teNotes")

        self.horizontalLayout_14.addWidget(self.teNotes)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.buttonBox = QDialogButtonBox(AddWorkOrderDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddWorkOrderDialog)
        self.buttonBox.accepted.connect(AddWorkOrderDialog.accept)
        self.buttonBox.rejected.connect(AddWorkOrderDialog.reject)

        QMetaObject.connectSlotsByName(AddWorkOrderDialog)
    # setupUi

    def retranslateUi(self, AddWorkOrderDialog):
        AddWorkOrderDialog.setWindowTitle(QCoreApplication.translate("AddWorkOrderDialog", u"Add Work Orders", None))
        self.lblWorkOrderNumber.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Work Order Number", None))
        self.Asset.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Asset", None))
        self.lblTitle.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Title", None))
        self.lblDescription.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Description", None))
        self.lblPriority.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Priority", None))
        self.lblStatus.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Status", None))
        self.lblTechnician.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Technician", None))
        self.lblRequestedBy.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Requested By", None))
        self.lblDateCreated.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Date Created", None))
        self.lblDueDate.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Due Date", None))
        self.lblEstimatedCost.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Estimated Cost", None))
        self.lblActualCost.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Actual Cost", None))
        self.lblLabourHours.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Labour Hours", None))
        self.lblNotes.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Notes", None))
    # retranslateUi

