# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSplitter, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 40, 801, 131))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 40, 113, 22))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 61, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 61, 16))
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 90, 113, 22))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 20, 111, 16))
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(140, 40, 113, 22))
        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(140, 90, 113, 22))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 70, 111, 16))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(-1, 179, 801, 411))
        self.tableView = QTableView(self.groupBox_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 20, 781, 381))
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 10, 791, 24))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.new_button = QPushButton(self.splitter)
        self.new_button.setObjectName(u"new_button")
        self.splitter.addWidget(self.new_button)
        self.edit_button = QPushButton(self.splitter)
        self.edit_button.setObjectName(u"edit_button")
        self.splitter.addWidget(self.edit_button)
        self.extended_button = QPushButton(self.splitter)
        self.extended_button.setObjectName(u"extended_button")
        self.splitter.addWidget(self.extended_button)
        self.revoke_button = QPushButton(self.splitter)
        self.revoke_button.setObjectName(u"revoke_button")
        self.splitter.addWidget(self.revoke_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CTP", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u2116 \u041f\u043e\u043b\u0438\u0441\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u2116 VIN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u2116 \u0430\u0434\u0434\u0435\u043d\u0434\u0443\u043c\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041e\u0421. \u043d\u043e\u043c\u0435\u0440", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.new_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439", None))
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.extended_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043b\u043e\u043d\u0433\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.revoke_button.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u043d\u0443\u043b\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

