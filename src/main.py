from functools import partial

from kivy.core.window import Window
from kivy.modules import inspector

from src.app_base import AppBase, get_logger
from src.model.enums import Languages
from src.model.people import FullName, Person
from src.views.people import EditNameLayout, EditPersonLayout, ManagePeopleLayout

# TODO(joel): save data using a consistent store
model = {
    "people": [Person(names=[FullName(language=Languages.ENGLISH,
                                      first_names="Joel", last_names="Koenka")]),
               Person(names=[FullName(language=Languages.ENGLISH,
                                      first_names="Noam", last_names="Koenka")])
               ]
}


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
        self.model = model

    def build(self):
        manage_people_layout: ManagePeopleLayout = \
            ManagePeopleLayout(people=self.model["people"])
        inspector.create_inspector(Window, manage_people_layout)
        return manage_people_layout

    # API
    def manage_people(self, *args) -> None:
        self._set_root_widget(
            widget=ManagePeopleLayout(people=self.model["people"]))

    def edit_person(self, person: Person, *args) -> None:
        self._set_root_widget(
            widget=EditPersonLayout(
                is_editable=True, person=person, on_close=self.manage_people))

    def edit_person_name(self, person: Person, name: FullName, *args) -> None:
        self._set_root_widget(
            widget=EditNameLayout(
                is_editable=True, person=person, name=name,
                on_close=partial(self.edit_person, person)))

    def save_model(self, *args) -> None:
        # TODO(joel): Save model
        get_logger().info(f"model saved:\n{self.model}")

    def get_cur_lang(self, *args) -> Languages:
        # TODO(joel): use app config for default language
        return Languages.ENGLISH


if __name__ == '__main__':
    app = UiMedApp()
    app.run()
