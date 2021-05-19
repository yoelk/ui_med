from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class ShapePhobias(Enum):
    """
    Shape Phobias Names
    """
    APEIROGOPHOBIA = auto()
    CIRCULAPHOBIA = auto()
    DUESANEREXAPHOBIA = auto()
    DWANIPHOBIA = auto()
    EDROPHOBIA = auto()
    HECTOGOPHOBIA = auto()
    ISOSCELESPHOBIA = auto()
    OVALPHOBIA = auto()
    PENTAGONAPHOBIA = auto()
    RECTANGLEPHOBIA = auto()
    SCHIMAPHOBIA = auto()
    SPHEREPHOBIA = auto()
    SQUAREPHOBIA = auto()
    TRIANGLEPHOBIA = auto()


SHAPE_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    ShapePhobias.APEIROGOPHOBIA: {
        Languages.ENGLISH: "Apeirogophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobias.CIRCULAPHOBIA: {
        Languages.ENGLISH: "Circulaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobias.DUESANEREXAPHOBIA: {
        Languages.ENGLISH: "Duesanerexaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobias.DWANIPHOBIA: {
        Languages.ENGLISH: "Dwaniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobias.EDROPHOBIA: {
        Languages.ENGLISH: "Edrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobias.HECTOGOPHOBIA: {
        Languages.ENGLISH: "Hectogophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobias.ISOSCELESPHOBIA: {
        Languages.ENGLISH: "Isoscelesphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobias.OVALPHOBIA: {
        Languages.ENGLISH: "Ovalphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobias.PENTAGONAPHOBIA: {
        Languages.ENGLISH: "Pentagonaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobias.RECTANGLEPHOBIA: {
        Languages.ENGLISH: "Rectanglephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobias.SCHIMAPHOBIA: {
        Languages.ENGLISH: "Schimaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobias.SPHEREPHOBIA: {
        Languages.ENGLISH: "Spherephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobias.SQUAREPHOBIA: {
        Languages.ENGLISH: "Squarephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobias.TRIANGLEPHOBIA: {
        Languages.ENGLISH: "Trianglephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class ShapePhobiasDescriptions(Enum):
    """
    Shape Phobias Descriptions
    """
    APEIROGOPHOBIA = auto()
    CIRCULAPHOBIA = auto()
    DUESANEREXAPHOBIA = auto()
    DWANIPHOBIA = auto()
    EDROPHOBIA = auto()
    HECTOGOPHOBIA = auto()
    ISOSCELESPHOBIA = auto()
    OVALPHOBIA = auto()
    PENTAGONAPHOBIA = auto()
    RECTANGLEPHOBIA = auto()
    SCHIMAPHOBIA = auto()
    SPHEREPHOBIA = auto()
    SQUAREPHOBIA = auto()
    TRIANGLEPHOBIA = auto()


SHAPE_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    ShapePhobiasDescriptions.APEIROGOPHOBIA: {
        Languages.ENGLISH: "Fear of apeirogons (branch of apeirophobia and schimaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobiasDescriptions.CIRCULAPHOBIA: {
        Languages.ENGLISH: "Fear of circles and circular structure (branch of schimaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobiasDescriptions.DUESANEREXAPHOBIA: {
        Languages.ENGLISH: "Fear of 2 sided shapes (branch of schimaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobiasDescriptions.DWANIPHOBIA: {
        Languages.ENGLISH: "Fear of irregular nonagons (branch of schimaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobiasDescriptions.EDROPHOBIA: {
        Languages.ENGLISH: "Fear of dodecahedrons (branch of schimaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobiasDescriptions.HECTOGOPHOBIA: {
        Languages.ENGLISH: "Fear of 100 sided shapes (branch of schimaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobiasDescriptions.ISOSCELESPHOBIA: {
        Languages.ENGLISH: "Fear of isosceles triangles (branch of schimaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobiasDescriptions.OVALPHOBIA: {
        Languages.ENGLISH: "Fear of ovals (branch of schimaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobiasDescriptions.PENTAGONAPHOBIA: {
        Languages.ENGLISH: "Fear of pentagons (branch of schimaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobiasDescriptions.RECTANGLEPHOBIA: {
        Languages.ENGLISH: "Fear of rectangles (branch of schimaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobiasDescriptions.SCHIMAPHOBIA: {
        Languages.ENGLISH: "Fear of shapes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobiasDescriptions.SPHEREPHOBIA: {
        Languages.ENGLISH: "Fear of spheres",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobiasDescriptions.SQUAREPHOBIA: {
        Languages.ENGLISH: "Fear of squares (branch of schimaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ShapePhobiasDescriptions.TRIANGLEPHOBIA: {
        Languages.ENGLISH: "Fear of triangles (branch of schimaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
