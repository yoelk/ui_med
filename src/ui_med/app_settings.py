import json
import os
from abc import ABC
from configparser import ConfigParser
from typing import List

from kivy import Config
from kivy.uix.settings import SettingsWithSidebar
from ui_med.app_base import AppBase, get_app
from ui_med.model.enums import Languages, Texts
from ui_med.model.languages import Lang


class ConfigSections(object):
    """
    Config sections
    """
    USER = "User"


class ConfigKeys(object):
    """
    Config keys
    """
    LANGUAGE = "language"


class AppWithSettings(AppBase, ABC):
    """
    Base class for our app settings
    """

    CFG_INI_FILENAME = 'cfg.ini'
    """The app's config file
    """

    def __init__(self, **kwargs) -> None:
        """
        Initialize
        :return: Nothing
        """
        super().__init__(**kwargs)
        self.settings_cls = SettingsWithSidebar
        self.use_kivy_settings = False

        self.init_kivy_config()

    @classmethod
    def init_kivy_config(cls) -> None:
        """
        Initialize the config file
        :return: Nothing
        """
        # Don't leave the app on 'Esc'
        Config.set('kivy', 'exit_on_escape', '0')

        # Disable multitouch
        Config.set('input', 'mouse', 'mouse,disable_multitouch')

        # Show everything
        Config.set('kivy', 'log_level', 'info')

        Config.write()

    @classmethod
    def get_cfg_path(cls, relpath: str) -> str:
        """
        :param relpath: The relative path in the config
        :return: The file's full path
        """
        return os.path.join(os.path.dirname(__file__), "cfg", relpath)

    @classmethod
    def get_settings(cls) -> List:
        """
        The app's settings
        :return:
        """
        # TODO(joel): Support more languages
        languages: List[Languages] = [Languages.ENGLISH]
        return [
            {"type": "options",
             "title": Lang.to_str(Texts.LANGUAGE),
             "section": ConfigSections.USER,
             "key": ConfigKeys.LANGUAGE,
             "options": [Lang.to_str(lang.value) for lang in languages]},
        ]

    def build_settings(self, settings: SettingsWithSidebar) -> None:
        """
        Build the settings panel
        :param settings: The settings instance
        :return: Nothing
        """
        settings.add_json_panel(get_app().title, self.config,
                                data=json.dumps(self.get_settings()))

    def build_config(self, config: ConfigParser) -> None:
        """
        Init the app's configuration defaults
        :param config: The config object
        :return: Nothing
        """
        super().build_config(config)
        config.setdefaults(ConfigSections.USER, {
            ConfigKeys.LANGUAGE: Languages.DEFAULT.value}
        )

    def get_application_config(self, **kwargs) -> str:
        """
        :return: The path to the app's config
        """
        return self.get_cfg_path(relpath=self.CFG_INI_FILENAME)
