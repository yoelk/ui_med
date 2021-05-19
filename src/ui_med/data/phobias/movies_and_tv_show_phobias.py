from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class MoviesAndTvShowPhobias(Enum):
    """
    Movies And Tv Show Phobias Names
    """
    ALADDINPHOBIA = auto()
    BARNEYPHOBIA = auto()
    CALLOUIPHOBIA = auto()
    CANDYMANPHOBIA = auto()
    CINDERELLAPHOBIA = auto()
    CINEPHOBIA = auto()
    COSMOBELLOPHOBIA = auto()
    DARIAPHOBIA = auto()
    DRAGONBALLPHOBIA = auto()
    NUMBERBLOCKIPHOBIA = auto()
    TVSHOWPHOBIA = auto()


MOVIES_AND_TV_SHOW_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    MoviesAndTvShowPhobias.ALADDINPHOBIA: {
        Languages.ENGLISH: "Aladdinphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobias.BARNEYPHOBIA: {
        Languages.ENGLISH: "Barneyphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobias.CALLOUIPHOBIA: {
        Languages.ENGLISH: "Callouiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobias.CANDYMANPHOBIA: {
        Languages.ENGLISH: "Candymanphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobias.CINDERELLAPHOBIA: {
        Languages.ENGLISH: "Cinderellaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobias.CINEPHOBIA: {
        Languages.ENGLISH: "Cinephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobias.COSMOBELLOPHOBIA: {
        Languages.ENGLISH: "Cosmobellophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobias.DARIAPHOBIA: {
        Languages.ENGLISH: "Dariaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobias.DRAGONBALLPHOBIA: {
        Languages.ENGLISH: "Dragonballphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobias.NUMBERBLOCKIPHOBIA: {
        Languages.ENGLISH: "Numberblockiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobias.TVSHOWPHOBIA: {
        Languages.ENGLISH: "Tvshowphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class MoviesAndTvShowPhobiasDescriptions(Enum):
    """
    Movies And Tv Show Phobias Descriptions
    """
    ALADDINPHOBIA = auto()
    BARNEYPHOBIA = auto()
    CALLOUIPHOBIA = auto()
    CANDYMANPHOBIA = auto()
    CINDERELLAPHOBIA = auto()
    CINEPHOBIA = auto()
    COSMOBELLOPHOBIA = auto()
    DARIAPHOBIA = auto()
    DRAGONBALLPHOBIA = auto()
    NUMBERBLOCKIPHOBIA = auto()
    TVSHOWPHOBIA = auto()


MOVIES_AND_TV_SHOW_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    MoviesAndTvShowPhobiasDescriptions.ALADDINPHOBIA: {
        Languages.ENGLISH: "Fear of the disney movie aladdin (branch of cinephobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobiasDescriptions.BARNEYPHOBIA: {
        Languages.ENGLISH: "Fear of the kids show barney (branch of tvshowphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobiasDescriptions.CALLOUIPHOBIA: {
        Languages.ENGLISH: "Fear of the kids show caillou (branch of tvshowphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobiasDescriptions.CANDYMANPHOBIA: {
        Languages.ENGLISH: "Fear of the horror movie candyman (branch of cinephobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobiasDescriptions.CINDERELLAPHOBIA: {
        Languages.ENGLISH: "Fear of the disney movie cinderella (branch of cinephobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobiasDescriptions.CINEPHOBIA: {
        Languages.ENGLISH: "Fear of movies",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobiasDescriptions.COSMOBELLOPHOBIA: {
        Languages.ENGLISH: "Fear of the space fantasy movie star wars (branch of cinephobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobiasDescriptions.DARIAPHOBIA: {
        Languages.ENGLISH: "Fear of the cartoon daria (dranch of tvshowphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobiasDescriptions.DRAGONBALLPHOBIA: {
        Languages.ENGLISH: "Fear of the anime dragonball z (branch of tvshowphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobiasDescriptions.NUMBERBLOCKIPHOBIA: {
        Languages.ENGLISH: "Fear of the kids show numberblocks (branch of tvshowphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    MoviesAndTvShowPhobiasDescriptions.TVSHOWPHOBIA: {
        Languages.ENGLISH: "Fear of tv shows",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
