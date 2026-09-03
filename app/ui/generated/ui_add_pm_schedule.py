# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_pm_schedule.ui'
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
    QFormLayout, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QPlainTextEdit, QSizePolicy,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_PreventiveMaintenaceDialog(object):
    def setupUi(self, PreventiveMaintenaceDialog):
        if not PreventiveMaintenaceDialog.objectName():
            PreventiveMaintenaceDialog.setObjectName(u"PreventiveMaintenaceDialog")
        PreventiveMaintenaceDialog.resize(820, 720)
        PreventiveMaintenaceDialog.setMinimumSize(QSize(720, 620))
        PreventiveMaintenaceDialog.setMaximumSize(QSize(1000, 16777215))
        self.verticalLayout = QVBoxLayout(PreventiveMaintenaceDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(PreventiveMaintenaceDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Scheduel = QWidget()
        self.Scheduel.setObjectName(u"Scheduel")
        self.verticalLayout_3 = QVBoxLayout(self.Scheduel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupGeneralInfo = QGroupBox(self.Scheduel)
        self.groupGeneralInfo.setObjectName(u"groupGeneralInfo")
        self.formLayout_2 = QFormLayout(self.groupGeneralInfo)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(12)
        self.formLayout_2.setVerticalSpacing(8)
        self.lblPMNumber = QLabel(self.groupGeneralInfo)
        self.lblPMNumber.setObjectName(u"lblPMNumber")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblPMNumber)

        self.txtPMNumber = QLineEdit(self.groupGeneralInfo)
        self.txtPMNumber.setObjectName(u"txtPMNumber")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtPMNumber)

        self.lblAsset = QLabel(self.groupGeneralInfo)
        self.lblAsset.setObjectName(u"lblAsset")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblAsset)

        self.cmbAsset = QComboBox(self.groupGeneralInfo)
        self.cmbAsset.setObjectName(u"cmbAsset")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbAsset)

        self.lblTask = QLabel(self.groupGeneralInfo)
        self.lblTask.setObjectName(u"lblTask")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblTask)

        self.txtTask = QLineEdit(self.groupGeneralInfo)
        self.txtTask.setObjectName(u"txtTask")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtTask)

        self.lblDescription = QLabel(self.groupGeneralInfo)
        self.lblDescription.setObjectName(u"lblDescription")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblDescription)

        self.teDescription = QPlainTextEdit(self.groupGeneralInfo)
        self.teDescription.setObjectName(u"teDescription")
        self.teDescription.setMinimumSize(QSize(0, 70))
        self.teDescription.setMaximumSize(QSize(16777215, 90))

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.teDescription)


        self.verticalLayout_3.addWidget(self.groupGeneralInfo)

        self.groupSchedule = QGroupBox(self.Scheduel)
        self.groupSchedule.setObjectName(u"groupSchedule")
        self.gridLayout = QGridLayout(self.groupSchedule)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(8)
        self.lblFrequencyType = QLabel(self.groupSchedule)
        self.lblFrequencyType.setObjectName(u"lblFrequencyType")

        self.gridLayout.addWidget(self.lblFrequencyType, 0, 0, 1, 1)

        self.cmbFrequencyType = QComboBox(self.groupSchedule)
        self.cmbFrequencyType.setObjectName(u"cmbFrequencyType")

        self.gridLayout.addWidget(self.cmbFrequencyType, 0, 1, 1, 1)

        self.lblFrequencyValue = QLabel(self.groupSchedule)
        self.lblFrequencyValue.setObjectName(u"lblFrequencyValue")

        self.gridLayout.addWidget(self.lblFrequencyValue, 0, 2, 1, 2)

        self.spnFrequencyValue = QSpinBox(self.groupSchedule)
        self.spnFrequencyValue.setObjectName(u"spnFrequencyValue")
        self.spnFrequencyValue.setMaximum(99999999)

        self.gridLayout.addWidget(self.spnFrequencyValue, 0, 4, 1, 1)

        self.lblLastService = QLabel(self.groupSchedule)
        self.lblLastService.setObjectName(u"lblLastService")

        self.gridLayout.addWidget(self.lblLastService, 1, 0, 1, 1)

        self.dtLastService = QDateEdit(self.groupSchedule)
        self.dtLastService.setObjectName(u"dtLastService")

        self.gridLayout.addWidget(self.dtLastService, 1, 1, 1, 1)

        self.lblNextDue = QLabel(self.groupSchedule)
        self.lblNextDue.setObjectName(u"lblNextDue")

        self.gridLayout.addWidget(self.lblNextDue, 1, 2, 1, 1)

        self.dtNextDue = QDateEdit(self.groupSchedule)
        self.dtNextDue.setObjectName(u"dtNextDue")

        self.gridLayout.addWidget(self.dtNextDue, 1, 4, 1, 1)


        self.verticalLayout_3.addWidget(self.groupSchedule)

        self.groupPlanning = QGroupBox(self.Scheduel)
        self.groupPlanning.setObjectName(u"groupPlanning")
        self.gridLayout_2 = QGridLayout(self.groupPlanning)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblPriority = QLabel(self.groupPlanning)
        self.lblPriority.setObjectName(u"lblPriority")

        self.gridLayout_2.addWidget(self.lblPriority, 0, 0, 1, 1)

        self.cmbPriority = QComboBox(self.groupPlanning)
        self.cmbPriority.setObjectName(u"cmbPriority")

        self.gridLayout_2.addWidget(self.cmbPriority, 0, 1, 1, 1)

        self.lblActive = QLabel(self.groupPlanning)
        self.lblActive.setObjectName(u"lblActive")

        self.gridLayout_2.addWidget(self.lblActive, 0, 2, 1, 1)

        self.chkActive = QCheckBox(self.groupPlanning)
        self.chkActive.setObjectName(u"chkActive")

        self.gridLayout_2.addWidget(self.chkActive, 0, 3, 1, 1)

        self.lblEstimatedHours = QLabel(self.groupPlanning)
        self.lblEstimatedHours.setObjectName(u"lblEstimatedHours")

        self.gridLayout_2.addWidget(self.lblEstimatedHours, 1, 0, 1, 1)

        self.dsbEstimatedHours = QDoubleSpinBox(self.groupPlanning)
        self.dsbEstimatedHours.setObjectName(u"dsbEstimatedHours")

        self.gridLayout_2.addWidget(self.dsbEstimatedHours, 1, 1, 1, 1)

        self.lblEstimatedCost = QLabel(self.groupPlanning)
        self.lblEstimatedCost.setObjectName(u"lblEstimatedCost")

        self.gridLayout_2.addWidget(self.lblEstimatedCost, 1, 2, 1, 2)

        self.dsbEstimatedCost = QDoubleSpinBox(self.groupPlanning)
        self.dsbEstimatedCost.setObjectName(u"dsbEstimatedCost")

        self.gridLayout_2.addWidget(self.dsbEstimatedCost, 1, 4, 1, 1)


        self.verticalLayout_3.addWidget(self.groupPlanning)

        self.groupNotes = QGroupBox(self.Scheduel)
        self.groupNotes.setObjectName(u"groupNotes")
        self.verticalLayout_2 = QVBoxLayout(self.groupNotes)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.teNotes = QPlainTextEdit(self.groupNotes)
        self.teNotes.setObjectName(u"teNotes")
        self.teNotes.setMinimumSize(QSize(0, 70))

        self.verticalLayout_2.addWidget(self.teNotes)


        self.verticalLayout_3.addWidget(self.groupNotes)

        self.tabWidget.addTab(self.Scheduel, "")
        self.WorkOrderHistory = QWidget()
        self.WorkOrderHistory.setObjectName(u"WorkOrderHistory")
        self.verticalLayout_5 = QVBoxLayout(self.WorkOrderHistory)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupHistory = QGroupBox(self.WorkOrderHistory)
        self.groupHistory.setObjectName(u"groupHistory")
        self.verticalLayout_4 = QVBoxLayout(self.groupHistory)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tblHistory = QTableWidget(self.groupHistory)
        self.tblHistory.setObjectName(u"tblHistory")

        self.verticalLayout_4.addWidget(self.tblHistory)

        self.lblHistoryCount = QLabel(self.groupHistory)
        self.lblHistoryCount.setObjectName(u"lblHistoryCount")

        self.verticalLayout_4.addWidget(self.lblHistoryCount)


        self.verticalLayout_5.addWidget(self.groupHistory)

        self.tabWidget.addTab(self.WorkOrderHistory, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(PreventiveMaintenaceDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(PreventiveMaintenaceDialog)
        self.buttonBox.accepted.connect(PreventiveMaintenaceDialog.accept)
        self.buttonBox.rejected.connect(PreventiveMaintenaceDialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PreventiveMaintenaceDialog)
    # setupUi

    def retranslateUi(self, PreventiveMaintenaceDialog):
        PreventiveMaintenaceDialog.setWindowTitle(QCoreApplication.translate("PreventiveMaintenaceDialog", u"PM Schedule", None))
        self.groupGeneralInfo.setTitle(QCoreApplication.translate("PreventiveMaintenaceDialog", u"General Information", None))
        self.lblPMNumber.setText(QCoreApplication.translate("PreventiveMaintenaceDialog", u"PM Number:", None))
        self.lblAsset.setText(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Asset:", None))
        self.lblTask.setText(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Task:", None))
        self.lblDescription.setText(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Description:", None))
        self.groupSchedule.setTitle(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Shedule", None))
        self.lblFrequencyType.setText(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Frequency Type:", None))
        self.lblFrequencyValue.setText(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Frequency Value:", None))
        self.lblLastService.setText(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Last Service:", None))
        self.lblNextDue.setText(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Next Due:", None))
        self.groupPlanning.setTitle(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Planning", None))
        self.lblPriority.setText(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Priority:", None))
        self.lblActive.setText(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Active:", None))
        self.chkActive.setText("")
        self.lblEstimatedHours.setText(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Estimated Hours:", None))
        self.lblEstimatedCost.setText(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Estimated Cost:", None))
        self.groupNotes.setTitle(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Notes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Scheduel), QCoreApplication.translate("PreventiveMaintenaceDialog", u"Scheduel", None))
        self.groupHistory.setTitle(QCoreApplication.translate("PreventiveMaintenaceDialog", u"Maintenance Work Order History", None))
        self.lblHistoryCount.setText(QCoreApplication.translate("PreventiveMaintenaceDialog", u"0 Work Orders", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.WorkOrderHistory), QCoreApplication.translate("PreventiveMaintenaceDialog", u"Work Order History", None))
    # retranslateUi

