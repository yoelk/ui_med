from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class PlanetPhobias(Enum):
    """
    Planet phobias
    """


PlanetPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class PlanetPhobiasDescriptions(Enum):
    """
    Planet phobias descriptions
    """


PlanetPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
