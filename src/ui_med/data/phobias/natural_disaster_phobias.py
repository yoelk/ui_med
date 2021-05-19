from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class NaturalDisasterPhobias(Enum):
    """
    Natural Disaster Phobias Names
    """
    ANTLOPHOBIA = auto()
    ARIDITAPHOBIA = auto()
    AGRIPYROPHOBIA = auto()
    CHIONOKATAIPHOBIA = auto()
    CHIONOTHYELLAPHOBIA = auto()
    CYCLONOPHOBIA = auto()
    DERECHOPHOBIA = auto()
    LILAPSOPHOBIA = auto()
    NIVISPHOBIA = auto()
    SEISMOPHOBIA = auto()
    TURBOPHOBIA = auto()
    TSUNAMIPHOBIA = auto()
    VOLCANOPHOBIA = auto()


NATURAL_DISASTER_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    NaturalDisasterPhobias.ANTLOPHOBIA: {
        Languages.ENGLISH: "Antlophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobias.ARIDITAPHOBIA: {
        Languages.ENGLISH: "Ariditaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobias.AGRIPYROPHOBIA: {
        Languages.ENGLISH: "Agripyrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobias.CHIONOKATAIPHOBIA: {
        Languages.ENGLISH: "Chionokataiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobias.CHIONOTHYELLAPHOBIA: {
        Languages.ENGLISH: "Chionothyellaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobias.CYCLONOPHOBIA: {
        Languages.ENGLISH: "Cyclonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobias.DERECHOPHOBIA: {
        Languages.ENGLISH: "Derechophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobias.LILAPSOPHOBIA: {
        Languages.ENGLISH: "Lilapsophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobias.NIVISPHOBIA: {
        Languages.ENGLISH: "Nivisphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobias.SEISMOPHOBIA: {
        Languages.ENGLISH: "Seismophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobias.TURBOPHOBIA: {
        Languages.ENGLISH: "Turbophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobias.TSUNAMIPHOBIA: {
        Languages.ENGLISH: "Tsunamiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobias.VOLCANOPHOBIA: {
        Languages.ENGLISH: "Volcanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class NaturalDisasterPhobiasDescriptions(Enum):
    """
    Natural Disaster Phobias Descriptions
    """
    ANTLOPHOBIA = auto()
    ARIDITAPHOBIA = auto()
    AGRIPYROPHOBIA = auto()
    CHIONOKATAIPHOBIA = auto()
    CHIONOTHYELLAPHOBIA = auto()
    CYCLONOPHOBIA = auto()
    DERECHOPHOBIA = auto()
    LILAPSOPHOBIA = auto()
    NIVISPHOBIA = auto()
    SEISMOPHOBIA = auto()
    TURBOPHOBIA = auto()
    TSUNAMIPHOBIA = auto()
    VOLCANOPHOBIA = auto()


NATURAL_DISASTER_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    NaturalDisasterPhobiasDescriptions.ANTLOPHOBIA: {
        Languages.ENGLISH: "Fear of flooding",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobiasDescriptions.ARIDITAPHOBIA: {
        Languages.ENGLISH: "Fear of droughts",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobiasDescriptions.AGRIPYROPHOBIA: {
        Languages.ENGLISH: "Fear of wildfires (branch of pyrophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobiasDescriptions.CHIONOKATAIPHOBIA: {
        Languages.ENGLISH: "Fear of ice storms",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobiasDescriptions.CHIONOTHYELLAPHOBIA: {
        Languages.ENGLISH: "Fear of blizzards (branch of chionophobia & tempestaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobiasDescriptions.CYCLONOPHOBIA: {
        Languages.ENGLISH: "Fear of tropical cyclones (satellite of lilapsophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobiasDescriptions.DERECHOPHOBIA: {
        Languages.ENGLISH: "Fear of drechos",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobiasDescriptions.LILAPSOPHOBIA: {
        Languages.ENGLISH: "Fear of tornadoes (turbophobia) and tropical cyclones (cyclonophobia) (branch of tempestaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobiasDescriptions.NIVISPHOBIA: {
        Languages.ENGLISH: "Fear of avalanches (branch of chionophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobiasDescriptions.SEISMOPHOBIA: {
        Languages.ENGLISH: "Fear of earthquake",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobiasDescriptions.TURBOPHOBIA: {
        Languages.ENGLISH: "Fear of tornadoes (branch of lilapsophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobiasDescriptions.TSUNAMIPHOBIA: {
        Languages.ENGLISH: "Fear of tsunamis",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    NaturalDisasterPhobiasDescriptions.VOLCANOPHOBIA: {
        Languages.ENGLISH: "Fear of volcanos",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
