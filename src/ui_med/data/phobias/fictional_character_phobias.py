from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class FictionalCharacterPhobias(Enum):
    """
    Fictional Character phobias
    """

FictionalCharacterPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}

class FictionalCharacterPhobiasDescriptions(Enum):
    """
    Fictional Character phobias descriptions
    """

FictionalCharacterPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },