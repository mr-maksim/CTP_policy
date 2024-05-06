import sys
from PySide6.QtWidgets import QApplication,QMainWindow

from ui.home import Ui_MainWindow


class CTP(QMainWindow):
    def __init__(self) -> None:
        super(CTP,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=CTP()
    window.show()

    sys.exit(app.exec())