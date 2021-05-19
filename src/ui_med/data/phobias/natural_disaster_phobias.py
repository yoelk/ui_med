from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class NaturalDisasterPhobias(Enum):
    """
    Natural Disaster phobias
    """


NaturalDisasterPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class NaturalDisasterPhobiasDescriptions(Enum):
    """
    Natural Disaster phobias descriptions
    """


NaturalDisasterPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
