# -*- coding: utf-8 -*-
from typing import Dict, Optional

from ui_med.app_base import get_app, get_logger
from ui_med.model.enums import Languages, Texts


class Lang(object):
    """
    Support for different languages
    """

    TRANSLATIONS: Dict[str, Dict[Languages, Optional[str]]] = {
    }
    """
    Representations in different allowed_languages of strings in the system.
    It's a static key-value store of texts and their translations.
    """

    @classmethod
    def add_translation(
            cls, text: str,
            translations: Optional[Dict[Languages, Optional[str]]] = None) -> None:
        """
        Add a translation
        :param text: The text
        :param translations: The translations
        :return: Nothing
        """
        if text not in cls.TRANSLATIONS:
            cls.TRANSLATIONS[text] = translations if translations else {}

        else:
            get_logger().debug(f"More than one translation for {text}")

    @classmethod
    def to_str(cls, text: str, language: Optional[Languages] = None) -> str:
        """
        :param text: The text
        :param language: The language
        :return: The text in the required language
        """
        if text not in cls.TRANSLATIONS:
            cls.TRANSLATIONS[text] = {}

        if not language:
            language = get_app().get_cur_lang()

        if language in cls.TRANSLATIONS[text]:
            text = cls.TRANSLATIONS[text][language]

            # Reverse the characters' order if needed
            if language.is_rtl:
                text = text[::-1]

        return text
