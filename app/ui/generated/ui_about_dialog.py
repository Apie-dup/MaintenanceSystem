# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(420, 380)
        AboutDialog.setMinimumSize(QSize(420, 380))
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(AboutDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.verticalSpacer = QSpacerItem(20, 47, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lblOrganization = QLabel(AboutDialog)
        self.lblOrganization.setObjectName(u"lblOrganization")
        self.lblOrganization.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblOrganization)

        self.verticalSpacer_2 = QSpacerItem(20, 47, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.lblVersion = QLabel(AboutDialog)
        self.lblVersion.setObjectName(u"lblVersion")

        self.verticalLayout.addWidget(self.lblVersion)

        self.lblBuild = QLabel(AboutDialog)
        self.lblBuild.setObjectName(u"lblBuild")

        self.verticalLayout.addWidget(self.lblBuild)

        self.lblAuthor = QLabel(AboutDialog)
        self.lblAuthor.setObjectName(u"lblAuthor")

        self.verticalLayout.addWidget(self.lblAuthor)

        self.lblDatabaseVersion = QLabel(AboutDialog)
        self.lblDatabaseVersion.setObjectName(u"lblDatabaseVersion")

        self.verticalLayout.addWidget(self.lblDatabaseVersion)

        self.verticalSpacer_3 = QSpacerItem(20, 47, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.lblDescription = QLabel(AboutDialog)
        self.lblDescription.setObjectName(u"lblDescription")

        self.verticalLayout.addWidget(self.lblDescription, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(379, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(AboutDialog)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AboutDialog)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.lblTitle.setText(QCoreApplication.translate("AboutDialog", u"Maintenance Management System", None))
        self.lblOrganization.setText(QCoreApplication.translate("AboutDialog", u"Organization", None))
        self.lblVersion.setText(QCoreApplication.translate("AboutDialog", u"Version:", None))
        self.lblBuild.setText(QCoreApplication.translate("AboutDialog", u"Build:", None))
        self.lblAuthor.setText(QCoreApplication.translate("AboutDialog", u"Author:", None))
        self.lblDatabaseVersion.setText(QCoreApplication.translate("AboutDialog", u"Database Version:", None))
        self.lblDescription.setText(QCoreApplication.translate("AboutDialog", u"Maintenance Management System", None))
        self.btnClose.setText(QCoreApplication.translate("AboutDialog", u"Close", None))
    # retranslateUi

