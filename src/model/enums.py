from enum import IntEnum, auto


class Languages(IntEnum):
    """
    Supported languages names
    """
    ENGLISH = auto()
    HEBREW = auto()
    ARAB = auto()
    ITALIAN = auto()

    @classmethod
    def default_language(cls) -> "Languages":
        """
        :return: The default language
        """
        return Languages.ENGLISH
