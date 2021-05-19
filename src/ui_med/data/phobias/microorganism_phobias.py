from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class MicroorganismPhobias(Enum):
    """
    Microorganism phobias
    """
    ANOPHELIPHOBIA = auto()
    BACILLOPHOBIA = auto()
    BACTERIOPHOBIA = auto()
    CHOLEROPHOBIA = auto()
    EBOLAPHOBIA = auto()
    MICROBIOPHOBIA = auto()
    VERMINOPHOBIA = auto()
    VIROPHOBIA = auto()


MicroorganismPhobias_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
    MicroorganismPhobias.ANOPHELIPHOBIA: {
        Languages.ENGLISH: "Anopheliphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobias.BACILLOPHOBIA: {
        Languages.ENGLISH: "Bacillophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobias.BACTERIOPHOBIA: {
        Languages.ENGLISH: "Bacteriophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobias.CHOLEROPHOBIA: {
        Languages.ENGLISH: "Cholerophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobias.EBOLAPHOBIA: {
        Languages.ENGLISH: "Ebolaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobias.MICROBIOPHOBIA: {
        Languages.ENGLISH: "Microbiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobias.VERMINOPHOBIA: {
        Languages.ENGLISH: "Verminophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobias.VIROPHOBIA: {
        Languages.ENGLISH: "Virophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class MicroorganismPhobiasDescriptions(Enum):
    """
    Microorganism phobias descriptions
    """
    ANOPHELIPHOBIA = auto()
    BACILLOPHOBIA = auto()
    BACTERIOPHOBIA = auto()
    CHOLEROPHOBIA = auto()
    EBOLAPHOBIA = auto()
    MICROBIOPHOBIA = auto()
    VERMINOPHOBIA = auto()
    VIROPHOBIA = auto()


MicroorganismPhobiasDescriptions_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
    MicroorganismPhobiasDescriptions.ANOPHELIPHOBIA: {
        Languages.ENGLISH: "fear of malaria (branch of micobiophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobiasDescriptions.BACILLOPHOBIA: {
        Languages.ENGLISH: "fear of bacillus (branch of microbiophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobiasDescriptions.BACTERIOPHOBIA: {
        Languages.ENGLISH: "fear of bacteria (branch of microbiophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobiasDescriptions.CHOLEROPHOBIA: {
        Languages.ENGLISH: "fear of Vibreo cholerae (the bacteria that causes cholera) (branch of microbiophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobiasDescriptions.EBOLAPHOBIA: {
        Languages.ENGLISH: "fear of the Ebola Virus (branch of virophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobiasDescriptions.MICROBIOPHOBIA: {
        Languages.ENGLISH: "fear of micro-organisms (branch of pantophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobiasDescriptions.VERMINOPHOBIA: {
        Languages.ENGLISH: "fear of germs (branch of microbiophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MicroorganismPhobiasDescriptions.VIROPHOBIA: {
        Languages.ENGLISH: "fear of viruses (not the ones on computers) (branch of microbiophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
