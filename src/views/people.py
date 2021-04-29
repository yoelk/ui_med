from typing import Callable, List, Optional

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

from src.app_base import ViewCfg, get_app
from src.model.languages import Texts, get_str
from src.model.enums import Languages
from src.model.people import FullName, Person
from src.views.input import EditTextFieldLayout, InputLayout
from src.views.people_recycle_view import PeopleRecycleView


class EditNameLayout(InputLayout):
    """
    A layout for adding/editing a name
    """

    def __init__(self, is_editable: bool, name: FullName,
                 allowed_languages: Optional[List[Languages]] = None, **kwargs) -> None:
        """
        Initialize
        :param is_editable: Are the details editable
        :param name: The existing full name if possible
        :param allowed_languages: Languages that can be chosen
        :return: Nothing
        """
        self.is_editable: bool = is_editable
        self.name: FullName = name

        super().__init__(**kwargs)
        self.orientation: str = "vertical"

        assert self.name.language in allowed_languages
        self.languages_widget = \
            Spinner(text=get_str(self.name.language),
                    values=sorted(get_str(lang) for lang in allowed_languages),
                    size_hint=(1, None), height=ViewCfg.TEXT_WIDGET_HEIGHT,
                    disabled=not self.is_editable)
        self.add_widget(self.languages_widget)

        self.first_names_widget = \
            EditTextFieldLayout(is_editable=is_editable,
                                field_name=Texts.FIRST_NAMES,
                                field_value=self.name.first_names,
                                disabled=not self.is_editable)
        self.add_widget(self.first_names_widget)

        self.last_names_widget = \
            EditTextFieldLayout(is_editable=is_editable,
                                field_name=Texts.LAST_NAMES,
                                field_value=self.name.last_names,
                                disabled=not self.is_editable)
        self.add_widget(self.last_names_widget)

        self.add_save_button()


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
        self.add_name_layout: Optional[EditNameLayout] = None

        super().__init__(**kwargs)
        self.orientation: str = "vertical"

        self.names_title = Label(text=f"{get_str(Texts.NAMES)}:",
                                 size_hint=(1, None), height=ViewCfg.TEXT_WIDGET_HEIGHT)
        self.add_widget(self.names_title)

        self.full_name_widgets = []
        for name in person.names:
            name_widget = EditNameLayout(is_editable=False, name=name,
                                         on_close=self.close_add_name_screen)
            self.full_name_widgets.append(name_widget)
            self.add_widget(name_widget)

        self.add_name_button: Optional[Button] = None
        self.add_name_button = Button(text=get_str(Texts.ADD_NAME),
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

        self.add_name_layout = EditNameLayout(
            is_editable=True, name=new_name,
            allowed_languages=languages_without_name,
            on_close=self.close_add_name_screen)
        get_app().set_root_widget(self.add_name_layout)

    # noinspection PyUnusedLocal
    def close_add_name_screen(self, *args) -> None:
        """
        Close the screen for adding a name
        :return: Nothing
        """
        get_app().set_root_widget(self)


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
        self.edit_person_layout: Optional[EditPersonLayout] = None

        super().__init__(**kwargs)
        self.orientation: str = "vertical"

        self.people_title = Label(text=f"{get_str(Texts.PEOPLE)}:",
                                  size_hint=(1, None), height=ViewCfg.TEXT_WIDGET_HEIGHT)
        self.add_widget(self.people_title)

        self.people_list = PeopleRecycleView(people=self.people, size_hint=(1, 1))
        self.add_widget(self.people_list)

        self.add_person_button = Button(text=get_str(Texts.ADD_PERSON),
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
        self.edit_person_layout = EditPersonLayout(
            is_editable=True, person=person, on_close=self.close_add_person_screen)
        get_app().set_root_widget(self.edit_person_layout)

    # noinspection PyUnusedLocal
    def close_add_person_screen(self, *args) -> None:
        """
        Close the screen for adding a person
        :return: Nothing
        """
        get_app().set_root_widget(self)
