import sys
from PyQt6 import QtWidgets
from PySide6.QtWidgets import QApplication,QMainWindow

from ui.home import Ui_MainWindow
from ui.edit import Ui_Dialog
from db_connect import Data

class CTP(QMainWindow):
    def __init__(self) -> None:
        super(CTP,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect = Data()

    def new_polices(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window.setupui(self.new_window)
        self.new_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=CTP()
    window.show()

    sys.exit(app.exec())