from enum import Enum
from typing import Callable, Optional

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.uix.textinput import TextInput

from src.app_base import ViewCfg, get_app
from src.model.languages import Texts, get_str


class EditTextFieldLayout(BoxLayout):
    """
    A layout for editing a single text field
    """

    def __init__(self, is_editable: bool, field_name: Enum,
                 field_value: Optional[str] = None, **kwargs) -> None:
        """
        Initialize
        :param is_editable: Are the details editable
        :param field_name: The text field's name
        :param field_value: The current text field's value
        :return: Nothing
        """
        self.is_editable: bool = is_editable
        field_value: str = field_value if field_value else ""

        super().__init__(**kwargs)
        self.orientation: str = "horizontal"
        self.size_hint = (1, None)
        self.height = ViewCfg.TEXT_WIDGET_HEIGHT

        self.name_widget = Label(text=f"{get_str(field_name)}:",
                                 size_hint=(None, 1), width=ViewCfg.TEXT_FIELD_NAME_WIDTH)
        self.add_widget(self.name_widget)

        self.value_widget = TextInput(text=field_value,
                                      size_hint=(1, 1))
        self.add_widget(self.value_widget)


class InputLayout(BoxLayout):
    """
    An input layout with a save button
    """

    def __init__(self, on_close: Callable[[], None],
                 **kwargs) -> None:
        """
        Initialize
        :param on_close: Callback for closing ourselves
        :return: Nothing
        """
        super().__init__(**kwargs)
        self.on_close: Callable[[], None] = on_close

        self.bottom_spacer = Label(size_hint=(1, 1))
        self.save_button: Button = Button(text=get_str(Texts.SAVE), size_hint=(1, None),
                                          height=ViewCfg.TEXT_WIDGET_HEIGHT,
                                          on_press=self.on_save)

    def add_save_button(self) -> None:
        """
        Add the save button
        :return: Nothing
        """
        self.add_widget(self.bottom_spacer)
        self.add_widget(self.save_button)

    def on_save(self, *args) -> None:
        """
        Callback for closing ourselves
        :return: Nothing
        """
        get_app().save_model()
        self.on_close()

    def __str__(self) -> str:
        """
        :return: Ourselves as a string
        """
        return f"{type(self)}"