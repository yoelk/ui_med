from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class CompanyPhobias(Enum):
    """
    Company phobias
    """


CompanyPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class CompanyPhobiasDescriptions(Enum):
    """
    Company phobias descriptions
    """


CompanyPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
