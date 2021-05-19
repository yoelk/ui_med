from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class WeatherPhobias(Enum):
    """
    Weather phobias
    """


WeatherPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class WeatherPhobiasDescriptions(Enum):
    """
    Weather phobias descriptions
    """


WeatherPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
