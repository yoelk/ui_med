from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from ui_med.views.view_cfg import ViewCfg
from ui_med.app_base import get_app
from ui_med.model.enums import Orientations, Texts
from ui_med.model.languages import Lang


class RootWidgetWrapper(BoxLayout):
    """
    A wrapper for root widgets (that take the whole screen)
    """

    def __init__(self, root_widget: Widget, title: str = "", **kwargs) -> None:
        """
        Initialize
        :param root_widget: The root widget we wrap
        :param title: The layout's title
        :return: Nothing
        """
        super().__init__(**kwargs)
        self.orientation = Orientations.VERTICAL

        # The top bar
        top_bar = BoxLayout(orientation=Orientations.HORIZONTAL,
                            size_hint=(1, None), height=ViewCfg.TEXT_WIDGET_HEIGHT)

        settings_button = Button(text=f"{Lang.to_str(Texts.SETTINGS)}",
                                 size_hint=(None, 1),
                                 height=ViewCfg.TEXT_FIELD_NAME_WIDTH)
        settings_button.bind(on_press=get_app().open_settings)
        top_bar.add_widget(settings_button)

        app_name = Label(text=get_app().screen_name,
                         size_hint=(None, 1), height=ViewCfg.TEXT_FIELD_NAME_WIDTH)
        top_bar.add_widget(app_name)

        title = Label(text=title, size_hint=(1, 1))
        top_bar.add_widget(title)

        self.add_widget(top_bar)

        # The root widget
        self.add_widget(root_widget)
