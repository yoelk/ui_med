from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class PlantPhobias(Enum):
    """
    Plant Phobias Names
    """
    AGROSTOPHOBIA = auto()
    ANTHOPHOBIA = auto()
    BOTANOPHOBIA = auto()
    CITAROPHOBIA = auto()
    'DENDROPHOBIA = auto()
    DISTLEPHOBIA = auto()
    DOGWOODPHOBIA = auto()
    DRUSOPHOBIA = auto()
    GRASARTOPHOBIA = auto()
    KACTOSOPHOBIA = auto()
    PEFKOPHOBIA = auto()
    PHYLLOPHOBIA = auto()
    MAPLELEAFAPHOBIA = auto()
    PTERIDOPHOBIA = auto()
    VIRIDITAPHOBIA = auto()


PLANT_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    PlantPhobias.AGROSTOPHOBIA: {
        Languages.ENGLISH: "Agrostophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.ANTHOPHOBIA: {
        Languages.ENGLISH: "Anthophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.BOTANOPHOBIA: {
        Languages.ENGLISH: "Botanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.CITAROPHOBIA: {
        Languages.ENGLISH: "Citarophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.'DENDROPHOBIA: {
        Languages.ENGLISH: "'Dendrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.DISTLEPHOBIA: {
        Languages.ENGLISH: "Distlephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.DOGWOODPHOBIA: {
        Languages.ENGLISH: "Dogwoodphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.DRUSOPHOBIA: {
        Languages.ENGLISH: "Drusophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.GRASARTOPHOBIA: {
        Languages.ENGLISH: "Grasartophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.KACTOSOPHOBIA: {
        Languages.ENGLISH: "Kactosophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.PEFKOPHOBIA: {
        Languages.ENGLISH: "Pefkophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.PHYLLOPHOBIA: {
        Languages.ENGLISH: "Phyllophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.MAPLELEAFAPHOBIA: {
        Languages.ENGLISH: "Mapleleafaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.PTERIDOPHOBIA: {
        Languages.ENGLISH: "Pteridophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobias.VIRIDITAPHOBIA: {
        Languages.ENGLISH: "Viriditaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class PlantPhobiasDescriptions(Enum):
    """
    Plant Phobias Descriptions
    """
    AGROSTOPHOBIA = auto()
    ANTHOPHOBIA = auto()
    BOTANOPHOBIA = auto()
    CITAROPHOBIA = auto()
    'DENDROPHOBIA = auto()
    DISTLEPHOBIA = auto()
    DOGWOODPHOBIA = auto()
    DRUSOPHOBIA = auto()
    GRASARTOPHOBIA = auto()
    KACTOSOPHOBIA = auto()
    PEFKOPHOBIA = auto()
    PHYLLOPHOBIA = auto()
    MAPLELEAFAPHOBIA = auto()
    PTERIDOPHOBIA = auto()
    VIRIDITAPHOBIA = auto()


PLANT_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    PlantPhobiasDescriptions.AGROSTOPHOBIA: {
        Languages.ENGLISH: "Fear of grass (branch of boranophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.ANTHOPHOBIA: {
        Languages.ENGLISH: "Fear of flowers (branch of botanophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.BOTANOPHOBIA: {
        Languages.ENGLISH: "Fear of plants (branch of pantophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.CITAROPHOBIA: {
        Languages.ENGLISH: "Fear of citrus (branch of botanophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.'DENDROPHOBIA: {
        Languages.ENGLISH: "Fear of trees (branch of botanophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.DISTLEPHOBIA: {
        Languages.ENGLISH: "Fear of thistles (branch of botanopgobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.DOGWOODPHOBIA: {
        Languages.ENGLISH: "Fear of dogwood trees (branch of dendrophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.DRUSOPHOBIA: {
        Languages.ENGLISH: "Fear of oak trees (branch of dendrophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.GRASARTOPHOBIA: {
        Languages.ENGLISH: "Fear of tumbleweeds (branch of botanophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.KACTOSOPHOBIA: {
        Languages.ENGLISH: "Fear of cacti (branch of botanophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.PEFKOPHOBIA: {
        Languages.ENGLISH: "Fear of pine trees (branch of dendrophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.PHYLLOPHOBIA: {
        Languages.ENGLISH: "Fear of leaves (branch of botanophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.MAPLELEAFAPHOBIA: {
        Languages.ENGLISH: "Fear of maple leaves (branch of phyllophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.PTERIDOPHOBIA: {
        Languages.ENGLISH: "Fear of ferns (branch of botanophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    PlantPhobiasDescriptions.VIRIDITAPHOBIA: {
        Languages.ENGLISH: "Fear of weeds (branch of botanophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
