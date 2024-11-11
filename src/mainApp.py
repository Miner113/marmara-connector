import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

from qtguidesign import Ui_MainWindow

from resources import resources

class MainWindow(QMainWindow, Ui_MainWindow): #Extend

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(':/images/mcl_logo.png'))
    win = MainWindow()
    win.show()
    sys.exit(app.exec())