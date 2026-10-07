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
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_AssetHistoryDialog(object):
    def setupUi(self, AssetHistoryDialog):
        if not AssetHistoryDialog.objectName():
            AssetHistoryDialog.setObjectName(u"AssetHistoryDialog")
        AssetHistoryDialog.resize(900, 650)
        AssetHistoryDialog.setMinimumSize(QSize(900, 650))
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

        self.grpSummary = QGroupBox(AssetHistoryDialog)
        self.grpSummary.setObjectName(u"grpSummary")
        self.gridLayout = QGridLayout(self.grpSummary)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblTitle_2 = QLabel(self.grpSummary)
        self.lblTitle_2.setObjectName(u"lblTitle_2")

        self.gridLayout.addWidget(self.lblTitle_2, 0, 0, 1, 1)

        self.lblCompletedMaintenance = QLabel(self.grpSummary)
        self.lblCompletedMaintenance.setObjectName(u"lblCompletedMaintenance")
        font1 = QFont()
        font1.setBold(True)
        self.lblCompletedMaintenance.setFont(font1)

        self.gridLayout.addWidget(self.lblCompletedMaintenance, 0, 1, 1, 1)

        self.lblTitle_3 = QLabel(self.grpSummary)
        self.lblTitle_3.setObjectName(u"lblTitle_3")

        self.gridLayout.addWidget(self.lblTitle_3, 0, 2, 1, 1)

        self.lblOpenWorkOrders = QLabel(self.grpSummary)
        self.lblOpenWorkOrders.setObjectName(u"lblOpenWorkOrders")
        self.lblOpenWorkOrders.setFont(font1)

        self.gridLayout.addWidget(self.lblOpenWorkOrders, 0, 3, 1, 1)

        self.lblTitle_4 = QLabel(self.grpSummary)
        self.lblTitle_4.setObjectName(u"lblTitle_4")

        self.gridLayout.addWidget(self.lblTitle_4, 1, 0, 1, 1)

        self.lblLabourHours = QLabel(self.grpSummary)
        self.lblLabourHours.setObjectName(u"lblLabourHours")
        self.lblLabourHours.setFont(font1)

        self.gridLayout.addWidget(self.lblLabourHours, 1, 1, 1, 1)

        self.lblTitle_5 = QLabel(self.grpSummary)
        self.lblTitle_5.setObjectName(u"lblTitle_5")

        self.gridLayout.addWidget(self.lblTitle_5, 1, 2, 1, 1)

        self.lblMaintenanceCost = QLabel(self.grpSummary)
        self.lblMaintenanceCost.setObjectName(u"lblMaintenanceCost")
        self.lblMaintenanceCost.setFont(font1)

        self.gridLayout.addWidget(self.lblMaintenanceCost, 1, 3, 1, 1)

        self.lblTitle_6 = QLabel(self.grpSummary)
        self.lblTitle_6.setObjectName(u"lblTitle_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle_6.sizePolicy().hasHeightForWidth())
        self.lblTitle_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lblTitle_6, 2, 0, 1, 1)

        self.lblLabourCost = QLabel(self.grpSummary)
        self.lblLabourCost.setObjectName(u"lblLabourCost")
        self.lblLabourCost.setFont(font1)

        self.gridLayout.addWidget(self.lblLabourCost, 2, 1, 1, 1)

        self.lblTitle_7 = QLabel(self.grpSummary)
        self.lblTitle_7.setObjectName(u"lblTitle_7")

        self.gridLayout.addWidget(self.lblTitle_7, 2, 2, 1, 1)

        self.lblPartsCost = QLabel(self.grpSummary)
        self.lblPartsCost.setObjectName(u"lblPartsCost")
        self.lblPartsCost.setFont(font1)

        self.gridLayout.addWidget(self.lblPartsCost, 2, 3, 1, 1)

        self.lblTitle_8 = QLabel(self.grpSummary)
        self.lblTitle_8.setObjectName(u"lblTitle_8")

        self.gridLayout.addWidget(self.lblTitle_8, 3, 0, 1, 1)

        self.lblLastMaintenance = QLabel(self.grpSummary)
        self.lblLastMaintenance.setObjectName(u"lblLastMaintenance")
        self.lblLastMaintenance.setFont(font1)

        self.gridLayout.addWidget(self.lblLastMaintenance, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.grpSummary)

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
        self.grpSummary.setTitle(QCoreApplication.translate("AssetHistoryDialog", u"Maintenance Summary", None))
        self.lblTitle_2.setText(QCoreApplication.translate("AssetHistoryDialog", u"Completed Maintenance:", None))
        self.lblCompletedMaintenance.setText(QCoreApplication.translate("AssetHistoryDialog", u"-", None))
        self.lblTitle_3.setText(QCoreApplication.translate("AssetHistoryDialog", u"Open Work Orders:", None))
        self.lblOpenWorkOrders.setText(QCoreApplication.translate("AssetHistoryDialog", u"-", None))
        self.lblTitle_4.setText(QCoreApplication.translate("AssetHistoryDialog", u"Labour Hours:", None))
        self.lblLabourHours.setText(QCoreApplication.translate("AssetHistoryDialog", u"-", None))
        self.lblTitle_5.setText(QCoreApplication.translate("AssetHistoryDialog", u"Maintenance Cost:", None))
        self.lblMaintenanceCost.setText(QCoreApplication.translate("AssetHistoryDialog", u"-", None))
        self.lblTitle_6.setText(QCoreApplication.translate("AssetHistoryDialog", u"Labour Cost:", None))
        self.lblLabourCost.setText(QCoreApplication.translate("AssetHistoryDialog", u"-", None))
        self.lblTitle_7.setText(QCoreApplication.translate("AssetHistoryDialog", u"Parts Cost:", None))
        self.lblPartsCost.setText(QCoreApplication.translate("AssetHistoryDialog", u"-", None))
        self.lblTitle_8.setText(QCoreApplication.translate("AssetHistoryDialog", u"Last Maintenance:", None))
        self.lblLastMaintenance.setText(QCoreApplication.translate("AssetHistoryDialog", u"-", None))
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

