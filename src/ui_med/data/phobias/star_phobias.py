from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class StarPhobias(Enum):
    """
    Star phobias
    """


StarPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class StarPhobiasDescriptions(Enum):
    """
    Star phobias descriptions
    """


StarPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
