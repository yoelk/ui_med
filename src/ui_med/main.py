from enum import Enum
from functools import partial
from typing import List, Optional

from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.widget import Widget

from ui_med.app_base import get_logger
from ui_med.app_settings import AppWithSettings, ConfigKeys, ConfigSections
from ui_med.data import get_data_resource
from ui_med.data.data_extractors.phobias_extractor import PhobiasExtractor
from ui_med.model.db import Db
from ui_med.model.enums import Languages, Texts
from ui_med.model.languages import Lang
from ui_med.model.people import FullName, Person
from ui_med.std.enum import enum_from_value
from ui_med.views.people import EditPersonLayout, ManagePeopleLayout
from ui_med.views.names import EditNameLayout
from ui_med.views.phobias import AddPhobiaLayout

# TODO(joel):
#  Views:
#  - How can I apply a style system-wide? I think I have to use inheritance for each
#    Widget class I use.
#  - Show titles nicer, using bigger fonts for example.
#  - Work out a nicer design for how the screen look
#  - Add icon buttons for stuff like "add", "edit" or "back"
#  - In the Person view, add a place for a photo
#  - To support different languages:
#    - Use a font that allows other languages. For example, this supports
#      both Hebrew and Arabic: 'font_name="DejaVuSans-Oblique.ttf"'. But does it exist
#      in installed devices like Android? Maybe better include the font as part of the
#      code as a resource.
#    - Make sure we reload the current view once the language is changed, so that when
#      we get back from the settings screen, you can see the changes
#  =======================================================================
#  Functionality:
#  - Add a part for getting the human code and providing information about your type.
#    To begin with, use questioners to get the info
#  - Add a Phobia page with explanation for how to treat it with FEEL/TTRT
#  - Add general information pages (not person-bound) about the chakras, meridians,
#    FEEL, TTRT, etc.
#  - Add a "diseases" section like "phobias"
#  - Automatically fill translations from google-translate or something like that
#  =======================================================================
#  Current:

from ui_med.views.view_wrapper import RootWidgetWrapper


class UiMedApp(AppWithSettings):
    """
    The main app
    """

    def __init__(self, **kwargs) -> None:
        """
        Initialize
        :return: Nothing
        """
        super().__init__(**kwargs)
        self.title = "UI MED"
        self.init_static_data()
        self.db: Db = Db()

    @classmethod
    def init_static_data(cls) -> None:
        """
        Initialize static data
        :return: Nothing
        """
        PhobiasExtractor.extract(
            phobias_file_path=get_data_resource(relpath="phobias.txt"))

    def build(self):
        manage_people_layout = \
            RootWidgetWrapper(root_widget=ManagePeopleLayout(people=self.db.people),
                              title=Lang.to_str(Texts.MANAGE_PEOPLE))
        inspector.create_inspector(Window, manage_people_layout)
        return manage_people_layout

    def _set_root_widget(self, widget: Widget, title: str) -> None:
        """
        Set the root root_widget
        :param widget: The new root_widget
        :param title: The title
        :return: Nothing
        """
        get_logger().info(f"set_root_widget {self.root} -> {widget}")
        window = self.root.parent
        window.remove_widget(self.root)
        self.root = RootWidgetWrapper(root_widget=widget, title=title)
        window.add_widget(self.root)

    # API
    def view_manage_people(self, *args) -> None:
        self._set_root_widget(widget=ManagePeopleLayout(people=self.db.people),
                              title=Lang.to_str(Texts.MANAGE_PEOPLE))

    def view_edit_person(self, person: Person, *args) -> None:
        self._set_root_widget(widget=EditPersonLayout(is_editable=True, person=person,
                                                      on_close=self.view_manage_people),
                              title=Lang.to_str(Texts.EDIT_PERSON))

    def view_add_person(self, *args) -> None:
        self.view_edit_person(Person())

    def view_edit_person_name(self, person: Person, name: FullName, *args) -> None:
        self._set_root_widget(
            widget=EditNameLayout(is_editable=True, person=person, name=name,
                                  on_close=partial(self.view_edit_person, person)),
            title=Lang.to_str(Texts.EDIT_NAME))

    def view_add_person_phobia(self, person: Person, *args) -> None:
        self._set_root_widget(
            widget=AddPhobiaLayout(person=person,
                                   on_close=partial(self.view_edit_person, person)),
            title=Lang.to_str(Texts.ADD_PHOBIA))

    def model_put_person(self, person: Person, *args) -> None:
        people: List[Person] = self.db.people

        # Overwrite an existing person if exists
        if person.uuid in [p.uuid for p in people]:
            for i, p in enumerate(list(people)):
                if person.uuid == p.uuid:
                    people[i] = person

        else:
            people.append(person)

        self.db.people = people

    def get_cur_lang(self, *args) -> Languages:
        language: Optional[Enum] = enum_from_value(
            enum_cls=Languages,
            value=self.config.get(ConfigSections.USER, ConfigKeys.LANGUAGE))
        assert isinstance(language, Languages)
        return language


if __name__ == '__main__':
    app = UiMedApp()
    app.run()
