from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class HolidayPhobias(Enum):
    """
    Holiday Phobias Names
    """
    CHRISTOUGENNIATIKOPHOBIA = auto()
    ERGASIAEMARPHOBIA = auto()
    GRATIAROPHOBIA = auto()
    HEORTOPHOBIA = auto()
    IMERATOUPATERAPHOBIA = auto()
    INASTIOPHOBIA = auto()
    LIBERTATOPHOBIA = auto()
    NATREDEMPHOBIA = auto()
    NEOANNOPHOBIA = auto()
    PASCHAPHOBIA = auto()
    PATRICOPHOBIA = auto()
    PROTAPRILIAPHOBIA = auto()
    SAMHAINOPHOBIA = auto()
    VALENTINOPHOBIA = auto()
    CARNIVALPHOBIA = auto()


HOLIDAY_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    HolidayPhobias.CHRISTOUGENNIATIKOPHOBIA: {
        Languages.ENGLISH: "Christougenniatikophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.ERGASIAEMARPHOBIA: {
        Languages.ENGLISH: "Ergasiaemarphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.GRATIAROPHOBIA: {
        Languages.ENGLISH: "Gratiarophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.HEORTOPHOBIA: {
        Languages.ENGLISH: "Heortophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.IMERATOUPATERAPHOBIA: {
        Languages.ENGLISH: "Imeratoupateraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.INASTIOPHOBIA: {
        Languages.ENGLISH: "Inastiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.LIBERTATOPHOBIA: {
        Languages.ENGLISH: "Libertatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.NATREDEMPHOBIA: {
        Languages.ENGLISH: "Natredemphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.NEOANNOPHOBIA: {
        Languages.ENGLISH: "Neoannophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.PASCHAPHOBIA: {
        Languages.ENGLISH: "Paschaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.PATRICOPHOBIA: {
        Languages.ENGLISH: "Patricophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.PROTAPRILIAPHOBIA: {
        Languages.ENGLISH: "Protapriliaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.SAMHAINOPHOBIA: {
        Languages.ENGLISH: "Samhainophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.VALENTINOPHOBIA: {
        Languages.ENGLISH: "Valentinophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobias.CARNIVALPHOBIA: {
        Languages.ENGLISH: "Carnivalphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class HolidayPhobiasDescriptions(Enum):
    """
    Holiday Phobias Descriptions
    """
    CHRISTOUGENNIATIKOPHOBIA = auto()
    ERGASIAEMARPHOBIA = auto()
    GRATIAROPHOBIA = auto()
    HEORTOPHOBIA = auto()
    IMERATOUPATERAPHOBIA = auto()
    INASTIOPHOBIA = auto()
    LIBERTATOPHOBIA = auto()
    NATREDEMPHOBIA = auto()
    NEOANNOPHOBIA = auto()
    PASCHAPHOBIA = auto()
    PATRICOPHOBIA = auto()
    PROTAPRILIAPHOBIA = auto()
    SAMHAINOPHOBIA = auto()
    VALENTINOPHOBIA = auto()
    CARNIVALPHOBIA = auto()


HOLIDAY_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    HolidayPhobiasDescriptions.CHRISTOUGENNIATIKOPHOBIA: {
        Languages.ENGLISH: "Fear of christmas (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.ERGASIAEMARPHOBIA: {
        Languages.ENGLISH: "Fear of labor day (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.GRATIAROPHOBIA: {
        Languages.ENGLISH: "Fear of thanksgiving (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.HEORTOPHOBIA: {
        Languages.ENGLISH: "Fear of [celebrating events]",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.IMERATOUPATERAPHOBIA: {
        Languages.ENGLISH: "Fear of father's day (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.INASTIOPHOBIA: {
        Languages.ENGLISH: "Fear of crackers on the keyboard day (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.LIBERTATOPHOBIA: {
        Languages.ENGLISH: "Fear of independence day (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.NATREDEMPHOBIA: {
        Languages.ENGLISH: "Fear of mother's day (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.NEOANNOPHOBIA: {
        Languages.ENGLISH: "Fear of new year (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.PASCHAPHOBIA: {
        Languages.ENGLISH: "Fear of easter (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.PATRICOPHOBIA: {
        Languages.ENGLISH: "Fear of st. patrick's (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.PROTAPRILIAPHOBIA: {
        Languages.ENGLISH: "Fear of april fools' day (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.SAMHAINOPHOBIA: {
        Languages.ENGLISH: "Fear of halloween (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.VALENTINOPHOBIA: {
        Languages.ENGLISH: "Fear of valentine's (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    HolidayPhobiasDescriptions.CARNIVALPHOBIA: {
        Languages.ENGLISH: "Fear of fairs or mardi gras festivities (branch of heortophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
