import logging
from logging import Formatter, Logger, StreamHandler
from typing import Optional

from kivy.app import App
from kivy.uix.widget import Widget

from src.model.enums import Languages


class ViewCfg(object):
    """
    Configuration for views
    """

    TEXT_WIDGET_HEIGHT: str = "50dp"
    """The height of a text field
    """

    TEXT_FIELD_NAME_WIDTH: str = "300dp"
    """The width of a text field's name
    """


class AppBase(App):
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

    def set_root_widget(self, widget: Widget) -> None:
        """
        Set the root widget
        :param widget: The new widget
        :return: Nothing
        """
        raise NotImplementedError

    # TODO(joel): the current language should be part of the settings
    def get_cur_lang(self) -> Languages:
        """
        :return: The current app language
        """
        raise NotImplementedError

    def save_model(self) -> None:
        """
        Save the current model
        :return: Nothing
        """
        raise NotImplementedError


def get_app() -> Optional[AppBase]:
    """
    :return: The current app
    """
    return App.get_running_app()


def get_logger() -> Logger:
    """
    :return: The app's logger
    """
    return get_app().logger
