from src.model.enums import Languages
from src.std.singleton import Singleton

TEXT_WIDGET_HEIGHT: str = "50dp"
"""The height of a text field
"""

TEXT_FIELD_NAME_WIDTH: str = "300dp"
"""The width of a text field's name
"""


class Settings(object, metaclass=Singleton):
    """
    The settings
    """

    def __init__(self) -> None:
        """
        Initialize
        :return: Nothing
        """
        self.language: Languages = Languages.ENGLISH
