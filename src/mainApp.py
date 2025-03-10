import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtCore import pyqtSlot, QTranslator
from qtguistyle import GuiStyle
from settings import get_setting, set_setting, save_geometry, restore_geometry, SettingsDialog, get_style, language_path


class MainApp(QMainWindow, GuiStyle):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.trans = QTranslator(self)
        restore_geometry(self)
        self.selected_styleSheet = ""
        self.current_language = 'EN'
        self.current_font_size = 12
        self.set_font_size(self.current_font_size)
        self.load_from_settings()
        # Connect signal & slot
        self.actionToolbar.triggered.connect(self.toggleToolbar)
        self.toolBar.visibilityChanged.connect(self.syncActionToolbar)
        self.actionLogout.triggered.connect(self.logout_host)
        self.local_button.clicked.connect(self.local_selection)
        self.fontsize_plus_button.clicked.connect(self.increase_fontsize)
        self.fontsize_minus_button.clicked.connect(self.decrease_fontsize)
        self.actionPreferances.triggered.connect(self.open_settings)

    def load_from_settings(self):
        style = str(get_setting("style", 'light'))
        icon_color = 'black'
        if style != 'light':
            icon_color = '#eff0f1'
            self.selected_styleSheet = get_style(style + '.qss')
        else:
            self.selected_styleSheet = ""
        self.set_icon_color(str(icon_color))
        self.setStyleSheet(self.selected_styleSheet)
        if int(get_setting("font_size", 12)) != self.current_font_size:
            self.current_font_size = int(get_setting("font_size", 12))
            self.set_font_size(self.current_font_size)
        if self.current_language != get_setting('language', 'EN'):
            self.change_language(get_setting('language'))

    def change_language(self, lang_name):
        language_files = {file.stem: file for file in language_path.iterdir() if file.suffix == '.qm'}
        if lang_name in language_files:
            self.trans.load(str(language_files[lang_name]))
            QApplication.instance().installTranslator(self.trans)
            self.retranslateUi(self)
            self.current_language = lang_name

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
            set_setting('font_size', self.current_font_size)

    @pyqtSlot()
    def decrease_fontsize(self):
        if self.current_font_size >= 9:
            self.current_font_size -= 1
            self.set_font_size(self.current_font_size)
            set_setting('font_size', self.current_font_size)

    @pyqtSlot()
    def local_selection(self):
        self.main_tab.setCurrentIndex(1)

    def host_selection(self):
        self.main_tab.setCurrentIndex(0)
        self.login_stackedWidget.setCurrentIndex(0)
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

    def open_settings(self):
        dialog = SettingsDialog(self)
        result = dialog.exec_()
        if result == QDialog.Accepted:
            self.load_from_settings()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
