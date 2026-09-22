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
from PySide6.QtWidgets import (QAbstractButton, QAbstractScrollArea, QApplication, QComboBox,
    QDateEdit, QDialog, QDialogButtonBox, QDoubleSpinBox,
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_AddWorkOrderDialog(object):
    def setupUi(self, AddWorkOrderDialog):
        if not AddWorkOrderDialog.objectName():
            AddWorkOrderDialog.setObjectName(u"AddWorkOrderDialog")
        AddWorkOrderDialog.resize(845, 702)
        AddWorkOrderDialog.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(AddWorkOrderDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWorkOrder = QTabWidget(AddWorkOrderDialog)
        self.tabWorkOrder.setObjectName(u"tabWorkOrder")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWorkOrder.sizePolicy().hasHeightForWidth())
        self.tabWorkOrder.setSizePolicy(sizePolicy)
        self.tabGeneral = QWidget()
        self.tabGeneral.setObjectName(u"tabGeneral")
        self.verticalLayout_3 = QVBoxLayout(self.tabGeneral)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupGeneralInfo = QGroupBox(self.tabGeneral)
        self.groupGeneralInfo.setObjectName(u"groupGeneralInfo")
        sizePolicy.setHeightForWidth(self.groupGeneralInfo.sizePolicy().hasHeightForWidth())
        self.groupGeneralInfo.setSizePolicy(sizePolicy)
        self.formGeneralInfo = QFormLayout(self.groupGeneralInfo)
        self.formGeneralInfo.setObjectName(u"formGeneralInfo")
        self.formGeneralInfo.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapLongRows)
        self.formGeneralInfo.setHorizontalSpacing(12)
        self.formGeneralInfo.setVerticalSpacing(8)
        self.lblWorkOrderNumber = QLabel(self.groupGeneralInfo)
        self.lblWorkOrderNumber.setObjectName(u"lblWorkOrderNumber")

        self.formGeneralInfo.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblWorkOrderNumber)

        self.txtWorkOrderNumber = QLineEdit(self.groupGeneralInfo)
        self.txtWorkOrderNumber.setObjectName(u"txtWorkOrderNumber")
        self.txtWorkOrderNumber.setMinimumSize(QSize(0, 20))

        self.formGeneralInfo.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtWorkOrderNumber)

        self.lblTitle = QLabel(self.groupGeneralInfo)
        self.lblTitle.setObjectName(u"lblTitle")

        self.formGeneralInfo.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblTitle)

        self.txtTitle = QLineEdit(self.groupGeneralInfo)
        self.txtTitle.setObjectName(u"txtTitle")
        self.txtTitle.setMinimumSize(QSize(0, 20))

        self.formGeneralInfo.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtTitle)

        self.lblDescription = QLabel(self.groupGeneralInfo)
        self.lblDescription.setObjectName(u"lblDescription")

        self.formGeneralInfo.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblDescription)

        self.teDescription = QPlainTextEdit(self.groupGeneralInfo)
        self.teDescription.setObjectName(u"teDescription")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.teDescription.sizePolicy().hasHeightForWidth())
        self.teDescription.setSizePolicy(sizePolicy1)
        self.teDescription.setMinimumSize(QSize(0, 80))

        self.formGeneralInfo.setWidget(2, QFormLayout.ItemRole.FieldRole, self.teDescription)

        self.lblPriority = QLabel(self.groupGeneralInfo)
        self.lblPriority.setObjectName(u"lblPriority")

        self.formGeneralInfo.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblPriority)

        self.cmbPriority = QComboBox(self.groupGeneralInfo)
        self.cmbPriority.setObjectName(u"cmbPriority")
        self.cmbPriority.setMinimumSize(QSize(0, 20))

        self.formGeneralInfo.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbPriority)

        self.lblStatus = QLabel(self.groupGeneralInfo)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formGeneralInfo.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.cmbStatus = QComboBox(self.groupGeneralInfo)
        self.cmbStatus.setObjectName(u"cmbStatus")
        self.cmbStatus.setMinimumSize(QSize(0, 20))

        self.formGeneralInfo.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbStatus)


        self.verticalLayout_3.addWidget(self.groupGeneralInfo)

        self.groupAssignment = QGroupBox(self.tabGeneral)
        self.groupAssignment.setObjectName(u"groupAssignment")
        sizePolicy.setHeightForWidth(self.groupAssignment.sizePolicy().hasHeightForWidth())
        self.groupAssignment.setSizePolicy(sizePolicy)
        self.formAssignment = QFormLayout(self.groupAssignment)
        self.formAssignment.setObjectName(u"formAssignment")
        self.formAssignment.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapLongRows)
        self.lblAsset = QLabel(self.groupAssignment)
        self.lblAsset.setObjectName(u"lblAsset")

        self.formAssignment.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblAsset)

        self.cmbAsset = QComboBox(self.groupAssignment)
        self.cmbAsset.setObjectName(u"cmbAsset")
        self.cmbAsset.setMinimumSize(QSize(0, 20))

        self.formAssignment.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbAsset)

        self.lblTechnician = QLabel(self.groupAssignment)
        self.lblTechnician.setObjectName(u"lblTechnician")

        self.formAssignment.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblTechnician)

        self.cmbTechnician = QComboBox(self.groupAssignment)
        self.cmbTechnician.setObjectName(u"cmbTechnician")
        self.cmbTechnician.setMinimumSize(QSize(0, 20))

        self.formAssignment.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbTechnician)

        self.lblRequestedBy = QLabel(self.groupAssignment)
        self.lblRequestedBy.setObjectName(u"lblRequestedBy")

        self.formAssignment.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblRequestedBy)

        self.txtRequestedBy = QLineEdit(self.groupAssignment)
        self.txtRequestedBy.setObjectName(u"txtRequestedBy")
        self.txtRequestedBy.setMinimumSize(QSize(0, 20))

        self.formAssignment.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtRequestedBy)


        self.verticalLayout_3.addWidget(self.groupAssignment)

        self.groupDatesCosts = QGroupBox(self.tabGeneral)
        self.groupDatesCosts.setObjectName(u"groupDatesCosts")
        sizePolicy.setHeightForWidth(self.groupDatesCosts.sizePolicy().hasHeightForWidth())
        self.groupDatesCosts.setSizePolicy(sizePolicy)
        self.gridDatesCosts = QGridLayout(self.groupDatesCosts)
        self.gridDatesCosts.setObjectName(u"gridDatesCosts")
        self.dsbEstimatedHours = QDoubleSpinBox(self.groupDatesCosts)
        self.dsbEstimatedHours.setObjectName(u"dsbEstimatedHours")
        self.dsbEstimatedHours.setMaximum(999999.989999999990687)

        self.gridDatesCosts.addWidget(self.dsbEstimatedHours, 2, 1, 1, 1)

        self.dsbEstimatedCost = QDoubleSpinBox(self.groupDatesCosts)
        self.dsbEstimatedCost.setObjectName(u"dsbEstimatedCost")
        self.dsbEstimatedCost.setMinimumSize(QSize(0, 20))
        self.dsbEstimatedCost.setMaximum(999999.989999999990687)

        self.gridDatesCosts.addWidget(self.dsbEstimatedCost, 1, 1, 1, 1)

        self.dtDueDate = QDateEdit(self.groupDatesCosts)
        self.dtDueDate.setObjectName(u"dtDueDate")
        self.dtDueDate.setMinimumSize(QSize(0, 20))

        self.gridDatesCosts.addWidget(self.dtDueDate, 0, 3, 1, 1)

        self.lblDateCreated = QLabel(self.groupDatesCosts)
        self.lblDateCreated.setObjectName(u"lblDateCreated")

        self.gridDatesCosts.addWidget(self.lblDateCreated, 0, 0, 1, 1)

        self.lblEstimatedCost = QLabel(self.groupDatesCosts)
        self.lblEstimatedCost.setObjectName(u"lblEstimatedCost")

        self.gridDatesCosts.addWidget(self.lblEstimatedCost, 1, 0, 1, 1)

        self.dsbActualCost = QDoubleSpinBox(self.groupDatesCosts)
        self.dsbActualCost.setObjectName(u"dsbActualCost")
        self.dsbActualCost.setMinimumSize(QSize(0, 20))
        self.dsbActualCost.setMaximum(999999.989999999990687)

        self.gridDatesCosts.addWidget(self.dsbActualCost, 1, 3, 1, 1)

        self.dtDateCreated = QDateEdit(self.groupDatesCosts)
        self.dtDateCreated.setObjectName(u"dtDateCreated")
        self.dtDateCreated.setMinimumSize(QSize(0, 20))

        self.gridDatesCosts.addWidget(self.dtDateCreated, 0, 1, 1, 1)

        self.lblDueDate = QLabel(self.groupDatesCosts)
        self.lblDueDate.setObjectName(u"lblDueDate")

        self.gridDatesCosts.addWidget(self.lblDueDate, 0, 2, 1, 1)

        self.lblLabourHours = QLabel(self.groupDatesCosts)
        self.lblLabourHours.setObjectName(u"lblLabourHours")

        self.gridDatesCosts.addWidget(self.lblLabourHours, 2, 2, 1, 1)

        self.lblEstimatedHours = QLabel(self.groupDatesCosts)
        self.lblEstimatedHours.setObjectName(u"lblEstimatedHours")

        self.gridDatesCosts.addWidget(self.lblEstimatedHours, 2, 0, 1, 1)

        self.lblActualCost = QLabel(self.groupDatesCosts)
        self.lblActualCost.setObjectName(u"lblActualCost")

        self.gridDatesCosts.addWidget(self.lblActualCost, 1, 2, 1, 1)

        self.dsbLabourHours = QDoubleSpinBox(self.groupDatesCosts)
        self.dsbLabourHours.setObjectName(u"dsbLabourHours")
        self.dsbLabourHours.setMinimumSize(QSize(0, 20))

        self.gridDatesCosts.addWidget(self.dsbLabourHours, 2, 3, 1, 1)

        self.lblMeterReading = QLabel(self.groupDatesCosts)
        self.lblMeterReading.setObjectName(u"lblMeterReading")

        self.gridDatesCosts.addWidget(self.lblMeterReading, 3, 0, 1, 1)

        self.dsbMeterReading = QDoubleSpinBox(self.groupDatesCosts)
        self.dsbMeterReading.setObjectName(u"dsbMeterReading")
        self.dsbMeterReading.setMinimumSize(QSize(0, 20))
        self.dsbMeterReading.setMaximum(999999.989999999990687)

        self.gridDatesCosts.addWidget(self.dsbMeterReading, 3, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupDatesCosts)

        self.groupNotes = QGroupBox(self.tabGeneral)
        self.groupNotes.setObjectName(u"groupNotes")
        sizePolicy1.setHeightForWidth(self.groupNotes.sizePolicy().hasHeightForWidth())
        self.groupNotes.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.groupNotes)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.teNotes = QPlainTextEdit(self.groupNotes)
        self.teNotes.setObjectName(u"teNotes")
        sizePolicy.setHeightForWidth(self.teNotes.sizePolicy().hasHeightForWidth())
        self.teNotes.setSizePolicy(sizePolicy)
        self.teNotes.setMinimumSize(QSize(0, 40))
        self.teNotes.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.verticalLayout_2.addWidget(self.teNotes)


        self.verticalLayout_3.addWidget(self.groupNotes)

        self.tabWorkOrder.addTab(self.tabGeneral, "")
        self.tabMaterials = QWidget()
        self.tabMaterials.setObjectName(u"tabMaterials")
        self.verticalLayout_5 = QVBoxLayout(self.tabMaterials)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupMaterials = QGroupBox(self.tabMaterials)
        self.groupMaterials.setObjectName(u"groupMaterials")
        self.layoutMaterials = QVBoxLayout(self.groupMaterials)
        self.layoutMaterials.setObjectName(u"layoutMaterials")
        self.tblParts = QTableWidget(self.groupMaterials)
        self.tblParts.setObjectName(u"tblParts")

        self.layoutMaterials.addWidget(self.tblParts)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnIssuePart = QPushButton(self.groupMaterials)
        self.btnIssuePart.setObjectName(u"btnIssuePart")

        self.horizontalLayout_2.addWidget(self.btnIssuePart)

        self.btnRemovePart = QPushButton(self.groupMaterials)
        self.btnRemovePart.setObjectName(u"btnRemovePart")

        self.horizontalLayout_2.addWidget(self.btnRemovePart)

        self.lblMaterialTotal = QLabel(self.groupMaterials)
        self.lblMaterialTotal.setObjectName(u"lblMaterialTotal")

        self.horizontalLayout_2.addWidget(self.lblMaterialTotal)


        self.layoutMaterials.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.groupMaterials)

        self.tabWorkOrder.addTab(self.tabMaterials, "")
        self.tabLabour = QWidget()
        self.tabLabour.setObjectName(u"tabLabour")
        self.verticalLayout_7 = QVBoxLayout(self.tabLabour)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tblLabour = QTableWidget(self.tabLabour)
        if (self.tblLabour.columnCount() < 8):
            self.tblLabour.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblLabour.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblLabour.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblLabour.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblLabour.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblLabour.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblLabour.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblLabour.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblLabour.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tblLabour.setObjectName(u"tblLabour")

        self.verticalLayout_7.addWidget(self.tblLabour)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnAddLabour = QPushButton(self.tabLabour)
        self.btnAddLabour.setObjectName(u"btnAddLabour")

        self.horizontalLayout_3.addWidget(self.btnAddLabour)

        self.btnRemoveLabour = QPushButton(self.tabLabour)
        self.btnRemoveLabour.setObjectName(u"btnRemoveLabour")

        self.horizontalLayout_3.addWidget(self.btnRemoveLabour)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tabWorkOrder.addTab(self.tabLabour, "")
        self.tabHistory = QWidget()
        self.tabHistory.setObjectName(u"tabHistory")
        self.verticalLayout_6 = QVBoxLayout(self.tabHistory)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupHistory = QGroupBox(self.tabHistory)
        self.groupHistory.setObjectName(u"groupHistory")
        self.verticalLayout_4 = QVBoxLayout(self.groupHistory)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tblHistory = QTableWidget(self.groupHistory)
        self.tblHistory.setObjectName(u"tblHistory")

        self.verticalLayout_4.addWidget(self.tblHistory)


        self.verticalLayout_6.addWidget(self.groupHistory)

        self.tabWorkOrder.addTab(self.tabHistory, "")

        self.verticalLayout.addWidget(self.tabWorkOrder)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnComplete = QPushButton(AddWorkOrderDialog)
        self.btnComplete.setObjectName(u"btnComplete")

        self.horizontalLayout.addWidget(self.btnComplete)

        self.btnCloseWorkOrder = QPushButton(AddWorkOrderDialog)
        self.btnCloseWorkOrder.setObjectName(u"btnCloseWorkOrder")

        self.horizontalLayout.addWidget(self.btnCloseWorkOrder)

        self.btnReopen = QPushButton(AddWorkOrderDialog)
        self.btnReopen.setObjectName(u"btnReopen")

        self.horizontalLayout.addWidget(self.btnReopen)

        self.btnCancelWorkOrder = QPushButton(AddWorkOrderDialog)
        self.btnCancelWorkOrder.setObjectName(u"btnCancelWorkOrder")

        self.horizontalLayout.addWidget(self.btnCancelWorkOrder)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(AddWorkOrderDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AddWorkOrderDialog)

        self.tabWorkOrder.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AddWorkOrderDialog)
    # setupUi

    def retranslateUi(self, AddWorkOrderDialog):
        AddWorkOrderDialog.setWindowTitle(QCoreApplication.translate("AddWorkOrderDialog", u"Add Work Order", None))
        self.groupGeneralInfo.setTitle(QCoreApplication.translate("AddWorkOrderDialog", u"General Information", None))
        self.lblWorkOrderNumber.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Work Order Number:", None))
        self.lblTitle.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Title:", None))
        self.lblDescription.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Description:", None))
        self.lblPriority.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Priority:", None))
        self.lblStatus.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Status:", None))
        self.groupAssignment.setTitle(QCoreApplication.translate("AddWorkOrderDialog", u"Assignment", None))
        self.lblAsset.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Asset:", None))
        self.lblTechnician.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Technician:", None))
        self.lblRequestedBy.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Requested By:", None))
        self.groupDatesCosts.setTitle(QCoreApplication.translate("AddWorkOrderDialog", u"Dates and Costs", None))
        self.dsbEstimatedCost.setPrefix("")
        self.lblDateCreated.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Date Created:", None))
        self.lblEstimatedCost.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Estimated Cost:", None))
        self.dsbActualCost.setPrefix("")
        self.lblDueDate.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Due Date:", None))
        self.lblLabourHours.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Labour Hours:", None))
        self.lblEstimatedHours.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Estimated Hours:", None))
        self.lblActualCost.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Actual Cost:", None))
        self.lblMeterReading.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Meter Reading:", None))
        self.groupNotes.setTitle(QCoreApplication.translate("AddWorkOrderDialog", u"Notes", None))
        self.tabWorkOrder.setTabText(self.tabWorkOrder.indexOf(self.tabGeneral), QCoreApplication.translate("AddWorkOrderDialog", u"General", None))
        self.groupMaterials.setTitle(QCoreApplication.translate("AddWorkOrderDialog", u"Materials Used", None))
        self.btnIssuePart.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Issue Parts", None))
        self.btnRemovePart.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Remove Parts", None))
        self.lblMaterialTotal.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Materials Total: 0.00", None))
        self.tabWorkOrder.setTabText(self.tabWorkOrder.indexOf(self.tabMaterials), QCoreApplication.translate("AddWorkOrderDialog", u"Materials", None))
        ___qtablewidgetitem = self.tblLabour.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Technician", None))
        ___qtablewidgetitem1 = self.tblLabour.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Work Date", None))
        ___qtablewidgetitem2 = self.tblLabour.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Hours", None))
        ___qtablewidgetitem3 = self.tblLabour.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Hourly Rate", None))
        ___qtablewidgetitem4 = self.tblLabour.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Labour Cost", None))
        ___qtablewidgetitem5 = self.tblLabour.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Description", None))
        ___qtablewidgetitem6 = self.tblLabour.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Entered By", None))
        ___qtablewidgetitem7 = self.tblLabour.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Created At", None))
        self.btnAddLabour.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Add Labour", None))
        self.btnRemoveLabour.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Remove Labour", None))
        self.tabWorkOrder.setTabText(self.tabWorkOrder.indexOf(self.tabLabour), QCoreApplication.translate("AddWorkOrderDialog", u"Labour", None))
        self.groupHistory.setTitle(QCoreApplication.translate("AddWorkOrderDialog", u"Work Order History", None))
        self.tabWorkOrder.setTabText(self.tabWorkOrder.indexOf(self.tabHistory), QCoreApplication.translate("AddWorkOrderDialog", u"History", None))
        self.btnComplete.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Complete Work Order", None))
        self.btnCloseWorkOrder.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Close Work Order", None))
        self.btnReopen.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Reopen Work Order", None))
        self.btnCancelWorkOrder.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Cancel Work Order", None))
    # retranslateUi

