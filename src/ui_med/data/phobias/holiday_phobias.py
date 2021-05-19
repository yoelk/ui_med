from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class HolidayPhobias(Enum):
    """
    Holiday phobias
    """


HolidayPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class HolidayPhobiasDescriptions(Enum):
    """
    Holiday phobias descriptions
    """


HolidayPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
