from typing import List, Optional

from ui_med.model.enums import PhobiaTypes
from ui_med.model.languages import add_translation
from ui_med.model.phobias import Phobia
from ui_med.std.enum import enum_names


class PhobiaEntry(object):
    """
    A phobia entry
    """

    def __init__(self) -> None:
        """
        Initialize
        :return: Nothing
        """
        self.name: Optional[str] = None
        self.desc: Optional[str] = None
        self.synonym: Optional[str] = None
        self.parents: Optional[List[str]] = None


class PhobiasExtractor(object):
    """
    Extract data about phobias
    """

    @classmethod
    def get_phobia_type_from_line(cls, line: str) -> Optional[PhobiaTypes]:
        """
        :param line: The line
        :return: The stated phobia type if possible, else None
        """
        phobia_type_str: str = "phobia_type"
        if phobia_type_str not in line:
            return None

        phobia_type_name: str = line.split(f"{phobia_type_str}=")[1]
        assert phobia_type_name in enum_names(PhobiaTypes)
        return PhobiaTypes[phobia_type_name]

    @classmethod
    def parse_phobia_line(cls, line: str) -> Phobia:
        """
        Parse an phobia line
        :param line: The line
        :return: The parsed phobia
        """

        def get_value(txt: str) -> str:
            return txt.split('=')[1].strip('"')

        parts: List[str] = line.split("; ")
        name: Optional[str] = None
        desc: Optional[str] = None
        synonym_name: Optional[str] = None
        parent_names: Optional[List[str]] = None
        phobia_types: Optional[List[PhobiaTypes]] = None
        for part in parts:
            if part.startswith("name="):
                assert name is None, "More than one name"
                name = get_value(part).title()

            if part.startswith("desc="):
                assert desc is None, "More than one description"
                desc = get_value(part).capitalize()

            if part.startswith("synonym="):
                assert synonym_name is None, "More than one synonym"
                synonym_name = get_value(part).title()

            if part.startswith("parents="):
                assert parent_names is None, "More than one parent_names"
                parent_names = eval(get_value(part))
                assert isinstance(parent_names, list)

            if part.startswith("phobia_types="):
                assert phobia_types is None, "More than one phobia_types"
                phobia_types_names: List[str] = eval(get_value(part))
                phobia_types = [PhobiaTypes[name] for name in phobia_types_names]
                assert isinstance(phobia_types, list)

        return Phobia(phobia_types=phobia_types, name=name, desc=desc,
                      synonym_name=synonym_name, parent_names=parent_names)

    @classmethod
    def extract_entry(cls, line: str) -> None:
        """
        Extract an entry
        :param line: The line
        :param phobia_type: The phobia type
        :return: Nothing
        """
        phobia = cls.parse_phobia_line(line=line)
        Phobia.register_phobia(phobia=phobia)
        add_translation(text=f"{phobia.name}")
        if phobia.desc:
            add_translation(text=f"{phobia.desc}")

    @classmethod
    def extract(cls, phobias_file_path: str) -> None:
        """
        Extract the data
        :param phobias_file_path: The phobias text file path
        :return: Nothing
        """
        with open(phobias_file_path, "r", encoding="utf-8") as fh:
            lines: List[str] = fh.read().split('\n')

        for line in lines:
            line = line.strip(" ")

            # Skip empty lines
            if not line:
                continue

            cls.extract_entry(line=line)
