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
        return f"{self.first_names} {self.last_names}"


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
        languages_with_names: List[Languages] = self.languages_with_names
        assert len(languages_with_names) == len(set(languages_with_names)), \
            f"More than one name in the same language: {self.names}"

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
        ret_name: FullName = FullName(language=Languages.DEFAULT, first_names="No Name",
                                      last_names="")
        for name in self.names:
            if name.language is language:
                return name

            elif name.language == Languages.DEFAULT:
                ret_name = name

        return ret_name

    def __str__(self) -> str:
        """
        :return: Ourselves as a string
        """
        return str(self.get_name(language=Languages.DEFAULT))
