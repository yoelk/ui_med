from functools import partial
from typing import Dict

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from ui_med.app_base import ViewCfg, get_app
from ui_med.model.enums import Languages, Orientations
from ui_med.model.languages import Texts, to_str
from ui_med.model.people import FullName, Person
from ui_med.views.input import EditTextFieldLayout, InputLayout


class NameEntryLayout(BoxLayout):
    """
    A layout for a name entry in a list
    """

    def __init__(self, person: Person, name: FullName, **kwargs) -> None:
        """
        Initialize
        :param person: The person
        :param name: The name
        :return: Nothing
        """
        super().__init__(**kwargs)
        self.orientation = Orientations.HORIZONTAL
        self.size_hint = (1, None)
        self.height = ViewCfg.TEXT_WIDGET_HEIGHT

        self.add_widget(
            Button(text=to_str(name.language.value), disabled=True,
                   size_hint=(None, 1), width=ViewCfg.TEXT_FIELD_NAME_WIDTH))
        self.add_widget(
            Label(text=str(name), size_hint=(1, 1)))
        self.add_widget(
            Button(text=to_str(Texts.EDIT),
                   size_hint=(None, 1), width=ViewCfg.TEXT_FIELD_NAME_WIDTH,
                   on_press=partial(get_app().view_edit_person_name, person, name)))
        self.add_widget(
            Button(text=to_str(Texts.DELETE),
                   size_hint=(None, 1), width=ViewCfg.TEXT_FIELD_NAME_WIDTH,
                   on_press=partial(self.delete_name, person, name)))

    @classmethod
    def delete_name(cls, person: Person, name: FullName, *args) -> None:
        """
        Delete a name
        :param person: The person
        :param name: The name
        :return: Nothing
        """
        person.names.remove(name)
        get_app().view_edit_person(person)


class EditNameLayout(InputLayout):
    """
    A layout for adding/editing a name
    """

    def __init__(self, is_editable: bool, person: Person, name: FullName,
                 **kwargs) -> None:
        """
        Initialize
        :param is_editable: Are the details editable
        :param person: The person
        :param name: The name
        :return: Nothing
        """
        super().__init__(close_button_text=to_str(Texts.BACK), **kwargs)
        self.orientation = Orientations.VERTICAL

        self.person: Person = person
        self.name: FullName = name

        self.language_values_to_languages: Dict[str, Languages] = {}
        for lang in person.languages_without_name + [self.name.language]:
            self.language_values_to_languages[to_str(lang.value)] = lang
        self.language_widget: Spinner = \
            Spinner(text=to_str(self.name.language.value),
                    values=sorted(self.language_values_to_languages.keys()),
                    size_hint=(1, None), height=ViewCfg.TEXT_WIDGET_HEIGHT,
                    disabled=not is_editable)
        self.add_widget(self.language_widget)

        self.first_names_widget: EditTextFieldLayout = \
            EditTextFieldLayout(is_editable=is_editable,
                                field_name=Texts.FIRST_NAMES,
                                field_value=self.name.first_names,
                                disabled=not is_editable)
        self.add_widget(self.first_names_widget)

        self.last_names_widget: EditTextFieldLayout = \
            EditTextFieldLayout(is_editable=is_editable,
                                field_name=Texts.LAST_NAMES,
                                field_value=self.name.last_names,
                                disabled=not is_editable)
        self.add_widget(self.last_names_widget)

        self.add_save_button()

    def on_close_button_pressed(self, *args) -> None:
        self.name.language = self.language_values_to_languages[self.language_widget.text]
        self.name.first_names = self.first_names_widget.get_value()
        self.name.last_names = self.last_names_widget.get_value()
        super().on_close_button_pressed()
