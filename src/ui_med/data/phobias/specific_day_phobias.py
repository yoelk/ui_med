from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class SpecificDayPhobias(Enum):
    """
    Specific Day phobias
    """


SpecificDayPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class SpecificDayPhobiasDescriptions(Enum):
    """
    Specific Day phobias descriptions
    """


SpecificDayPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
