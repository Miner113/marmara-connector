from pathlib import Path
from os import listdir
from PyQt5.QtCore import QSettings, QByteArray
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from settingsDialog import Ui_Settings  # Import the auto-generated dialog UI

base_path = Path(__file__).resolve().parent
language_path = base_path / 'language'
styles_path = base_path / 'styles'
images_path = base_path / 'images'

ORGANIZATION = "MarmaraChainOfficial"
APPLICATION = "MarmaraConnector"
settings = QSettings(ORGANIZATION, APPLICATION)


def save_geometry(window):
    """Save the window geometry and state."""
    settings.setValue("geometry", window.saveGeometry())
    settings.setValue("windowState", window.saveState())


def restore_geometry(window):
    """Restore the window geometry and state."""
    geometry = settings.value("geometry", QByteArray())
    window_state = settings.value("windowState", QByteArray())
    if geometry:
        window.restoreGeometry(geometry)
    if window_state:
        window.restoreState(window_state)


def get_setting(key, default=None):
    """Retrieve a setting."""
    return settings.value(key, default)


def set_setting(key, value):
    """Save a setting."""
    settings.setValue(key, value)

def get_style(style_name):
    file = open(styles_path / style_name, "r")
    style = file.read()
    file.close()
    return style

class SettingsDialog(QDialog):
    """Class to manage the settings dialog."""

    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)

        # Set up the UI
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self._load_settings()

    def _load_settings(self):
        self.load_languages()
        lang_from_settings = get_setting('language', 'EN')
        self.set_combobox_index(self.ui.lang_comboBox, lang_from_settings, 'EN')
        self.load_styles()
        style_from_settings = get_setting('style', 'light')
        self.set_combobox_index(self.ui.style_comboBox, style_from_settings, 'light')
        self.ui.font_size_spinBox.setValue(int(get_setting('font_size')))

    def load_languages(self):
        language_files = sorted(f for f in language_path.iterdir() if f.suffix == '.qm')
        for file in language_files:
            lang_name = file.stem
            self.ui.lang_comboBox.addItem(lang_name)
            lang_icon = images_path / f"{lang_name}.png"
            if lang_icon.exists():
                lang_index = self.ui.lang_comboBox.findText(lang_name)
                self.ui.lang_comboBox.setItemIcon(lang_index, QIcon(str(lang_icon)))

    def load_styles(self):
        style_files = sorted(f for f in styles_path.iterdir() if f.suffix == '.qss')
        self.ui.style_comboBox.addItem('light')
        for file in style_files:
            style_name = file.stem
            self.ui.style_comboBox.addItem(style_name)

    def done(self, result):
        """Override the done method to capture the result (OK/Cancel)."""
        if result == QDialog.Accepted:
            self._save_settings()
        super(SettingsDialog, self).done(result)

    def _save_settings(self):
        set_setting('language', self.ui.lang_comboBox.currentText())
        set_setting('style', self.ui.style_comboBox.currentText())
        set_setting('font_size', self.ui.font_size_spinBox.value())

    def set_combobox_index(self, combo_box, setting_value, default_value):
        index = combo_box.findText(setting_value)
        if index == -1:
            index = combo_box.findText(default_value)  # Fallback to default value
        if index != -1:
            combo_box.setCurrentIndex(index)
