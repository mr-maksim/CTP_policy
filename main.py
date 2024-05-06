from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.new_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_button.setGeometry(QtCore.QRect(10, 10, 71, 41))
        self.new_button.setObjectName("new_button")
        self.edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_button.setGeometry(QtCore.QRect(90, 10, 71, 41))
        self.edit_button.setObjectName("edit_button")
        self.extended_button = QtWidgets.QPushButton(self.centralwidget)
        self.extended_button.setGeometry(QtCore.QRect(170, 10, 110, 41))
        self.extended_button.setObjectName("extended_button")
        self.revoke_button = QtWidgets.QPushButton(self.centralwidget)
        self.revoke_button.setGeometry(QtCore.QRect(290, 10, 110, 41))
        self.revoke_button.setObjectName("revoke_button")
        self.ctp_view = QtWidgets.QTableView(self.centralwidget)
        self.ctp_view.setGeometry(QtCore.QRect(10, 70, 611, 601))
        self.ctp_view.setObjectName("ctp_view")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CTP"))
        self.new_button.setText(_translate("MainWindow", "Новый"))
        self.edit_button.setText(_translate("MainWindow", "Изменить"))
        self.extended_button.setText(_translate("MainWindow", "Пролонгировать"))
        self.revoke_button.setText(_translate("MainWindow", "Аннулировать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
