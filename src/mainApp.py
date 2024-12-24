import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot
from qtguistyle import GuiStyle
from settings import get_setting, set_setting, save_geometry, restore_geometry


class MainApp(QMainWindow, GuiStyle):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.current_font_size = get_setting("font_size", 12)
        self.load_from_settings()
        # Connect signal & slot
        self.actionToolbar.triggered.connect(self.toggleToolbar)
        self.toolBar.visibilityChanged.connect(self.syncActionToolbar)
        self.actionLogout.triggered.connect(self.logout_host)
        self.local_button.clicked.connect(self.local_selection)
        self.fontsize_plus_button.clicked.connect(self.increase_fontsize)
        self.fontsize_minus_button.clicked.connect(self.decrease_fontsize)

    def load_from_settings(self):
        restore_geometry(self)
        self.set_icon_color('black')  # default is black
        self.setStyleSheet("")  # default is stylesheet
        self.set_font_size(self.current_font_size)

    def closeEvent(self, event):
        """Save settings when the window is closed."""
        save_geometry(self)
        set_setting("font_size", self.current_font_size)
        super().closeEvent(event)

    @pyqtSlot()
    def increase_fontsize(self):
        if self.current_font_size <= 20:
            self.current_font_size += 1
            self.set_font_size(self.current_font_size)

    @pyqtSlot()
    def decrease_fontsize(self):
        if self.current_font_size >= 9:
            self.current_font_size -= 1
            self.set_font_size(self.current_font_size)

    @pyqtSlot()
    def local_selection(self):
        self.main_tab.setCurrentIndex(1)

    def host_selection(self):
        self.main_tab.setCurrentIndex(0)
        self.login_stackedWidget.setCurrentIndex(0)
        self.home_button.setVisible(False)
        self.login_message_label.clear()
        self.host_name_label.clear()

    @pyqtSlot()
    def logout_host(self):
        self.current_pubkey_value.clear()
        self.currentaddress_value.clear()
        self.host_selection()

    def syncActionToolbar(self, visible):
        self.actionToolbar.setChecked(visible)

    def toggleToolbar(self):
        self.toolBar.setVisible(self.actionToolbar.isChecked())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
