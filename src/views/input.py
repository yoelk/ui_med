from enum import Enum
from typing import Callable, Optional

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.uix.textinput import TextInput

from src.model.languages import Texts, get_str
from src.views.settings import TEXT_FIELD_NAME_WIDTH, TEXT_WIDGET_HEIGHT


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
        self.orientation = "horizontal"
        self.size_hint = (1, None)
        self.height = TEXT_WIDGET_HEIGHT

        self.name_widget = Label(text=f"{get_str(field_name)}:",
                                 size_hint=(None, 1), width=TEXT_FIELD_NAME_WIDTH)
        self.add_widget(self.name_widget)

        self.value_widget = TextInput(text=field_value,
                                      size_hint=(1, 1))
        self.add_widget(self.value_widget)


class InputLayoutContainer(BoxLayout):
    """
    A container for an input layout
    """

    def __init__(self, input_layout: Layout, on_save: Callable[[], None],
                 **kwargs) -> None:
        """
        Initialize
        :param input_layout: The input layout
        :param on_save: Callback for saving the input
        :return: Nothing
        """
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.input_layout: Layout = input_layout
        self.input_layout.size_hint = (1, 1)
        self.add_widget(self.input_layout)

        self.save_button: Button = Button(text=get_str(Texts.SAVE), size_hint=(1, None),
                                          height=TEXT_WIDGET_HEIGHT, on_press=on_save)
        self.add_widget(self.save_button)
