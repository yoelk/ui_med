from enum import Enum
from typing import Dict, Optional

from src.app_base import get_app
from src.model.enums import Languages


class Texts(Enum):
    """
    Texts in the system
    """
    PEOPLE = "PEOPLE"
    ADD_PERSON = "ADD_PERSON"
    FIRST_NAMES = "FIRST_NAMES"
    LAST_NAMES = "LAST_NAMES"
    FULL_NAME = "FULL_NAME"
    SAVE = "SAVE"
    NAMES = "NAMES"
    ADD_NAME = "ADD_NAME"


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
    Texts.NAMES: {Languages.ENGLISH: "Names",
                  Languages.HEBREW: None,
                  Languages.ARAB: None,
                  Languages.ITALIAN: None, },
    Texts.ADD_NAME: {Languages.ENGLISH: "Add Name",
                     Languages.HEBREW: None,
                     Languages.ARAB: None,
                     Languages.ITALIAN: None, },
}
"""
Representations in different allowed_languages of strings in the system.
It's a static key-value store of texts and their translations.
For enums, the key is the enum's name
"""


def get_str(text: Enum, language: Optional[Languages] = None) -> str:
    """
    :param text: A text
    :param language: The required language
    :return: the translation of the text
    """
    assert text in LANGUAGE_STRINGS, f"Missing language string: {text}"

    if not language:
        language = get_app().get_cur_lang()
    if language in LANGUAGE_STRINGS[text]:
        return LANGUAGE_STRINGS[text][language]

    else:
        assert Languages.DEFAULT in LANGUAGE_STRINGS[text]
        return LANGUAGE_STRINGS[text][Languages.DEFAULT]
