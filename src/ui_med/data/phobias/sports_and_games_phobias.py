from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class SportsAndGamesPhobias(Enum):
    """
    Sports and Games phobias
    """


SportsPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class SportsAndGamesPhobiasDescriptions(Enum):
    """
    Sports and Games phobias descriptions
    """


SportsPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
