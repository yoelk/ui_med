from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class PunctuationMarkPhobias(Enum):
    """
    Punctuation Mark Phobias Names
    """
    ~PHOBIA = auto()
    ANTICURLYBRACKETOPHOBIA = auto()
    BINDAPHOBIA = auto()
    EROTIMATIKOPHOBIA = auto()
    HEITOPHOBIA = auto()
    PISTAPHOBIA = auto()
    THAUMASTIKAPHOBIA = auto()
    VIRGUPHOBIA = auto()
    COLOPHOBIA = auto()


PUNCTUATION_MARK_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    PunctuationMarkPhobias.~PHOBIA: {
        Languages.ENGLISH: "~Phobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobias.ANTICURLYBRACKETOPHOBIA: {
        Languages.ENGLISH: "Anticurlybracketophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobias.BINDAPHOBIA: {
        Languages.ENGLISH: "Bindaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobias.EROTIMATIKOPHOBIA: {
        Languages.ENGLISH: "Erotimatikophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobias.HEITOPHOBIA: {
        Languages.ENGLISH: "Heitophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobias.PISTAPHOBIA: {
        Languages.ENGLISH: "Pistaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobias.THAUMASTIKAPHOBIA: {
        Languages.ENGLISH: "Thaumastikaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobias.VIRGUPHOBIA: {
        Languages.ENGLISH: "Virguphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobias.COLOPHOBIA: {
        Languages.ENGLISH: "Colophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class PunctuationMarkPhobiasDescriptions(Enum):
    """
    Punctuation Mark Phobias Descriptions
    """
    ~PHOBIA = auto()
    ANTICURLYBRACKETOPHOBIA = auto()
    BINDAPHOBIA = auto()
    EROTIMATIKOPHOBIA = auto()
    HEITOPHOBIA = auto()
    PISTAPHOBIA = auto()
    THAUMASTIKAPHOBIA = auto()
    VIRGUPHOBIA = auto()
    COLOPHOBIA = auto()


PUNCTUATION_MARK_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    PunctuationMarkPhobiasDescriptions.~PHOBIA: {
        Languages.ENGLISH: "Fear of tildes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobiasDescriptions.ANTICURLYBRACKETOPHOBIA: {
        Languages.ENGLISH: "Fear of curly brackets {}",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobiasDescriptions.BINDAPHOBIA: {
        Languages.ENGLISH: "Fear of hyphens (people with this may be scared to the brim because there are hyhens everywhere)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobiasDescriptions.EROTIMATIKOPHOBIA: {
        Languages.ENGLISH: "Fear of question marks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobiasDescriptions.HEITOPHOBIA: {
        Languages.ENGLISH: "Fear of apostrophes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobiasDescriptions.PISTAPHOBIA: {
        Languages.ENGLISH: "Fear of periods",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobiasDescriptions.THAUMASTIKAPHOBIA: {
        Languages.ENGLISH: "Fear of exclamation points",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobiasDescriptions.VIRGUPHOBIA: {
        Languages.ENGLISH: "Fear of commas",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PunctuationMarkPhobiasDescriptions.COLOPHOBIA: {
        Languages.ENGLISH: "Fear of colons",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
