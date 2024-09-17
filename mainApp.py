import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from qtguidesign import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow): #Extend

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())