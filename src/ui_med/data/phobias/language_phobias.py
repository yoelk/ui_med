from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class LanguagePhobias(Enum):
    """
    Language Phobias Names
    """
    ABBREVIATOPHOBIA = auto()
    AIBOHPHOBIA = auto()
    ALBUMISTAPHOBIA = auto()
    ALLODOXAPHOBIA = auto()
    ALPHABETICALPHOBIA = auto()
    ANAGRAMIPHOBIA = auto()
    CLIAHIYUATAPHOBIA = auto()
    DOXPHOBIA = auto()
    EUPHOBIA = auto()
    HELLENOLOGOPHOBIA = auto()
    HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA = auto()
    KAKOLOGOPHOBIA = auto()
    KAKOSPHOBIA = auto()
    LEXICOPHOBIA = auto()
    LOGOPHOBIA = auto()
    MYCROLOGOPHOBIA = auto()
    NEOLOGISTOPHOBIA = auto()
    NOMATOPHOBIA = auto()
    PANGRAMIPHOBIA = auto()
    PHOPINACIPHOBIA = auto()
    SENTENCEPHOBIA = auto()
    XENOGLOSSOPHOBIA = auto()


LANGUAGE_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    LanguagePhobias.ABBREVIATOPHOBIA: {
        Languages.ENGLISH: "Abbreviatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.AIBOHPHOBIA: {
        Languages.ENGLISH: "Aibohphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.ALBUMISTAPHOBIA: {
        Languages.ENGLISH: "Albumistaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.ALLODOXAPHOBIA: {
        Languages.ENGLISH: "Allodoxaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.ALPHABETICALPHOBIA: {
        Languages.ENGLISH: "Alphabeticalphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.ANAGRAMIPHOBIA: {
        Languages.ENGLISH: "Anagramiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.CLIAHIYUATAPHOBIA: {
        Languages.ENGLISH: "Cliahiyuataphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.DOXPHOBIA: {
        Languages.ENGLISH: "Doxphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.EUPHOBIA: {
        Languages.ENGLISH: "Euphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.HELLENOLOGOPHOBIA: {
        Languages.ENGLISH: "Hellenologophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA: {
        Languages.ENGLISH: "Hippopotomonstrosesquippedaliophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.KAKOLOGOPHOBIA: {
        Languages.ENGLISH: "Kakologophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.KAKOSPHOBIA: {
        Languages.ENGLISH: "Kakosphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.LEXICOPHOBIA: {
        Languages.ENGLISH: "Lexicophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.LOGOPHOBIA: {
        Languages.ENGLISH: "Logophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.MYCROLOGOPHOBIA: {
        Languages.ENGLISH: "Mycrologophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.NEOLOGISTOPHOBIA: {
        Languages.ENGLISH: "Neologistophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.NOMATOPHOBIA: {
        Languages.ENGLISH: "Nomatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.PANGRAMIPHOBIA: {
        Languages.ENGLISH: "Pangramiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.PHOPINACIPHOBIA: {
        Languages.ENGLISH: "Phopinaciphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.SENTENCEPHOBIA: {
        Languages.ENGLISH: "Sentencephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobias.XENOGLOSSOPHOBIA: {
        Languages.ENGLISH: "Xenoglossophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class LanguagePhobiasDescriptions(Enum):
    """
    Language Phobias Descriptions
    """
    ABBREVIATOPHOBIA = auto()
    AIBOHPHOBIA = auto()
    ALBUMISTAPHOBIA = auto()
    ALLODOXAPHOBIA = auto()
    ALPHABETICALPHOBIA = auto()
    ANAGRAMIPHOBIA = auto()
    CLIAHIYUATAPHOBIA = auto()
    DOXPHOBIA = auto()
    EUPHOBIA = auto()
    HELLENOLOGOPHOBIA = auto()
    HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA = auto()
    KAKOLOGOPHOBIA = auto()
    KAKOSPHOBIA = auto()
    LEXICOPHOBIA = auto()
    LOGOPHOBIA = auto()
    MYCROLOGOPHOBIA = auto()
    NEOLOGISTOPHOBIA = auto()
    NOMATOPHOBIA = auto()
    PANGRAMIPHOBIA = auto()
    PHOPINACIPHOBIA = auto()
    SENTENCEPHOBIA = auto()
    XENOGLOSSOPHOBIA = auto()


LANGUAGE_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    LanguagePhobiasDescriptions.ABBREVIATOPHOBIA: {
        Languages.ENGLISH: "Fear of abbreviations",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.AIBOHPHOBIA: {
        Languages.ENGLISH: "Fear of palindromes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.ALBUMISTAPHOBIA: {
        Languages.ENGLISH: "Fear of lists",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.ALLODOXAPHOBIA: {
        Languages.ENGLISH: "Fear of different people's opinions (branch of doxphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.ALPHABETICALPHOBIA: {
        Languages.ENGLISH: "Fear of the alphabet",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.ANAGRAMIPHOBIA: {
        Languages.ENGLISH: "Fear of anagrams",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.CLIAHIYUATAPHOBIA: {
        Languages.ENGLISH: "Fear of complicated words (branch of hippopotomonstrosesquippedaliophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.DOXPHOBIA: {
        Languages.ENGLISH: "Fear of opinions",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.EUPHOBIA: {
        Languages.ENGLISH: "Fear of good news",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.HELLENOLOGOPHOBIA: {
        Languages.ENGLISH: "Fear of greek terms or complex scientific terminology (branch of logophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA: {
        Languages.ENGLISH: "Fear of long or complicated words (branch of logophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.KAKOLOGOPHOBIA: {
        Languages.ENGLISH: "Fear of swearwords (branch of deprecophobia)branch of logophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.KAKOSPHOBIA: {
        Languages.ENGLISH: "Fear of bad news",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.LEXICOPHOBIA: {
        Languages.ENGLISH: "Fear of dictionary",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.LOGOPHOBIA: {
        Languages.ENGLISH: "Fear of words (branch of logophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.MYCROLOGOPHOBIA: {
        Languages.ENGLISH: "Fear of short words (branch of logophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.NEOLOGISTOPHOBIA: {
        Languages.ENGLISH: "Fear of new words (branch of logophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.NOMATOPHOBIA: {
        Languages.ENGLISH: "Fear of names",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.PANGRAMIPHOBIA: {
        Languages.ENGLISH: "Fear of pangrams (branch of alphabeticalphobia and sentencephobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.PHOPINACIPHOBIA: {
        Languages.ENGLISH: "Fear of phobia lists (branch of logophobia and albumistaphboia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.SENTENCEPHOBIA: {
        Languages.ENGLISH: "Fear of sentences (branch of logophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    LanguagePhobiasDescriptions.XENOGLOSSOPHOBIA: {
        Languages.ENGLISH: "Fear of foreign languages",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
