from typing import List, Optional

from ui_med.model.enums import PhobiaTypes

ALL_PHOBIAS: List['Phobia'] = []
"""All of the phobias
"""


class Phobia(object):
    """
    A phobia
    """

    def __init__(self, phobia_type: PhobiaTypes, name: str, desc: Optional[str],
                 synonym_name: Optional[str], parent_names: Optional[List[str]]) -> None:
        """
        Initialize
        :param phobia_type: The phobia type
        :param name: The name
        :param desc: The description
        :param synonym_name: The name of our synonym
        :param parent_names: The names of our parents
        :return: Nothing
        """
        self.phobia_type: PhobiaTypes = phobia_type
        assert self.phobia_type is not None

        self.name: str = name
        assert self.name is not None

        self.desc: Optional[str] = desc
        self.synonym_name: Optional[str] = synonym_name
        assert self.desc is not None or self.synonym_name is not None

        self.parent_names: Optional[List[str]] = parent_names

    @classmethod
    def register_phobia(cls, phobia: 'Phobia') -> None:
        """
        Register a phobia
        :param phobia: The phobia
        :return: Nothing
        """
        assert phobia.name not in [p.name for p in ALL_PHOBIAS]
        ALL_PHOBIAS.append(phobia)
