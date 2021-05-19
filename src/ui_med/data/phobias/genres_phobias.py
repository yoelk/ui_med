from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class GenresPhobias(Enum):
    """
    Genres phobias
    """


GenresPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class GenresPhobiasDescriptions(Enum):
    """
    Genres phobias descriptions
    """


GenresPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },