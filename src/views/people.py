from functools import partial
from typing import Dict, List, Optional

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

from src.app_base import ViewCfg, get_app
from src.model.languages import Texts, to_str
from src.model.enums import Languages, Orientations
from src.model.people import FullName, Person
from src.views.input import EditTextFieldLayout, InputLayout
from src.views.people_recycle_view import PeopleRecycleView


class ShowNameLayout(BoxLayout):
    """
    A layout for showing a name
    """

    def __init__(self, name: FullName, person: Person, **kwargs) -> None:
        """
        Initialize
        :param name: The name
        :param person: The person
        :return: Nothing
        """
        super().__init__(**kwargs)
        self.orientation = Orientations.HORIZONTAL
        self.size_hint = (1, None)
        self.height = ViewCfg.TEXT_WIDGET_HEIGHT

        self.add_widget(
            Button(text=to_str(name.language), disabled=True,
                   size_hint=(None, 1), width=ViewCfg.TEXT_FIELD_NAME_WIDTH))
        self.add_widget(
            Label(text=str(name), size_hint=(1, 1)))
        self.add_widget(
            Button(text=to_str(Texts.EDIT),
                   size_hint=(None, 1), width=ViewCfg.TEXT_FIELD_NAME_WIDTH,
                   on_press=partial(get_app().edit_person_name, person, name)))


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
        super().__init__(**kwargs)
        self.orientation = Orientations.VERTICAL

        self.name: FullName = name

        self.language_values_to_languages: Dict[str, Languages] = {}
        for lang in person.languages_without_name + [name.language]:
            self.language_values_to_languages[to_str(lang)] = lang
        self.language_widget: Spinner = \
            Spinner(text=to_str(name.language),
                    values=sorted(self.language_values_to_languages.keys()),
                    size_hint=(1, None), height=ViewCfg.TEXT_WIDGET_HEIGHT,
                    disabled=not is_editable)
        self.add_widget(self.language_widget)

        self.first_names_widget: EditTextFieldLayout = \
            EditTextFieldLayout(is_editable=is_editable,
                                field_name=Texts.FIRST_NAMES,
                                field_value=name.first_names,
                                disabled=not is_editable)
        self.add_widget(self.first_names_widget)

        self.last_names_widget: EditTextFieldLayout = \
            EditTextFieldLayout(is_editable=is_editable,
                                field_name=Texts.LAST_NAMES,
                                field_value=name.last_names,
                                disabled=not is_editable)
        self.add_widget(self.last_names_widget)

        self.add_save_button()

    def on_save(self, *args) -> None:
        self.name.language = self.language_values_to_languages[self.language_widget.text]
        self.name.first_names = self.first_names_widget.get_value()
        self.name.last_names = self.last_names_widget.get_value()
        super().on_save()


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

        super().__init__(**kwargs)
        self.orientation = Orientations.VERTICAL

        self.names_title = Label(text=f"{to_str(Texts.NAMES)}:",
                                 size_hint=(1, None), height=ViewCfg.TEXT_WIDGET_HEIGHT)
        self.add_widget(self.names_title)

        self.full_name_widgets = []
        for name in person.names:
            name_widget = ShowNameLayout(name=name, person=person)
            self.full_name_widgets.append(name_widget)
            self.add_widget(name_widget)

        self.add_name_button: Optional[Button] = None
        self.add_name_button = Button(text=to_str(Texts.ADD_NAME),
                                      size_hint=(1, None),
                                      height=ViewCfg.TEXT_WIDGET_HEIGHT,
                                      on_press=self.open_add_name_screen,
                                      disabled=not self.is_add_name_enabled)
        self.add_widget(self.add_name_button)

        self.add_save_button()

    @property
    def is_add_name_enabled(self) -> bool:
        """
        :return: Is the name adding button enabled
        """
        return self.is_editable and self.person.languages_without_name

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

        get_app().edit_person_name(person=self.person, name=new_name)


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
        self.people: List[Person] = people if people else []

        super().__init__(**kwargs)
        self.orientation = Orientations.VERTICAL

        self.people_title = Label(text=f"{to_str(Texts.PEOPLE)}:",
                                  size_hint=(1, None), height=ViewCfg.TEXT_WIDGET_HEIGHT)
        self.add_widget(self.people_title)

        self.people_list = PeopleRecycleView(people=self.people, size_hint=(1, 1))
        self.add_widget(self.people_list)

        self.add_person_button = Button(text=to_str(Texts.ADD_PERSON),
                                        size_hint=(1, None),
                                        height=ViewCfg.TEXT_WIDGET_HEIGHT,
                                        on_press=self.open_add_person_screen)
        self.add_widget(self.add_person_button)

    # noinspection PyUnusedLocal
    def open_add_person_screen(self, *args) -> None:
        """
        Open a screen for adding a person
        :return: Nothing
        """
        person: Person = Person()
        self.people.append(person)
        get_app().edit_person(person=person)
