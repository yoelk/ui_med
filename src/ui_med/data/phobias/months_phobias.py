from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class MonthsPhobias(Enum):
    """
    Months Phobias Names
    """
    BAYUEPHOBIA = auto()
    CHAPITGOEPHOBIA = auto()
    ERYUEPHOBIA = auto()
    JIUYUEPHOBIA = auto()
    LIUYUEPHOBIA = auto()
    QIYUEPHOBIA = auto()
    SANYUEPHOBIA = auto()
    SHIERYUEPHOBIA = auto()
    SHIYUEPHOBIA = auto()
    SIYUEPHOBIA = auto()
    WUYUEPHOBIA = auto()
    YIYUEPHOBIA = auto()


MONTHS_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    MonthsPhobias.BAYUEPHOBIA: {
        Languages.ENGLISH: "Bayuephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobias.CHAPITGOEPHOBIA: {
        Languages.ENGLISH: "Chapitgoephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobias.ERYUEPHOBIA: {
        Languages.ENGLISH: "Eryuephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobias.JIUYUEPHOBIA: {
        Languages.ENGLISH: "Jiuyuephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobias.LIUYUEPHOBIA: {
        Languages.ENGLISH: "Liuyuephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobias.QIYUEPHOBIA: {
        Languages.ENGLISH: "Qiyuephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobias.SANYUEPHOBIA: {
        Languages.ENGLISH: "Sanyuephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobias.SHIERYUEPHOBIA: {
        Languages.ENGLISH: "Shieryuephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobias.SHIYUEPHOBIA: {
        Languages.ENGLISH: "Shiyuephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobias.SIYUEPHOBIA: {
        Languages.ENGLISH: "Siyuephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobias.WUYUEPHOBIA: {
        Languages.ENGLISH: "Wuyuephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobias.YIYUEPHOBIA: {
        Languages.ENGLISH: "Yiyuephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class MonthsPhobiasDescriptions(Enum):
    """
    Months Phobias Descriptions
    """
    BAYUEPHOBIA = auto()
    CHAPITGOEPHOBIA = auto()
    ERYUEPHOBIA = auto()
    JIUYUEPHOBIA = auto()
    LIUYUEPHOBIA = auto()
    QIYUEPHOBIA = auto()
    SANYUEPHOBIA = auto()
    SHIERYUEPHOBIA = auto()
    SHIYUEPHOBIA = auto()
    SIYUEPHOBIA = auto()
    WUYUEPHOBIA = auto()
    YIYUEPHOBIA = auto()


MONTHS_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    MonthsPhobiasDescriptions.BAYUEPHOBIA: {
        Languages.ENGLISH: "Fear of august",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobiasDescriptions.CHAPITGOEPHOBIA: {
        Languages.ENGLISH: "Fear of november",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobiasDescriptions.ERYUEPHOBIA: {
        Languages.ENGLISH: "Fear of february",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobiasDescriptions.JIUYUEPHOBIA: {
        Languages.ENGLISH: "Fear of september",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobiasDescriptions.LIUYUEPHOBIA: {
        Languages.ENGLISH: "Fear of june",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobiasDescriptions.QIYUEPHOBIA: {
        Languages.ENGLISH: "Fear of july",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobiasDescriptions.SANYUEPHOBIA: {
        Languages.ENGLISH: "Fear of march",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobiasDescriptions.SHIERYUEPHOBIA: {
        Languages.ENGLISH: "Fear of december",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobiasDescriptions.SHIYUEPHOBIA: {
        Languages.ENGLISH: "Fear of october",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobiasDescriptions.SIYUEPHOBIA: {
        Languages.ENGLISH: "Fear of april",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobiasDescriptions.WUYUEPHOBIA: {
        Languages.ENGLISH: "Fear of may",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MonthsPhobiasDescriptions.YIYUEPHOBIA: {
        Languages.ENGLISH: "Fear of january",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
