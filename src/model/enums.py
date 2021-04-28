from enum import Enum


class Languages(Enum):
    """
    Supported allowed_languages names
    """
    ENGLISH = "ENGLISH"
    HEBREW = "HEBREW"
    ARAB = "ARAB"
    ITALIAN = "ITALIAN"

    DEFAULT = ENGLISH
