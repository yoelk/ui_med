from typing import List, Optional
from uuid import UUID, uuid4

from ui_med.data.fears import Fear
from ui_med.model.enums import Languages


class FullName(object):
    """
    A person's full name
    """

    def __init__(self, language: Languages, first_names: str = "",
                 last_names: str = "") -> None:
        """
        Initialize
        :param language: The names' language
        :param first_names: The first names
        :param last_names: The last names
        :return: Nothing
        """
        self.language: Languages = language
        self.first_names: str = first_names
        self.last_names: str = last_names

    def __str__(self) -> str:
        """
        :return: Ourselves as a string
        """
        return f"{self.first_names} {self.last_names}"

    def __eq__(self, other: 'FullName') -> bool:
        """
        :param other: Another instance
        :return: True if we are equal to other, else False
        """
        return self.language == other.language \
               and self.first_names == other.first_names \
               and self.last_names == other.last_names


class Person(object):
    """
    A person
    """

    def __init__(self) -> None:
        """
        Initialize
        :return: Nothing
        """
        self.uuid: UUID = uuid4()
        self.names: List[FullName] = []
        self.fears: List[Fear] = []

    @property
    def languages_with_names(self) -> List[Languages]:
        """
        :return: The current allowed_languages we have names for
        """
        return [name.language for name in self.names]

    @property
    def languages_without_name(self) -> List[Languages]:
        """
        :return: The current allowed_languages we don't have names for
        """
        return list(set(Languages) - set(self.languages_with_names))

    def get_name(self, language: Languages) -> FullName:
        """
        :param language: The asked language
        :return: The name in the requested language
        """
        ret_name: Optional[FullName] = None

        for name in self.names:
            if name.language is language:
                return name

            elif name.language == Languages.DEFAULT:
                ret_name = name

        if ret_name is None:
            ret_name = self.names[0] if self.names \
                else FullName(language=Languages.DEFAULT, first_names="No Name",
                              last_names="")

        return ret_name

    def __str__(self) -> str:
        """
        :return: Ourselves as a string
        """
        return str(self.get_name(language=Languages.DEFAULT))
