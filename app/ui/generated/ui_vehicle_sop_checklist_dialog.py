# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehicle_sop_checklist_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_VehicleSopChecklistDialog(object):
    def setupUi(self, VehicleSopChecklistDialog):
        if not VehicleSopChecklistDialog.objectName():
            VehicleSopChecklistDialog.setObjectName(u"VehicleSopChecklistDialog")
        VehicleSopChecklistDialog.resize(589, 565)
        self.verticalLayout = QVBoxLayout(VehicleSopChecklistDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(VehicleSopChecklistDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.lblSop = QLabel(VehicleSopChecklistDialog)
        self.lblSop.setObjectName(u"lblSop")

        self.verticalLayout.addWidget(self.lblSop)

        self.lblAsset = QLabel(VehicleSopChecklistDialog)
        self.lblAsset.setObjectName(u"lblAsset")

        self.verticalLayout.addWidget(self.lblAsset)

        self.lblFrequency = QLabel(VehicleSopChecklistDialog)
        self.lblFrequency.setObjectName(u"lblFrequency")

        self.verticalLayout.addWidget(self.lblFrequency)

        self.tblChecklist = QTableWidget(VehicleSopChecklistDialog)
        if (self.tblChecklist.columnCount() < 3):
            self.tblChecklist.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblChecklist.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblChecklist.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblChecklist.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tblChecklist.setObjectName(u"tblChecklist")

        self.verticalLayout.addWidget(self.tblChecklist)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnDelete = QPushButton(VehicleSopChecklistDialog)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout.addWidget(self.btnDelete)

        self.btnAdd = QPushButton(VehicleSopChecklistDialog)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(VehicleSopChecklistDialog)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout.addWidget(self.btnEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(VehicleSopChecklistDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(VehicleSopChecklistDialog)
        self.buttonBox.accepted.connect(VehicleSopChecklistDialog.accept)
        self.buttonBox.rejected.connect(VehicleSopChecklistDialog.reject)

        QMetaObject.connectSlotsByName(VehicleSopChecklistDialog)
    # setupUi

    def retranslateUi(self, VehicleSopChecklistDialog):
        VehicleSopChecklistDialog.setWindowTitle(QCoreApplication.translate("VehicleSopChecklistDialog", u"Vehicle SOP Checklist", None))
        self.lblTitle.setText(QCoreApplication.translate("VehicleSopChecklistDialog", u"Vehicle SOP Checklist", None))
        self.lblSop.setText(QCoreApplication.translate("VehicleSopChecklistDialog", u"SOP:", None))
        self.lblAsset.setText(QCoreApplication.translate("VehicleSopChecklistDialog", u"Vehicle:", None))
        self.lblFrequency.setText(QCoreApplication.translate("VehicleSopChecklistDialog", u"Frequency:", None))
        ___qtablewidgetitem = self.tblChecklist.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VehicleSopChecklistDialog", u"Seq.", None))
        ___qtablewidgetitem1 = self.tblChecklist.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VehicleSopChecklistDialog", u"Check Description", None))
        ___qtablewidgetitem2 = self.tblChecklist.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VehicleSopChecklistDialog", u"Required", None))
        self.btnDelete.setText(QCoreApplication.translate("VehicleSopChecklistDialog", u"Delete", None))
        self.btnAdd.setText(QCoreApplication.translate("VehicleSopChecklistDialog", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("VehicleSopChecklistDialog", u"Edit", None))
    # retranslateUi

