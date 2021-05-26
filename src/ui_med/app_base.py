import logging
from abc import ABC
from logging import Formatter, Logger, StreamHandler
from typing import Optional

from kivy.app import App
from ui_med.app_api_ui_med import UiMedAppApi


class AppBase(App, UiMedAppApi, ABC):
    """
    Base class for our app
    """

    def __init__(self, **kwargs) -> None:
        """
        Initialize
        :return: Nothing
        """
        super().__init__(**kwargs)
        self.logger: Logger = logging.getLogger(self.name)
        self.init_logger()

    def init_logger(self) -> None:
        """
        Initialize the logger
        :return: Nothing
        """
        self.logger.setLevel(logging.INFO)
        console_handler: StreamHandler = logging.StreamHandler()
        console_handler.setFormatter(fmt=Formatter(
            fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(hdlr=console_handler)


def get_app() -> Optional[AppBase]:
    """
    :return: The current app
    """
    app = App.get_running_app()
    assert isinstance(app, AppBase)
    return app


def get_logger() -> Logger:
    """
    :return: The app's logger
    """
    return get_app().logger
