import json
from pathlib import Path
from PyQt5.QtCore import QSettings, QByteArray

base_path = Path(__file__).resolve().parent
language_path = base_path / 'src' / 'language'
styles_path = base_path / 'src' / 'styles'

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

