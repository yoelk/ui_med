from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class FictionalPhobias(Enum):
    """
    Fictional phobias
    """


FictionalPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class FictionalPhobiasDescriptions(Enum):
    """
    Fictional phobias descriptions
    """


FictionalPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
