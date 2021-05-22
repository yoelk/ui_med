from typing import Optional, Union

from kivy.app import App

from ui_med.model.enums import Languages
from ui_med.model.people import FullName, Person


class UiMedAppApi(object):
    """
    API for our app
    """

    def view_manage_people(self, *args) -> None:
        """
        Open the view for Managing people
        :return: Nothing
        """
        raise NotImplementedError

    def view_edit_person(self, person: Union[Person, int], *args) -> None:
        """
        Open the view for editing a person
        :param person: The person object or its index in the people list
        None means a new person needs to be created
        :return: Nothing
        """
        raise NotImplementedError

    def view_add_person(self, *args) -> None:
        """
        Open the view for adding a person
        :return: Nothing
        """
        raise NotImplementedError

    def view_edit_person_name(self, person: Person, name: FullName, *args) -> None:
        """
        Open the view for editing a person's name
        :param person: The person
        :param name: The name
        :return: Nothing
        """
        raise NotImplementedError

    def view_add_person_phobia(self, person: Person, *args) -> None:
        """
        Open the view for adding a person's fear
        :param person: The person
        :return: Nothing
        """
        raise NotImplementedError

    def model_put_person(self, person: Person, *args) -> None:
        """
        Put a person in the database
        :return: Nothing
        """
        raise NotImplementedError

    # TODO(joel): the current language should be part of the settings
    def get_cur_lang(self, *args) -> Languages:
        """
        :return: The current app language
        """
        raise NotImplementedError
