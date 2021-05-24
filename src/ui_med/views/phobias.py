from functools import partial
from typing import List, Optional

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from ui_med.app_base import ViewCfg, get_app
from ui_med.model.enums import Orientations
from ui_med.model.languages import Texts, to_str
from ui_med.model.people import Person
from ui_med.model.phobias import ALL_PHOBIAS, Phobia
from ui_med.views.input import InputLayout
from ui_med.views.selection_recycle_view import SelectionRecycleView


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
        person.phobias.remove(phobia)
        get_app().view_edit_person(person)


class AddPhobiaLayout(InputLayout):
    """
    A layout for adding a phobia
    """

    def __init__(self, person: Person, **kwargs) -> None:
        """
        Initialize
        :param person: The person
        :return: Nothing
        """
        super().__init__(close_button_text=to_str(Texts.BACK), **kwargs)
        self.orientation = Orientations.VERTICAL

        self.person: Person = person
        self.all_objects: List[Phobia] = ALL_PHOBIAS

        self.search_bar: TextInput = TextInput(text="", multiline=False,
                                               size_hint=(1, None),
                                               height=ViewCfg.TEXT_WIDGET_HEIGHT)
        self.search_bar.bind(text=self.update_phobias_list)
        self.add_widget(self.search_bar)

        self.phobias_list_container = BoxLayout(orientation=Orientations.VERTICAL,
                                                size_hint=(1, 1))
        self.add_widget(self.phobias_list_container)
        self.phobias_list_widget: Optional[SelectionRecycleView] = None
        self.update_phobias_list()

        self.add_save_button()

    @property
    def narrowed_objects_list(self) -> List[Phobia]:
        """
        :return: The narrowed objects list, according to the search bar
        """
        objects: List[Phobia] = []
        for x in self.all_objects:
            if self.search_bar.text in str(x) \
                    and x not in self.person.phobias:
                objects.append(x)

        return objects

    def update_phobias_list(self, *args) -> None:
        """
        Update the phobias' list widget
        :return: Nothing
        """
        self.phobias_list_container.clear_widgets()
        self.phobias_list_widget = \
            SelectionRecycleView(objects=self.narrowed_objects_list)
        self.phobias_list_container.add_widget(self.phobias_list_widget)

    def on_close_button_pressed(self, *args) -> None:
        assert len(self.phobias_list_widget.selected_objects) <= 1
        if len(self.phobias_list_widget.selected_objects) == 1:
            self.person.phobias.append(self.phobias_list_widget.selected_objects[0])

        get_app().view_edit_person(self.person)
        super().on_close_button_pressed()
