from typing import Dict, Optional

from ui_med.app_base import get_app
from ui_med.model.enums import Languages


# TODO(joel): Encapsulate this file's contents in a class

class Texts(object):
    """
    Texts in the system
    """
    ADD_PHOBIA = "Add Phobia"
    ADD_NAME = "Add Name"
    ADD_PERSON = "Add Person"
    BACK = "Back"
    DELETE = "Delete"
    EDIT = "Edit"
    FIRST_NAMES = "First Names"
    FULL_NAME = "Full Name"
    LAST_NAMES = "Last Names"
    NAMES = "Names"
    PEOPLE = "People"
    PHOBIAS = "Phobias"
    SAVE = "Save"


TRANSLATIONS: Dict[str, Dict[Languages, Optional[str]]] = {
    Languages.ARAB.value: {},
    Languages.ENGLISH.value: {},
    Languages.HEBREW.value: {},
    Languages.ITALIAN.value: {},

    Texts.ADD_PHOBIA: {},
    Texts.ADD_NAME: {},
    Texts.ADD_PERSON: {},
    Texts.BACK: {},
    Texts.DELETE: {},
    Texts.EDIT: {},
    Texts.FIRST_NAMES: {},
    Texts.FULL_NAME: {},
    Texts.LAST_NAMES: {},
    Texts.NAMES: {},
    Texts.PEOPLE: {},
    Texts.PHOBIAS: {},
    Texts.SAVE: {},
}
"""
Representations in different allowed_languages of strings in the system.
It's a static key-value store of texts and their translations.
"""


def add_translation(
        text: str, translations: Optional[Dict[Languages, Optional[str]]] = None) -> None:
    """
    Add a translation
    :param text: The text
    :param translations: The translations
    :return: Nothing
    """
    assert text not in TRANSLATIONS, f"Translation already exists for {text}"
    TRANSLATIONS[text] = translations if translations else {}


def to_str(text: str, language: Optional[Languages] = None) -> str:
    """
    :param text: The text
    :param language: The language
    :return: The text in the required language
    """
    assert text in TRANSLATIONS, f"Missing language string: {text}"

    if not language:
        language = get_app().get_cur_lang()
    if language in TRANSLATIONS[text]:
        return TRANSLATIONS[text][language]

    else:
        return text
