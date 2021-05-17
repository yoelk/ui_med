from enum import Enum


class Languages(Enum):
    """
    Supported allowed_languages names
    """
    ARAB = "ARAB"
    ENGLISH = "ENGLISH"
    HEBREW = "HEBREW"
    ITALIAN = "ITALIAN"

    DEFAULT = ENGLISH


class Orientations(object):
    """
    Orientations
    """

    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
