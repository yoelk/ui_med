from typing import List, Optional

from src.model.enums import Languages


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
        return " ".join(self.first_names + self.last_names)


class Person(object):
    """
    A person
    """

    def __init__(self, names: Optional[List[FullName]] = None) -> None:
        """
        Initialize
        :param names: The person's names
        :return: Nothing
        """
        self.names: List[FullName] = names if names else []
        name_languages: List[Languages] = self.name_languages
        assert len(name_languages) == len(set(name_languages)), \
            f"More than one name in the same language: {self.names}"

    @property
    def name_languages(self) -> List[Languages]:
        """
        :return: The current languages we have names for
        """
        return [name.language for name in self.names]
