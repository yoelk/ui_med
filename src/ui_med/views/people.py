from functools import partial
from typing import Dict, List, Optional

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

from ui_med.app_base import ViewCfg, get_app
from ui_med.model.languages import Texts, to_str
from ui_med.model.enums import Languages, Orientations
from ui_med.model.people import FullName, Person
from ui_med.model.phobias import Phobia
from ui_med.views.input import EditTextFieldLayout, InputLayout
from ui_med.views.people_recycle_view import PeopleRecycleView


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


class PhobiaEntryLayout(BoxLayout):
    """
    A layout for a fear entry in a list
    """

    def __init__(self, person: Person, phobia: Phobia, **kwargs) -> None:
        """
        Initialize
        :param person: The person
        :param phobia: The phobia
        :return: Nothing
        """
        super().__init__(**kwargs)
        self.orientation = Orientations.HORIZONTAL
        self.size_hint = (1, None)
        self.height = ViewCfg.TEXT_WIDGET_HEIGHT

        self.add_widget(
            Label(text=phobia.name, size_hint=(1, 1)))
        self.add_widget(
            Button(text=to_str(Texts.DELETE),
                   size_hint=(None, 1), width=ViewCfg.TEXT_FIELD_NAME_WIDTH,
                   on_press=partial(self.delete_phobia, person, phobia)))

    @classmethod
    def delete_phobia(cls, person: Person, phobia: Phobia, *args) -> None:
        """
        Delete a name
        :param person: The person
        :param phobia: The phobia
        :return: Nothing
        """
        person.fears.remove(phobia)
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


class EditPersonLayout(InputLayout):
    """
    A layout for adding/editing a person
    """

    def __init__(self, is_editable: bool, person: Person, **kwargs) -> None:
        """
        Initialize
        :param is_editable: Are the details editable
        :param person: The existing person's details if possible
        :return: Nothing
        """
        self.is_editable: bool = is_editable
        self.person: Person = person

        super().__init__(close_button_text=to_str(Texts.SAVE), **kwargs)
        self.orientation = Orientations.VERTICAL

        # Names
        names_title = Label(text=f"{to_str(Texts.NAMES)}:",
                            size_hint=(1, None), height=ViewCfg.TEXT_WIDGET_HEIGHT)
        self.add_widget(names_title)
        for name in person.names:
            name_widget = NameEntryLayout(person=person, name=name)
            self.add_widget(name_widget)

        self.add_name_button: Optional[Button] = None
        self.add_name_button = Button(text=to_str(Texts.ADD_NAME),
                                      size_hint=(1, None),
                                      height=ViewCfg.TEXT_WIDGET_HEIGHT,
                                      on_press=self.open_add_name_screen,
                                      disabled=not self.is_add_name_enabled)
        self.add_widget(self.add_name_button)

        # Fears
        fears_title = Label(text=f"{to_str(Texts.PHOBIAS)}:",
                            size_hint=(1, None), height=ViewCfg.TEXT_WIDGET_HEIGHT)
        self.add_widget(fears_title)
        for fear in person.fears:
            fear_widget = PhobiaEntryLayout(person=person, fear=fear)
            self.add_widget(fear_widget)

        add_fear_button = Button(text=to_str(Texts.ADD_PHOBIA),
                                 size_hint=(1, None),
                                 height=ViewCfg.TEXT_WIDGET_HEIGHT,
                                 on_press=get_app().view_add_person_fear,
                                 disabled=not self.is_add_name_enabled)
        self.add_widget(add_fear_button)

        # Save
        self.add_save_button()

    # noinspection PyUnusedLocal
    def open_add_name_screen(self, *args) -> None:
        """
        Open a screen for adding a name
        :return: Nothing
        """
        languages_without_name: List[Languages] = self.person.languages_without_name
        language: Languages = languages_without_name[0]
        if get_app().get_cur_lang() in languages_without_name:
            language = get_app().get_cur_lang()
        elif Languages.DEFAULT in languages_without_name:
            language = Languages.DEFAULT
        new_name: FullName = FullName(language=language)
        self.person.names.append(new_name)
        self.add_name_button.disabled = not self.is_add_name_enabled

        get_app().view_edit_person_name(person=self.person, name=new_name)

    def on_close_button_pressed(self, *args) -> None:
        get_app().model_put_person(person=self.person)
        super().on_close_button_pressed()


class ManagePeopleLayout(BoxLayout):
    """
    A layout for managing people
    """

    def __init__(self, people: Optional[List[Person]], **kwargs) -> None:
        """
        Initialize
        :param people: The existing people's list
        :return: Nothing
        """
        super().__init__(**kwargs)
        self.orientation = Orientations.VERTICAL

        people_title = Label(text=f"{to_str(Texts.PEOPLE)}:",
                             size_hint=(1, None), height=ViewCfg.TEXT_WIDGET_HEIGHT)
        self.add_widget(people_title)

        people_list = PeopleRecycleView(people=people, size_hint=(1, 1))
        self.add_widget(people_list)

        add_person_button = Button(
            text=to_str(Texts.ADD_PERSON),
            size_hint=(1, None),
            height=ViewCfg.TEXT_WIDGET_HEIGHT,
            on_press=get_app().view_add_person)
        self.add_widget(add_person_button)
