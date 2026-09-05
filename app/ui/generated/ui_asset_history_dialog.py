# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asset_history_dialog.ui'
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
    QHeaderView, QLabel, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_AssetHistoryDialog(object):
    def setupUi(self, AssetHistoryDialog):
        if not AssetHistoryDialog.objectName():
            AssetHistoryDialog.setObjectName(u"AssetHistoryDialog")
        AssetHistoryDialog.resize(900, 550)
        AssetHistoryDialog.setMinimumSize(QSize(900, 550))
        self.verticalLayout = QVBoxLayout(AssetHistoryDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(AssetHistoryDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.lblAsset = QLabel(AssetHistoryDialog)
        self.lblAsset.setObjectName(u"lblAsset")

        self.verticalLayout.addWidget(self.lblAsset)

        self.tblHistory = QTableWidget(AssetHistoryDialog)
        if (self.tblHistory.columnCount() < 6):
            self.tblHistory.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblHistory.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblHistory.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblHistory.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblHistory.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblHistory.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblHistory.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblHistory.setObjectName(u"tblHistory")

        self.verticalLayout.addWidget(self.tblHistory)

        self.buttonBox = QDialogButtonBox(AssetHistoryDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AssetHistoryDialog)

        QMetaObject.connectSlotsByName(AssetHistoryDialog)
    # setupUi

    def retranslateUi(self, AssetHistoryDialog):
        AssetHistoryDialog.setWindowTitle(QCoreApplication.translate("AssetHistoryDialog", u"Asset Maintenance History", None))
        self.lblTitle.setText(QCoreApplication.translate("AssetHistoryDialog", u"Asset Maintenance History", None))
        self.lblAsset.setText(QCoreApplication.translate("AssetHistoryDialog", u"Asset:", None))
        ___qtablewidgetitem = self.tblHistory.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AssetHistoryDialog", u"Date", None))
        ___qtablewidgetitem1 = self.tblHistory.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AssetHistoryDialog", u"Type", None))
        ___qtablewidgetitem2 = self.tblHistory.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AssetHistoryDialog", u"Reference", None))
        ___qtablewidgetitem3 = self.tblHistory.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AssetHistoryDialog", u"Description", None))
        ___qtablewidgetitem4 = self.tblHistory.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AssetHistoryDialog", u"Status", None))
        ___qtablewidgetitem5 = self.tblHistory.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AssetHistoryDialog", u"Meter", None))
    # retranslateUi

