from typing import Optional

from kivy.app import App

from src.model.enums import Languages
from src.model.people import FullName, Person


class UiMedAppApi(object):
    """
    API for our app
    """

    def view_manage_people(self, *args) -> None:
        """
        Manage the people
        :return: Nothing
        """
        raise NotImplementedError

    def view_edit_person(self, person: Optional[Person], *args) -> None:
        """
        Edit a person
        :param person: The person, or None if one needs to be created
        :return: Nothing
        """
        raise NotImplementedError

    def view_edit_person_name(self, person: Person, name: FullName, *args) -> None:
        """
        Edit a person
        :param person: The person
        :param name: The name
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
