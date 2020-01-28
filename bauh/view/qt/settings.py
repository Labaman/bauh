from io import StringIO

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QToolBar, QSizePolicy, QPushButton

from bauh.api.abstract.controller import SoftwareManager
from bauh.api.abstract.view import MessageType
from bauh.view.core.controller import GenericSoftwareManager
from bauh.view.qt import dialog, css
from bauh.view.qt.components import to_widget, new_spacer
from bauh.view.util import util
from bauh.view.util.translation import I18n


class SettingsWindow(QWidget):

    def __init__(self, manager: SoftwareManager, i18n: I18n, screen_size: QSize, tray: bool, window: QWidget, parent: QWidget = None):
        super(SettingsWindow, self).__init__(parent=parent)
        self.setWindowTitle(i18n['settings'].capitalize())
        self.setLayout(QVBoxLayout())
        self.manager = manager
        self.i18n = i18n
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.tray = tray
        self.window = window

        self.settings_model = self.manager.get_settings()

        tab_group = to_widget(self.settings_model, i18n)
        tab_group.setMinimumWidth(int(screen_size.width() / 3))
        self.layout().addWidget(tab_group)

        action_bar = QToolBar()
        action_bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        bt_close = QPushButton()
        bt_close.setText(self.i18n['close'].capitalize())
        bt_close.clicked.connect(lambda: self.close())
        action_bar.addWidget(bt_close)

        action_bar.addWidget(new_spacer())

        bt_change = QPushButton()
        bt_change.setStyleSheet(css.OK_BUTTON)
        bt_change.setText(self.i18n['change'].capitalize())
        bt_change.clicked.connect(self._save_settings)
        action_bar.addWidget(bt_change)

        self.layout().addWidget(action_bar)

    def _save_settings(self):
        success, warnings = self.manager.save_settings(self.settings_model)

        # Configurações alteradas com sucesso, porém algumas delas só surtirão após a reinicialização

        if success:
            if dialog.ask_confirmation(title=self.i18n['warning'].capitalize(),
                                       body="<p>{}</p><p>{}</p>".format(self.i18n['settings.changed.success.warning'],
                                                                             self.i18n['settings.changed.success.reboot']),
                                       i18n=self.i18n):
                util.restart_app(self.tray)
            else:
                if isinstance(self.manager, GenericSoftwareManager):
                    self.manager.reset_cache()

                self.manager.prepare()
                self.window.verify_warnings()
                self.window.types_changed = True
                self.window.refresh_apps()
                self.close()
        else:
            msg = StringIO()
            msg.write("<p>It was not possible to properly save the settings</p>")

            for w in warnings:
                msg.write('<p style="font-weight: bold">* ' + w + '</p><br/>')

            msg.seek(0)

            dialog.show_message(title="Warning", body=msg.read(), type_=MessageType.WARNING)
