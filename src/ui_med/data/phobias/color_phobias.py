from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class ColorPhobias(Enum):
    """
    Color Phobias Names
    """
    AUROPHOBIA = auto()
    CHROMOPHOBIA = auto()
    CHRYSOPHOBIA = auto()
    CYANOPHOBIA = auto()
    ERYTHROPHOBIA = auto()
    GLAUCOPHOBIA = auto()
    KASTANOPHOBIA = auto()
    LEUKOPHOBIA = auto()
    MELANOPHOBIA = auto()
    PERSICOPHOBIA = auto()
    PORPHYROPHOBIA = auto()
    PRASINOPHOBIA = auto()
    RHODOPHOBIA = auto()
    XANTHOPHOBIA = auto()


COLOR_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    ColorPhobias.AUROPHOBIA: {
        Languages.ENGLISH: "Aurophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobias.CHROMOPHOBIA: {
        Languages.ENGLISH: "Chromophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobias.CHRYSOPHOBIA: {
        Languages.ENGLISH: "Chrysophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobias.CYANOPHOBIA: {
        Languages.ENGLISH: "Cyanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobias.ERYTHROPHOBIA: {
        Languages.ENGLISH: "Erythrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobias.GLAUCOPHOBIA: {
        Languages.ENGLISH: "Glaucophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobias.KASTANOPHOBIA: {
        Languages.ENGLISH: "Kastanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobias.LEUKOPHOBIA: {
        Languages.ENGLISH: "Leukophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobias.MELANOPHOBIA: {
        Languages.ENGLISH: "Melanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobias.PERSICOPHOBIA: {
        Languages.ENGLISH: "Persicophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobias.PORPHYROPHOBIA: {
        Languages.ENGLISH: "Porphyrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobias.PRASINOPHOBIA: {
        Languages.ENGLISH: "Prasinophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobias.RHODOPHOBIA: {
        Languages.ENGLISH: "Rhodophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobias.XANTHOPHOBIA: {
        Languages.ENGLISH: "Xanthophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class ColorPhobiasDescriptions(Enum):
    """
    Color Phobias Descriptions
    """
    AUROPHOBIA = auto()
    CHROMOPHOBIA = auto()
    CHRYSOPHOBIA = auto()
    CYANOPHOBIA = auto()
    ERYTHROPHOBIA = auto()
    GLAUCOPHOBIA = auto()
    KASTANOPHOBIA = auto()
    LEUKOPHOBIA = auto()
    MELANOPHOBIA = auto()
    PERSICOPHOBIA = auto()
    PORPHYROPHOBIA = auto()
    PRASINOPHOBIA = auto()
    RHODOPHOBIA = auto()
    XANTHOPHOBIA = auto()


COLOR_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    ColorPhobiasDescriptions.AUROPHOBIA: {
        Languages.ENGLISH: "Fear of gold (branch of chromophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobiasDescriptions.CHROMOPHOBIA: {
        Languages.ENGLISH: "Fear of colors (not to be confused with chronophobia, fear of not having enough time)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobiasDescriptions.CHRYSOPHOBIA: {
        Languages.ENGLISH: "Fear of orange (branch of chromophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobiasDescriptions.CYANOPHOBIA: {
        Languages.ENGLISH: "Fear of blue (branch of chromophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobiasDescriptions.ERYTHROPHOBIA: {
        Languages.ENGLISH: "Fear of red (branch of chromophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobiasDescriptions.GLAUCOPHOBIA: {
        Languages.ENGLISH: "Fear of gray (branch of chromophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobiasDescriptions.KASTANOPHOBIA: {
        Languages.ENGLISH: "Fear of brown (branch of chromophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobiasDescriptions.LEUKOPHOBIA: {
        Languages.ENGLISH: "Fear of white (branch of chromophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobiasDescriptions.MELANOPHOBIA: {
        Languages.ENGLISH: "Fear of black (branch of chromophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobiasDescriptions.PERSICOPHOBIA: {
        Languages.ENGLISH: "Fear of peach (branch of chromophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobiasDescriptions.PORPHYROPHOBIA: {
        Languages.ENGLISH: "Fear of purple (branch of chromophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobiasDescriptions.PRASINOPHOBIA: {
        Languages.ENGLISH: "Fear of green (branch of chromophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobiasDescriptions.RHODOPHOBIA: {
        Languages.ENGLISH: "Fear of pink (branch of chromophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ColorPhobiasDescriptions.XANTHOPHOBIA: {
        Languages.ENGLISH: "Fear of yellow (branch of chromophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
