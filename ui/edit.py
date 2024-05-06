# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(943, 463)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 50, 941, 261))
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 921, 51))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)

        self.widget1 = QWidget(self.groupBox)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(11, 80, 921, 48))
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.dateEdit = QDateEdit(self.widget1)
        self.dateEdit.setObjectName(u"dateEdit")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.dateEdit)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_6 = QLineEdit(self.widget1)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.lineEdit_6)


        self.gridLayout_2.addLayout(self.formLayout_2, 0, 1, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_4 = QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout_3.setWidget(1, QFormLayout.SpanningRole, self.lineEdit_4)


        self.gridLayout_2.addLayout(self.formLayout_3, 0, 2, 1, 1)

        self.widget2 = QWidget(self.groupBox)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 140, 431, 51))
        self.gridLayout_3 = QGridLayout(self.widget2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 0, 1, 1, 1)

        self.dateEdit_2 = QDateEdit(self.widget2)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.gridLayout_3.addWidget(self.dateEdit_2, 1, 0, 1, 1)

        self.dateEdit_3 = QDateEdit(self.widget2)
        self.dateEdit_3.setObjectName(u"dateEdit_3")

        self.gridLayout_3.addWidget(self.dateEdit_3, 1, 1, 1, 1)

        self.widget3 = QWidget(self.groupBox)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 200, 921, 51))
        self.gridLayout_4 = QGridLayout(self.widget3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 0, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.widget3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_4.addWidget(self.lineEdit_7, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.widget3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_4.addWidget(self.lineEdit_8, 1, 1, 1, 1)

        self.label_9 = QLabel(self.widget3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 310, 941, 141))
        self.widget4 = QWidget(self.groupBox_2)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(11, 21, 921, 51))
        self.gridLayout_5 = QGridLayout(self.widget4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_14 = QLabel(self.widget4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 0, 2, 1, 1)

        self.dateEdit_4 = QDateEdit(self.widget4)
        self.dateEdit_4.setObjectName(u"dateEdit_4")

        self.gridLayout_5.addWidget(self.dateEdit_4, 1, 2, 1, 1)

        self.label_12 = QLabel(self.widget4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 0, 1, 1, 1)

        self.lineEdit_9 = QLineEdit(self.widget4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_5.addWidget(self.lineEdit_9, 1, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.widget4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_5.addWidget(self.lineEdit_10, 1, 3, 1, 1)

        self.lineEdit_5 = QLineEdit(self.widget4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_5.addWidget(self.lineEdit_5, 1, 0, 1, 1)

        self.label_13 = QLabel(self.widget4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 0, 3, 1, 1)

        self.widget5 = QWidget(self.groupBox_2)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(11, 78, 921, 51))
        self.gridLayout_6 = QGridLayout(self.widget5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.widget5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_21 = QLabel(self.widget5)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_6.addWidget(self.label_21, 0, 1, 1, 1)

        self.label_22 = QLabel(self.widget5)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_6.addWidget(self.label_22, 0, 2, 1, 1)

        self.label_16 = QLabel(self.widget5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 0, 3, 1, 1)

        self.lineEdit_11 = QLineEdit(self.widget5)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_6.addWidget(self.lineEdit_11, 1, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.widget5)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_6.addWidget(self.lineEdit_15, 1, 1, 1, 1)

        self.lineEdit_16 = QLineEdit(self.widget5)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_6.addWidget(self.lineEdit_16, 1, 2, 1, 1)

        self.lineEdit_12 = QLineEdit(self.widget5)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_6.addWidget(self.lineEdit_12, 1, 3, 1, 1)

        self.widget6 = QWidget(Dialog)
        self.widget6.setObjectName(u"widget6")
        self.widget6.setGeometry(QRect(0, 10, 158, 26))
        self.horizontalLayout = QHBoxLayout(self.widget6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget6)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget6)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u0438\u0441\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043e\u043b\u0438\u0441\u0435", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u2116 \u041f\u043e\u043b\u0438\u0441\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u2116 \u0410\u0434\u0434\u0435\u043d\u0434\u0443\u043c\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u044f", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0410\u0433\u0435\u043d\u0442 \u0424\u0418\u041e", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0434 \u0430\u0433\u0435\u043d\u0442\u0430", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0434 \u0421\u0442\u0440\u0430\u0445\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0440\u0430\u0445\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0424\u0418\u041e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0422\u0421", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u0440\u043a\u0430", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430", None))
        self.dateEdit_4.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0431\u0435\u0433 \u041a\u041c", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u2116VIN", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"\u0413\u041e\u0421 \u2116", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a \u0424\u0418\u041e", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c", None))
        self.lineEdit_16.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

