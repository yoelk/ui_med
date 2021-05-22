from typing import List, Optional

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from ui_med.app_base import ViewCfg, get_app
from ui_med.model.languages import Texts, to_str
from ui_med.model.enums import Languages, Orientations
from ui_med.model.people import FullName, Person
from ui_med.views.input import InputLayout
from ui_med.views.names import NameEntryLayout
from ui_med.views.selection_recycle_view import SelectionRecycleView
from ui_med.views.phobias import PhobiaEntryLayout


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

        # Phobias
        phobias_title = Label(text=f"{to_str(Texts.PHOBIAS)}:",
                              size_hint=(1, None), height=ViewCfg.TEXT_WIDGET_HEIGHT)
        self.add_widget(phobias_title)
        for phobia in person.phobias:
            phobia_widget = PhobiaEntryLayout(person=person, phobia=phobia)
            self.add_widget(phobia_widget)

        add_phobia_button = Button(text=to_str(Texts.ADD_PHOBIA),
                                   size_hint=(1, None),
                                   height=ViewCfg.TEXT_WIDGET_HEIGHT,
                                   on_press=get_app().view_add_person_phobia,
                                   disabled=not self.is_add_name_enabled)
        self.add_widget(add_phobia_button)

        # Save
        self.add_save_button()

    # TODO(joel): figure out who adds the phobia entry to Person and how on_close works
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

        people_list = SelectionRecycleView(objects=people,
                                           on_selection=get_app().view_edit_person,
                                           size_hint=(1, 1))
        self.add_widget(people_list)

        add_person_button = Button(
            text=to_str(Texts.ADD_PERSON),
            size_hint=(1, None),
            height=ViewCfg.TEXT_WIDGET_HEIGHT,
            on_press=get_app().view_add_person)
        self.add_widget(add_person_button)
