import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

import qtguistyle

class MainWindow(QMainWindow, qtguistyle.GuiStyle):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.set_icon_color('light')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())