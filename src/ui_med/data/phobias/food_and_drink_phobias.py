from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class FoodAndDrinkPhobias(Enum):
    """
    Food and Drink phobias
    """


FoodAndDrinkPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}


class FoodAndDrinkPhobiasDescriptions(Enum):
    """
    Food and Drink phobias descriptions
    """


FoodAndDrinkPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
}
# : {Languages.ENGLISH: "", Languages.HEBREW: None, Languages.ARAB: None, Languages.ITALIAN: None, },
