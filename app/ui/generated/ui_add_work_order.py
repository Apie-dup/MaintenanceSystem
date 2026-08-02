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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_AddWorkOrderDialog(object):
    def setupUi(self, AddWorkOrderDialog):
        if not AddWorkOrderDialog.objectName():
            AddWorkOrderDialog.setObjectName(u"AddWorkOrderDialog")
        AddWorkOrderDialog.resize(800, 780)
        self.mainLayout = QVBoxLayout(AddWorkOrderDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.groupGeneralInfo = QGroupBox(AddWorkOrderDialog)
        self.groupGeneralInfo.setObjectName(u"groupGeneralInfo")
        self.groupGeneralInfo.setFlat(True)
        self.formGeneralInfo = QFormLayout(self.groupGeneralInfo)
        self.formGeneralInfo.setObjectName(u"formGeneralInfo")
        self.lblWorkOrderNumber = QLabel(self.groupGeneralInfo)
        self.lblWorkOrderNumber.setObjectName(u"lblWorkOrderNumber")

        self.formGeneralInfo.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblWorkOrderNumber)

        self.txtWorkOrderNumber = QLineEdit(self.groupGeneralInfo)
        self.txtWorkOrderNumber.setObjectName(u"txtWorkOrderNumber")
        self.txtWorkOrderNumber.setReadOnly(True)

        self.formGeneralInfo.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtWorkOrderNumber)

        self.lblTitle = QLabel(self.groupGeneralInfo)
        self.lblTitle.setObjectName(u"lblTitle")

        self.formGeneralInfo.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblTitle)

        self.txtTitle = QLineEdit(self.groupGeneralInfo)
        self.txtTitle.setObjectName(u"txtTitle")

        self.formGeneralInfo.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtTitle)

        self.lblDescription = QLabel(self.groupGeneralInfo)
        self.lblDescription.setObjectName(u"lblDescription")

        self.formGeneralInfo.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblDescription)

        self.teDescription = QTextEdit(self.groupGeneralInfo)
        self.teDescription.setObjectName(u"teDescription")

        self.formGeneralInfo.setWidget(2, QFormLayout.ItemRole.FieldRole, self.teDescription)

        self.lblPriority = QLabel(self.groupGeneralInfo)
        self.lblPriority.setObjectName(u"lblPriority")

        self.formGeneralInfo.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblPriority)

        self.cmbPriority = QComboBox(self.groupGeneralInfo)
        self.cmbPriority.addItem("")
        self.cmbPriority.addItem("")
        self.cmbPriority.addItem("")
        self.cmbPriority.setObjectName(u"cmbPriority")

        self.formGeneralInfo.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbPriority)

        self.lblStatus = QLabel(self.groupGeneralInfo)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formGeneralInfo.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.cmbStatus = QComboBox(self.groupGeneralInfo)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.formGeneralInfo.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbStatus)


        self.mainLayout.addWidget(self.groupGeneralInfo)

        self.groupAssignment = QGroupBox(AddWorkOrderDialog)
        self.groupAssignment.setObjectName(u"groupAssignment")
        self.groupAssignment.setFlat(True)
        self.formAssignment = QFormLayout(self.groupAssignment)
        self.formAssignment.setObjectName(u"formAssignment")
        self.lblAsset = QLabel(self.groupAssignment)
        self.lblAsset.setObjectName(u"lblAsset")

        self.formAssignment.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblAsset)

        self.cmbAsset = QComboBox(self.groupAssignment)
        self.cmbAsset.setObjectName(u"cmbAsset")

        self.formAssignment.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbAsset)

        self.lblTechnician = QLabel(self.groupAssignment)
        self.lblTechnician.setObjectName(u"lblTechnician")

        self.formAssignment.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblTechnician)

        self.cmbTechnician = QComboBox(self.groupAssignment)
        self.cmbTechnician.setObjectName(u"cmbTechnician")

        self.formAssignment.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbTechnician)

        self.lblRequestedBy = QLabel(self.groupAssignment)
        self.lblRequestedBy.setObjectName(u"lblRequestedBy")

        self.formAssignment.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblRequestedBy)

        self.txtRequestedBy = QLineEdit(self.groupAssignment)
        self.txtRequestedBy.setObjectName(u"txtRequestedBy")

        self.formAssignment.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtRequestedBy)


        self.mainLayout.addWidget(self.groupAssignment)

        self.groupDatesCosts = QGroupBox(AddWorkOrderDialog)
        self.groupDatesCosts.setObjectName(u"groupDatesCosts")
        self.groupDatesCosts.setFlat(True)
        self.gridDatesCosts = QGridLayout(self.groupDatesCosts)
        self.gridDatesCosts.setObjectName(u"gridDatesCosts")
        self.lblDateCreated = QLabel(self.groupDatesCosts)
        self.lblDateCreated.setObjectName(u"lblDateCreated")

        self.gridDatesCosts.addWidget(self.lblDateCreated, 0, 0, 1, 1)

        self.dtDateCreated = QDateEdit(self.groupDatesCosts)
        self.dtDateCreated.setObjectName(u"dtDateCreated")
        self.dtDateCreated.setCalendarPopup(True)

        self.gridDatesCosts.addWidget(self.dtDateCreated, 0, 1, 1, 1)

        self.lblDueDate = QLabel(self.groupDatesCosts)
        self.lblDueDate.setObjectName(u"lblDueDate")

        self.gridDatesCosts.addWidget(self.lblDueDate, 0, 2, 1, 1)

        self.dtDueDate = QDateEdit(self.groupDatesCosts)
        self.dtDueDate.setObjectName(u"dtDueDate")
        self.dtDueDate.setCalendarPopup(True)

        self.gridDatesCosts.addWidget(self.dtDueDate, 0, 3, 1, 1)

        self.lblEstimatedCost = QLabel(self.groupDatesCosts)
        self.lblEstimatedCost.setObjectName(u"lblEstimatedCost")

        self.gridDatesCosts.addWidget(self.lblEstimatedCost, 1, 0, 1, 1)

        self.dsbEstimatedCost = QDoubleSpinBox(self.groupDatesCosts)
        self.dsbEstimatedCost.setObjectName(u"dsbEstimatedCost")
        self.dsbEstimatedCost.setDecimals(2)
        self.dsbEstimatedCost.setMaximum(999999.989999999990687)

        self.gridDatesCosts.addWidget(self.dsbEstimatedCost, 1, 1, 1, 1)

        self.lblActualCost = QLabel(self.groupDatesCosts)
        self.lblActualCost.setObjectName(u"lblActualCost")

        self.gridDatesCosts.addWidget(self.lblActualCost, 1, 2, 1, 1)

        self.dsbActualCost = QDoubleSpinBox(self.groupDatesCosts)
        self.dsbActualCost.setObjectName(u"dsbActualCost")
        self.dsbActualCost.setDecimals(2)
        self.dsbActualCost.setMaximum(999999.989999999990687)

        self.gridDatesCosts.addWidget(self.dsbActualCost, 1, 3, 1, 1)

        self.lblLabourHours = QLabel(self.groupDatesCosts)
        self.lblLabourHours.setObjectName(u"lblLabourHours")

        self.gridDatesCosts.addWidget(self.lblLabourHours, 2, 0, 1, 1)

        self.dsbLabourHours = QDoubleSpinBox(self.groupDatesCosts)
        self.dsbLabourHours.setObjectName(u"dsbLabourHours")
        self.dsbLabourHours.setDecimals(2)
        self.dsbLabourHours.setMaximum(9999.989999999999782)

        self.gridDatesCosts.addWidget(self.dsbLabourHours, 2, 1, 1, 1)


        self.mainLayout.addWidget(self.groupDatesCosts)

        self.groupNotes = QGroupBox(AddWorkOrderDialog)
        self.groupNotes.setObjectName(u"groupNotes")
        self.groupNotes.setFlat(True)
        self.layoutNotes = QVBoxLayout(self.groupNotes)
        self.layoutNotes.setObjectName(u"layoutNotes")
        self.teNotes = QTextEdit(self.groupNotes)
        self.teNotes.setObjectName(u"teNotes")

        self.layoutNotes.addWidget(self.teNotes)


        self.mainLayout.addWidget(self.groupNotes)

        self.groupMaterials = QGroupBox(AddWorkOrderDialog)
        self.groupMaterials.setObjectName(u"groupMaterials")
        self.groupMaterials.setFlat(True)
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

        self.layoutMaterialButtons = QHBoxLayout()
        self.layoutMaterialButtons.setObjectName(u"layoutMaterialButtons")
        self.btnIssuePart = QPushButton(self.groupMaterials)
        self.btnIssuePart.setObjectName(u"btnIssuePart")

        self.layoutMaterialButtons.addWidget(self.btnIssuePart)

        self.btnRemovePart = QPushButton(self.groupMaterials)
        self.btnRemovePart.setObjectName(u"btnRemovePart")

        self.layoutMaterialButtons.addWidget(self.btnRemovePart)

        self.lblMaterieTotalTitle = QLabel(self.groupMaterials)
        self.lblMaterieTotalTitle.setObjectName(u"lblMaterieTotalTitle")

        self.layoutMaterialButtons.addWidget(self.lblMaterieTotalTitle)

        self.lblMaterialTotal = QLabel(self.groupMaterials)
        self.lblMaterialTotal.setObjectName(u"lblMaterialTotal")

        self.layoutMaterialButtons.addWidget(self.lblMaterialTotal)


        self.layoutMaterials.addLayout(self.layoutMaterialButtons)


        self.mainLayout.addWidget(self.groupMaterials)

        self.buttonBox = QDialogButtonBox(AddWorkOrderDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.mainLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddWorkOrderDialog)

        QMetaObject.connectSlotsByName(AddWorkOrderDialog)
    # setupUi

    def retranslateUi(self, AddWorkOrderDialog):
        AddWorkOrderDialog.setWindowTitle(QCoreApplication.translate("AddWorkOrderDialog", u"Add Work Order", None))
        self.groupGeneralInfo.setTitle(QCoreApplication.translate("AddWorkOrderDialog", u"General Information", None))
        self.lblWorkOrderNumber.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Work Order Number:", None))
        self.lblTitle.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Title:", None))
        self.lblDescription.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Description:", None))
        self.lblPriority.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Priority:", None))
        self.cmbPriority.setItemText(0, QCoreApplication.translate("AddWorkOrderDialog", u"Low", None))
        self.cmbPriority.setItemText(1, QCoreApplication.translate("AddWorkOrderDialog", u"Medium", None))
        self.cmbPriority.setItemText(2, QCoreApplication.translate("AddWorkOrderDialog", u"High", None))

        self.lblStatus.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Status:", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("AddWorkOrderDialog", u"Open", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("AddWorkOrderDialog", u"In Progress", None))
        self.cmbStatus.setItemText(2, QCoreApplication.translate("AddWorkOrderDialog", u"Closed", None))

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
        self.btnIssuePart.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Issue Part", None))
        self.btnRemovePart.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Remove Part", None))
        self.lblMaterieTotalTitle.setText(QCoreApplication.translate("AddWorkOrderDialog", u"Material Total:", None))
        self.lblMaterialTotal.setText(QCoreApplication.translate("AddWorkOrderDialog", u"N$ 0.00", None))
    # retranslateUi

