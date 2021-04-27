from enum import Enum, IntEnum, auto
from typing import Dict, Optional, Union

from src.model.enums import Languages
from src.views.settings import Settings


class Texts(IntEnum):
    """
    Texts in the system
    """
    PEOPLE = auto()
    ADD_PERSON = auto()
    FIRST_NAMES = auto()
    LAST_NAMES = auto()
    FULL_NAME = auto()
    SAVE = auto()


LANGUAGE_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
    Languages.ENGLISH: {Languages.ENGLISH: "English",
                        Languages.HEBREW: None,
                        Languages.ARAB: None,
                        Languages.ITALIAN: None, },
    Languages.HEBREW: {Languages.ENGLISH: "Hebrew",
                       Languages.HEBREW: None,
                       Languages.ARAB: None,
                       Languages.ITALIAN: None, },
    Languages.ARAB: {Languages.ENGLISH: "Arab",
                     Languages.HEBREW: None,
                     Languages.ARAB: None,
                     Languages.ITALIAN: None, },
    Languages.ITALIAN: {Languages.ENGLISH: "Italian",
                        Languages.HEBREW: None,
                        Languages.ARAB: None,
                        Languages.ITALIAN: None, },
    Texts.PEOPLE: {Languages.ENGLISH: "People",
                   Languages.HEBREW: None,
                   Languages.ARAB: None,
                   Languages.ITALIAN: None, },
    Texts.ADD_PERSON: {Languages.ENGLISH: "Add Person",
                       Languages.HEBREW: None,
                       Languages.ARAB: None,
                       Languages.ITALIAN: None, },
    Texts.FIRST_NAMES: {Languages.ENGLISH: "First Names",
                        Languages.HEBREW: None,
                        Languages.ARAB: None,
                        Languages.ITALIAN: None, },
    Texts.LAST_NAMES: {Languages.ENGLISH: "Last Names",
                       Languages.HEBREW: None,
                       Languages.ARAB: None,
                       Languages.ITALIAN: None, },
    Texts.FULL_NAME: {Languages.ENGLISH: "Full name",
                      Languages.HEBREW: None,
                      Languages.ARAB: None,
                      Languages.ITALIAN: None, },
    Texts.SAVE: {Languages.ENGLISH: "Save",
                 Languages.HEBREW: None,
                 Languages.ARAB: None,
                 Languages.ITALIAN: None, },
}
"""
Representations in different languages of strings in the system.
It's a static key-value store of texts and their translations.
For enums, the key is the enum's name
"""


def get_str(text: Enum, language: Optional[Languages] = Settings().language) -> str:
    """
    :param text: A text
    :param language: The required language
    :return: the translation of the text
    """
    assert text in LANGUAGE_STRINGS, f"Missing language string: {text}"

    if language in LANGUAGE_STRINGS[text]:
        return LANGUAGE_STRINGS[text][language]

    else:
        assert Languages.default_language() in LANGUAGE_STRINGS[text]
        return LANGUAGE_STRINGS[text][Languages.default_language()]
