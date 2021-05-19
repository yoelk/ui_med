from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class LettersPhobias(Enum):
    """
    Letters phobias
    """


LettersPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class LettersPhobiasDescriptions(Enum):
    """
    Letters phobias descriptions
    """


LettersPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
