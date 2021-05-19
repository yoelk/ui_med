from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class SpecificDayPhobias(Enum):
    """
    Specific Day Phobias Names
    """
    ALPIPHOBIA = auto()
    ALPBIROPHOBIA = auto()
    ALPEKOPHOBIA = auto()
    ALPUSOPHOBIA = auto()
    ALPTORTPHOBIA = auto()
    ALPSIKOPHOBIA = auto()


SPECIFIC_DAY_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    SpecificDayPhobias.ALPIPHOBIA: {
        Languages.ENGLISH: "Alpiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    SpecificDayPhobias.ALPBIROPHOBIA: {
        Languages.ENGLISH: "Alpbirophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    SpecificDayPhobias.ALPEKOPHOBIA: {
        Languages.ENGLISH: "Alpekophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    SpecificDayPhobias.ALPUSOPHOBIA: {
        Languages.ENGLISH: "Alpusophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    SpecificDayPhobias.ALPTORTPHOBIA: {
        Languages.ENGLISH: "Alptortphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    SpecificDayPhobias.ALPSIKOPHOBIA: {
        Languages.ENGLISH: "Alpsikophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class SpecificDayPhobiasDescriptions(Enum):
    """
    Specific Day Phobias Descriptions
    """
    ALPIPHOBIA = auto()
    ALPBIROPHOBIA = auto()
    ALPEKOPHOBIA = auto()
    ALPUSOPHOBIA = auto()
    ALPTORTPHOBIA = auto()
    ALPSIKOPHOBIA = auto()


SPECIFIC_DAY_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    SpecificDayPhobiasDescriptions.ALPIPHOBIA: {
        Languages.ENGLISH: "Fear of march 1st",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    SpecificDayPhobiasDescriptions.ALPBIROPHOBIA: {
        Languages.ENGLISH: "Fear of march 2nd",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    SpecificDayPhobiasDescriptions.ALPEKOPHOBIA: {
        Languages.ENGLISH: "Fear of march 3rd",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    SpecificDayPhobiasDescriptions.ALPUSOPHOBIA: {
        Languages.ENGLISH: "Fear of march 4th",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    SpecificDayPhobiasDescriptions.ALPTORTPHOBIA: {
        Languages.ENGLISH: "Fear of march 5th",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    SpecificDayPhobiasDescriptions.ALPSIKOPHOBIA: {
        Languages.ENGLISH: "Fear of march 6th",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
