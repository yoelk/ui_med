from typing import Callable, List, Optional

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.recycleview import RecycleView
from kivy.uix.label import Label

from src.model.languages import Texts, get_str
from src.model.enums import Languages
from src.model.people import FullName, Person
from src.views.input import EditTextFieldLayout, InputLayoutContainer
from src.views.settings import TEXT_WIDGET_HEIGHT

Builder.load_string('''
<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
<RV>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
''')


class PeopleRecycleView(RecycleView):
    def __init__(self, people: Optional[List[Person]], **kwargs):
        super(PeopleRecycleView, self).__init__(**kwargs)

        if people is None:
            people = []
        self.data = [{'text': str(x)} for x in people]


class EditFullNameLayout(BoxLayout):
    """
    A layout for adding/editing a full name
    """

    def __init__(self, is_editable: bool, languages: List[Languages],
                 full_name: FullName, **kwargs) -> None:
        """
        Initialize
        :param is_editable: Are the details editable
        :param languages: Languages that can be chosen
        :param full_name: The existing full name if possible
        :return: Nothing
        """
        self.is_editable: bool = is_editable
        self.full_name: FullName = full_name

        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.languages_widget = DropDown()
        for language in languages:
            self.languages_widget.add_widget(Label(text=get_str(language)))
        self.add_widget(self.languages_widget)

        self.first_names_widget = \
            EditTextFieldLayout(is_editable=is_editable,
                                field_name=Texts.FIRST_NAMES,
                                field_value=self.full_name.first_names)
        self.add_widget(self.first_names_widget)

        self.last_names_widget = \
            EditTextFieldLayout(is_editable=is_editable,
                                field_name=Texts.LAST_NAMES,
                                field_value=self.full_name.last_names)
        self.add_widget(self.last_names_widget)


class EditPersonLayout(BoxLayout):
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
        self.orientation = "vertical"

        self.full_name_widgets = []
        for name in person.names:
            full_name_widget = EditTextFieldLayout(is_editable=False,
                                                   field_name=Texts.FULL_NAME,
                                                   field_value=str(name))
            self.full_name_widgets.append(full_name_widget)
            self.add_widget(full_name_widget)


class ManagePeopleLayout(BoxLayout):
    """
    A layout for managing people
    """

    def __init__(self, people: Optional[List[Person]],
                 on_add_person: Callable[[Person], None], **kwargs) -> None:
        """
        Initialize
        :param people: The existing people's list
        :param on_add_person: Callback for adding a person
        :return: Nothing
        """
        self.people: List[Person] = people if people else []
        self.on_add_person: Callable[[Person], None] = on_add_person
        self.edit_person_layout: Optional[InputLayoutContainer] = None

        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.headline = Label(text=f"{get_str(Texts.PEOPLE)}:",
                              size_hint=(1, None), height=TEXT_WIDGET_HEIGHT)
        self.add_widget(self.headline)

        self.people_list = PeopleRecycleView(people=self.people, size_hint=(1, 1))
        self.add_widget(self.people_list)

        self.add_person_button = Button(text=get_str(Texts.ADD_PERSON),
                                        size_hint=(1, None), height=TEXT_WIDGET_HEIGHT,
                                        on_press=self.open_add_person_screen)
        self.add_widget(self.add_person_button)

    # noinspection PyUnusedLocal
    def open_add_person_screen(self, *args) -> None:
        """
        Open a screen for adding a person
        :return: Nothing
        """
        self.edit_person_layout: InputLayoutContainer = \
            InputLayoutContainer(input_layout=EditPersonLayout(is_editable=True,
                                                               person=Person()),
                                 on_save=self.close_add_person_screen)
        parent = self.parent
        parent.remove_widget(self)
        parent.add_widget(self.edit_person_layout)

    # noinspection PyUnusedLocal
    def close_add_person_screen(self, *args) -> None:
        """
        Close the screen for adding a person
        :return: Nothing
        """
        self.on_add_person(self.edit_person_layout.input_layout.person)
        parent = self.edit_person_layout.parent
        parent.remove_widget(self.edit_person_layout)
        parent.add_widget(self)
