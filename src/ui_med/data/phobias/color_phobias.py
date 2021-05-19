from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class ColorPhobias(Enum):
    """
    Color phobias
    """

ColorPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}



class ColorPhobiasDescriptions(Enum):
    """
    Color phobias descriptions
    """

ColorPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
