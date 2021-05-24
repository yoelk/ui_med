from typing import List, Optional

from ui_med.model.enums import PhobiaExplanations, PhobiaTypes

ALL_PHOBIAS: List['Phobia'] = []
"""All of the phobias
"""


class Phobia(object):
    """
    A phobia
    """

    def __init__(self, phobia_types: List[PhobiaTypes], name: str, desc: Optional[str],
                 synonym_name: Optional[str], parent_names: Optional[List[str]]) -> None:
        """
        Initialize
        :param phobia_types: The phobia types
        :param name: The name
        :param desc: The description
        :param synonym_name: The name of our synonym
        :param parent_names: The names of our parents
        :return: Nothing
        """
        self.name: str = name
        assert isinstance(self.name, str)

        self.desc: Optional[str] = desc
        self.synonym_name: Optional[str] = synonym_name
        assert isinstance(self.desc, str) or isinstance(self.synonym_name, str)

        self.parent_names: Optional[List[str]] = parent_names
        self.phobia_types: List[PhobiaTypes] = phobia_types

    # TODO(joel): Decide how to map phobias to their explanations
    # @property
    # def phobia_explanation(self) -> PhobiaExplanations:
    #     """
    #     :return: The explanation for the phobia
    #     """
    #     return PhobiaExplanations.

    def __str__(self) -> str:
        """
        :return: Ourselves as a string
        """
        return f"{self.name}: {self.desc}"

    def __eq__(self, other: 'Phobia') -> bool:
        """
        :param other: Another instance
        :return: True if we are equal to other, else False
        """
        return self.name == other.name \
               and self.desc == other.desc

    @classmethod
    def register_phobia(cls, phobia: 'Phobia') -> None:
        """
        Register a phobia
        :param phobia: The phobia
        :return: Nothing
        """
        ALL_PHOBIAS.append(phobia)
