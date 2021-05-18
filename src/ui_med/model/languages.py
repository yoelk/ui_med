from enum import Enum
from typing import Dict, Optional

from ui_med.app_base import get_app
from ui_med.data.fears import FearDescriptions, FearNames
from ui_med.model.enums import Languages


# TODO(joel): Encapsulate this file's contents in a class

class Texts(Enum):
    """
    Texts in the system
    """
    ADD_FEAR = "ADD_FEAR"
    ADD_NAME = "ADD_NAME"
    ADD_PERSON = "ADD_PERSON"
    BACK = "BACK"
    DELETE = "DELETE"
    EDIT = "EDIT"
    FEARS = "FEARS"
    FIRST_NAMES = "FIRST_NAMES"
    FULL_NAME = "FULL_NAME"
    LAST_NAMES = "LAST_NAMES"
    NAMES = "NAMES"
    PEOPLE = "PEOPLE"
    SAVE = "SAVE"


LANGUAGE_STRINGS: Dict[Enum, Dict[Languages, Optional[str]]] = {
    FearDescriptions.ACHLUOPHOBIA: {
        Languages.ENGLISH: "Fear of darkness",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ACROPHOBIA: {
        Languages.ENGLISH: "Fear of heights",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.AEROPHOBIA: {
        Languages.ENGLISH: "Fear of flying",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ALGOPHOBIA: {
        Languages.ENGLISH: "Fear of pain",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.AGORAPHOBIA: {
        Languages.ENGLISH: "Fear of open spaces or crowds",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.AICHMOPHOBIA: {
        Languages.ENGLISH: "Fear of needles or pointed objects",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.AMAXOPHOBIA: {
        Languages.ENGLISH: "Fear of riding in a car",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ANDROPHOBIA: {
        Languages.ENGLISH: "Fear of men",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ANGINOPHOBIA: {
        Languages.ENGLISH: "Fear of angina or choking",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ANTHROPHOBIA: {
        Languages.ENGLISH: "Fear of flowers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ANTHROPOPHOBIA: {
        Languages.ENGLISH: "Fear of people or society",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.APHENPHOSMPHOBIA: {
        Languages.ENGLISH: "Fear of being touched",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ARACHIBUTYROPHOBIA: {
        Languages.ENGLISH: "Fear of peanut butter",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ARACHNOPHOBIA: {
        Languages.ENGLISH: "Fear of spiders",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ARITHMOPHOBIA: {
        Languages.ENGLISH: "Fear of numbers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ASTRAPHOBIA: {
        Languages.ENGLISH: "Fear of thunder and lightning",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ATAXOPHOBIA: {
        Languages.ENGLISH: "Fear of disorder or untidiness",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ATELOPHOBIA: {
        Languages.ENGLISH: "Fear of imperfection",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ATYCHIPHOBIA: {
        Languages.ENGLISH: "Fear of failure",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.AUTOMATONOPHOBIA: {
        Languages.ENGLISH: "Fear of Human-Like Figures",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.AUTOMYSOPHOBIA: {
        Languages.ENGLISH: "Fear of being dirty",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.AUTOPHOBIA: {
        Languages.ENGLISH: "Fear of being alone",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.BACTERIOPHOBIA: {
        Languages.ENGLISH: "Fear of bacteria",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.BAROPHOBIA: {
        Languages.ENGLISH: "Fear of gravity",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.BATHMOPHOBIA: {
        Languages.ENGLISH: "Fear of stairs or steep slopes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.BATRACHOPHOBIA: {
        Languages.ENGLISH: "Fear of amphibians",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.BELONEPHOBIA: {
        Languages.ENGLISH: "Fear of pins and needles",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.BIBLIOPHOBIA: {
        Languages.ENGLISH: "Fear of books",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.BOTANOPHOBIA: {
        Languages.ENGLISH: "Fear of plants",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.CACOPHOBIA: {
        Languages.ENGLISH: "Fear of ugliness",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.CATAGELOPHOBIA: {
        Languages.ENGLISH: "Fear of being ridiculed",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.CATOPTROPHOBIA: {
        Languages.ENGLISH: "Fear of mirrors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.CHIONOPHOBIA: {
        Languages.ENGLISH: "Fear of snow",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.CHROMOPHOBIA: {
        Languages.ENGLISH: "Fear of colors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.CHRONOMENTROPHOBIA: {
        Languages.ENGLISH: "Fear of clocks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.CHRONOPHOBIA: {
        Languages.ENGLISH: "Fear of Time",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.CLAUSTROPHOBIA: {
        Languages.ENGLISH: "Fear of confined spaces",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.COULROPHOBIA: {
        Languages.ENGLISH: "Fear of clowns",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.CYBERPHOBIA: {
        Languages.ENGLISH: "Fear of computers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.CYNOPHOBIA: {
        Languages.ENGLISH: "Fear of dogs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.DENDROPHOBIA: {
        Languages.ENGLISH: "Fear of trees",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.DENTOPHOBIA: {
        Languages.ENGLISH: "Fear of dentists",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.DOMATOPHOBIA: {
        Languages.ENGLISH: "Fear of houses",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.DYSTYCHIPHOBIA: {
        Languages.ENGLISH: "Fear of accidents",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ECOPHOBIA: {
        Languages.ENGLISH: "Fear of the home",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ELUROPHOBIA: {
        Languages.ENGLISH: "Fear of cats",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ENTOMOPHOBIA: {
        Languages.ENGLISH: "Fear of insects",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.EPHEBIPHOBIA: {
        Languages.ENGLISH: "Fear of teenagers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.EQUINOPHOBIA: {
        Languages.ENGLISH: "Fear of horses",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.GAMOPHOBIA: {
        Languages.ENGLISH: "Fear of marriage",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.GENUPHOBIA: {
        Languages.ENGLISH: "Fear of knees",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.GLOSSOPHOBIA: {
        Languages.ENGLISH: "Fear of speaking in public",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.GYNOPHOBIA: {
        Languages.ENGLISH: "Fear of women",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.HAPHEPHOBIA: {
        Languages.ENGLISH: "Fear of touch",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.HELIOPHOBIA: {
        Languages.ENGLISH: "Fear of the sun",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.HEMOPHOBIA: {
        Languages.ENGLISH: "Fear of blood",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.HERPETOPHOBIA: {
        Languages.ENGLISH: "Fear of reptiles",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.HIPPOPOTOMONSTROSESQUIPEDALIOPHOBIA: {
        Languages.ENGLISH: "Fear of long words",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.HYDROPHOBIA: {
        Languages.ENGLISH: "Fear of water",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.HYPOCHONDRIA: {
        Languages.ENGLISH: "Fear of illness",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.IATROPHOBIA: {
        Languages.ENGLISH: "Fear of doctors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.INSECTOPHOBIA: {
        Languages.ENGLISH: "Fear of insects",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.KOINONIPHOBIA: {
        Languages.ENGLISH: "Fear of rooms",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.KOUMPOUNOPHOBIA: {
        Languages.ENGLISH: "Fear of buttons",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.LEUKOPHOBIA: {
        Languages.ENGLISH: "Fear of the color white",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.LILAPSOPHOBIA: {
        Languages.ENGLISH: "Fear of tornadoes and hurricanes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.LOCKIOPHOBIA: {
        Languages.ENGLISH: "Fear of childbirth",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.MAGEIROCOPHOBIA: {
        Languages.ENGLISH: "Fear of cooking",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.MEGALOPHOBIA: {
        Languages.ENGLISH: "Fear of large things",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.MENOPHOBIA: {
        Languages.ENGLISH: "Fear of Menstrual Blood",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.MELANOPHOBIA: {
        Languages.ENGLISH: "Fear of the color black",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.MICROPHOBIA: {
        Languages.ENGLISH: "Fear of small things",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.MYSOPHOBIA: {
        Languages.ENGLISH: "Fear of dirt and germs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.NECROPHOBIA: {
        Languages.ENGLISH: "Fear of death or dead things",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.NOCTIPHOBIA: {
        Languages.ENGLISH: "Fear of the night",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.NOSOCOMEPHOBIA: {
        Languages.ENGLISH: "Fear of hospitals",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.NYCTOPHOBIA: {
        Languages.ENGLISH: "Fear of the dark",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.OBESOPHOBIA: {
        Languages.ENGLISH: "Fear of gaining weight",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.OCTOPHOBIA: {
        Languages.ENGLISH: "Fear of the figure 8",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.OMBROPHOBIA: {
        Languages.ENGLISH: "Fear of rain",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.OPHIDIOPHOBIA: {
        Languages.ENGLISH: "Fear of snakes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ORNITHOPHOBIA: {
        Languages.ENGLISH: "Fear of birds",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.PAPYROPHOBIA: {
        Languages.ENGLISH: "Fear of paper",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.PARURESIS: {
        Languages.ENGLISH: "Fear of urinating in public",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.PATHOPHOBIA: {
        Languages.ENGLISH: "Fear of disease",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.PEDOPHOBIA: {
        Languages.ENGLISH: "Fear of children",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.PHILEMATOPHOBIA: {
        Languages.ENGLISH: "Fear of Kissing",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.PHILOPHOBIA: {
        Languages.ENGLISH: "Fear of love",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.PHOBOPHOBIA: {
        Languages.ENGLISH: "Fear of phobias",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.PODOPHOBIA: {
        Languages.ENGLISH: "Fear of feet",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.PORPHYROPHOBIA: {
        Languages.ENGLISH: "Fear of the color purple",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.PTERIDOPHOBIA: {
        Languages.ENGLISH: "Fear of ferns",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.PTEROMERHANOPHOBIA: {
        Languages.ENGLISH: "Fear of flying",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.PYROPHOBIA: {
        Languages.ENGLISH: "Fear of fire",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.SAMHAINOPHOBIA: {
        Languages.ENGLISH: "Fear of Halloween",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.SCOLIONOPHOBIA: {
        Languages.ENGLISH: "Fear of school",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.SCOPTOPHOBIA: {
        Languages.ENGLISH: "Fear of being stared at",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.SCYPHOPHOBIA: {
        Languages.ENGLISH: "Fear of jellyfish",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.SELENOPHOBIA: {
        Languages.ENGLISH: "Fear of the moon",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.SOCIOPHOBIA: {
        Languages.ENGLISH: "Fear of social evaluation",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.SOMNIPHOBIA: {
        Languages.ENGLISH: "Fear of sleep",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.TACHOPHOBIA: {
        Languages.ENGLISH: "Fear of speed",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.TECHNOPHOBIA: {
        Languages.ENGLISH: "Fear of technology",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.TONITROPHOBIA: {
        Languages.ENGLISH: "Fear of thunder",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.TRYPANOPHOBIA: {
        Languages.ENGLISH: "Fear of needles/injections",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.TRYPOPHOBIA: {
        Languages.ENGLISH: "Fear of Holes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.VENUSTRAPHOBIA: {
        Languages.ENGLISH: "Fear of beautiful women",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.VERMINOPHOBIA: {
        Languages.ENGLISH: "Fear of germs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.WICCAPHOBIA: {
        Languages.ENGLISH: "Fear of witches and witchcraft",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.XENOPHOBIA: {
        Languages.ENGLISH: "Fear of strangers or foreigners",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearDescriptions.ZOOPHOBIA: {
        Languages.ENGLISH: "Fear of animals",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },

    FearNames.ACHLUOPHOBIA: {
        Languages.ENGLISH: "Achluophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ACROPHOBIA: {
        Languages.ENGLISH: "Acrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.AEROPHOBIA: {
        Languages.ENGLISH: "Aerophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ALGOPHOBIA: {
        Languages.ENGLISH: "Algophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.AGORAPHOBIA: {
        Languages.ENGLISH: "Agoraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.AICHMOPHOBIA: {
        Languages.ENGLISH: "Aichmophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.AMAXOPHOBIA: {
        Languages.ENGLISH: "Amaxophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ANDROPHOBIA: {
        Languages.ENGLISH: "Androphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ANGINOPHOBIA: {
        Languages.ENGLISH: "Anginophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ANTHROPHOBIA: {
        Languages.ENGLISH: "Anthrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ANTHROPOPHOBIA: {
        Languages.ENGLISH: "Anthropophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.APHENPHOSMPHOBIA: {
        Languages.ENGLISH: "Aphenphosmphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ARACHIBUTYROPHOBIA: {
        Languages.ENGLISH: "Arachibutyrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ARACHNOPHOBIA: {
        Languages.ENGLISH: "Arachnophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ARITHMOPHOBIA: {
        Languages.ENGLISH: "Arithmophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ASTRAPHOBIA: {
        Languages.ENGLISH: "Astraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ATAXOPHOBIA: {
        Languages.ENGLISH: "Ataxophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ATELOPHOBIA: {
        Languages.ENGLISH: "Atelophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ATYCHIPHOBIA: {
        Languages.ENGLISH: "Atychiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.AUTOMATONOPHOBIA: {
        Languages.ENGLISH: "Automatonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.AUTOMYSOPHOBIA: {
        Languages.ENGLISH: "Automysophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.AUTOPHOBIA: {
        Languages.ENGLISH: "Autophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.BACTERIOPHOBIA: {
        Languages.ENGLISH: "Bacteriophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.BAROPHOBIA: {
        Languages.ENGLISH: "Barophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.BATHMOPHOBIA: {
        Languages.ENGLISH: "Bathmophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.BATRACHOPHOBIA: {
        Languages.ENGLISH: "Batrachophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.BELONEPHOBIA: {
        Languages.ENGLISH: "Belonephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.BIBLIOPHOBIA: {
        Languages.ENGLISH: "Bibliophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.BOTANOPHOBIA: {
        Languages.ENGLISH: "Botanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.CACOPHOBIA: {
        Languages.ENGLISH: "Cacophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.CATAGELOPHOBIA: {
        Languages.ENGLISH: "Catagelophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.CATOPTROPHOBIA: {
        Languages.ENGLISH: "Catoptrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.CHIONOPHOBIA: {
        Languages.ENGLISH: "Chionophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.CHROMOPHOBIA: {
        Languages.ENGLISH: "Chromophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.CHRONOMENTROPHOBIA: {
        Languages.ENGLISH: "Chronomentrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.CHRONOPHOBIA: {
        Languages.ENGLISH: "Chronophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.CLAUSTROPHOBIA: {
        Languages.ENGLISH: "Claustrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.COULROPHOBIA: {
        Languages.ENGLISH: "Coulrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.CYBERPHOBIA: {
        Languages.ENGLISH: "Cyberphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.CYNOPHOBIA: {
        Languages.ENGLISH: "Cynophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.DENDROPHOBIA: {
        Languages.ENGLISH: "Dendrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.DENTOPHOBIA: {
        Languages.ENGLISH: "Dentophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.DOMATOPHOBIA: {
        Languages.ENGLISH: "Domatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.DYSTYCHIPHOBIA: {
        Languages.ENGLISH: "Dystychiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ECOPHOBIA: {
        Languages.ENGLISH: "Ecophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ELUROPHOBIA: {
        Languages.ENGLISH: "Elurophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ENTOMOPHOBIA: {
        Languages.ENGLISH: "Entomophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.EPHEBIPHOBIA: {
        Languages.ENGLISH: "Ephebiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.EQUINOPHOBIA: {
        Languages.ENGLISH: "Equinophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.GAMOPHOBIA: {
        Languages.ENGLISH: "Gamophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.GENUPHOBIA: {
        Languages.ENGLISH: "Genuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.GLOSSOPHOBIA: {
        Languages.ENGLISH: "Glossophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.GYNOPHOBIA: {
        Languages.ENGLISH: "Gynophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.HAPHEPHOBIA: {
        Languages.ENGLISH: "Haphephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.HELIOPHOBIA: {
        Languages.ENGLISH: "Heliophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.HEMOPHOBIA: {
        Languages.ENGLISH: "Hemophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.HERPETOPHOBIA: {
        Languages.ENGLISH: "Herpetophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.HIPPOPOTOMONSTROSESQUIPEDALIOPHOBIA: {
        Languages.ENGLISH: "Hippopotomonstrosesquipedaliophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.HYDROPHOBIA: {
        Languages.ENGLISH: "Hydrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.HYPOCHONDRIA: {
        Languages.ENGLISH: "Hypochondria",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.IATROPHOBIA: {
        Languages.ENGLISH: "Iatrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.INSECTOPHOBIA: {
        Languages.ENGLISH: "Insectophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.KOINONIPHOBIA: {
        Languages.ENGLISH: "Koinoniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.KOUMPOUNOPHOBIA: {
        Languages.ENGLISH: "Koumpounophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.LEUKOPHOBIA: {
        Languages.ENGLISH: "Leukophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.LILAPSOPHOBIA: {
        Languages.ENGLISH: "Lilapsophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.LOCKIOPHOBIA: {
        Languages.ENGLISH: "Lockiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.MAGEIROCOPHOBIA: {
        Languages.ENGLISH: "Mageirocophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.MEGALOPHOBIA: {
        Languages.ENGLISH: "Megalophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.MENOPHOBIA: {
        Languages.ENGLISH: "Menophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.MELANOPHOBIA: {
        Languages.ENGLISH: "Melanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.MICROPHOBIA: {
        Languages.ENGLISH: "Microphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.MYSOPHOBIA: {
        Languages.ENGLISH: "Mysophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.NECROPHOBIA: {
        Languages.ENGLISH: "Necrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.NOCTIPHOBIA: {
        Languages.ENGLISH: "Noctiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.NOSOCOMEPHOBIA: {
        Languages.ENGLISH: "Nosocomephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.NYCTOPHOBIA: {
        Languages.ENGLISH: "Nyctophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.OBESOPHOBIA: {
        Languages.ENGLISH: "Obesophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.OCTOPHOBIA: {
        Languages.ENGLISH: "Octophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.OMBROPHOBIA: {
        Languages.ENGLISH: "Ombrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.OPHIDIOPHOBIA: {
        Languages.ENGLISH: "Ophidiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ORNITHOPHOBIA: {
        Languages.ENGLISH: "Ornithophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.PAPYROPHOBIA: {
        Languages.ENGLISH: "Papyrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.PARURESIS: {
        Languages.ENGLISH: "Paruresis",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.PATHOPHOBIA: {
        Languages.ENGLISH: "Pathophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.PEDOPHOBIA: {
        Languages.ENGLISH: "Pedophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.PHILEMATOPHOBIA: {
        Languages.ENGLISH: "Philematophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.PHILOPHOBIA: {
        Languages.ENGLISH: "Philophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.PHOBOPHOBIA: {
        Languages.ENGLISH: "Phobophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.PODOPHOBIA: {
        Languages.ENGLISH: "Podophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.PORPHYROPHOBIA: {
        Languages.ENGLISH: "Porphyrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.PTERIDOPHOBIA: {
        Languages.ENGLISH: "Pteridophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.PTEROMERHANOPHOBIA: {
        Languages.ENGLISH: "Pteromerhanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.PYROPHOBIA: {
        Languages.ENGLISH: "Pyrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.SAMHAINOPHOBIA: {
        Languages.ENGLISH: "Samhainophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.SCOLIONOPHOBIA: {
        Languages.ENGLISH: "Scolionophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.SCOPTOPHOBIA: {
        Languages.ENGLISH: "Scoptophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.SCYPHOPHOBIA: {
        Languages.ENGLISH: "Scyphophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.SELENOPHOBIA: {
        Languages.ENGLISH: "Selenophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.SOCIOPHOBIA: {
        Languages.ENGLISH: "Sociophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.SOMNIPHOBIA: {
        Languages.ENGLISH: "Somniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.TACHOPHOBIA: {
        Languages.ENGLISH: "Tachophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.TECHNOPHOBIA: {
        Languages.ENGLISH: "Technophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.TONITROPHOBIA: {
        Languages.ENGLISH: "Tonitrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.TRYPANOPHOBIA: {
        Languages.ENGLISH: "Trypanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.TRYPOPHOBIA: {
        Languages.ENGLISH: "Trypophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.VENUSTRAPHOBIA: {
        Languages.ENGLISH: "Venustraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.VERMINOPHOBIA: {
        Languages.ENGLISH: "Verminophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.WICCAPHOBIA: {
        Languages.ENGLISH: "Wiccaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.XENOPHOBIA: {
        Languages.ENGLISH: "Xenophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    FearNames.ZOOPHOBIA: {
        Languages.ENGLISH: "Zoophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },

    Languages.ARAB: {
        Languages.ENGLISH: "Arab",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Languages.ENGLISH: {
        Languages.ENGLISH: "English",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Languages.HEBREW: {
        Languages.ENGLISH: "Hebrew",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Languages.ITALIAN: {
        Languages.ENGLISH: "Italian",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },

    Texts.ADD_FEAR: {
        Languages.ENGLISH: "Add Fear",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Texts.ADD_NAME: {
        Languages.ENGLISH: "Add Name",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Texts.ADD_PERSON: {
        Languages.ENGLISH: "Add Person",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Texts.BACK: {
        Languages.ENGLISH: "Back",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Texts.DELETE: {
        Languages.ENGLISH: "Delete",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Texts.EDIT: {
        Languages.ENGLISH: "Edit",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Texts.FEARS: {
        Languages.ENGLISH: "Fears",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Texts.FIRST_NAMES: {
        Languages.ENGLISH: "First Names",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Texts.FULL_NAME: {
        Languages.ENGLISH: "Full name",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Texts.LAST_NAMES: {
        Languages.ENGLISH: "Last Names",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Texts.NAMES: {
        Languages.ENGLISH: "Names",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Texts.PEOPLE: {
        Languages.ENGLISH: "People",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    Texts.SAVE: {
        Languages.ENGLISH: "Save",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
"""
Representations in different allowed_languages of strings in the system.
It's a static key-value store of texts and their translations.
For enums, the key is the enum's name
"""


def to_str(text_enum: Enum, language: Optional[Languages] = None) -> str:
    """
    :param text_enum: A text enum
    :param language: The language
    :return: The text in the required language
    """
    assert text_enum in LANGUAGE_STRINGS, f"Missing language string: {text_enum}"

    if not language:
        language = get_app().get_cur_lang()
    if language in LANGUAGE_STRINGS[text_enum]:
        return LANGUAGE_STRINGS[text_enum][language]

    else:
        assert Languages.DEFAULT in LANGUAGE_STRINGS[text_enum]
        return LANGUAGE_STRINGS[text_enum][Languages.DEFAULT]
