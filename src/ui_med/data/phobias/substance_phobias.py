from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class SubstancePhobias(Enum):
    """
    Substance phobias
    """


SubstancePhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class SubstancePhobiasDescriptions(Enum):
    """
    Substance phobias descriptions
    """


SubstancePhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
