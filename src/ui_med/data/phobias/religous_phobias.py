from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class ReligousPhobias(Enum):
    """
    Religous Phobias Names
    """
    ANGELOPHOBIA = auto()
    ATHEOPHOBIA = auto()
    BIBLEPHOBIA = auto()
    BUDDHIPHOBIA = auto()
    CHRISTIANOPHOBIA = auto()
    CHRISTOPHOBIA = auto()
    ECCLESIOPHOBIA = auto()
    DEMONOPHOBIA = auto()
    DIABOLOPHOBIA = auto()
    FEGEFPHOBIA = auto()
    GODOAPHINPHOBIA = auto()
    HELIOTHUSIAPHOBIA = auto()
    HINDUPHOBIA = auto()
    ISLAMOPHOBIA = auto()
    JESUSOPHOBIA = auto()
    LIOSUSCHRISTUSPHOBIA = auto()
    JUDEOPHOBIA = auto()
    PAPAPHOBIA = auto()
    RITOURGIAPHOBIA = auto()
    SATANOPHOBIA = auto()
    SPIRITUPHOBIA = auto()
    STAUROPHOBIA = auto()
    STYGIOPHOBIA = auto()
    TELEOPHOBIA = auto()
    THEOPHOBIA = auto()
    URANOPHOBIA = auto()


RELIGOUS_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    ReligousPhobias.ANGELOPHOBIA: {
        Languages.ENGLISH: "Angelophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.ATHEOPHOBIA: {
        Languages.ENGLISH: "Atheophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.BIBLEPHOBIA: {
        Languages.ENGLISH: "Biblephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.BUDDHIPHOBIA: {
        Languages.ENGLISH: "Buddhiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.CHRISTIANOPHOBIA: {
        Languages.ENGLISH: "Christianophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.CHRISTOPHOBIA: {
        Languages.ENGLISH: "Christophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.ECCLESIOPHOBIA: {
        Languages.ENGLISH: "Ecclesiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.DEMONOPHOBIA: {
        Languages.ENGLISH: "Demonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.DIABOLOPHOBIA: {
        Languages.ENGLISH: "Diabolophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.FEGEFPHOBIA: {
        Languages.ENGLISH: "Fegefphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.GODOAPHINPHOBIA: {
        Languages.ENGLISH: "Godoaphinphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.HELIOTHUSIAPHOBIA: {
        Languages.ENGLISH: "Heliothusiaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.HINDUPHOBIA: {
        Languages.ENGLISH: "Hinduphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.ISLAMOPHOBIA: {
        Languages.ENGLISH: "Islamophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.JESUSOPHOBIA: {
        Languages.ENGLISH: "Jesusophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.LIOSUSCHRISTUSPHOBIA: {
        Languages.ENGLISH: "Liosuschristusphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.JUDEOPHOBIA: {
        Languages.ENGLISH: "Judeophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.PAPAPHOBIA: {
        Languages.ENGLISH: "Papaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.RITOURGIAPHOBIA: {
        Languages.ENGLISH: "Ritourgiaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.SATANOPHOBIA: {
        Languages.ENGLISH: "Satanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.SPIRITUPHOBIA: {
        Languages.ENGLISH: "Spirituphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.STAUROPHOBIA: {
        Languages.ENGLISH: "Staurophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.STYGIOPHOBIA: {
        Languages.ENGLISH: "Stygiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.TELEOPHOBIA: {
        Languages.ENGLISH: "Teleophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.THEOPHOBIA: {
        Languages.ENGLISH: "Theophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobias.URANOPHOBIA: {
        Languages.ENGLISH: "Uranophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class ReligousPhobiasDescriptions(Enum):
    """
    Religous Phobias Descriptions
    """
    ANGELOPHOBIA = auto()
    ATHEOPHOBIA = auto()
    BIBLEPHOBIA = auto()
    BUDDHIPHOBIA = auto()
    CHRISTIANOPHOBIA = auto()
    CHRISTOPHOBIA = auto()
    ECCLESIOPHOBIA = auto()
    DEMONOPHOBIA = auto()
    DIABOLOPHOBIA = auto()
    FEGEFPHOBIA = auto()
    GODOAPHINPHOBIA = auto()
    HELIOTHUSIAPHOBIA = auto()
    HINDUPHOBIA = auto()
    ISLAMOPHOBIA = auto()
    JESUSOPHOBIA = auto()
    LIOSUSCHRISTUSPHOBIA = auto()
    JUDEOPHOBIA = auto()
    PAPAPHOBIA = auto()
    RITOURGIAPHOBIA = auto()
    SATANOPHOBIA = auto()
    SPIRITUPHOBIA = auto()
    STAUROPHOBIA = auto()
    STYGIOPHOBIA = auto()
    TELEOPHOBIA = auto()
    THEOPHOBIA = auto()
    URANOPHOBIA = auto()


RELIGOUS_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    ReligousPhobiasDescriptions.ANGELOPHOBIA: {
        Languages.ENGLISH: "Fear of angels (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.ATHEOPHOBIA: {
        Languages.ENGLISH: "Fear of atheists (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.BIBLEPHOBIA: {
        Languages.ENGLISH: "Fear of bibles (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.BUDDHIPHOBIA: {
        Languages.ENGLISH: "Fear of buddhuism (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.CHRISTIANOPHOBIA: {
        Languages.ENGLISH: "Fear of the christians (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.CHRISTOPHOBIA: {
        Languages.ENGLISH: "Fear of people that hate christian faith (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.ECCLESIOPHOBIA: {
        Languages.ENGLISH: "Fear of church (branch of theophobia and christianophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.DEMONOPHOBIA: {
        Languages.ENGLISH: "Fear of demons (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.DIABOLOPHOBIA: {
        Languages.ENGLISH: "Fear of devils (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.FEGEFPHOBIA: {
        Languages.ENGLISH: "Fear of the word 'hell' (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.GODOAPHINPHOBIA: {
        Languages.ENGLISH: "Fear of god's number, 555 (branch of theophobia and numerophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.HELIOTHUSIAPHOBIA: {
        Languages.ENGLISH: "Fear of sun sacrifices (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.HINDUPHOBIA: {
        Languages.ENGLISH: "Fear of hinduism (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.ISLAMOPHOBIA: {
        Languages.ENGLISH: "Fear of muslims (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.JESUSOPHOBIA: {
        Languages.ENGLISH: "Fear of jesus (branch of theophobia and christianophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.LIOSUSCHRISTUSPHOBIA: {
        Languages.ENGLISH: "Same as jesusophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.JUDEOPHOBIA: {
        Languages.ENGLISH: "Fear of jews (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.PAPAPHOBIA: {
        Languages.ENGLISH: "Fear of the pope (branch of theophobia and christianophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.RITOURGIAPHOBIA: {
        Languages.ENGLISH: "Fear of rituals (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.SATANOPHOBIA: {
        Languages.ENGLISH: "Fear of satan (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.SPIRITUPHOBIA: {
        Languages.ENGLISH: "Fear of spiritual things",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.STAUROPHOBIA: {
        Languages.ENGLISH: "Fear of crosses or the crucifix (branch of theophobia and christianophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.STYGIOPHOBIA: {
        Languages.ENGLISH: "Fear of hell (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.TELEOPHOBIA: {
        Languages.ENGLISH: "Fear of religious ceremonies (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.THEOPHOBIA: {
        Languages.ENGLISH: "Fear of religion",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ReligousPhobiasDescriptions.URANOPHOBIA: {
        Languages.ENGLISH: "Fear of heaven (branch of theophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
