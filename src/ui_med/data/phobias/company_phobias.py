from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class CompanyPhobias(Enum):
    """
    Company Phobias Names
    """
    AMAZONPHOBIA = auto()
    BANDCAMPHOBIA = auto()
    BEMANOPHOBIA = auto()
    BMWPHOBIA = auto()
    CHEVROLETPHOBIA = auto()
    COCAPHOBIA = auto()
    DISCORDPHOBIA = auto()
    DISNEYPHOBIA = auto()
    EBAYPHOBIA = auto()
    EARTHVIULAPHOBIA = auto()
    FACEBOOKPHOBIA = auto()
    LAZADAPHOBIA = auto()
    MICROSOFTPHOBIA = auto()
    SONYPHOBIA = auto()
    THX_PHOBIA = auto()
    TWITTERPHOBIA = auto()


COMPANY_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    CompanyPhobias.AMAZONPHOBIA: {
        Languages.ENGLISH: "Amazonphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.BANDCAMPHOBIA: {
        Languages.ENGLISH: "Bandcamphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.BEMANOPHOBIA: {
        Languages.ENGLISH: "Bemanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.BMWPHOBIA: {
        Languages.ENGLISH: "Bmwphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.CHEVROLETPHOBIA: {
        Languages.ENGLISH: "Chevroletphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.COCAPHOBIA: {
        Languages.ENGLISH: "Cocaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.DISCORDPHOBIA: {
        Languages.ENGLISH: "Discordphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.DISNEYPHOBIA: {
        Languages.ENGLISH: "Disneyphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.EBAYPHOBIA: {
        Languages.ENGLISH: "Ebayphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.EARTHVIULAPHOBIA: {
        Languages.ENGLISH: "Earthviulaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.FACEBOOKPHOBIA: {
        Languages.ENGLISH: "Facebookphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.LAZADAPHOBIA: {
        Languages.ENGLISH: "Lazadaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.MICROSOFTPHOBIA: {
        Languages.ENGLISH: "Microsoftphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.SONYPHOBIA: {
        Languages.ENGLISH: "Sonyphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.THX_PHOBIA: {
        Languages.ENGLISH: "Thx Phobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobias.TWITTERPHOBIA: {
        Languages.ENGLISH: "Twitterphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class CompanyPhobiasDescriptions(Enum):
    """
    Company Phobias Descriptions
    """
    AMAZONPHOBIA = auto()
    BANDCAMPHOBIA = auto()
    BEMANOPHOBIA = auto()
    BMWPHOBIA = auto()
    CHEVROLETPHOBIA = auto()
    COCAPHOBIA = auto()
    DISCORDPHOBIA = auto()
    DISNEYPHOBIA = auto()
    EBAYPHOBIA = auto()
    EARTHVIULAPHOBIA = auto()
    FACEBOOKPHOBIA = auto()
    LAZADAPHOBIA = auto()
    MICROSOFTPHOBIA = auto()
    SONYPHOBIA = auto()
    THX_PHOBIA = auto()
    TWITTERPHOBIA = auto()


COMPANY_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    CompanyPhobiasDescriptions.AMAZONPHOBIA: {
        Languages.ENGLISH: "Fear of amazon",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.BANDCAMPHOBIA: {
        Languages.ENGLISH: "Fear of bandcamp",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.BEMANOPHOBIA: {
        Languages.ENGLISH: "Fear of bemani",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.BMWPHOBIA: {
        Languages.ENGLISH: "Fear of bmw",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.CHEVROLETPHOBIA: {
        Languages.ENGLISH: "Fear of chevrolet",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.COCAPHOBIA: {
        Languages.ENGLISH: "Fear of coca cola (branch of dipsophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.DISCORDPHOBIA: {
        Languages.ENGLISH: "Fear of discord",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.DISNEYPHOBIA: {
        Languages.ENGLISH: "Fear of the walt disney company",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.EBAYPHOBIA: {
        Languages.ENGLISH: "Fear of ebay",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.EARTHVIULAPHOBIA: {
        Languages.ENGLISH: "Fear of google earth (branch of googlephobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.FACEBOOKPHOBIA: {
        Languages.ENGLISH: "Fear of facebook",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.LAZADAPHOBIA: {
        Languages.ENGLISH: "Fear of lazada",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.MICROSOFTPHOBIA: {
        Languages.ENGLISH: "Fear of microsoft",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.SONYPHOBIA: {
        Languages.ENGLISH: "Fear of sony",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.THX_PHOBIA: {
        Languages.ENGLISH: "Fear of thx",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    CompanyPhobiasDescriptions.TWITTERPHOBIA: {
        Languages.ENGLISH: "Fear of twitter",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
