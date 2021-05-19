from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class VehiclePhobias(Enum):
    """
    Vehicle phobias
    """


VehiclePhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class VehiclePhobiasDescriptions(Enum):
    """
    Vehicle phobias descriptions
    """


VehiclePhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
