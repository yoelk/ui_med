from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class PunctuationMarksPhobias(Enum):
    """
    Punctuation Marks phobias
    """


PunctuationMarksPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class PunctuationMarksPhobiasDescriptions(Enum):
    """
    Punctuation Marks phobias descriptions
    """


PunctuationMarksPhobiasDescriptions_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },