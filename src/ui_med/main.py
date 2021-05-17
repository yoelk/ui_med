from functools import partial
from typing import Any, List, Optional, Union

from kivy.core.window import Window
from kivy.modules import inspector
from kivy.storage.dictstore import DictStore

from ui_med.app_base import AppBase, get_logger
from ui_med.model.db import DB_STORAGE_FILENAME, DbKeys
from ui_med.model.enums import Languages
from ui_med.model.people import FullName, Person
from ui_med.views.people import EditNameLayout, EditPersonLayout, ManagePeopleLayout


class UiMedApp(AppBase):
    """
    The main app
    """

    def __init__(self, **kwargs) -> None:
        """
        Initialize
        :return: Nothing
        """
        super().__init__(**kwargs)
        self.init_db()

    # noinspection PyAttributeOutsideInit
    def init_db(self) -> None:
        """
        Initialize the database
        :return: Nothing
        """
        self.db: DictStore = DictStore(filename=DB_STORAGE_FILENAME)
        self.db.store_load()
        if DbKeys.PEOPLE not in self.db.keys():
            self.db_put(DbKeys.PEOPLE, [])

    def build(self):
        manage_people_layout: ManagePeopleLayout = \
            ManagePeopleLayout(people=self.db_get(DbKeys.PEOPLE))
        inspector.create_inspector(Window, manage_people_layout)
        return manage_people_layout

    def db_put(self, key: str, value: Any) -> None:
        """
        Put a value in the database
        :param key: The key
        :param value: The value
        :return: Nothing
        """
        self.logger.info(f"db_put: {key}, {value}")
        self.db.put(key, **{DbKeys.VALUE: value})

    def db_get(self, key: str) -> Any:
        """
        :param key: The key
        :return: A value from the database
        """
        return self.db.get(key)[DbKeys.VALUE]

    # API
    def view_manage_people(self, *args) -> None:
        self._set_root_widget(
            widget=ManagePeopleLayout(people=self.db_get(DbKeys.PEOPLE)))

    def view_edit_person(self, person: Union[Person, int], *args) -> None:
        if isinstance(person, int):
            person = self.db_get(DbKeys.PEOPLE)[person]

        assert isinstance(person, Person)
        self._set_root_widget(
            widget=EditPersonLayout(
                is_editable=True, person=person, on_close=self.view_manage_people))

    def view_add_person(self, *args) -> None:
        self.view_edit_person(Person())

    def view_edit_person_name(self, person: Person, name: FullName, *args) -> None:
        self._set_root_widget(
            widget=EditNameLayout(
                is_editable=True, person=person, name=name,
                on_close=partial(self.view_edit_person, person)))

    def view_add_person_fear(self, person: Person, *args) -> None:
        # TODO(joel): implement choice view for fears, with a search box
        pass

    def model_put_person(self, person: Person, *args) -> None:
        people: List[Person] = self.db_get(DbKeys.PEOPLE)

        # Overwrite an existing person if exists
        if person.uuid in [p.uuid for p in people]:
            for i, p in enumerate(list(people)):
                if person.uuid == p.uuid:
                    people[i] = person

        else:
            people.append(person)

        self.db_put(key=DbKeys.PEOPLE, value=people)

    def get_cur_lang(self, *args) -> Languages:
        # TODO(joel): use app config for default language
        return Languages.ENGLISH


if __name__ == '__main__':
    app = UiMedApp()
    app.run()