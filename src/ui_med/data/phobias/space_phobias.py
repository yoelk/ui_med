from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class SpacePhobias(Enum):
    """
    Space phobias
    """


SpacePhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class SpacePhobiasDescriptions(Enum):
    """
    Space phobias descriptions
    """


SpacePhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
