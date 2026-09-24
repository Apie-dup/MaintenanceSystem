# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'purchase_order_receive_dialog.ui'
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
    QDoubleSpinBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_PurchaseOrderReceiveDialog(object):
    def setupUi(self, PurchaseOrderReceiveDialog):
        if not PurchaseOrderReceiveDialog.objectName():
            PurchaseOrderReceiveDialog.setObjectName(u"PurchaseOrderReceiveDialog")
        PurchaseOrderReceiveDialog.resize(463, 509)
        self.verticalLayout = QVBoxLayout(PurchaseOrderReceiveDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(PurchaseOrderReceiveDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblInventoryItem = QLabel(PurchaseOrderReceiveDialog)
        self.lblInventoryItem.setObjectName(u"lblInventoryItem")

        self.horizontalLayout.addWidget(self.lblInventoryItem)

        self.txtInventoryItem = QLineEdit(PurchaseOrderReceiveDialog)
        self.txtInventoryItem.setObjectName(u"txtInventoryItem")
        self.txtInventoryItem.setReadOnly(True)

        self.horizontalLayout.addWidget(self.txtInventoryItem)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblQuantityOrdered = QLabel(PurchaseOrderReceiveDialog)
        self.lblQuantityOrdered.setObjectName(u"lblQuantityOrdered")

        self.horizontalLayout_2.addWidget(self.lblQuantityOrdered)

        self.dsbQuantityOrdered = QDoubleSpinBox(PurchaseOrderReceiveDialog)
        self.dsbQuantityOrdered.setObjectName(u"dsbQuantityOrdered")
        self.dsbQuantityOrdered.setReadOnly(True)
        self.dsbQuantityOrdered.setMaximum(999999.989999999990687)

        self.horizontalLayout_2.addWidget(self.dsbQuantityOrdered)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblAlreadyReceived = QLabel(PurchaseOrderReceiveDialog)
        self.lblAlreadyReceived.setObjectName(u"lblAlreadyReceived")

        self.horizontalLayout_3.addWidget(self.lblAlreadyReceived)

        self.dsbQuantityReceived = QDoubleSpinBox(PurchaseOrderReceiveDialog)
        self.dsbQuantityReceived.setObjectName(u"dsbQuantityReceived")
        self.dsbQuantityReceived.setReadOnly(True)
        self.dsbQuantityReceived.setMaximum(999999.989999999990687)

        self.horizontalLayout_3.addWidget(self.dsbQuantityReceived)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblOutstanding = QLabel(PurchaseOrderReceiveDialog)
        self.lblOutstanding.setObjectName(u"lblOutstanding")

        self.horizontalLayout_4.addWidget(self.lblOutstanding)

        self.dsbOutstanding = QDoubleSpinBox(PurchaseOrderReceiveDialog)
        self.dsbOutstanding.setObjectName(u"dsbOutstanding")
        self.dsbOutstanding.setMaximum(999999.989999999990687)

        self.horizontalLayout_4.addWidget(self.dsbOutstanding)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblReceiveQuantity = QLabel(PurchaseOrderReceiveDialog)
        self.lblReceiveQuantity.setObjectName(u"lblReceiveQuantity")

        self.horizontalLayout_5.addWidget(self.lblReceiveQuantity)

        self.dsbReceiveQuantity = QDoubleSpinBox(PurchaseOrderReceiveDialog)
        self.dsbReceiveQuantity.setObjectName(u"dsbReceiveQuantity")
        self.dsbReceiveQuantity.setReadOnly(False)
        self.dsbReceiveQuantity.setMinimum(0.010000000000000)
        self.dsbReceiveQuantity.setMaximum(999999.989999999990687)

        self.horizontalLayout_5.addWidget(self.dsbReceiveQuantity)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblNotes = QLabel(PurchaseOrderReceiveDialog)
        self.lblNotes.setObjectName(u"lblNotes")

        self.horizontalLayout_6.addWidget(self.lblNotes)

        self.txtNotes = QPlainTextEdit(PurchaseOrderReceiveDialog)
        self.txtNotes.setObjectName(u"txtNotes")

        self.horizontalLayout_6.addWidget(self.txtNotes)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.buttonBox = QDialogButtonBox(PurchaseOrderReceiveDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(PurchaseOrderReceiveDialog)

        QMetaObject.connectSlotsByName(PurchaseOrderReceiveDialog)
    # setupUi

    def retranslateUi(self, PurchaseOrderReceiveDialog):
        PurchaseOrderReceiveDialog.setWindowTitle(QCoreApplication.translate("PurchaseOrderReceiveDialog", u"Receive Stock", None))
        self.lblTitle.setText(QCoreApplication.translate("PurchaseOrderReceiveDialog", u"Receive Stock", None))
        self.lblInventoryItem.setText(QCoreApplication.translate("PurchaseOrderReceiveDialog", u"Inventory Item:", None))
        self.lblQuantityOrdered.setText(QCoreApplication.translate("PurchaseOrderReceiveDialog", u"Quantity Ordered:", None))
        self.lblAlreadyReceived.setText(QCoreApplication.translate("PurchaseOrderReceiveDialog", u"Already Received:", None))
        self.lblOutstanding.setText(QCoreApplication.translate("PurchaseOrderReceiveDialog", u"Outstanding:", None))
        self.lblReceiveQuantity.setText(QCoreApplication.translate("PurchaseOrderReceiveDialog", u"Receive Quantity:", None))
        self.lblNotes.setText(QCoreApplication.translate("PurchaseOrderReceiveDialog", u"Notes:", None))
    # retranslateUi

