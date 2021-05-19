from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class MoviesAndTvPhobias(Enum):
    """
    Movies and TV phobias
    """


MoviesAndTvPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class MoviesAndTvPhobiasDescriptions(Enum):
    """
    Movies and TV phobias descriptions
    """


MoviesAndTvPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
