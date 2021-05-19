from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class WeatherPhobias(Enum):
    """
    Weather Phobias Names
    """
    AESTOPHOBIA = auto()
    ANEMOPHOBIA = auto()
    ASTRAPHOBIA = auto()
    BRONTOPHOBIA = auto()
    CERAUNOPHOBIA = auto()
    CHIONOPHOBIA = auto()
    CHIONOTHYELLAPHOBIA = auto()
    CYCLONOPHOBIA = auto()
    CYMOPHOBIA = auto()
    FRIGORIPHOBIA = auto()
    GRANDOPHOBIA = auto()
    HOMICHLOPHOBIA = auto()
    HUMIDOPHOBIA = auto()
    METEOPHOBIA = auto()
    NEBULOPHOBIA = auto()
    NEPHOPHOBIA = auto()
    OMBROPHOBIA = auto()
    PLUVIFRIGOPHOBIA = auto()
    SERENOPHOBIA = auto()
    TEMPESTAPHOBIA = auto()


WEATHER_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    WeatherPhobias.AESTOPHOBIA: {
        Languages.ENGLISH: "Aestophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.ANEMOPHOBIA: {
        Languages.ENGLISH: "Anemophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.ASTRAPHOBIA: {
        Languages.ENGLISH: "Astraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.BRONTOPHOBIA: {
        Languages.ENGLISH: "Brontophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.CERAUNOPHOBIA: {
        Languages.ENGLISH: "Ceraunophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.CHIONOPHOBIA: {
        Languages.ENGLISH: "Chionophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.CHIONOTHYELLAPHOBIA: {
        Languages.ENGLISH: "Chionothyellaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.CYCLONOPHOBIA: {
        Languages.ENGLISH: "Cyclonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.CYMOPHOBIA: {
        Languages.ENGLISH: "Cymophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.FRIGORIPHOBIA: {
        Languages.ENGLISH: "Frigoriphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.GRANDOPHOBIA: {
        Languages.ENGLISH: "Grandophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.HOMICHLOPHOBIA: {
        Languages.ENGLISH: "Homichlophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.HUMIDOPHOBIA: {
        Languages.ENGLISH: "Humidophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.METEOPHOBIA: {
        Languages.ENGLISH: "Meteophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.NEBULOPHOBIA: {
        Languages.ENGLISH: "Nebulophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.NEPHOPHOBIA: {
        Languages.ENGLISH: "Nephophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.OMBROPHOBIA: {
        Languages.ENGLISH: "Ombrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.PLUVIFRIGOPHOBIA: {
        Languages.ENGLISH: "Pluvifrigophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.SERENOPHOBIA: {
        Languages.ENGLISH: "Serenophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobias.TEMPESTAPHOBIA: {
        Languages.ENGLISH: "Tempestaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class WeatherPhobiasDescriptions(Enum):
    """
    Weather Phobias Descriptions
    """
    AESTOPHOBIA = auto()
    ANEMOPHOBIA = auto()
    ASTRAPHOBIA = auto()
    BRONTOPHOBIA = auto()
    CERAUNOPHOBIA = auto()
    CHIONOPHOBIA = auto()
    CHIONOTHYELLAPHOBIA = auto()
    CYCLONOPHOBIA = auto()
    CYMOPHOBIA = auto()
    FRIGORIPHOBIA = auto()
    GRANDOPHOBIA = auto()
    HOMICHLOPHOBIA = auto()
    HUMIDOPHOBIA = auto()
    METEOPHOBIA = auto()
    NEBULOPHOBIA = auto()
    NEPHOPHOBIA = auto()
    OMBROPHOBIA = auto()
    PLUVIFRIGOPHOBIA = auto()
    SERENOPHOBIA = auto()
    TEMPESTAPHOBIA = auto()


WEATHER_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    WeatherPhobiasDescriptions.AESTOPHOBIA: {
        Languages.ENGLISH: "Fear of hot weather (branch of meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.ANEMOPHOBIA: {
        Languages.ENGLISH: "Fear of winds or drafts (branch of meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.ASTRAPHOBIA: {
        Languages.ENGLISH: "Fear of thunder and lightning (branch of meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.BRONTOPHOBIA: {
        Languages.ENGLISH: "Fear of thunder (branch of astraphobia & meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.CERAUNOPHOBIA: {
        Languages.ENGLISH: "Fear of lightning (branch of astraphobia & tempestaphobia & meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.CHIONOPHOBIA: {
        Languages.ENGLISH: "Fear of snow (branch of meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.CHIONOTHYELLAPHOBIA: {
        Languages.ENGLISH: "Fear of blizzards (branch of chionophobia & meteophobia & tempestaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.CYCLONOPHOBIA: {
        Languages.ENGLISH: "Fear of tropical cyclones (branch of lilapsophobia and meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.CYMOPHOBIA: {
        Languages.ENGLISH: "Fear of wind-driven waves (branch of meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.FRIGORIPHOBIA: {
        Languages.ENGLISH: "Fear of cold weather (branch of meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.GRANDOPHOBIA: {
        Languages.ENGLISH: "Fear of hail (branch of meteophobia & tempestaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.HOMICHLOPHOBIA: {
        Languages.ENGLISH: "Fear of fog (branch of nebulophobia & meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.HUMIDOPHOBIA: {
        Languages.ENGLISH: "Fear of humidity (branch of meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.METEOPHOBIA: {
        Languages.ENGLISH: "Fear of weather",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.NEBULOPHOBIA: {
        Languages.ENGLISH: "Fear of fog or clouds (branch of meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.NEPHOPHOBIA: {
        Languages.ENGLISH: "Fear of clouds (branch of nebulophobia & meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.OMBROPHOBIA: {
        Languages.ENGLISH: "Fear of rain or of being rained on (branch of meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.PLUVIFRIGOPHOBIA: {
        Languages.ENGLISH: "Fear of freezing rain (branch of meteophoia & ombrophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.SERENOPHOBIA: {
        Languages.ENGLISH: "Fear of fair weather (branch of meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    WeatherPhobiasDescriptions.TEMPESTAPHOBIA: {
        Languages.ENGLISH: "Fear of storms (branch of meteophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
