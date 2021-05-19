from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class WordPhobias(Enum):
    """
    Word phobias
    """


WordPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class WordPhobiasDescriptions(Enum):
    """
    Word phobias descriptions
    """


WordPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
