from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class NumericalPhobias(Enum):
    """
    Numerical phobias
    """


NumericalPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class NumericalPhobiasDescriptions(Enum):
    """
    Numerical phobias descriptions
    """


NumericalPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
