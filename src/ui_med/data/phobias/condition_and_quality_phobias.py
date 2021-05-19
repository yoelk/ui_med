from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class ConditionAndQualityPhobias(Enum):
    """
    Condition and Quality phobias
    """


ConditionAndQualityPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class ConditionAndQualityPhobiasDescriptions(Enum):
    """
    Condition and Quality phobias descriptions
    """


ConditionAndQualityPhobiasDescriptions_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
