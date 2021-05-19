from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class ThingsPhobias(Enum):
    """
    Things phobias
    """


ThingsPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class ThingsPhobiasDescriptions(Enum):
    """
    Things phobias descriptions
    """


ThingsPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
