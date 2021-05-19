from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class StarPhobias(Enum):
    """
    Star Phobias Names
    """
    SIRIUSPHOBIA = auto()
    HIP_13044PHOBIA = auto()
    HD_140283PHOBIA = auto()
    HE_1327-2326PHOBIA = auto()
    HD_224693PHOBIA = auto()


STAR_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    StarPhobias.SIRIUSPHOBIA: {
        Languages.ENGLISH: "Siriusphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    StarPhobias.HIP_13044PHOBIA: {
        Languages.ENGLISH: "Hip 13044Phobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    StarPhobias.HD_140283PHOBIA: {
        Languages.ENGLISH: "Hd 140283Phobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    StarPhobias.HE_1327-2326PHOBIA: {
        Languages.ENGLISH: "He 1327-2326Phobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    StarPhobias.HD_224693PHOBIA: {
        Languages.ENGLISH: "Hd 224693Phobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class StarPhobiasDescriptions(Enum):
    """
    Star Phobias Descriptions
    """
    SIRIUSPHOBIA = auto()
    HIP_13044PHOBIA = auto()
    HD_140283PHOBIA = auto()
    HE_1327-2326PHOBIA = auto()
    HD_224693PHOBIA = auto()


STAR_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    StarPhobiasDescriptions.SIRIUSPHOBIA: {
        Languages.ENGLISH: "Fear of star sirius",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    StarPhobiasDescriptions.HIP_13044PHOBIA: {
        Languages.ENGLISH: "Fear of star hip 13044",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    StarPhobiasDescriptions.HD_140283PHOBIA: {
        Languages.ENGLISH: "Fear of star hd 140283",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    StarPhobiasDescriptions.HE_1327-2326PHOBIA: {
        Languages.ENGLISH: "Fear of star he 1327-2326",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    StarPhobiasDescriptions.HD_224693PHOBIA: {
        Languages.ENGLISH: "Fear of star hd 224693",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
