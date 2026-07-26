# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'issue_parts.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_IssuePartsDialog(object):
    def setupUi(self, IssuePartsDialog):
        if not IssuePartsDialog.objectName():
            IssuePartsDialog.setObjectName(u"IssuePartsDialog")
        IssuePartsDialog.resize(650, 1063)
        self.verticalLayout = QVBoxLayout(IssuePartsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(IssuePartsDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.lblSearch = QLabel(IssuePartsDialog)
        self.lblSearch.setObjectName(u"lblSearch")

        self.verticalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(IssuePartsDialog)
        self.txtSearch.setObjectName(u"txtSearch")

        self.verticalLayout.addWidget(self.txtSearch)

        self.lblInventory = QLabel(IssuePartsDialog)
        self.lblInventory.setObjectName(u"lblInventory")

        self.verticalLayout.addWidget(self.lblInventory)

        self.tblInventory = QTableWidget(IssuePartsDialog)
        if (self.tblInventory.columnCount() < 6):
            self.tblInventory.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblInventory.setObjectName(u"tblInventory")
        self.tblInventory.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblInventory.setAlternatingRowColors(True)
        self.tblInventory.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblInventory.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblInventory.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tblInventory)

        self.lblSelectedPart = QLabel(IssuePartsDialog)
        self.lblSelectedPart.setObjectName(u"lblSelectedPart")

        self.verticalLayout.addWidget(self.lblSelectedPart)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblPartNumber = QLabel(IssuePartsDialog)
        self.lblPartNumber.setObjectName(u"lblPartNumber")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblPartNumber)

        self.txtPartNumber = QLineEdit(IssuePartsDialog)
        self.txtPartNumber.setObjectName(u"txtPartNumber")
        self.txtPartNumber.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.txtPartNumber)

        self.lblPartName = QLabel(IssuePartsDialog)
        self.lblPartName.setObjectName(u"lblPartName")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblPartName)

        self.txtPartName = QLineEdit(IssuePartsDialog)
        self.txtPartName.setObjectName(u"txtPartName")
        self.txtPartName.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.txtPartName)

        self.lblAvailableStock = QLabel(IssuePartsDialog)
        self.lblAvailableStock.setObjectName(u"lblAvailableStock")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblAvailableStock)

        self.txtAvailableStock = QLineEdit(IssuePartsDialog)
        self.txtAvailableStock.setObjectName(u"txtAvailableStock")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.txtAvailableStock)


        self.verticalLayout.addLayout(self.formLayout)

        self.lblIssueDetails = QLabel(IssuePartsDialog)
        self.lblIssueDetails.setObjectName(u"lblIssueDetails")

        self.verticalLayout.addWidget(self.lblIssueDetails)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lblQuantityToIssue = QLabel(IssuePartsDialog)
        self.lblQuantityToIssue.setObjectName(u"lblQuantityToIssue")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblQuantityToIssue)

        self.spnQuantity = QSpinBox(IssuePartsDialog)
        self.spnQuantity.setObjectName(u"spnQuantity")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.spnQuantity)

        self.lblUnitCost = QLabel(IssuePartsDialog)
        self.lblUnitCost.setObjectName(u"lblUnitCost")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblUnitCost)

        self.dsbUnitCost = QDoubleSpinBox(IssuePartsDialog)
        self.dsbUnitCost.setObjectName(u"dsbUnitCost")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.dsbUnitCost)

        self.lblTotalCost = QLabel(IssuePartsDialog)
        self.lblTotalCost.setObjectName(u"lblTotalCost")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblTotalCost)

        self.dsbTotalCost = QDoubleSpinBox(IssuePartsDialog)
        self.dsbTotalCost.setObjectName(u"dsbTotalCost")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.dsbTotalCost)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.lblNotes = QLabel(IssuePartsDialog)
        self.lblNotes.setObjectName(u"lblNotes")

        self.verticalLayout.addWidget(self.lblNotes)

        self.teNotse = QTextEdit(IssuePartsDialog)
        self.teNotse.setObjectName(u"teNotse")

        self.verticalLayout.addWidget(self.teNotse)

        self.buttonBox = QDialogButtonBox(IssuePartsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.NoButton)

        self.verticalLayout.addWidget(self.buttonBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnCancel = QPushButton(IssuePartsDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnIssuePart = QPushButton(IssuePartsDialog)
        self.btnIssuePart.setObjectName(u"btnIssuePart")

        self.horizontalLayout.addWidget(self.btnIssuePart)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(IssuePartsDialog)
        self.buttonBox.accepted.connect(IssuePartsDialog.accept)
        self.buttonBox.rejected.connect(IssuePartsDialog.reject)

        QMetaObject.connectSlotsByName(IssuePartsDialog)
    # setupUi

    def retranslateUi(self, IssuePartsDialog):
        IssuePartsDialog.setWindowTitle(QCoreApplication.translate("IssuePartsDialog", u"Issue Parts", None))
        self.lblTitle.setText(QCoreApplication.translate("IssuePartsDialog", u"Issue Parts", None))
        self.lblSearch.setText(QCoreApplication.translate("IssuePartsDialog", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("IssuePartsDialog", u"Search Part Number or Name...", None))
        self.lblInventory.setText(QCoreApplication.translate("IssuePartsDialog", u"Inventory", None))
        ___qtablewidgetitem = self.tblInventory.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("IssuePartsDialog", u"Part No", None))
        ___qtablewidgetitem1 = self.tblInventory.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("IssuePartsDialog", u"Part Name", None))
        ___qtablewidgetitem2 = self.tblInventory.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("IssuePartsDialog", u"Category", None))
        ___qtablewidgetitem3 = self.tblInventory.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("IssuePartsDialog", u"Stock", None))
        ___qtablewidgetitem4 = self.tblInventory.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("IssuePartsDialog", u"Unit", None))
        ___qtablewidgetitem5 = self.tblInventory.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("IssuePartsDialog", u"Unit Cost", None))
        self.lblSelectedPart.setText(QCoreApplication.translate("IssuePartsDialog", u"Selected Part", None))
        self.lblPartNumber.setText(QCoreApplication.translate("IssuePartsDialog", u"Part Number", None))
        self.lblPartName.setText(QCoreApplication.translate("IssuePartsDialog", u"Part Name", None))
        self.lblAvailableStock.setText(QCoreApplication.translate("IssuePartsDialog", u"Available Stock", None))
        self.lblIssueDetails.setText(QCoreApplication.translate("IssuePartsDialog", u"Issue Details", None))
        self.lblQuantityToIssue.setText(QCoreApplication.translate("IssuePartsDialog", u"Quantity to issue", None))
        self.lblUnitCost.setText(QCoreApplication.translate("IssuePartsDialog", u"Unit Cost", None))
        self.lblTotalCost.setText(QCoreApplication.translate("IssuePartsDialog", u"Total Cost", None))
        self.lblNotes.setText(QCoreApplication.translate("IssuePartsDialog", u"Notes", None))
        self.btnCancel.setText(QCoreApplication.translate("IssuePartsDialog", u"Cancel", None))
        self.btnIssuePart.setText(QCoreApplication.translate("IssuePartsDialog", u"Issue Part", None))
    # retranslateUi

