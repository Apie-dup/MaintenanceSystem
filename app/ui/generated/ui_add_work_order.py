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
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_AddWorkOrderDialog(object):
    def setupUi(self, AddWorkOrderDialog):
        if not AddWorkOrderDialog.objectName():
            AddWorkOrderDialog.setObjectName(u"AddWorkOrderDialog")
        AddWorkOrderDialog.resize(560, 970)
        AddWorkOrderDialog.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(AddWorkOrderDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWorkOrder = QTabWidget(AddWorkOrderDialog)
        self.tabWorkOrder.setObjectName(u"tabWorkOrder")
        self.General = QWidget()
        self.General.setObjectName(u"General")
        self.verticalLayout_3 = QVBoxLayout(self.General)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupGeneralInfo = QGroupBox(self.General)
        self.groupGeneralInfo.setObjectName(u"groupGeneralInfo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupGeneralInfo.sizePolicy().hasHeightForWidth())
        self.groupGeneralInfo.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.groupGeneralInfo)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(8)
        self.lblWorkOrderNumber = QLabel(self.groupGeneralInfo)
        self.lblWorkOrderNumber.setObjectName(u"lblWorkOrderNumber")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblWorkOrderNumber)

        self.txtWorkOrderNumber = QLineEdit(self.groupGeneralInfo)
        self.txtWorkOrderNumber.setObjectName(u"txtWorkOrderNumber")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtWorkOrderNumber)

        self.lblTitle = QLabel(self.groupGeneralInfo)
        self.lblTitle.setObjectName(u"lblTitle")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblTitle)

        self.txtTitle = QLineEdit(self.groupGeneralInfo)
        self.txtTitle.setObjectName(u"txtTitle")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtTitle)

        self.lblDescription = QLabel(self.groupGeneralInfo)
        self.lblDescription.setObjectName(u"lblDescription")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblDescription)

        self.teDescription = QPlainTextEdit(self.groupGeneralInfo)
        self.teDescription.setObjectName(u"teDescription")
        sizePolicy.setHeightForWidth(self.teDescription.sizePolicy().hasHeightForWidth())
        self.teDescription.setSizePolicy(sizePolicy)
        self.teDescription.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.teDescription)

        self.lblPriority = QLabel(self.groupGeneralInfo)
        self.lblPriority.setObjectName(u"lblPriority")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblPriority)

        self.cmbPriority = QComboBox(self.groupGeneralInfo)
        self.cmbPriority.setObjectName(u"cmbPriority")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbPriority)

        self.lblStatus = QLabel(self.groupGeneralInfo)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.cmbStatus = QComboBox(self.groupGeneralInfo)
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbStatus)


        self.verticalLayout_3.addWidget(self.groupGeneralInfo)

        self.groupAssignment = QGroupBox(self.General)
        self.groupAssignment.setObjectName(u"groupAssignment")
        sizePolicy.setHeightForWidth(self.groupAssignment.sizePolicy().hasHeightForWidth())
        self.groupAssignment.setSizePolicy(sizePolicy)
        self.formLayout_2 = QFormLayout(self.groupAssignment)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lblAsset = QLabel(self.groupAssignment)
        self.lblAsset.setObjectName(u"lblAsset")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblAsset)

        self.cmbAsset = QComboBox(self.groupAssignment)
        self.cmbAsset.setObjectName(u"cmbAsset")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbAsset)

        self.lblTechnician = QLabel(self.groupAssignment)
        self.lblTechnician.setObjectName(u"lblTechnician")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblTechnician)

        self.cmbTechnician = QComboBox(self.groupAssignment)
        self.cmbTechnician.setObjectName(u"cmbTechnician")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbTechnician)

        self.lblRequestedBy = QLabel(self.groupAssignment)
        self.lblRequestedBy.setObjectName(u"lblRequestedBy")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblRequestedBy)

        self.txtRequestedBy = QLineEdit(self.groupAssignment)
        self.txtRequestedBy.setObjectName(u"txtRequestedBy")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtRequestedBy)


        self.verticalLayout_3.addWidget(self.groupAssignment)

        self.groupDatesCosts = QGroupBox(self.General)
        self.groupDatesCosts.setObjectName(u"groupDatesCosts")
        sizePolicy.setHeightForWidth(self.groupDatesCosts.sizePolicy().hasHeightForWidth())
        self.groupDatesCosts.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.groupDatesCosts)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblDateCreated = QLabel(self.groupDatesCosts)
        self.lblDateCreated.setObjectName(u"lblDateCreated")

        self.gridLayout.addWidget(self.lblDateCreated, 0, 0, 1, 1)

        self.dtDateCreated = QDateEdit(self.groupDatesCosts)
        self.dtDateCreated.setObjectName(u"dtDateCreated")

        self.gridLayout.addWidget(self.dtDateCreated, 0, 1, 1, 1)

        self.lblDueDate = QLabel(self.groupDatesCosts)
        self.lblDueDate.setObjectName(u"lblDueDate")

        self.gridLayout.addWidget(self.lblDueDate, 0, 2, 1, 1)

        self.dtDueDate = QDateEdit(self.groupDatesCosts)
        self.dtDueDate.setObjectName(u"dtDueDate")

        self.gridLayout.addWidget(self.dtDueDate, 0, 3, 1, 1)

        self.lblEstimatedCost = QLabel(self.groupDatesCosts)
        self.lblEstimatedCost.setObjectName(u"lblEstimatedCost")

        self.gridLayout.addWidget(self.lblEstimatedCost, 1, 0, 1, 1)

        self.dsbEstimatedCost = QDoubleSpinBox(self.groupDatesCosts)
        self.dsbEstimatedCost.setObjectName(u"dsbEstimatedCost")

        self.gridLayout.addWidget(self.dsbEstimatedCost, 1, 1, 1, 1)

        self.lblActualCost = QLabel(self.groupDatesCosts)
        self.lblActualCost.setObjectName(u"lblActualCost")

        self.gridLayout.addWidget(self.lblActualCost, 1, 2, 1, 1)

        self.dsbActualCost = QDoubleSpinBox(self.groupDatesCosts)
        self.dsbActualCost.setObjectName(u"dsbActualCost")

        self.gridLayout.addWidget(self.dsbActualCost, 1, 3, 1, 1)

        self.lblLabourHours = QLabel(self.groupDatesCosts)
        self.lblLabourHours.setObjectName(u"lblLabourHours")

        self.gridLayout.addWidget(self.lblLabourHours, 2, 0, 1, 1)

        self.dsbLabourHours = QDoubleSpinBox(self.groupDatesCosts)
        self.dsbLabourHours.setObjectName(u"dsbLabourHours")

        self.gridLayout.addWidget(self.dsbLabourHours, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupDatesCosts)

        self.groupNotes = QGroupBox(self.General)
        self.groupNotes.setObjectName(u"groupNotes")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupNotes.sizePolicy().hasHeightForWidth())
        self.groupNotes.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.groupNotes)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.teNotes = QPlainTextEdit(self.groupNotes)
        self.teNotes.setObjectName(u"teNotes")
        sizePolicy1.setHeightForWidth(self.teNotes.sizePolicy().hasHeightForWidth())
        self.teNotes.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.teNotes)


        self.verticalLayout_3.addWidget(self.groupNotes)

        self.tabWorkOrder.addTab(self.General, "")
        self.Materials = QWidget()
        self.Materials.setObjectName(u"Materials")
        self.verticalLayout_5 = QVBoxLayout(self.Materials)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupMaterials = QGroupBox(self.Materials)
        self.groupMaterials.setObjectName(u"groupMaterials")
        self.layoutMaterials = QVBoxLayout(self.groupMaterials)
        self.layoutMaterials.setObjectName(u"layoutMaterials")
        self.tblParts = QTableWidget(self.groupMaterials)
        if (self.tblParts.columnCount() < 5):
            self.tblParts.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblParts.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblParts.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblParts.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblParts.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblParts.setHorizontalHeaderItem(4, __qtablewidgetitem4)
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

        self.labelMaterialsTotal = QLabel(self.groupMaterials)
        self.labelMaterialsTotal.setObjectName(u"labelMaterialsTotal")

        self.horizontalLayout_2.addWidget(self.labelMaterialsTotal)


        self.layoutMaterials.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.groupMaterials)

        self.tabWorkOrder.addTab(self.Materials, "")
        self.History = QWidget()
        self.History.setObjectName(u"History")
        self.verticalLayout_6 = QVBoxLayout(self.History)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupHistory = QGroupBox(self.History)
        self.groupHistory.setObjectName(u"groupHistory")
        self.verticalLayout_4 = QVBoxLayout(self.groupHistory)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tblHistory = QTableWidget(self.groupHistory)
        self.tblHistory.setObjectName(u"tblHistory")

        self.verticalLayout_4.addWidget(self.tblHistory)


        self.verticalLayout_6.addWidget(self.groupHistory)

        self.tabWorkOrder.addTab(self.History, "")

        self.verticalLayout.addWidget(self.tabWorkOrder)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnComplete = QPushButton(AddWorkOrderDialog)
        self.btnComplete.setObjectName(u"btnComplete")

        self.horizontalLayout.addWidget(self.btnComplete)

        self.btnCloseWorkOrder = QPushButton(AddWorkOrderDialog)
        self.btnCloseWorkOrder.setObjectName(u"btnCloseWorkOrder")

        self.horizontalLayout.addWidget(self.btnCloseWorkOrder)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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
        self.lblDateCreated.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Date Created:", None))
        self.lblDueDate.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Due Date:", None))
        self.lblEstimatedCost.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Estimated Cost:", None))
        self.lblActualCost.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Actual Cost:", None))
        self.lblLabourHours.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Labour Hours:", None))
        self.groupNotes.setTitle(QCoreApplication.translate("AddWorkOrderDialog", u"Notes", None))
        self.tabWorkOrder.setTabText(self.tabWorkOrder.indexOf(self.General), QCoreApplication.translate("AddWorkOrderDialog", u"Genareal", None))
        self.groupMaterials.setTitle(QCoreApplication.translate("AddWorkOrderDialog", u"Materials Used", None))
        ___qtablewidgetitem = self.tblParts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Part Number", None))
        ___qtablewidgetitem1 = self.tblParts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Part Name", None))
        ___qtablewidgetitem2 = self.tblParts.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Qty", None))
        ___qtablewidgetitem3 = self.tblParts.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Unit Cost", None))
        ___qtablewidgetitem4 = self.tblParts.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Total", None))
        self.btnIssuePart.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Issue Parts", None))
        self.btnRemovePart.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Remove Parts", None))
        self.labelMaterialsTotal.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Materials Total: N$0.00", None))
        self.tabWorkOrder.setTabText(self.tabWorkOrder.indexOf(self.Materials), QCoreApplication.translate("AddWorkOrderDialog", u"Materials", None))
        self.groupHistory.setTitle(QCoreApplication.translate("AddWorkOrderDialog", u"Work Order History", None))
        self.tabWorkOrder.setTabText(self.tabWorkOrder.indexOf(self.History), QCoreApplication.translate("AddWorkOrderDialog", u"History", None))
        self.btnComplete.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Complete Work Order", None))
        self.btnCloseWorkOrder.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Close Work Order", None))
    # retranslateUi

