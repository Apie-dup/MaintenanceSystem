# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_pm_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDialog, QDialogButtonBox, QDoubleSpinBox,
    QFormLayout, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QSizePolicy, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_PreventiveMaintenanceDialog(object):
    def setupUi(self, PreventiveMaintenanceDialog):
        if not PreventiveMaintenanceDialog.objectName():
            PreventiveMaintenanceDialog.setObjectName(u"PreventiveMaintenanceDialog")
        PreventiveMaintenanceDialog.resize(637, 878)
        self.mainLayout = QVBoxLayout(PreventiveMaintenanceDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.groupGeneralInfo = QGroupBox(PreventiveMaintenanceDialog)
        self.groupGeneralInfo.setObjectName(u"groupGeneralInfo")
        self.groupGeneralInfo.setFlat(True)
        self.formGeneralInfo = QFormLayout(self.groupGeneralInfo)
        self.formGeneralInfo.setObjectName(u"formGeneralInfo")
        self.lblPMNumber = QLabel(self.groupGeneralInfo)
        self.lblPMNumber.setObjectName(u"lblPMNumber")

        self.formGeneralInfo.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblPMNumber)

        self.txtPMNumber = QLineEdit(self.groupGeneralInfo)
        self.txtPMNumber.setObjectName(u"txtPMNumber")
        self.txtPMNumber.setReadOnly(True)

        self.formGeneralInfo.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtPMNumber)

        self.lblAsset = QLabel(self.groupGeneralInfo)
        self.lblAsset.setObjectName(u"lblAsset")

        self.formGeneralInfo.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblAsset)

        self.cmbAsset = QComboBox(self.groupGeneralInfo)
        self.cmbAsset.setObjectName(u"cmbAsset")

        self.formGeneralInfo.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbAsset)

        self.lblTask = QLabel(self.groupGeneralInfo)
        self.lblTask.setObjectName(u"lblTask")

        self.formGeneralInfo.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblTask)

        self.txtTask = QLineEdit(self.groupGeneralInfo)
        self.txtTask.setObjectName(u"txtTask")

        self.formGeneralInfo.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtTask)

        self.lblDescription = QLabel(self.groupGeneralInfo)
        self.lblDescription.setObjectName(u"lblDescription")

        self.formGeneralInfo.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblDescription)

        self.teDescription = QTextEdit(self.groupGeneralInfo)
        self.teDescription.setObjectName(u"teDescription")

        self.formGeneralInfo.setWidget(3, QFormLayout.ItemRole.FieldRole, self.teDescription)


        self.mainLayout.addWidget(self.groupGeneralInfo)

        self.groupSchedule = QGroupBox(PreventiveMaintenanceDialog)
        self.groupSchedule.setObjectName(u"groupSchedule")
        self.groupSchedule.setFlat(True)
        self.gridSchedule = QGridLayout(self.groupSchedule)
        self.gridSchedule.setObjectName(u"gridSchedule")
        self.lblFrequencyType = QLabel(self.groupSchedule)
        self.lblFrequencyType.setObjectName(u"lblFrequencyType")

        self.gridSchedule.addWidget(self.lblFrequencyType, 0, 0, 1, 1)

        self.cmbFrequencyType = QComboBox(self.groupSchedule)
        self.cmbFrequencyType.addItem("")
        self.cmbFrequencyType.addItem("")
        self.cmbFrequencyType.addItem("")
        self.cmbFrequencyType.addItem("")
        self.cmbFrequencyType.setObjectName(u"cmbFrequencyType")

        self.gridSchedule.addWidget(self.cmbFrequencyType, 0, 1, 1, 1)

        self.lblFrequencyValue = QLabel(self.groupSchedule)
        self.lblFrequencyValue.setObjectName(u"lblFrequencyValue")

        self.gridSchedule.addWidget(self.lblFrequencyValue, 0, 2, 1, 1)

        self.spnFrequencyValue = QSpinBox(self.groupSchedule)
        self.spnFrequencyValue.setObjectName(u"spnFrequencyValue")
        self.spnFrequencyValue.setMinimum(1)
        self.spnFrequencyValue.setMaximum(365)

        self.gridSchedule.addWidget(self.spnFrequencyValue, 0, 3, 1, 1)

        self.lblLastService = QLabel(self.groupSchedule)
        self.lblLastService.setObjectName(u"lblLastService")

        self.gridSchedule.addWidget(self.lblLastService, 1, 0, 1, 1)

        self.dtLastService = QDateEdit(self.groupSchedule)
        self.dtLastService.setObjectName(u"dtLastService")
        self.dtLastService.setCalendarPopup(True)

        self.gridSchedule.addWidget(self.dtLastService, 1, 1, 1, 1)

        self.lblNextDue = QLabel(self.groupSchedule)
        self.lblNextDue.setObjectName(u"lblNextDue")

        self.gridSchedule.addWidget(self.lblNextDue, 1, 2, 1, 1)

        self.dtNextDue = QDateEdit(self.groupSchedule)
        self.dtNextDue.setObjectName(u"dtNextDue")
        self.dtNextDue.setCalendarPopup(True)

        self.gridSchedule.addWidget(self.dtNextDue, 1, 3, 1, 1)


        self.mainLayout.addWidget(self.groupSchedule)

        self.groupPlanning = QGroupBox(PreventiveMaintenanceDialog)
        self.groupPlanning.setObjectName(u"groupPlanning")
        self.groupPlanning.setFlat(True)
        self.formPlanning = QFormLayout(self.groupPlanning)
        self.formPlanning.setObjectName(u"formPlanning")
        self.lblPriority = QLabel(self.groupPlanning)
        self.lblPriority.setObjectName(u"lblPriority")

        self.formPlanning.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblPriority)

        self.cmbPriority = QComboBox(self.groupPlanning)
        self.cmbPriority.addItem("")
        self.cmbPriority.addItem("")
        self.cmbPriority.addItem("")
        self.cmbPriority.setObjectName(u"cmbPriority")

        self.formPlanning.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbPriority)

        self.lblEstimatedHours = QLabel(self.groupPlanning)
        self.lblEstimatedHours.setObjectName(u"lblEstimatedHours")

        self.formPlanning.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblEstimatedHours)

        self.dsbEstimatedHours = QDoubleSpinBox(self.groupPlanning)
        self.dsbEstimatedHours.setObjectName(u"dsbEstimatedHours")
        self.dsbEstimatedHours.setDecimals(2)
        self.dsbEstimatedHours.setMaximum(9999.989999999999782)

        self.formPlanning.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dsbEstimatedHours)

        self.lblEstimatedCost = QLabel(self.groupPlanning)
        self.lblEstimatedCost.setObjectName(u"lblEstimatedCost")

        self.formPlanning.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblEstimatedCost)

        self.dsbEstimatedCost = QDoubleSpinBox(self.groupPlanning)
        self.dsbEstimatedCost.setObjectName(u"dsbEstimatedCost")
        self.dsbEstimatedCost.setDecimals(2)
        self.dsbEstimatedCost.setMaximum(999999.989999999990687)

        self.formPlanning.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dsbEstimatedCost)

        self.lblActive = QLabel(self.groupPlanning)
        self.lblActive.setObjectName(u"lblActive")

        self.formPlanning.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblActive)

        self.chkActive = QCheckBox(self.groupPlanning)
        self.chkActive.setObjectName(u"chkActive")

        self.formPlanning.setWidget(3, QFormLayout.ItemRole.FieldRole, self.chkActive)


        self.mainLayout.addWidget(self.groupPlanning)

        self.groupNotes = QGroupBox(PreventiveMaintenanceDialog)
        self.groupNotes.setObjectName(u"groupNotes")
        self.groupNotes.setFlat(True)
        self.layoutNotes = QVBoxLayout(self.groupNotes)
        self.layoutNotes.setObjectName(u"layoutNotes")
        self.teNotes = QTextEdit(self.groupNotes)
        self.teNotes.setObjectName(u"teNotes")

        self.layoutNotes.addWidget(self.teNotes)


        self.mainLayout.addWidget(self.groupNotes)

        self.buttonBox = QDialogButtonBox(PreventiveMaintenanceDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.mainLayout.addWidget(self.buttonBox)


        self.retranslateUi(PreventiveMaintenanceDialog)

        QMetaObject.connectSlotsByName(PreventiveMaintenanceDialog)
    # setupUi

    def retranslateUi(self, PreventiveMaintenanceDialog):
        PreventiveMaintenanceDialog.setWindowTitle(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Preventive Maintenance", None))
        self.groupGeneralInfo.setTitle(QCoreApplication.translate("PreventiveMaintenanceDialog", u"General Information", None))
        self.lblPMNumber.setText(QCoreApplication.translate("PreventiveMaintenanceDialog", u"PM Number:", None))
        self.lblAsset.setText(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Asset:", None))
        self.lblTask.setText(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Task:", None))
        self.lblDescription.setText(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Description:", None))
        self.groupSchedule.setTitle(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Schedule", None))
        self.lblFrequencyType.setText(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Frequency Type:", None))
        self.cmbFrequencyType.setItemText(0, QCoreApplication.translate("PreventiveMaintenanceDialog", u"Daily", None))
        self.cmbFrequencyType.setItemText(1, QCoreApplication.translate("PreventiveMaintenanceDialog", u"Weekly", None))
        self.cmbFrequencyType.setItemText(2, QCoreApplication.translate("PreventiveMaintenanceDialog", u"Monthly", None))
        self.cmbFrequencyType.setItemText(3, QCoreApplication.translate("PreventiveMaintenanceDialog", u"Yearly", None))

        self.lblFrequencyValue.setText(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Frequency Value:", None))
        self.lblLastService.setText(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Last Service:", None))
        self.lblNextDue.setText(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Next Due:", None))
        self.groupPlanning.setTitle(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Planning", None))
        self.lblPriority.setText(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Priority:", None))
        self.cmbPriority.setItemText(0, QCoreApplication.translate("PreventiveMaintenanceDialog", u"Low", None))
        self.cmbPriority.setItemText(1, QCoreApplication.translate("PreventiveMaintenanceDialog", u"Medium", None))
        self.cmbPriority.setItemText(2, QCoreApplication.translate("PreventiveMaintenanceDialog", u"High", None))

        self.lblEstimatedHours.setText(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Estimated Hours:", None))
        self.lblEstimatedCost.setText(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Estimated Cost:", None))
        self.lblActive.setText(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Active:", None))
        self.groupNotes.setTitle(QCoreApplication.translate("PreventiveMaintenanceDialog", u"Notes", None))
    # retranslateUi

