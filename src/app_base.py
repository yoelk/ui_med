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

    def set_root_widget(self, widget: Widget) -> None:
        """
        Set the root widget
        :param widget: The new widget
        :return: Nothing
        """
        raise NotImplementedError

    def get_cur_lang(self) -> Languages:
        """
        :return: The current app language
        """
        raise NotImplementedError


def get_app() -> Optional[AppBase]:
    """
    :return: The current app
    """
    return App.get_running_app()
