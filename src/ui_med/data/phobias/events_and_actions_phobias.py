from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class EventsAndActionsPhobias(Enum):
    """
    Events And Actions Phobias Names
    """
    ABDUCTOPHOBIA = auto()
    ABLUTOPHOBIA = auto()
    ABOREANISPHOBIA = auto()
    ACATOPTROPHOBIA = auto()
    ACCIDENSOPHOBIA = auto()
    ADDITIONPHOBIA = auto()
    ADHAESITOPHOBIA = auto()
    AELOSACCOPHOBIA = auto()
    AEROPHOBIA = auto()
    AGORAPHOBIA = auto()
    AGRAPHOBIA = auto()
    AGYROPHOBIA = auto()
    ALEMERCIALICEPTIOPHOBIA = auto()
    ALIENABDUCTOPHOBIA = auto()
    ALTHAZAGORAPHOBIA = auto()
    AMBULOPHOBIA = auto()
    STASIPHOBIA = auto()
    AMMIDYPHOBIA = auto()
    AMMOPHOBIA = auto()
    AMMOSOPHOBIA = auto()
    AMYCHOPHOBIA = auto()
    ANABLEPHOBIA = auto()
    ANAGNOSMAPHOBIA = auto()
    ANALAFROPHOBIA = auto()
    ANAPODAPHOBIA = auto()
    ANATIDAEPHOBIA = auto()
    ANKYLOPHOBIA = auto()
    ANOIXIPHOBIA = auto()
    ANDITCHOPHOBIA = auto()
    ANUPTAPHOBIA = auto()
    APOLLYMOPHOBIA = auto()
    APPLOGROPHINOPHOBIA = auto()
    ATHAZAGORAPHOBIA = auto()
    ATHLIMATAPHOBIA = auto()
    ATOMOSOPHOBIA = auto()
    ATYCHIPHOBIA = auto()
    KAKORRHAPHIOPHOBIA = auto()
    AUCHLOCLAUSTROPHOBIA = auto()
    AUTODYSOMOPHOBIA = auto()
    AUTOVOCALPHOBIA = auto()
    AVIOPHOBIA = auto()
    BACKTOSCHOOLAPHOBIA = auto()
    BAOWENPHOBIA = auto()
    BASIPHOBIA = auto()
    BASOPHOBIA = auto()
    BATOPHOBIA = auto()
    BIAPHOBIA = auto()
    BIOCHRONOPHOBIA = auto()
    BIOPHOBIA = auto()
    BIOTRIOCULARMECHANOPHOBIA = auto()
    BOITANOPHOBIA = auto()
    BROWNOUTPHOBIA = auto()
    CAPILLUSSETISPHOBIA = auto()
    CAPIOPHOBIA = auto()
    CAPNOPHOBIA = auto()
    CAPTOPHOBIA = auto()
    CASADASTRAPHOBIA = auto()
    CATAGELOPHOBIA = auto()
    CATAPEDAPHOBIA = auto()
    CATASTROPHOBIA = auto()
    CATHISOPHOBIA = auto()
    CEDEIAPHOBIA = auto()
    CHEMOPHOBIA = auto()
    CHOLOLEPUSUPHOBIA = auto()
    CHORIVANTHOKOLYMVISIPHOBIA = auto()
    CHOROPHOBIA = auto()
    CHROMPADAPHOBIA = auto()
    CHRONAPHOBIA = auto()
    CHRONOHODOPHOBIA = auto()
    CHRONOPHOBIA = auto()
    CHTYPIMAPHOBIA = auto()
    CHTYPISOPHOBIA = auto()
    CIDEOPHOBIA = auto()
    CIERIPHOBIA = auto()
    CLARUSPHOBIA = auto()
    CLAUDIPHOBIA = auto()
    CLIMACOPHOBIA = auto()
    CLIMATOPHOBIA = auto()
    CLINOPHOBIA = auto()
    CNIDOPHOBIA = auto()
    COMMUPHOBIA = auto()
    CONTRELTOPHOBIA = auto()
    CONTROVERSUSROGATIOPHOBIA = auto()
    CONVIVOPHOBIA = auto()
    CRAPOSANDWICHOPHOBIA = auto()
    CRYOCHIROPHOBIA = auto()
    CUNNIPHOBIA = auto()
    CYNOLINGOPUGOPHOBIA = auto()
    DAKNOPHOBIA = auto()
    DAKROPHOBIA = auto()
    DATALOSSOPHOBIA = auto()
    DECANNOPHOBIA = auto()
    DECIDOPHOBIA = auto()
    DEIPNOPHOBIA = auto()
    DEKAENNEAORAPHOBIA = auto()
    DEKAEPTAORAPHOBIA = auto()
    DEKAEXIORAPHOBIA = auto()
    DEKAOKTOORAPHOBIA = auto()
    DEKAORAPHOBIA = auto()
    DEKAPENTEORAPHOBIA = auto()
    DEKATESSERAPHOBIA = auto()
    DEKATRIAORAPHOBIA = auto()
    DENTOPHOBIA = auto()
    DEPRECOROPHOBIA = auto()
    DESTIRPEPHOBIA = auto()
    DETRECTOPHOBIA = auto()
    DEUTEROPHOBIA = auto()
    DEVWAHRPHOBIA = auto()
    DIMANCHOPHOBIA = auto()
    DISCONTINUAPHOBIA = auto()
    DISHABILIOPHOBIA = auto()
    DISPOSOPHOBIA = auto()
    DIVISIONPHOBIA = auto()
    DODEKAORAPHOBIA = auto()
    DOLOROPHOBIA = auto()
    DORONOPHOBIA = auto()
    DOXOPHOBIA = auto()
    DUOORAPHOBIA = auto()
    EARCOUNTOPHOBIA = auto()
    ECLEPOHELIOPHOBIA = auto()
    ECOTHERMOPHOBIA = auto()
    EHSANOPHOBIA = auto()
    EKRIXIPHOBIA = auto()
    EMARPHOBIA = auto()
    EMETOPHOBIA = auto()
    ENCAVMAPHOBIA = auto()
    ENOSIOPHOBIA = auto()
    EPISTAXIOPHOBIA = auto()
    EREUTHROPHOBIA = auto()
    ERGALEOPHOBIA = auto()
    ERGASIOPHOBIA = auto()
    ERRATOPHOBIA_(FEAR_OF_MAKING_MISTAKES),_ERROPHOBIA = auto()
    ERUCTOPHOBIA = auto()
    FLATUPHOBIA = auto()
    FLIPFLOPUPHOBIA = auto()
    FOOTBALLPHOBIA = auto()
    FRACTOPHOBIA = auto()
    FRAGAPANOPHOBIA = auto()
    FUMUSTERROREMOPHOBIA = auto()
    GAMOCEDEIAPHOBIA = auto()
    GAMOPHOBIA = auto()
    GARGALAPHOBIA = auto()
    GELOTOPHOBIA = auto()
    GENOPHOBIA = auto()
    GEPHYROPHOBIA = auto()
    GERASCOPHOBIA = auto()
    GLOSSOPHOBIA = auto()
    GOLFPHOBIA = auto()
    GRAPHOPHOBIA = auto()
    GROTHOPHOBIA = auto()
    GRONTHOKOPOPHOBIA = auto()
    HAMARTOPHOBIA = auto()
    HAPHEPHOBIA = auto()
    HARPAXOPHOBIA = auto()
    HEDONOPHOBIA = auto()
    HODOPHOBIA = auto()
    HONEPHOBIA = auto()
    HYPNOPHOBIA = auto()
    IGNITERROREMOPHOBIA = auto()
    INCESTOPHOBIA = auto()
    IPOVLOPSYCHOPHOBIA = auto()
    JACKBOXOPHOBIA = auto()
    JOCOPHOBIA = auto()
    KAKOLOGOPHOBIA = auto()
    KAKONEIROPHOBIA = auto()
    KAKOPHOBIA = auto()
    KELNGOPHOBIA = auto()
    KHEIMONPHOBIA = auto()
    KLEPTOPHOBIA = auto()
    KINETOPTOPHOBIA = auto()
    KOPOPHOBIA = auto()
    KYPHOPHOBIA = auto()
    KYRIAKIPHOBIA = auto()
    LALIOPHOBIA = auto()
    LATROPHOBIA = auto()
    LAMBOPHOBIA = auto()
    LEPTOPHOBIA = auto()
    LITICAPHOBIA = auto()
    LOCKIOPHOBIA = auto()
    LUPOSLIPOPHOBIA = auto()
    MACROPHOBIA = auto()
    MAGEIROCOPHOBIA = auto()
    MASTIGOPHOBIA = auto()
    MATHEMAPHOBIA = auto()
    MEDOMALACUPHOBIA = auto()
    MEDORTHOPHOBIA = auto()
    MERINTHOPHOBIA = auto()
    METATHESIOPHOBIA = auto()
    MIDNIGHTPHOBIA = auto()
    MISVACCINOPHOBIA = auto()
    MITSOPHOBIA = auto()
    MONOXEIDIOANTHRAKASKISIPHOBIA = auto()
    MULTIPLICATIONPHOBIA = auto()
    MYOCLUNUSDIAGPHRAGMAPHOBIA = auto()
    SINGULTOPHOBIA = auto()
    MYSOPHOBIA = auto()
    NATATOPHOBIA = auto()
    NATUROPHOBIA = auto()
    NOMOPHOBIA = auto()
    NONAMOPHOBIA = auto()
    NAIEISAIKAKOPHOBIA = auto()
    NUCLEOMITUPHOBIA = auto()
    NYCTOURINARIPHOBIA = auto()
    OBESOPHOBIA = auto()
    OBLITOPHOBIA = auto()
    DEDISCOPHOBIA = auto()
    OBSCURSOLISPHOBIA = auto()
    OLYMPICPHOBIA = auto()
    ONEIROGMOPHOBIA = auto()
    ONEIROPHOBIA = auto()
    ONEIROPOLIMAPHOBIA = auto()
    ONOMATOPHOBIA = auto()
    OPHTHALMOPHOBIA = auto()
    OPTOPHOBIA = auto()
    PAINTBALLPHOBIA = auto()
    PANTHOPHOBIA = auto()
    PANTREIAPHOBIA = auto()
    PARALIPOPHOBIA = auto()
    PARASKEVIDEKATRIAPHOBIA = auto()
    PERICULOPHOBIA = auto()
    PHAGOPHOBIA = auto()
    PHALACROPHOBIA = auto()
    PHARSAPHOBIA = auto()
    PHILEMAPHOBIA = auto()
    PHRONEMOPHOBIA = auto()
    PICNICPHOBIA = auto()
    PINCHOPHOBIA = auto()
    PIPTOPHOBIA = auto()
    PNIGOPHOBIA = auto()
    PNIGEROPHOBIA = auto()
    POLEMOPHOBIA = auto()
    PONOPHOBIA = auto()
    POSTHOCALYPTROPHOBIA = auto()
    PRESENTATIONPHOPHOBIA = auto()
    PROIPHOBIA = auto()
    PROSCHOPHOBIA = auto()
    PRURITOPHOBIA = auto()
    PSELLISMOPHOBIA = auto()
    PTERONOPHOBIA = auto()
    PUNGOPHOBIA = auto()
    PURASKISIPHOBIA = auto()
    QUESTIOPHOBIA = auto()
    QUEUNLISKANPHOBIA = auto()
    RHABDOPHOBIA = auto()
    RHYPOPHOBIA = auto()
    RUNDFUPHOBIA = auto()
    SARMASSOPHOBIA = auto()
    SCOPOPHOBIA = auto()
    SCRIPTOPHOBIA = auto()
    SCYTHEPHOBIA = auto()
    SEISMOPHOBIA = auto()
    SEISMOASKISIPHOBIA = auto()
    SELAPHOBIA = auto()
    SEXOPHOBIA = auto()
    SIENTOPHOBIA = auto()
    SIFOUNASKISIPHOBIA = auto()
    SNAPOPHOBIA = auto()
    SOCCERPHOBIA = auto()
    SOCIAPHOBIA = auto()
    SOMNIPHOBIA = auto()
    SOPHOPHOBIA = auto()
    STANIOPHOBIA = auto()
    STASIHYELOPHOBIA = auto()
    STERNUTAPHOBIA = auto()
    STUBAPHOBIA = auto()
    SUBTERRANEAPREMORTEPHOBIA = auto()
    SUBTRACTIONPHOBIA = auto()
    TAPHEPHOBIA = auto()
    TELEPHONOPHOBIA = auto()
    TELEVISIOPHOBIA = auto()
    TELOCHRONOPHOBIA = auto()
    TENNISPHOBIA = auto()
    TESTOPHOBIA = auto()
    THANATOPHOBIA = auto()
    THEROPHOBIA = auto()
    THINOPOROPHOBIA = auto()
    TOKOPHOBIA = auto()
    TOMOPHOBIA = auto()
    TONSUREPHOBIA = auto()
    TOXIPHOBIA = auto()
    TRAUMAPHOBIA = auto()
    TRAUMATOPHOBIA = auto()
    TREMOPHOBIA = auto()
    TROPOPHOBIA = auto()
    TSUNAMIPHOBIA = auto()
    TUSSAPHOBIA = auto()
    URINOPHOBIA = auto()
    VICTOROPHOBIA = auto()
    VINYLPHOBIA = auto()
    VIVIAPHOBIA = auto()
    VOLCANOPHOBIA = auto()
    VOLLEYBALLPHOBIA = auto()
    WANSHANGPHOBIA = auto()
    XIAWUPHOBIA = auto()


EVENTS_AND_ACTIONS_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    EventsAndActionsPhobias.ABDUCTOPHOBIA: {
        Languages.ENGLISH: "Abductophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ABLUTOPHOBIA: {
        Languages.ENGLISH: "Ablutophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ABOREANISPHOBIA: {
        Languages.ENGLISH: "Aboreanisphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ACATOPTROPHOBIA: {
        Languages.ENGLISH: "Acatoptrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ACCIDENSOPHOBIA: {
        Languages.ENGLISH: "Accidensophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ADDITIONPHOBIA: {
        Languages.ENGLISH: "Additionphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ADHAESITOPHOBIA: {
        Languages.ENGLISH: "Adhaesitophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AELOSACCOPHOBIA: {
        Languages.ENGLISH: "Aelosaccophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AEROPHOBIA: {
        Languages.ENGLISH: "Aerophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AGORAPHOBIA: {
        Languages.ENGLISH: "Agoraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AGRAPHOBIA: {
        Languages.ENGLISH: "Agraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AGYROPHOBIA: {
        Languages.ENGLISH: "Agyrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ALEMERCIALICEPTIOPHOBIA: {
        Languages.ENGLISH: "Alemercialiceptiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ALIENABDUCTOPHOBIA: {
        Languages.ENGLISH: "Alienabductophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ALTHAZAGORAPHOBIA: {
        Languages.ENGLISH: "Althazagoraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AMBULOPHOBIA: {
        Languages.ENGLISH: "Ambulophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.STASIPHOBIA: {
        Languages.ENGLISH: "Stasiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AMMIDYPHOBIA: {
        Languages.ENGLISH: "Ammidyphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AMMOPHOBIA: {
        Languages.ENGLISH: "Ammophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AMMOSOPHOBIA: {
        Languages.ENGLISH: "Ammosophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AMYCHOPHOBIA: {
        Languages.ENGLISH: "Amychophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ANABLEPHOBIA: {
        Languages.ENGLISH: "Anablephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ANAGNOSMAPHOBIA: {
        Languages.ENGLISH: "Anagnosmaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ANALAFROPHOBIA: {
        Languages.ENGLISH: "Analafrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ANAPODAPHOBIA: {
        Languages.ENGLISH: "Anapodaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ANATIDAEPHOBIA: {
        Languages.ENGLISH: "Anatidaephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ANKYLOPHOBIA: {
        Languages.ENGLISH: "Ankylophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ANOIXIPHOBIA: {
        Languages.ENGLISH: "Anoixiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ANDITCHOPHOBIA: {
        Languages.ENGLISH: "Anditchophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ANUPTAPHOBIA: {
        Languages.ENGLISH: "Anuptaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.APOLLYMOPHOBIA: {
        Languages.ENGLISH: "Apollymophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.APPLOGROPHINOPHOBIA: {
        Languages.ENGLISH: "Applogrophinophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ATHAZAGORAPHOBIA: {
        Languages.ENGLISH: "Athazagoraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ATHLIMATAPHOBIA: {
        Languages.ENGLISH: "Athlimataphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ATOMOSOPHOBIA: {
        Languages.ENGLISH: "Atomosophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ATYCHIPHOBIA: {
        Languages.ENGLISH: "Atychiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.KAKORRHAPHIOPHOBIA: {
        Languages.ENGLISH: "Kakorrhaphiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AUCHLOCLAUSTROPHOBIA: {
        Languages.ENGLISH: "Auchloclaustrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AUTODYSOMOPHOBIA: {
        Languages.ENGLISH: "Autodysomophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AUTOVOCALPHOBIA: {
        Languages.ENGLISH: "Autovocalphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.AVIOPHOBIA: {
        Languages.ENGLISH: "Aviophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.BACKTOSCHOOLAPHOBIA: {
        Languages.ENGLISH: "Backtoschoolaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.BAOWENPHOBIA: {
        Languages.ENGLISH: "Baowenphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.BASIPHOBIA: {
        Languages.ENGLISH: "Basiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.BASOPHOBIA: {
        Languages.ENGLISH: "Basophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.BATOPHOBIA: {
        Languages.ENGLISH: "Batophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.BIAPHOBIA: {
        Languages.ENGLISH: "Biaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.BIOCHRONOPHOBIA: {
        Languages.ENGLISH: "Biochronophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.BIOPHOBIA: {
        Languages.ENGLISH: "Biophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.BIOTRIOCULARMECHANOPHOBIA: {
        Languages.ENGLISH: "Biotriocularmechanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.BOITANOPHOBIA: {
        Languages.ENGLISH: "Boitanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.BROWNOUTPHOBIA: {
        Languages.ENGLISH: "Brownoutphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CAPILLUSSETISPHOBIA: {
        Languages.ENGLISH: "Capillussetisphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CAPIOPHOBIA: {
        Languages.ENGLISH: "Capiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CAPNOPHOBIA: {
        Languages.ENGLISH: "Capnophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CAPTOPHOBIA: {
        Languages.ENGLISH: "Captophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CASADASTRAPHOBIA: {
        Languages.ENGLISH: "Casadastraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CATAGELOPHOBIA: {
        Languages.ENGLISH: "Catagelophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CATAPEDAPHOBIA: {
        Languages.ENGLISH: "Catapedaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CATASTROPHOBIA: {
        Languages.ENGLISH: "Catastrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CATHISOPHOBIA: {
        Languages.ENGLISH: "Cathisophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CEDEIAPHOBIA: {
        Languages.ENGLISH: "Cedeiaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CHEMOPHOBIA: {
        Languages.ENGLISH: "Chemophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CHOLOLEPUSUPHOBIA: {
        Languages.ENGLISH: "Chololepusuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CHORIVANTHOKOLYMVISIPHOBIA: {
        Languages.ENGLISH: "Chorivanthokolymvisiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CHOROPHOBIA: {
        Languages.ENGLISH: "Chorophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CHROMPADAPHOBIA: {
        Languages.ENGLISH: "Chrompadaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CHRONAPHOBIA: {
        Languages.ENGLISH: "Chronaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CHRONOHODOPHOBIA: {
        Languages.ENGLISH: "Chronohodophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CHRONOPHOBIA: {
        Languages.ENGLISH: "Chronophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CHTYPIMAPHOBIA: {
        Languages.ENGLISH: "Chtypimaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CHTYPISOPHOBIA: {
        Languages.ENGLISH: "Chtypisophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CIDEOPHOBIA: {
        Languages.ENGLISH: "Cideophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CIERIPHOBIA: {
        Languages.ENGLISH: "Cieriphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CLARUSPHOBIA: {
        Languages.ENGLISH: "Clarusphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CLAUDIPHOBIA: {
        Languages.ENGLISH: "Claudiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CLIMACOPHOBIA: {
        Languages.ENGLISH: "Climacophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CLIMATOPHOBIA: {
        Languages.ENGLISH: "Climatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CLINOPHOBIA: {
        Languages.ENGLISH: "Clinophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CNIDOPHOBIA: {
        Languages.ENGLISH: "Cnidophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.COMMUPHOBIA: {
        Languages.ENGLISH: "Commuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CONTRELTOPHOBIA: {
        Languages.ENGLISH: "Contreltophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CONTROVERSUSROGATIOPHOBIA: {
        Languages.ENGLISH: "Controversusrogatiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CONVIVOPHOBIA: {
        Languages.ENGLISH: "Convivophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CRAPOSANDWICHOPHOBIA: {
        Languages.ENGLISH: "Craposandwichophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CRYOCHIROPHOBIA: {
        Languages.ENGLISH: "Cryochirophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CUNNIPHOBIA: {
        Languages.ENGLISH: "Cunniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.CYNOLINGOPUGOPHOBIA: {
        Languages.ENGLISH: "Cynolingopugophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DAKNOPHOBIA: {
        Languages.ENGLISH: "Daknophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DAKROPHOBIA: {
        Languages.ENGLISH: "Dakrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DATALOSSOPHOBIA: {
        Languages.ENGLISH: "Datalossophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DECANNOPHOBIA: {
        Languages.ENGLISH: "Decannophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DECIDOPHOBIA: {
        Languages.ENGLISH: "Decidophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DEIPNOPHOBIA: {
        Languages.ENGLISH: "Deipnophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DEKAENNEAORAPHOBIA: {
        Languages.ENGLISH: "Dekaenneaoraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DEKAEPTAORAPHOBIA: {
        Languages.ENGLISH: "Dekaeptaoraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DEKAEXIORAPHOBIA: {
        Languages.ENGLISH: "Dekaexioraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DEKAOKTOORAPHOBIA: {
        Languages.ENGLISH: "Dekaoktooraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DEKAORAPHOBIA: {
        Languages.ENGLISH: "Dekaoraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DEKAPENTEORAPHOBIA: {
        Languages.ENGLISH: "Dekapenteoraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DEKATESSERAPHOBIA: {
        Languages.ENGLISH: "Dekatesseraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DEKATRIAORAPHOBIA: {
        Languages.ENGLISH: "Dekatriaoraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DENTOPHOBIA: {
        Languages.ENGLISH: "Dentophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DEPRECOROPHOBIA: {
        Languages.ENGLISH: "Deprecorophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DESTIRPEPHOBIA: {
        Languages.ENGLISH: "Destirpephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DETRECTOPHOBIA: {
        Languages.ENGLISH: "Detrectophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DEUTEROPHOBIA: {
        Languages.ENGLISH: "Deuterophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DEVWAHRPHOBIA: {
        Languages.ENGLISH: "Devwahrphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DIMANCHOPHOBIA: {
        Languages.ENGLISH: "Dimanchophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DISCONTINUAPHOBIA: {
        Languages.ENGLISH: "Discontinuaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DISHABILIOPHOBIA: {
        Languages.ENGLISH: "Dishabiliophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DISPOSOPHOBIA: {
        Languages.ENGLISH: "Disposophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DIVISIONPHOBIA: {
        Languages.ENGLISH: "Divisionphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DODEKAORAPHOBIA: {
        Languages.ENGLISH: "Dodekaoraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DOLOROPHOBIA: {
        Languages.ENGLISH: "Dolorophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DORONOPHOBIA: {
        Languages.ENGLISH: "Doronophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DOXOPHOBIA: {
        Languages.ENGLISH: "Doxophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DUOORAPHOBIA: {
        Languages.ENGLISH: "Duooraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.EARCOUNTOPHOBIA: {
        Languages.ENGLISH: "Earcountophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ECLEPOHELIOPHOBIA: {
        Languages.ENGLISH: "Eclepoheliophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ECOTHERMOPHOBIA: {
        Languages.ENGLISH: "Ecothermophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.EHSANOPHOBIA: {
        Languages.ENGLISH: "Ehsanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.EKRIXIPHOBIA: {
        Languages.ENGLISH: "Ekrixiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.EMARPHOBIA: {
        Languages.ENGLISH: "Emarphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.EMETOPHOBIA: {
        Languages.ENGLISH: "Emetophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ENCAVMAPHOBIA: {
        Languages.ENGLISH: "Encavmaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ENOSIOPHOBIA: {
        Languages.ENGLISH: "Enosiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.EPISTAXIOPHOBIA: {
        Languages.ENGLISH: "Epistaxiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.EREUTHROPHOBIA: {
        Languages.ENGLISH: "Ereuthrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ERGALEOPHOBIA: {
        Languages.ENGLISH: "Ergaleophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ERGASIOPHOBIA: {
        Languages.ENGLISH: "Ergasiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ERRATOPHOBIA_(FEAR_OF_MAKING_MISTAKES),_ERROPHOBIA: {
        Languages.ENGLISH: "Erratophobia (Fear Of Making Mistakes), Errophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ERUCTOPHOBIA: {
        Languages.ENGLISH: "Eructophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.FLATUPHOBIA: {
        Languages.ENGLISH: "Flatuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.FLIPFLOPUPHOBIA: {
        Languages.ENGLISH: "Flipflopuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.FOOTBALLPHOBIA: {
        Languages.ENGLISH: "Footballphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.FRACTOPHOBIA: {
        Languages.ENGLISH: "Fractophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.FRAGAPANOPHOBIA: {
        Languages.ENGLISH: "Fragapanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.FUMUSTERROREMOPHOBIA: {
        Languages.ENGLISH: "Fumusterroremophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.GAMOCEDEIAPHOBIA: {
        Languages.ENGLISH: "Gamocedeiaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.GAMOPHOBIA: {
        Languages.ENGLISH: "Gamophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.GARGALAPHOBIA: {
        Languages.ENGLISH: "Gargalaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.GELOTOPHOBIA: {
        Languages.ENGLISH: "Gelotophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.GENOPHOBIA: {
        Languages.ENGLISH: "Genophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.GEPHYROPHOBIA: {
        Languages.ENGLISH: "Gephyrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.GERASCOPHOBIA: {
        Languages.ENGLISH: "Gerascophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.GLOSSOPHOBIA: {
        Languages.ENGLISH: "Glossophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.GOLFPHOBIA: {
        Languages.ENGLISH: "Golfphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.GRAPHOPHOBIA: {
        Languages.ENGLISH: "Graphophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.GROTHOPHOBIA: {
        Languages.ENGLISH: "Grothophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.GRONTHOKOPOPHOBIA: {
        Languages.ENGLISH: "Gronthokopophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.HAMARTOPHOBIA: {
        Languages.ENGLISH: "Hamartophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.HAPHEPHOBIA: {
        Languages.ENGLISH: "Haphephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.HARPAXOPHOBIA: {
        Languages.ENGLISH: "Harpaxophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.HEDONOPHOBIA: {
        Languages.ENGLISH: "Hedonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.HODOPHOBIA: {
        Languages.ENGLISH: "Hodophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.HONEPHOBIA: {
        Languages.ENGLISH: "Honephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.HYPNOPHOBIA: {
        Languages.ENGLISH: "Hypnophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.IGNITERROREMOPHOBIA: {
        Languages.ENGLISH: "Igniterroremophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.INCESTOPHOBIA: {
        Languages.ENGLISH: "Incestophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.IPOVLOPSYCHOPHOBIA: {
        Languages.ENGLISH: "Ipovlopsychophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.JACKBOXOPHOBIA: {
        Languages.ENGLISH: "Jackboxophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.JOCOPHOBIA: {
        Languages.ENGLISH: "Jocophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.KAKOLOGOPHOBIA: {
        Languages.ENGLISH: "Kakologophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.KAKONEIROPHOBIA: {
        Languages.ENGLISH: "Kakoneirophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.KAKOPHOBIA: {
        Languages.ENGLISH: "Kakophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.KELNGOPHOBIA: {
        Languages.ENGLISH: "Kelngophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.KHEIMONPHOBIA: {
        Languages.ENGLISH: "Kheimonphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.KLEPTOPHOBIA: {
        Languages.ENGLISH: "Kleptophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.KINETOPTOPHOBIA: {
        Languages.ENGLISH: "Kinetoptophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.KOPOPHOBIA: {
        Languages.ENGLISH: "Kopophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.KYPHOPHOBIA: {
        Languages.ENGLISH: "Kyphophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.KYRIAKIPHOBIA: {
        Languages.ENGLISH: "Kyriakiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.LALIOPHOBIA: {
        Languages.ENGLISH: "Laliophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.LATROPHOBIA: {
        Languages.ENGLISH: "Latrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.LAMBOPHOBIA: {
        Languages.ENGLISH: "Lambophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.LEPTOPHOBIA: {
        Languages.ENGLISH: "Leptophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.LITICAPHOBIA: {
        Languages.ENGLISH: "Liticaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.LOCKIOPHOBIA: {
        Languages.ENGLISH: "Lockiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.LUPOSLIPOPHOBIA: {
        Languages.ENGLISH: "Luposlipophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MACROPHOBIA: {
        Languages.ENGLISH: "Macrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MAGEIROCOPHOBIA: {
        Languages.ENGLISH: "Mageirocophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MASTIGOPHOBIA: {
        Languages.ENGLISH: "Mastigophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MATHEMAPHOBIA: {
        Languages.ENGLISH: "Mathemaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MEDOMALACUPHOBIA: {
        Languages.ENGLISH: "Medomalacuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MEDORTHOPHOBIA: {
        Languages.ENGLISH: "Medorthophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MERINTHOPHOBIA: {
        Languages.ENGLISH: "Merinthophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.METATHESIOPHOBIA: {
        Languages.ENGLISH: "Metathesiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MIDNIGHTPHOBIA: {
        Languages.ENGLISH: "Midnightphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MISVACCINOPHOBIA: {
        Languages.ENGLISH: "Misvaccinophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MITSOPHOBIA: {
        Languages.ENGLISH: "Mitsophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MONOXEIDIOANTHRAKASKISIPHOBIA: {
        Languages.ENGLISH: "Monoxeidioanthrakaskisiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MULTIPLICATIONPHOBIA: {
        Languages.ENGLISH: "Multiplicationphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MYOCLUNUSDIAGPHRAGMAPHOBIA: {
        Languages.ENGLISH: "Myoclunusdiagphragmaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SINGULTOPHOBIA: {
        Languages.ENGLISH: "Singultophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.MYSOPHOBIA: {
        Languages.ENGLISH: "Mysophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.NATATOPHOBIA: {
        Languages.ENGLISH: "Natatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.NATUROPHOBIA: {
        Languages.ENGLISH: "Naturophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.NOMOPHOBIA: {
        Languages.ENGLISH: "Nomophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.NONAMOPHOBIA: {
        Languages.ENGLISH: "Nonamophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.NAIEISAIKAKOPHOBIA: {
        Languages.ENGLISH: "Naieisaikakophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.NUCLEOMITUPHOBIA: {
        Languages.ENGLISH: "Nucleomituphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.NYCTOURINARIPHOBIA: {
        Languages.ENGLISH: "Nyctourinariphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.OBESOPHOBIA: {
        Languages.ENGLISH: "Obesophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.OBLITOPHOBIA: {
        Languages.ENGLISH: "Oblitophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.DEDISCOPHOBIA: {
        Languages.ENGLISH: "Dediscophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.OBSCURSOLISPHOBIA: {
        Languages.ENGLISH: "Obscursolisphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.OLYMPICPHOBIA: {
        Languages.ENGLISH: "Olympicphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ONEIROGMOPHOBIA: {
        Languages.ENGLISH: "Oneirogmophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ONEIROPHOBIA: {
        Languages.ENGLISH: "Oneirophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ONEIROPOLIMAPHOBIA: {
        Languages.ENGLISH: "Oneiropolimaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.ONOMATOPHOBIA: {
        Languages.ENGLISH: "Onomatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.OPHTHALMOPHOBIA: {
        Languages.ENGLISH: "Ophthalmophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.OPTOPHOBIA: {
        Languages.ENGLISH: "Optophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PAINTBALLPHOBIA: {
        Languages.ENGLISH: "Paintballphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PANTHOPHOBIA: {
        Languages.ENGLISH: "Panthophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PANTREIAPHOBIA: {
        Languages.ENGLISH: "Pantreiaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PARALIPOPHOBIA: {
        Languages.ENGLISH: "Paralipophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PARASKEVIDEKATRIAPHOBIA: {
        Languages.ENGLISH: "Paraskevidekatriaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PERICULOPHOBIA: {
        Languages.ENGLISH: "Periculophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PHAGOPHOBIA: {
        Languages.ENGLISH: "Phagophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PHALACROPHOBIA: {
        Languages.ENGLISH: "Phalacrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PHARSAPHOBIA: {
        Languages.ENGLISH: "Pharsaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PHILEMAPHOBIA: {
        Languages.ENGLISH: "Philemaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PHRONEMOPHOBIA: {
        Languages.ENGLISH: "Phronemophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PICNICPHOBIA: {
        Languages.ENGLISH: "Picnicphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PINCHOPHOBIA: {
        Languages.ENGLISH: "Pinchophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PIPTOPHOBIA: {
        Languages.ENGLISH: "Piptophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PNIGOPHOBIA: {
        Languages.ENGLISH: "Pnigophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PNIGEROPHOBIA: {
        Languages.ENGLISH: "Pnigerophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.POLEMOPHOBIA: {
        Languages.ENGLISH: "Polemophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PONOPHOBIA: {
        Languages.ENGLISH: "Ponophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.POSTHOCALYPTROPHOBIA: {
        Languages.ENGLISH: "Posthocalyptrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PRESENTATIONPHOPHOBIA: {
        Languages.ENGLISH: "Presentationphophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PROIPHOBIA: {
        Languages.ENGLISH: "Proiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PROSCHOPHOBIA: {
        Languages.ENGLISH: "Proschophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PRURITOPHOBIA: {
        Languages.ENGLISH: "Pruritophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PSELLISMOPHOBIA: {
        Languages.ENGLISH: "Psellismophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PTERONOPHOBIA: {
        Languages.ENGLISH: "Pteronophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PUNGOPHOBIA: {
        Languages.ENGLISH: "Pungophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.PURASKISIPHOBIA: {
        Languages.ENGLISH: "Puraskisiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.QUESTIOPHOBIA: {
        Languages.ENGLISH: "Questiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.QUEUNLISKANPHOBIA: {
        Languages.ENGLISH: "Queunliskanphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.RHABDOPHOBIA: {
        Languages.ENGLISH: "Rhabdophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.RHYPOPHOBIA: {
        Languages.ENGLISH: "Rhypophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.RUNDFUPHOBIA: {
        Languages.ENGLISH: "Rundfuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SARMASSOPHOBIA: {
        Languages.ENGLISH: "Sarmassophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SCOPOPHOBIA: {
        Languages.ENGLISH: "Scopophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SCRIPTOPHOBIA: {
        Languages.ENGLISH: "Scriptophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SCYTHEPHOBIA: {
        Languages.ENGLISH: "Scythephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SEISMOPHOBIA: {
        Languages.ENGLISH: "Seismophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SEISMOASKISIPHOBIA: {
        Languages.ENGLISH: "Seismoaskisiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SELAPHOBIA: {
        Languages.ENGLISH: "Selaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SEXOPHOBIA: {
        Languages.ENGLISH: "Sexophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SIENTOPHOBIA: {
        Languages.ENGLISH: "Sientophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SIFOUNASKISIPHOBIA: {
        Languages.ENGLISH: "Sifounaskisiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SNAPOPHOBIA: {
        Languages.ENGLISH: "Snapophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SOCCERPHOBIA: {
        Languages.ENGLISH: "Soccerphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SOCIAPHOBIA: {
        Languages.ENGLISH: "Sociaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SOMNIPHOBIA: {
        Languages.ENGLISH: "Somniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SOPHOPHOBIA: {
        Languages.ENGLISH: "Sophophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.STANIOPHOBIA: {
        Languages.ENGLISH: "Staniophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.STASIHYELOPHOBIA: {
        Languages.ENGLISH: "Stasihyelophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.STERNUTAPHOBIA: {
        Languages.ENGLISH: "Sternutaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.STUBAPHOBIA: {
        Languages.ENGLISH: "Stubaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SUBTERRANEAPREMORTEPHOBIA: {
        Languages.ENGLISH: "Subterraneapremortephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.SUBTRACTIONPHOBIA: {
        Languages.ENGLISH: "Subtractionphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TAPHEPHOBIA: {
        Languages.ENGLISH: "Taphephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TELEPHONOPHOBIA: {
        Languages.ENGLISH: "Telephonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TELEVISIOPHOBIA: {
        Languages.ENGLISH: "Televisiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TELOCHRONOPHOBIA: {
        Languages.ENGLISH: "Telochronophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TENNISPHOBIA: {
        Languages.ENGLISH: "Tennisphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TESTOPHOBIA: {
        Languages.ENGLISH: "Testophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.THANATOPHOBIA: {
        Languages.ENGLISH: "Thanatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.THEROPHOBIA: {
        Languages.ENGLISH: "Therophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.THINOPOROPHOBIA: {
        Languages.ENGLISH: "Thinoporophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TOKOPHOBIA: {
        Languages.ENGLISH: "Tokophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TOMOPHOBIA: {
        Languages.ENGLISH: "Tomophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TONSUREPHOBIA: {
        Languages.ENGLISH: "Tonsurephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TOXIPHOBIA: {
        Languages.ENGLISH: "Toxiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TRAUMAPHOBIA: {
        Languages.ENGLISH: "Traumaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TRAUMATOPHOBIA: {
        Languages.ENGLISH: "Traumatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TREMOPHOBIA: {
        Languages.ENGLISH: "Tremophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TROPOPHOBIA: {
        Languages.ENGLISH: "Tropophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TSUNAMIPHOBIA: {
        Languages.ENGLISH: "Tsunamiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.TUSSAPHOBIA: {
        Languages.ENGLISH: "Tussaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.URINOPHOBIA: {
        Languages.ENGLISH: "Urinophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.VICTOROPHOBIA: {
        Languages.ENGLISH: "Victorophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.VINYLPHOBIA: {
        Languages.ENGLISH: "Vinylphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.VIVIAPHOBIA: {
        Languages.ENGLISH: "Viviaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.VOLCANOPHOBIA: {
        Languages.ENGLISH: "Volcanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.VOLLEYBALLPHOBIA: {
        Languages.ENGLISH: "Volleyballphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.WANSHANGPHOBIA: {
        Languages.ENGLISH: "Wanshangphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobias.XIAWUPHOBIA: {
        Languages.ENGLISH: "Xiawuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class EventsAndActionsPhobiasDescriptions(Enum):
    """
    Events And Actions Phobias Descriptions
    """
    ABDUCTOPHOBIA = auto()
    ABLUTOPHOBIA = auto()
    ABOREANISPHOBIA = auto()
    ACATOPTROPHOBIA = auto()
    ACCIDENSOPHOBIA = auto()
    ADDITIONPHOBIA = auto()
    ADHAESITOPHOBIA = auto()
    AELOSACCOPHOBIA = auto()
    AEROPHOBIA = auto()
    AGORAPHOBIA = auto()
    AGRAPHOBIA = auto()
    AGYROPHOBIA = auto()
    ALEMERCIALICEPTIOPHOBIA = auto()
    ALIENABDUCTOPHOBIA = auto()
    ALTHAZAGORAPHOBIA = auto()
    AMBULOPHOBIA = auto()
    STASIPHOBIA = auto()
    AMMIDYPHOBIA = auto()
    AMMOPHOBIA = auto()
    AMMOSOPHOBIA = auto()
    AMYCHOPHOBIA = auto()
    ANABLEPHOBIA = auto()
    ANAGNOSMAPHOBIA = auto()
    ANALAFROPHOBIA = auto()
    ANAPODAPHOBIA = auto()
    ANATIDAEPHOBIA = auto()
    ANKYLOPHOBIA = auto()
    ANOIXIPHOBIA = auto()
    ANDITCHOPHOBIA = auto()
    ANUPTAPHOBIA = auto()
    APOLLYMOPHOBIA = auto()
    APPLOGROPHINOPHOBIA = auto()
    ATHAZAGORAPHOBIA = auto()
    ATHLIMATAPHOBIA = auto()
    ATOMOSOPHOBIA = auto()
    ATYCHIPHOBIA = auto()
    KAKORRHAPHIOPHOBIA = auto()
    AUCHLOCLAUSTROPHOBIA = auto()
    AUTODYSOMOPHOBIA = auto()
    AUTOVOCALPHOBIA = auto()
    AVIOPHOBIA = auto()
    BACKTOSCHOOLAPHOBIA = auto()
    BAOWENPHOBIA = auto()
    BASIPHOBIA = auto()
    BASOPHOBIA = auto()
    BATOPHOBIA = auto()
    BIAPHOBIA = auto()
    BIOCHRONOPHOBIA = auto()
    BIOPHOBIA = auto()
    BIOTRIOCULARMECHANOPHOBIA = auto()
    BOITANOPHOBIA = auto()
    BROWNOUTPHOBIA = auto()
    CAPILLUSSETISPHOBIA = auto()
    CAPIOPHOBIA = auto()
    CAPNOPHOBIA = auto()
    CAPTOPHOBIA = auto()
    CASADASTRAPHOBIA = auto()
    CATAGELOPHOBIA = auto()
    CATAPEDAPHOBIA = auto()
    CATASTROPHOBIA = auto()
    CATHISOPHOBIA = auto()
    CEDEIAPHOBIA = auto()
    CHEMOPHOBIA = auto()
    CHOLOLEPUSUPHOBIA = auto()
    CHORIVANTHOKOLYMVISIPHOBIA = auto()
    CHOROPHOBIA = auto()
    CHROMPADAPHOBIA = auto()
    CHRONAPHOBIA = auto()
    CHRONOHODOPHOBIA = auto()
    CHRONOPHOBIA = auto()
    CHTYPIMAPHOBIA = auto()
    CHTYPISOPHOBIA = auto()
    CIDEOPHOBIA = auto()
    CIERIPHOBIA = auto()
    CLARUSPHOBIA = auto()
    CLAUDIPHOBIA = auto()
    CLIMACOPHOBIA = auto()
    CLIMATOPHOBIA = auto()
    CLINOPHOBIA = auto()
    CNIDOPHOBIA = auto()
    COMMUPHOBIA = auto()
    CONTRELTOPHOBIA = auto()
    CONTROVERSUSROGATIOPHOBIA = auto()
    CONVIVOPHOBIA = auto()
    CRAPOSANDWICHOPHOBIA = auto()
    CRYOCHIROPHOBIA = auto()
    CUNNIPHOBIA = auto()
    CYNOLINGOPUGOPHOBIA = auto()
    DAKNOPHOBIA = auto()
    DAKROPHOBIA = auto()
    DATALOSSOPHOBIA = auto()
    DECANNOPHOBIA = auto()
    DECIDOPHOBIA = auto()
    DEIPNOPHOBIA = auto()
    DEKAENNEAORAPHOBIA = auto()
    DEKAEPTAORAPHOBIA = auto()
    DEKAEXIORAPHOBIA = auto()
    DEKAOKTOORAPHOBIA = auto()
    DEKAORAPHOBIA = auto()
    DEKAPENTEORAPHOBIA = auto()
    DEKATESSERAPHOBIA = auto()
    DEKATRIAORAPHOBIA = auto()
    DENTOPHOBIA = auto()
    DEPRECOROPHOBIA = auto()
    DESTIRPEPHOBIA = auto()
    DETRECTOPHOBIA = auto()
    DEUTEROPHOBIA = auto()
    DEVWAHRPHOBIA = auto()
    DIMANCHOPHOBIA = auto()
    DISCONTINUAPHOBIA = auto()
    DISHABILIOPHOBIA = auto()
    DISPOSOPHOBIA = auto()
    DIVISIONPHOBIA = auto()
    DODEKAORAPHOBIA = auto()
    DOLOROPHOBIA = auto()
    DORONOPHOBIA = auto()
    DOXOPHOBIA = auto()
    DUOORAPHOBIA = auto()
    EARCOUNTOPHOBIA = auto()
    ECLEPOHELIOPHOBIA = auto()
    ECOTHERMOPHOBIA = auto()
    EHSANOPHOBIA = auto()
    EKRIXIPHOBIA = auto()
    EMARPHOBIA = auto()
    EMETOPHOBIA = auto()
    ENCAVMAPHOBIA = auto()
    ENOSIOPHOBIA = auto()
    EPISTAXIOPHOBIA = auto()
    EREUTHROPHOBIA = auto()
    ERGALEOPHOBIA = auto()
    ERGASIOPHOBIA = auto()
    ERRATOPHOBIA_(FEAR_OF_MAKING_MISTAKES),_ERROPHOBIA = auto()
    ERUCTOPHOBIA = auto()
    FLATUPHOBIA = auto()
    FLIPFLOPUPHOBIA = auto()
    FOOTBALLPHOBIA = auto()
    FRACTOPHOBIA = auto()
    FRAGAPANOPHOBIA = auto()
    FUMUSTERROREMOPHOBIA = auto()
    GAMOCEDEIAPHOBIA = auto()
    GAMOPHOBIA = auto()
    GARGALAPHOBIA = auto()
    GELOTOPHOBIA = auto()
    GENOPHOBIA = auto()
    GEPHYROPHOBIA = auto()
    GERASCOPHOBIA = auto()
    GLOSSOPHOBIA = auto()
    GOLFPHOBIA = auto()
    GRAPHOPHOBIA = auto()
    GROTHOPHOBIA = auto()
    GRONTHOKOPOPHOBIA = auto()
    HAMARTOPHOBIA = auto()
    HAPHEPHOBIA = auto()
    HARPAXOPHOBIA = auto()
    HEDONOPHOBIA = auto()
    HODOPHOBIA = auto()
    HONEPHOBIA = auto()
    HYPNOPHOBIA = auto()
    IGNITERROREMOPHOBIA = auto()
    INCESTOPHOBIA = auto()
    IPOVLOPSYCHOPHOBIA = auto()
    JACKBOXOPHOBIA = auto()
    JOCOPHOBIA = auto()
    KAKOLOGOPHOBIA = auto()
    KAKONEIROPHOBIA = auto()
    KAKOPHOBIA = auto()
    KELNGOPHOBIA = auto()
    KHEIMONPHOBIA = auto()
    KLEPTOPHOBIA = auto()
    KINETOPTOPHOBIA = auto()
    KOPOPHOBIA = auto()
    KYPHOPHOBIA = auto()
    KYRIAKIPHOBIA = auto()
    LALIOPHOBIA = auto()
    LATROPHOBIA = auto()
    LAMBOPHOBIA = auto()
    LEPTOPHOBIA = auto()
    LITICAPHOBIA = auto()
    LOCKIOPHOBIA = auto()
    LUPOSLIPOPHOBIA = auto()
    MACROPHOBIA = auto()
    MAGEIROCOPHOBIA = auto()
    MASTIGOPHOBIA = auto()
    MATHEMAPHOBIA = auto()
    MEDOMALACUPHOBIA = auto()
    MEDORTHOPHOBIA = auto()
    MERINTHOPHOBIA = auto()
    METATHESIOPHOBIA = auto()
    MIDNIGHTPHOBIA = auto()
    MISVACCINOPHOBIA = auto()
    MITSOPHOBIA = auto()
    MONOXEIDIOANTHRAKASKISIPHOBIA = auto()
    MULTIPLICATIONPHOBIA = auto()
    MYOCLUNUSDIAGPHRAGMAPHOBIA = auto()
    SINGULTOPHOBIA = auto()
    MYSOPHOBIA = auto()
    NATATOPHOBIA = auto()
    NATUROPHOBIA = auto()
    NOMOPHOBIA = auto()
    NONAMOPHOBIA = auto()
    NAIEISAIKAKOPHOBIA = auto()
    NUCLEOMITUPHOBIA = auto()
    NYCTOURINARIPHOBIA = auto()
    OBESOPHOBIA = auto()
    OBLITOPHOBIA = auto()
    DEDISCOPHOBIA = auto()
    OBSCURSOLISPHOBIA = auto()
    OLYMPICPHOBIA = auto()
    ONEIROGMOPHOBIA = auto()
    ONEIROPHOBIA = auto()
    ONEIROPOLIMAPHOBIA = auto()
    ONOMATOPHOBIA = auto()
    OPHTHALMOPHOBIA = auto()
    OPTOPHOBIA = auto()
    PAINTBALLPHOBIA = auto()
    PANTHOPHOBIA = auto()
    PANTREIAPHOBIA = auto()
    PARALIPOPHOBIA = auto()
    PARASKEVIDEKATRIAPHOBIA = auto()
    PERICULOPHOBIA = auto()
    PHAGOPHOBIA = auto()
    PHALACROPHOBIA = auto()
    PHARSAPHOBIA = auto()
    PHILEMAPHOBIA = auto()
    PHRONEMOPHOBIA = auto()
    PICNICPHOBIA = auto()
    PINCHOPHOBIA = auto()
    PIPTOPHOBIA = auto()
    PNIGOPHOBIA = auto()
    PNIGEROPHOBIA = auto()
    POLEMOPHOBIA = auto()
    PONOPHOBIA = auto()
    POSTHOCALYPTROPHOBIA = auto()
    PRESENTATIONPHOPHOBIA = auto()
    PROIPHOBIA = auto()
    PROSCHOPHOBIA = auto()
    PRURITOPHOBIA = auto()
    PSELLISMOPHOBIA = auto()
    PTERONOPHOBIA = auto()
    PUNGOPHOBIA = auto()
    PURASKISIPHOBIA = auto()
    QUESTIOPHOBIA = auto()
    QUEUNLISKANPHOBIA = auto()
    RHABDOPHOBIA = auto()
    RHYPOPHOBIA = auto()
    RUNDFUPHOBIA = auto()
    SARMASSOPHOBIA = auto()
    SCOPOPHOBIA = auto()
    SCRIPTOPHOBIA = auto()
    SCYTHEPHOBIA = auto()
    SEISMOPHOBIA = auto()
    SEISMOASKISIPHOBIA = auto()
    SELAPHOBIA = auto()
    SEXOPHOBIA = auto()
    SIENTOPHOBIA = auto()
    SIFOUNASKISIPHOBIA = auto()
    SNAPOPHOBIA = auto()
    SOCCERPHOBIA = auto()
    SOCIAPHOBIA = auto()
    SOMNIPHOBIA = auto()
    SOPHOPHOBIA = auto()
    STANIOPHOBIA = auto()
    STASIHYELOPHOBIA = auto()
    STERNUTAPHOBIA = auto()
    STUBAPHOBIA = auto()
    SUBTERRANEAPREMORTEPHOBIA = auto()
    SUBTRACTIONPHOBIA = auto()
    TAPHEPHOBIA = auto()
    TELEPHONOPHOBIA = auto()
    TELEVISIOPHOBIA = auto()
    TELOCHRONOPHOBIA = auto()
    TENNISPHOBIA = auto()
    TESTOPHOBIA = auto()
    THANATOPHOBIA = auto()
    THEROPHOBIA = auto()
    THINOPOROPHOBIA = auto()
    TOKOPHOBIA = auto()
    TOMOPHOBIA = auto()
    TONSUREPHOBIA = auto()
    TOXIPHOBIA = auto()
    TRAUMAPHOBIA = auto()
    TRAUMATOPHOBIA = auto()
    TREMOPHOBIA = auto()
    TROPOPHOBIA = auto()
    TSUNAMIPHOBIA = auto()
    TUSSAPHOBIA = auto()
    URINOPHOBIA = auto()
    VICTOROPHOBIA = auto()
    VINYLPHOBIA = auto()
    VIVIAPHOBIA = auto()
    VOLCANOPHOBIA = auto()
    VOLLEYBALLPHOBIA = auto()
    WANSHANGPHOBIA = auto()
    XIAWUPHOBIA = auto()


EVENTS_AND_ACTIONS_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    EventsAndActionsPhobiasDescriptions.ABDUCTOPHOBIA: {
        Languages.ENGLISH: "Fear of abduction",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ABLUTOPHOBIA: {
        Languages.ENGLISH: "Fear of being wet",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ABOREANISPHOBIA: {
        Languages.ENGLISH: "Fear of feeding goats",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ACATOPTROPHOBIA: {
        Languages.ENGLISH: "Fear of seeing your reflection in something else than a mirror",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ACCIDENSOPHOBIA: {
        Languages.ENGLISH: "Fear of accidents",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ADDITIONPHOBIA: {
        Languages.ENGLISH: "Fear of doing addition",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ADHAESITOPHOBIA: {
        Languages.ENGLISH: "Fear of getting stuck",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AELOSACCOPHOBIA: {
        Languages.ENGLISH: "Fear of injury resulting from the unexpected release of a vehicle airbag",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AEROPHOBIA: {
        Languages.ENGLISH: "Fear of flying",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AGORAPHOBIA: {
        Languages.ENGLISH: "Fear of going out",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AGRAPHOBIA: {
        Languages.ENGLISH: "Fear of sexual contact",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AGYROPHOBIA: {
        Languages.ENGLISH: "Fear of crossing the road",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ALEMERCIALICEPTIOPHOBIA: {
        Languages.ENGLISH: "Fear of beer in comercials not being accurate as they are in real life",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ALIENABDUCTOPHOBIA: {
        Languages.ENGLISH: "Fear of alien abduction (branch of alienophobia and abductophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ALTHAZAGORAPHOBIA: {
        Languages.ENGLISH: "Fear of ignorance",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AMBULOPHOBIA: {
        Languages.ENGLISH: "Fear of walking",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.STASIPHOBIA: {
        Languages.ENGLISH: "Fear of standing",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AMMIDYPHOBIA: {
        Languages.ENGLISH: "Fear of a loved one leaving you",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AMMOPHOBIA: {
        Languages.ENGLISH: "Fear of walking on sand",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AMMOSOPHOBIA: {
        Languages.ENGLISH: "Fear of standing on sand",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AMYCHOPHOBIA: {
        Languages.ENGLISH: "Fear of being scratched",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ANABLEPHOBIA: {
        Languages.ENGLISH: "Fear of looking up",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ANAGNOSMAPHOBIA: {
        Languages.ENGLISH: "Fear of reading",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ANALAFROPHOBIA: {
        Languages.ENGLISH: "Fear of tripping over something",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ANAPODAPHOBIA: {
        Languages.ENGLISH: "Fear of being upsidedown",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ANATIDAEPHOBIA: {
        Languages.ENGLISH: "Fear of a duck watching you",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ANKYLOPHOBIA: {
        Languages.ENGLISH: "Fear of a joint being immobile",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ANOIXIPHOBIA: {
        Languages.ENGLISH: "Fear of spring",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ANDITCHOPHOBIA: {
        Languages.ENGLISH: "Fear of being on time",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ANUPTAPHOBIA: {
        Languages.ENGLISH: "Fear of breaking up",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.APOLLYMOPHOBIA: {
        Languages.ENGLISH: "Fear of destruction",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.APPLOGROPHINOPHOBIA: {
        Languages.ENGLISH: "Fear of being addictted to porn",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ATHAZAGORAPHOBIA: {
        Languages.ENGLISH: "Fear of being forgotten",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ATHLIMATAPHOBIA: {
        Languages.ENGLISH: "Fear of someone whispering",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ATOMOSOPHOBIA: {
        Languages.ENGLISH: "Fear of atomic explosions",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ATYCHIPHOBIA: {
        Languages.ENGLISH: "Fear of failure",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.KAKORRHAPHIOPHOBIA: {
        Languages.ENGLISH: "Fear of defeat",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AUCHLOCLAUSTROPHOBIA: {
        Languages.ENGLISH: "Fear of opening closets",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AUTODYSOMOPHOBIA: {
        Languages.ENGLISH: "Fear of having stinky feet",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AUTOVOCALPHOBIA: {
        Languages.ENGLISH: "Fear of hear owns voice",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.AVIOPHOBIA: {
        Languages.ENGLISH: "Fear of flying",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.BACKTOSCHOOLAPHOBIA: {
        Languages.ENGLISH: "Fear of going back to school",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.BAOWENPHOBIA: {
        Languages.ENGLISH: "Fear of baby kissing",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.BASIPHOBIA: {
        Languages.ENGLISH: "Fear of walking or falling",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.BASOPHOBIA: {
        Languages.ENGLISH: "Fear of standing/walking erect",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.BATOPHOBIA: {
        Languages.ENGLISH: "Fear of being close to tall buildings",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.BIAPHOBIA: {
        Languages.ENGLISH: "Fear of rules where you cannot eat",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.BIOCHRONOPHOBIA: {
        Languages.ENGLISH: "Fear of one's biological clock had run down before one has had a chance to adequately replenish the species",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.BIOPHOBIA: {
        Languages.ENGLISH: "Fear of developing life",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.BIOTRIOCULARMECHANOPHOBIA: {
        Languages.ENGLISH: "Fear of having a third cyborg eye attached to you",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.BOITANOPHOBIA: {
        Languages.ENGLISH: "Fear of being forced to watch competitive male figure skating",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.BROWNOUTPHOBIA: {
        Languages.ENGLISH: "Fear of brownout",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CAPILLUSSETISPHOBIA: {
        Languages.ENGLISH: "Fear of having your hair brushed",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CAPIOPHOBIA: {
        Languages.ENGLISH: "Fear of getting arrested",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CAPNOPHOBIA: {
        Languages.ENGLISH: "Fear of smoking",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CAPTOPHOBIA: {
        Languages.ENGLISH: "Fear of being caught",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CASADASTRAPHOBIA: {
        Languages.ENGLISH: "Fear of falling into the sky",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CATAGELOPHOBIA: {
        Languages.ENGLISH: "Fear of being ridiculed",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CATAPEDAPHOBIA: {
        Languages.ENGLISH: "Fear of jumping from high and low places",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CATASTROPHOBIA: {
        Languages.ENGLISH: "Fear of disasters",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CATHISOPHOBIA: {
        Languages.ENGLISH: "Fear of sitting",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CEDEIAPHOBIA: {
        Languages.ENGLISH: "Fear of attending funerals (branch of gamocedeiaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CHEMOPHOBIA: {
        Languages.ENGLISH: "Fear of working with chemicals",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CHOLOLEPUSUPHOBIA: {
        Languages.ENGLISH: "Fear of dyeing fur of bunnies",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CHORIVANTHOKOLYMVISIPHOBIA: {
        Languages.ENGLISH: "Fear of being told not to dive past a centain depth mark",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CHOROPHOBIA: {
        Languages.ENGLISH: "Fear of dancing",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CHROMPADAPHOBIA: {
        Languages.ENGLISH: "Fear of long photo shoots",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CHRONAPHOBIA: {
        Languages.ENGLISH: "Fear of seeing colors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CHRONOHODOPHOBIA: {
        Languages.ENGLISH: "Fear of time travel",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CHRONOPHOBIA: {
        Languages.ENGLISH: "Fear of time",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CHTYPIMAPHOBIA: {
        Languages.ENGLISH: "Fear of bumping into someone or something",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CHTYPISOPHOBIA: {
        Languages.ENGLISH: "Fear of getting bumped by someone",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CIDEOPHOBIA: {
        Languages.ENGLISH: "Fear of commiting acts of violence or murder",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CIERIPHOBIA: {
        Languages.ENGLISH: "Fear of lunar eclipse",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CLARUSPHOBIA: {
        Languages.ENGLISH: "Fear of becoming famous and then losing the fame",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CLAUDIPHOBIA: {
        Languages.ENGLISH: "Fear of heading out to the place unaware that it is closed",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CLIMACOPHOBIA: {
        Languages.ENGLISH: "Fear of climbing, or of falling downstairs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CLIMATOPHOBIA: {
        Languages.ENGLISH: "Fear of climate change",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CLINOPHOBIA: {
        Languages.ENGLISH: "Fear of going to bed",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CNIDOPHOBIA: {
        Languages.ENGLISH: "Fear of getting stung by bees, etc.",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.COMMUPHOBIA: {
        Languages.ENGLISH: "Fear of communism or becoming a communist",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CONTRELTOPHOBIA: {
        Languages.ENGLISH: "Fear of sexual abuse",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CONTROVERSUSROGATIOPHOBIA: {
        Languages.ENGLISH: "Fear of questionable questions",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CONVIVOPHOBIA: {
        Languages.ENGLISH: "Fear of parties",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CRAPOSANDWICHOPHOBIA: {
        Languages.ENGLISH: "Fear of someone giving you a hamburger full of feces",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CRYOCHIROPHOBIA: {
        Languages.ENGLISH: "Fear of your hands being cold",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CUNNIPHOBIA: {
        Languages.ENGLISH: "Fear of performing cunnilingus except for no reason",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.CYNOLINGOPUGOPHOBIA: {
        Languages.ENGLISH: "Fear of a dog licking someones buttocks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DAKNOPHOBIA: {
        Languages.ENGLISH: "Fear of being bitten",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DAKROPHOBIA: {
        Languages.ENGLISH: "Fear of crying",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DATALOSSOPHOBIA: {
        Languages.ENGLISH: "Fear of losing your data",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DECANNOPHOBIA: {
        Languages.ENGLISH: "Fear of turning 10 years old",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DECIDOPHOBIA: {
        Languages.ENGLISH: "Fear of making decisions",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DEIPNOPHOBIA: {
        Languages.ENGLISH: "Fear of dinner",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DEKAENNEAORAPHOBIA: {
        Languages.ENGLISH: "Fear of 7:00pm",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DEKAEPTAORAPHOBIA: {
        Languages.ENGLISH: "Fear of 5:00pm",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DEKAEXIORAPHOBIA: {
        Languages.ENGLISH: "Fear of 4:00pm",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DEKAOKTOORAPHOBIA: {
        Languages.ENGLISH: "Fear of 6:00pm",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DEKAORAPHOBIA: {
        Languages.ENGLISH: "Fear of 10:00am",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DEKAPENTEORAPHOBIA: {
        Languages.ENGLISH: "Fear of 3:00pm",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DEKATESSERAPHOBIA: {
        Languages.ENGLISH: "Fear of 2:00pm",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DEKATRIAORAPHOBIA: {
        Languages.ENGLISH: "Fear of 1:00pm",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DENTOPHOBIA: {
        Languages.ENGLISH: "Fear of dental procedures",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DEPRECOROPHOBIA: {
        Languages.ENGLISH: "Fear of curses and being cursed",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DESTIRPEPHOBIA: {
        Languages.ENGLISH: "Fear of finding the item you are looking for but it is out of stock",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DETRECTOPHOBIA: {
        Languages.ENGLISH: "Fear of mismanagement",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DEUTEROPHOBIA: {
        Languages.ENGLISH: "Fear of mondays",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DEVWAHRPHOBIA: {
        Languages.ENGLISH: "Fear of doing homework",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DIMANCHOPHOBIA: {
        Languages.ENGLISH: "Fear of sundays",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DISCONTINUAPHOBIA: {
        Languages.ENGLISH: "Fear of your favorite show being discontinued",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DISHABILIOPHOBIA: {
        Languages.ENGLISH: "Fear of undressing in front of someone",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DISPOSOPHOBIA: {
        Languages.ENGLISH: "Fear of getting rid of or losing things - sometimes wrongly defined as 'compulsive hoarding'",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DIVISIONPHOBIA: {
        Languages.ENGLISH: "Fear of doing division",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DODEKAORAPHOBIA: {
        Languages.ENGLISH: "Fear of 12:00pm",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DOLOROPHOBIA: {
        Languages.ENGLISH: "Fear of suffering",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DORONOPHOBIA: {
        Languages.ENGLISH: "Fear of opening gifts",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DOXOPHOBIA: {
        Languages.ENGLISH: "Fear of expressing opinions or of receiving praise",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DUOORAPHOBIA: {
        Languages.ENGLISH: "Fear of 2:00 am",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.EARCOUNTOPHOBIA: {
        Languages.ENGLISH: "Fear of counting ears",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ECLEPOHELIOPHOBIA: {
        Languages.ENGLISH: "Fear of sun vanishing",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ECOTHERMOPHOBIA: {
        Languages.ENGLISH: "Fear of global warming",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.EHSANOPHOBIA: {
        Languages.ENGLISH: "Fear of expending money",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.EKRIXIPHOBIA: {
        Languages.ENGLISH: "Fear of explosions",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.EMARPHOBIA: {
        Languages.ENGLISH: "Fear of daytime",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.EMETOPHOBIA: {
        Languages.ENGLISH: "Fear of vomiting",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ENCAVMAPHOBIA: {
        Languages.ENGLISH: "Fear of getting burned (branch of traumatophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ENOSIOPHOBIA: {
        Languages.ENGLISH: "Fear of having committed an unpardonable sin or of criticism",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.EPISTAXIOPHOBIA: {
        Languages.ENGLISH: "Fear of nosebleeds",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.EREUTHROPHOBIA: {
        Languages.ENGLISH: "Fear of blushing",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ERGALEOPHOBIA: {
        Languages.ENGLISH: "Fear of using tools",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ERGASIOPHOBIA: {
        Languages.ENGLISH: "Fear of work or functioning, or a surgeon's fear of operating",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ERRATOPHOBIA_(FEAR_OF_MAKING_MISTAKES),_ERROPHOBIA: {
        Languages.ENGLISH: "Fear of getting wrong answers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ERUCTOPHOBIA: {
        Languages.ENGLISH: "Fear of burping",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.FLATUPHOBIA: {
        Languages.ENGLISH: "Fear of farting",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.FLIPFLOPUPHOBIA: {
        Languages.ENGLISH: "Fear of being severely beaten by flip flops",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.FOOTBALLPHOBIA: {
        Languages.ENGLISH: "Fear of football",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.FRACTOPHOBIA: {
        Languages.ENGLISH: "Fear of breaking things",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.FRAGAPANOPHOBIA: {
        Languages.ENGLISH: "Fear of birthdays",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.FUMUSTERROREMOPHOBIA: {
        Languages.ENGLISH: "Fear of smoke alarms (branch of ligyrophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.GAMOCEDEIAPHOBIA: {
        Languages.ENGLISH: "Fear of commitment and of attending funerals",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.GAMOPHOBIA: {
        Languages.ENGLISH: "Fear of getting married or commitment",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.GARGALAPHOBIA: {
        Languages.ENGLISH: "Fear of being tickled",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.GELOTOPHOBIA: {
        Languages.ENGLISH: "Fear of being laughed at",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.GENOPHOBIA: {
        Languages.ENGLISH: "Fear of sex",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.GEPHYROPHOBIA: {
        Languages.ENGLISH: "Fear of crossing bridges",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.GERASCOPHOBIA: {
        Languages.ENGLISH: "Fear of growing old or aging",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.GLOSSOPHOBIA: {
        Languages.ENGLISH: "Fear of speaking in public or of trying to speak",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.GOLFPHOBIA: {
        Languages.ENGLISH: "Fear of golf",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.GRAPHOPHOBIA: {
        Languages.ENGLISH: "Fear of writing or handwriting",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.GROTHOPHOBIA: {
        Languages.ENGLISH: "Fear of getting punched",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.GRONTHOKOPOPHOBIA: {
        Languages.ENGLISH: "Same as grothophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.HAMARTOPHOBIA: {
        Languages.ENGLISH: "Fear of sinning",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.HAPHEPHOBIA: {
        Languages.ENGLISH: "Fear of touching things or being touched",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.HARPAXOPHOBIA: {
        Languages.ENGLISH: "Fear of being robbed",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.HEDONOPHOBIA: {
        Languages.ENGLISH: "Fear of feeling pleasure",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.HODOPHOBIA: {
        Languages.ENGLISH: "Fear of travel",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.HONEPHOBIA: {
        Languages.ENGLISH: "Fear of eating (or breathing through mouth) when someone has burped or farted near or around them",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.HYPNOPHOBIA: {
        Languages.ENGLISH: "Fear of sleep",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.IGNITERROREMOPHOBIA: {
        Languages.ENGLISH: "Fear of fire alarms (branch of ligyrophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.INCESTOPHOBIA: {
        Languages.ENGLISH: "Fear of incest",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.IPOVLOPSYCHOPHOBIA: {
        Languages.ENGLISH: "Fear of having one’s photograph taken",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.JACKBOXOPHOBIA: {
        Languages.ENGLISH: "Fear of objects suddenly popping out of boxes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.JOCOPHOBIA: {
        Languages.ENGLISH: "Fear of having fun",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.KAKOLOGOPHOBIA: {
        Languages.ENGLISH: "Fear of swearing and of hearing swear words",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.KAKONEIROPHOBIA: {
        Languages.ENGLISH: "Fear of nightmares (branch of oneirophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.KAKOPHOBIA: {
        Languages.ENGLISH: "Fear of bad situations",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.KELNGOPHOBIA: {
        Languages.ENGLISH: "Fear of potlucks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.KHEIMONPHOBIA: {
        Languages.ENGLISH: "Fear of winter",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.KLEPTOPHOBIA: {
        Languages.ENGLISH: "Fear of being stolen",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.KINETOPTOPHOBIA: {
        Languages.ENGLISH: "Fear of movement or motion",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.KOPOPHOBIA: {
        Languages.ENGLISH: "Fear of fatigue",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.KYPHOPHOBIA: {
        Languages.ENGLISH: "Fear of stooping",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.KYRIAKIPHOBIA: {
        Languages.ENGLISH: "Fear of sundays",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.LALIOPHOBIA: {
        Languages.ENGLISH: "Fear of speaking",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.LATROPHOBIA: {
        Languages.ENGLISH: "Fear of worship",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.LAMBOPHOBIA: {
        Languages.ENGLISH: "Fear of being licked",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.LEPTOPHOBIA: {
        Languages.ENGLISH: "Fear of losing weight",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.LITICAPHOBIA: {
        Languages.ENGLISH: "Fear of being sued",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.LOCKIOPHOBIA: {
        Languages.ENGLISH: "Fear of childbirth",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.LUPOSLIPOPHOBIA: {
        Languages.ENGLISH: "Fear of running around a kitchen table, being pursued by wolves, while wearing fresh socks on a newly waxed floor (innate fear).",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MACROPHOBIA: {
        Languages.ENGLISH: "Fear of long waits",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MAGEIROCOPHOBIA: {
        Languages.ENGLISH: "Fear of cooking",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MASTIGOPHOBIA: {
        Languages.ENGLISH: "Fear of being punished",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MATHEMAPHOBIA: {
        Languages.ENGLISH: "Fear of mathematics",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MEDOMALACUPHOBIA: {
        Languages.ENGLISH: "Fear of losing an erection (branch of medomalacophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MEDORTHOPHOBIA: {
        Languages.ENGLISH: "Fear of penis being erected",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MERINTHOPHOBIA: {
        Languages.ENGLISH: "Fear of being bound or tied up",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.METATHESIOPHOBIA: {
        Languages.ENGLISH: "Fear of changes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MIDNIGHTPHOBIA: {
        Languages.ENGLISH: "Fear of midnight",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MISVACCINOPHOBIA: {
        Languages.ENGLISH: "Fear on missing out on a vaccine",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MITSOPHOBIA: {
        Languages.ENGLISH: "Fear of being commanded/to command",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MONOXEIDIOANTHRAKASKISIPHOBIA: {
        Languages.ENGLISH: "Fear of carbon monoxide drills",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MULTIPLICATIONPHOBIA: {
        Languages.ENGLISH: "Fear of doing multiplication",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MYOCLUNUSDIAGPHRAGMAPHOBIA: {
        Languages.ENGLISH: "Fear of hiccups",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SINGULTOPHOBIA: {
        Languages.ENGLISH: "Same as myoclunusdiagphragmaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.MYSOPHOBIA: {
        Languages.ENGLISH: "Fear of being contaminated with dirt or germs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.NATATOPHOBIA: {
        Languages.ENGLISH: "Fear of swimming",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.NATUROPHOBIA: {
        Languages.ENGLISH: "Fear of natural phenomena",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.NOMOPHOBIA: {
        Languages.ENGLISH: "Fear of being out of mobile phone contact",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.NONAMOPHOBIA: {
        Languages.ENGLISH: "Fear of blackout",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.NAIEISAIKAKOPHOBIA: {
        Languages.ENGLISH: "Fear of being bad",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.NUCLEOMITUPHOBIA: {
        Languages.ENGLISH: "Fear of nuclear holocaust",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.NYCTOURINARIPHOBIA: {
        Languages.ENGLISH: "Fear of wetting the bed at night",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.OBESOPHOBIA: {
        Languages.ENGLISH: "Fear of gaining weight",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.OBLITOPHOBIA: {
        Languages.ENGLISH: "Fear of forgetting",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.DEDISCOPHOBIA: {
        Languages.ENGLISH: "Same as oblitophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.OBSCURSOLISPHOBIA: {
        Languages.ENGLISH: "Fear of solar eclipse",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.OLYMPICPHOBIA: {
        Languages.ENGLISH: "Fear of the olympics",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ONEIROGMOPHOBIA: {
        Languages.ENGLISH: "Fear of wet dreams (branch of oneirophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ONEIROPHOBIA: {
        Languages.ENGLISH: "Fear of dreams",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ONEIROPOLIMAPHOBIA: {
        Languages.ENGLISH: "Fear of daydreams",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.ONOMATOPHOBIA: {
        Languages.ENGLISH: "Fear of hearing a certain word or of names",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.OPHTHALMOPHOBIA: {
        Languages.ENGLISH: "Fear of being stared at",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.OPTOPHOBIA: {
        Languages.ENGLISH: "Fear of opening one's eyes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PAINTBALLPHOBIA: {
        Languages.ENGLISH: "Fear of paintball",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PANTHOPHOBIA: {
        Languages.ENGLISH: "Fear of suffering",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PANTREIAPHOBIA: {
        Languages.ENGLISH: "Fear of attending weddings (branch of gamocedeiaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PARALIPOPHOBIA: {
        Languages.ENGLISH: "Fear of neglecting duty or responsibility",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PARASKEVIDEKATRIAPHOBIA: {
        Languages.ENGLISH: "Fear of friday the 13th (branch of friggatriskaidekaphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PERICULOPHOBIA: {
        Languages.ENGLISH: "Fear of taking risks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PHAGOPHOBIA: {
        Languages.ENGLISH: "Fear of swallowing or of eating or of being eaten",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PHALACROPHOBIA: {
        Languages.ENGLISH: "Fear of becoming bald",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PHARSAPHOBIA: {
        Languages.ENGLISH: "Fear of pranks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PHILEMAPHOBIA: {
        Languages.ENGLISH: "Fear of kissin'",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PHRONEMOPHOBIA: {
        Languages.ENGLISH: "Fear of thinking",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PICNICPHOBIA: {
        Languages.ENGLISH: "Fear of picnics",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PINCHOPHOBIA: {
        Languages.ENGLISH: "Fear of being pinched",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PIPTOPHOBIA: {
        Languages.ENGLISH: "Fear of falling",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PNIGOPHOBIA: {
        Languages.ENGLISH: "Fear of being choked",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PNIGEROPHOBIA: {
        Languages.ENGLISH: "Fear of being smothered",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.POLEMOPHOBIA: {
        Languages.ENGLISH: "Fear of wars",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PONOPHOBIA: {
        Languages.ENGLISH: "Fear of overworking",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.POSTHOCALYPTROPHOBIA: {
        Languages.ENGLISH: "Fear of buying or using condom",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PRESENTATIONPHOPHOBIA: {
        Languages.ENGLISH: "Fear of making a presentation on phobias",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PROIPHOBIA: {
        Languages.ENGLISH: "Fear of mornings",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PROSCHOPHOBIA: {
        Languages.ENGLISH: "Fear of preschool",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PRURITOPHOBIA: {
        Languages.ENGLISH: "Fear of itches",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PSELLISMOPHOBIA: {
        Languages.ENGLISH: "Fear of stuttering",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PTERONOPHOBIA: {
        Languages.ENGLISH: "Fear of being tickled by feathers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PUNGOPHOBIA: {
        Languages.ENGLISH: "Fear of getting stabbed",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.PURASKISIPHOBIA: {
        Languages.ENGLISH: "Fear of fire drills",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.QUESTIOPHOBIA: {
        Languages.ENGLISH: "Fear of being asked questions",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.QUEUNLISKANPHOBIA: {
        Languages.ENGLISH: "Fear of spitting",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.RHABDOPHOBIA: {
        Languages.ENGLISH: "Fear of being severely punished or beaten by a rod, or of being severely criticized. also fear of magic wands",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.RHYPOPHOBIA: {
        Languages.ENGLISH: "Fear of defecation",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.RUNDFUPHOBIA: {
        Languages.ENGLISH: "Fear of listening to the radio",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SARMASSOPHOBIA: {
        Languages.ENGLISH: "Fear of love play",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SCOPOPHOBIA: {
        Languages.ENGLISH: "Fear of being looked at or stared at",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SCRIPTOPHOBIA: {
        Languages.ENGLISH: "Fear of writing in public",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SCYTHEPHOBIA: {
        Languages.ENGLISH: "Fear of cutting grass",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SEISMOPHOBIA: {
        Languages.ENGLISH: "Fear of earthquakes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SEISMOASKISIPHOBIA: {
        Languages.ENGLISH: "Fear of earthquake drills",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SELAPHOBIA: {
        Languages.ENGLISH: "Fear of light flashes (branch of photophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SEXOPHOBIA: {
        Languages.ENGLISH: "Fear of porns or sexes etc.",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SIENTOPHOBIA: {
        Languages.ENGLISH: "Fear of apologizing too excessively",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SIFOUNASKISIPHOBIA: {
        Languages.ENGLISH: "Fear of tornado drills",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SNAPOPHOBIA: {
        Languages.ENGLISH: "Fear of finger snapping",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SOCCERPHOBIA: {
        Languages.ENGLISH: "Fear of soccer",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SOCIAPHOBIA: {
        Languages.ENGLISH: "Fear of being judged in public",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SOMNIPHOBIA: {
        Languages.ENGLISH: "Fear of falling asleep (branch of hyprophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SOPHOPHOBIA: {
        Languages.ENGLISH: "Fear of learning",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.STANIOPHOBIA: {
        Languages.ENGLISH: "Fear of abortion",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.STASIHYELOPHOBIA: {
        Languages.ENGLISH: "Fear of standing on glass",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.STERNUTAPHOBIA: {
        Languages.ENGLISH: "Fear of sneezing",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.STUBAPHOBIA: {
        Languages.ENGLISH: "Fear of cutting nails",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SUBTERRANEAPREMORTEPHOBIA: {
        Languages.ENGLISH: "Fear of being buried alive",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.SUBTRACTIONPHOBIA: {
        Languages.ENGLISH: "Fear of doing subtraction",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TAPHEPHOBIA: {
        Languages.ENGLISH: "Fear of being placed in a grave while still alive",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TELEPHONOPHOBIA: {
        Languages.ENGLISH: "Fear of telephones ringing",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TELEVISIOPHOBIA: {
        Languages.ENGLISH: "Fear of watching television",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TELOCHRONOPHOBIA: {
        Languages.ENGLISH: "Fear of running out of time, branch of chronophobia (fear of time)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TENNISPHOBIA: {
        Languages.ENGLISH: "Fear of tennis",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TESTOPHOBIA: {
        Languages.ENGLISH: "Fear of taking tests",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.THANATOPHOBIA: {
        Languages.ENGLISH: "Fear of dying",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.THEROPHOBIA: {
        Languages.ENGLISH: "Fear of summer",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.THINOPOROPHOBIA: {
        Languages.ENGLISH: "Fear of autumn",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TOKOPHOBIA: {
        Languages.ENGLISH: "Fear of pregnancy",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TOMOPHOBIA: {
        Languages.ENGLISH: "Fear of surgical operations",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TONSUREPHOBIA: {
        Languages.ENGLISH: "Fear of getting haircut",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TOXIPHOBIA: {
        Languages.ENGLISH: "Fear of being poisoned",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TRAUMAPHOBIA: {
        Languages.ENGLISH: "Fear of physical injury",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TRAUMATOPHOBIA: {
        Languages.ENGLISH: "Fear of war",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TREMOPHOBIA: {
        Languages.ENGLISH: "Fear of trembling",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TROPOPHOBIA: {
        Languages.ENGLISH: "Fear of moving or making changes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TSUNAMIPHOBIA: {
        Languages.ENGLISH: "Fear of tsunamis (branch of cymophobia and seismophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.TUSSAPHOBIA: {
        Languages.ENGLISH: "Fear of coughing",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.URINOPHOBIA: {
        Languages.ENGLISH: "Fear of urinating",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.VICTOROPHOBIA: {
        Languages.ENGLISH: "Fear of victories",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.VINYLPHOBIA: {
        Languages.ENGLISH: "Fear of scratching vinyl surfaces",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.VIVIAPHOBIA: {
        Languages.ENGLISH: "Fear of licking ice-cream",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.VOLCANOPHOBIA: {
        Languages.ENGLISH: "Fear of volcanic eruptions",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.VOLLEYBALLPHOBIA: {
        Languages.ENGLISH: "Fear of volleyball",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.WANSHANGPHOBIA: {
        Languages.ENGLISH: "Fear of evenings",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    EventsAndActionsPhobiasDescriptions.XIAWUPHOBIA: {
        Languages.ENGLISH: "Fear of afternoons",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
