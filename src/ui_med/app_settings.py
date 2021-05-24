import json
from abc import ABC
from typing import List

from kivy.uix.settings import SettingsWithSidebar
from ui_med.app_base import AppBase, get_app
from ui_med.model.enums import Languages, Texts
from ui_med.model.languages import Lang


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

    @classmethod
    def get_settings(cls) -> List:
        """
        The app's settings
        :return:
        """
        return [
            {"type": "options",
             "title": Lang.to_str(Texts.LANGUAGE),
             "section": "All",
             "key": "language",
             "options": [Lang.to_str(lang.value) for lang in Languages]},
        ]

    def build_settings(self, settings: SettingsWithSidebar) -> None:
        """
        Build the settings panel
        :param settings: The settings instance
        :return: Nothing
        """
        settings.add_json_panel(get_app().title, self.config,
                                data=json.dumps(self.get_settings()))

    def get_application_config(self, **kwargs) -> str:
        """
        :return: The path to the app's config
        """
        return self.CFG_INI_FILENAME
