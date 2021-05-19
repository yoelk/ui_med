from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class OtherPhobias(Enum):
    """
    Other phobias
    """


OtherPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class OtherPhobiasDescriptions(Enum):
    """
    Other phobias descriptions
    """


OtherPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
