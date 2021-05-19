from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class PlanetPhobias(Enum):
    """
    Planet Phobias Names
    """
    ARISPHOBIA = auto()
    HAIWANGPHOBIA = auto()
    JINXIPHOBIA = auto()
    MUXIPHOBIA = auto()
    PLANITIPHOBIA = auto()
    SHUIXPHOBIA = auto()
    TENNOPHOBIA = auto()
    TERRAPHOBIA = auto()
    TUXIPHOBIA = auto()


PLANET_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    PlanetPhobias.ARISPHOBIA: {
        Languages.ENGLISH: "Arisphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobias.HAIWANGPHOBIA: {
        Languages.ENGLISH: "Haiwangphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobias.JINXIPHOBIA: {
        Languages.ENGLISH: "Jinxiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobias.MUXIPHOBIA: {
        Languages.ENGLISH: "Muxiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobias.PLANITIPHOBIA: {
        Languages.ENGLISH: "Planitiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobias.SHUIXPHOBIA: {
        Languages.ENGLISH: "Shuixphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobias.TENNOPHOBIA: {
        Languages.ENGLISH: "Tennophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobias.TERRAPHOBIA: {
        Languages.ENGLISH: "Terraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobias.TUXIPHOBIA: {
        Languages.ENGLISH: "Tuxiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class PlanetPhobiasDescriptions(Enum):
    """
    Planet Phobias Descriptions
    """
    ARISPHOBIA = auto()
    HAIWANGPHOBIA = auto()
    JINXIPHOBIA = auto()
    MUXIPHOBIA = auto()
    PLANITIPHOBIA = auto()
    SHUIXPHOBIA = auto()
    TENNOPHOBIA = auto()
    TERRAPHOBIA = auto()
    TUXIPHOBIA = auto()


PLANET_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    PlanetPhobiasDescriptions.ARISPHOBIA: {
        Languages.ENGLISH: "Fear of mars (branch of plantiphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobiasDescriptions.HAIWANGPHOBIA: {
        Languages.ENGLISH: "Fear of neptune (branch of planitiphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobiasDescriptions.JINXIPHOBIA: {
        Languages.ENGLISH: "Fear of venus (branch of planitiphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobiasDescriptions.MUXIPHOBIA: {
        Languages.ENGLISH: "Fear of jupiter (branch of planitiphobii)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobiasDescriptions.PLANITIPHOBIA: {
        Languages.ENGLISH: "Fear of planets",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobiasDescriptions.SHUIXPHOBIA: {
        Languages.ENGLISH: "Fear of mercury (branch of planitiphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobiasDescriptions.TENNOPHOBIA: {
        Languages.ENGLISH: "Fear of uranus (branch of planitiphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobiasDescriptions.TERRAPHOBIA: {
        Languages.ENGLISH: "Fear of earth (branch of planitiphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlanetPhobiasDescriptions.TUXIPHOBIA: {
        Languages.ENGLISH: "Fear of saturn (branch of planitiphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
