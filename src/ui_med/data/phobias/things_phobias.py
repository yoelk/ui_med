from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


class ThingsPhobias(Enum):
    """
    Things Phobias Names
    """
    ADIAFANOPHOBIA = auto()
    ADVERTISEMENTPHOBIA = auto()
    AEROSAKAPHOBIA = auto()
    AICHMOPHOBIA = auto()
    AIRCOPHOBIA = auto()
    AIRPODAPHOBIA = auto()
    ALARMOPHOBIA = auto()
    ALLODOXAPHOBIA = auto()
    ALTOCELAROPHOBIA = auto()
    ANEMISTIRAPHOBIA = auto()
    ANIMAPHOBIA = auto()
    ANTANAKLOPHOBIA = auto()
    ANTENNAPHOBIA = auto()
    APEIROPHOBIA = auto()
    APOSTASIPHOBIA = auto()
    APPLETVAPHOBIA = auto()
    AQUAMECHANOPHOBIA = auto()
    ARACHTOPHOBIA = auto()
    ARCHEIOTHIKIPHOBIA = auto()
    ARMAROPHOBIA = auto()
    ARPAPHOBIA = auto()
    ARTEMOPHOBIA = auto()
    AULOPHOBIA = auto()
    AUTOKERAPHOBIA = auto()
    AUTOPLENOPHOBIA = auto()
    AUTOMATONOPHOBIA = auto()
    BACOPHOBIA = auto()
    BAHNUBOPHOBIA = auto()
    BALLISTOPHOBIA = auto()
    BALTEUSPHOBIA = auto()
    BALTICOPHOBIA = auto()
    BANDZOPHOBIA = auto()
    BANMAXIANPHOBIA = auto()
    BAROPHOBIA = auto()
    BASSOLOPHOBIA = auto()
    BATHMOPHOBIA = auto()
    BATHROBEPHOBIA = auto()
    BATTEROPHOBIA = auto()
    BEEPOPHOBIA = auto()
    BELONEPHOBIA = auto()
    BIBLIOPHOBIA = auto()
    BILLBOARDPHOBIA = auto()
    BIJIXPHOBIA = auto()
    BINOCULOPHOBIA = auto()
    BLEIMPNOPHOBIA = auto()
    BLEMENSAPHOBIA = auto()
    BLENDERPHOBIA = auto()
    BLOWERPEELPHOBIA = auto()
    BRACESPHOBIA = auto()
    BRUGNOPHOBIA = auto()
    BODENSTANDOPHOBIA = auto()
    BONOCKOPHOBIA = auto()
    BOOGIEBOARDPHOBIA = auto()
    BOWERPHOBIA = auto()
    BOWPHOBIA = auto()
    BRIEFSHIEPHOBIA = auto()
    BUHUAJIPHOBIA = auto()
    BUZZOPHOBIA = auto()
    BWAOPIPHOBIA = auto()
    BWAUKPHOBIA = auto()
    CABLEPHOBIA = auto()
    CAELOPHOBIA = auto()
    CALCULAPHOBIA = auto()
    CAMCORDERPHOBIA = auto()
    CAMERAPHOBIA = auto()
    CAPILLUSSETISPHOBIA = auto()
    CASSETTOPHOBIA = auto()
    CATASTOLEPHOBIA = auto()
    CATHEDRAPHOBIA = auto()
    CATOPTROPHOBIA = auto()
    CELAROPHOBIA = auto()
    CENOSILICAPHOBIA = auto()
    CHARAKAPHOBIA = auto()
    CHARTIPHOBIA = auto()
    CHEDOANGPHOBIA = auto()
    CHEKUXISHOPHOBIA = auto()
    CHIONOFYSOPHOBIA = auto()
    CHLOEPHOBIA = auto()
    CHREOSTIKIKARTAPHOBIA = auto()
    CHROMETOPHOBIA = auto()
    CHRONOMENTROPHOBIA = auto()
    CHUFXISHOPHOBIA = auto()
    CISTULAPHOBIA = auto()
    CITHARAPHOBIA = auto()
    CLAPPERPHOBIA = auto()
    CLEITHROPHOBIA = auto()
    CLINEPHOBIA = auto()
    CLOACAPHOBIA = auto()
    COGOMBOPHOBIA = auto()
    COLIMBOPHOBIA = auto()
    COMMERCIALPHOBIA = auto()
    COMPASSPHOBIA = auto()
    CONFETTIPHOBIA = auto()
    CONSECOTALEOPHOBIA = auto()
    CONTROSOFFITTOPHOBIA = auto()
    COZAMPIOPHOBIA = auto()
    CRANOPHOBIA = auto()
    CREMNOPHOBIA = auto()
    CRUSRUMBLOPHOBIA = auto()
    CUPROLAMINOPHOBIA = auto()
    CYBERPHOBIA = auto()
    CYMOPHOBIA = auto()
    DACHOINGPHOBIA = auto()
    DARTBOARDPHOBIA = auto()
    DARTOPHOBIA = auto()
    DEFENESTRAPHOBIA = auto()
    DEKANIKIPHOBIA = auto()
    DELEOPHOBIA = auto()
    DENGPAOPHOBIA = auto()
    DENTODRAPANOPHOBIA = auto()
    DENTUREPHOBIA = auto()
    DEXTROPHOBIA = auto()
    DIAFANOPHOBIA = auto()
    DIANZIFANKUIPHOBIA = auto()
    DIAPERPHOBIA = auto()
    DIAPHIMISTICOPHOBIA = auto()
    DIASTIMAPHOBIA = auto()
    DIATHLASOPHOBIA = auto()
    DICLEBGOPHOBIA = auto()
    DIETHNESYSTIMAMONADONOPHOBIA = auto()
    DIKEPHOBIA = auto()
    DIMEPHOBIA = auto()
    DINGOPHOBIA = auto()
    DINOPHOBIA = auto()
    DISHLEPROPHOBIA = auto()
    DIZOANGPHOBIA = auto()
    DLITOPHOBIA = auto()
    DOMINEATHERPHOBIA = auto()
    DOORBELLPHOBIA = auto()
    DORAPHOBIA = auto()
    DORNGOPHOBIA = auto()
    DORYFORIKOCHARTIPHOBIA = auto()
    DOTTOPHOBIA = auto()
    DRAPANOPHOBIA = auto()
    DRIKRONPHOBIA = auto()
    DROGERPHOBIA = auto()
    DROMUSEPHOBIA = auto()
    DULUNCHEPHOBIA = auto()
    DUMASAPHOBIA = auto()
    DUMPSTERPHOBIA = auto()
    DUOPHOBIA = auto()
    DVDPHOBIA = auto()
    EAPALLIOPHOBIA = auto()
    EARMUFFPHOBIA = auto()
    EBULLIOPHOBIA = auto()
    OIKOPHOBIA = auto()
    EIFFELTURRIPHOBIA = auto()
    EISOPTROPHOBIA = auto()
    ELECTROPHOBIA = auto()
    ELEVATOPHOBIA = auto()
    ELEVAPHOBIA = auto()
    EMAILPHOBIA = auto()
    ENERGYPHOBIA = auto()
    ENISSOPHOBIA = auto()
    ENTAMAPHOBIA = auto()
    ENYDREIOPHOBIA = auto()
    EPIPLAPHOBIA = auto()
    EPISTOLAPHOBIA = auto()
    EPISTEMOPHOBIA = auto()
    ERGALEIOPHOBIA = auto()
    ERYTHOPHOBIA = auto()
    EREUTHOPHOBIA = auto()
    ESCALAPHOBIA = auto()
    ROLTRAPHOBIA = auto()
    ESCALATOPHOBIA = auto()
    ESOROUCHAPHOBIA = auto()
    ETHISMOSOPHOBIA = auto()
    EUPHOBIA = auto()
    EUPISTOPHOBIA = auto()
    EVODIAPHOBIA = auto()
    FADCHOONGPHOBIA = auto()
    FASCIOLISPHOBIA = auto()
    FAKELOPHOBIA = auto()
    FAKOSPHOBIA = auto()
    FANARIPHOBIA = auto()
    FARASIPHOBIA = auto()
    FENBANPHOBIA = auto()
    FERETROPHOBIA = auto()
    FERROPHOBIA = auto()
    FICTOPHOBIA = auto()
    FILICOPHOBIA = auto()
    FILOPHOBIA = auto()
    FIREHYDRANTPHOBIA = auto()
    FLASCIPHOBIA = auto()
    FLITZANIPHOBIA = auto()
    FLITZANISAGIOUPHOBIA = auto()
    FOCOPHOBIA = auto()
    FOONIPHOBIA = auto()
    FOREMAPHOBIA = auto()
    FORMIDOPHOBIA = auto()
    FORNACIPHOBIA = auto()
    FORUMPHOBIA = auto()
    FOSSILPHOBIA = auto()
    FOURNOPHOBIA = auto()
    FOUSTAPHOBIA = auto()
    FRACHTIPHOBIA = auto()
    FRAGMAPHOBIA = auto()
    FREARPHOBIA = auto()
    FRENOPHOBIA = auto()
    FR%PLOPHOBIA = auto()
    FUMIPHOBIA = auto()
    FURNGZUPHOBIA = auto()
    FWAUTPHOBIA = auto()
    FWONGIPHOBIA = auto()
    FYLLOFYSOPHOBIA = auto()
    GAKKIPHOBIA = auto()
    GASGAUGEPHOBIA = auto()
    GASPEDALPHOBIA = auto()
    GELIOPHOBIA = auto()
    GERAPHOBIA = auto()
    GEUMAPHOBIA = auto()
    GATNOBPHOBIA = auto()
    GLEYMOPHOBIA = auto()
    GLOBOPHOBIA = auto()
    GL÷NDOPHOBIA = auto()
    GOOGLEPHOBIA = auto()
    GOUWUCHEPHOBIA = auto()
    GRAFEIOPHOBIA = auto()
    GRAFFITIPHOBIA = auto()
    GRAMMATOSIMOPHOBIA = auto()
    GRANDSLAMWICHPHOBIA = auto()
    GR?SOPHOBIA = auto()
    GYALIAILIOUPHOBIA = auto()
    G4GOPHOBIA = auto()
    HAGIOPHOBIA = auto()
    HANDCUFFPHOBIA = auto()
    HEADLIGHTPHOBIA = auto()
    HEADPHONOPHOBIA = auto()
    HEARINGAIDPHOBIA = auto()
    HEDGETROPHOBIA = auto()
    HEIZGEPHOBIA = auto()
    HERESYPHOBIA = auto()
    HEREIOPHOBIA = auto()
    HERPETOPHOBIA = auto()
    HIBERNICAPHOBIA = auto()
    HIEROPHOBIA = auto()
    HLEGUPHOBIA = auto()
    HMOSHGOPHOBIA = auto()
    HNIRSHUNPHOBIA = auto()
    HOCKEYPHOBIA = auto()
    HOPLOPHOBIA = auto()
    HOSEPHOBIA = auto()
    HRONGYOPHOBIA = auto()
    HUMORPHOBIA = auto()
    HYELOPHOBIA = auto()
    HYGROPHOBIA = auto()
    HYLEPHOBIA = auto()
    HYPENGYOPHOBIA = auto()
    H8POPHOBIA = auto()
    ICONOPHOBIA = auto()
    IDEOPHOBIA = auto()
    IMEROLOGIOPHOBIA = auto()
    INTERCOMPHOBIA = auto()
    INTERNETPHOBIA = auto()
    JIJINGPHOBIA = auto()
    JUKEBOXOPHOBIA = auto()
    JULELOPHOBIA = auto()
    J9DOBPHOBIA = auto()
    KAFETIPHOBIA = auto()
    KALATHIPHOBIA = auto()
    KALTSAPHOBIA = auto()
    KAMARAKIPHOBIA = auto()
    KAMPANAPHOBIA = auto()
    KANAYAPHOBIA = auto()
    KAPELAPHOBIA = auto()
    KARAZPHOBIA = auto()
    KARAZPORTANOICHTIRIPHOBIA = auto()
    KARAZPORTAPHOBIA = auto()
    KARFIPHOBIA = auto()
    KAROTSAKIPHOBIA = auto()
    KASSAPHOBIA = auto()
    KASONIPHOBIA = auto()
    KATAGELOPHOBIA = auto()
    KATSAVIDIPHOBIA = auto()
    KATARRAKTIPHOBIA = auto()
    KEFIPHOBIA = auto()
    KENOPHOBIA = auto()
    KERAPHOBIA = auto()
    KERASOPHOBIA = auto()
    KERIPHOBIA = auto()
    KIFNAPHOBIA = auto()
    KILNPHOBIA = auto()
    KINZODOPHOBIA = auto()
    KIROMPIGIAPHOBIA = auto()
    KLEIDARIAPHOBIA = auto()
    KLEIDIPHOBIA = auto()
    KLƐBZEENPHOBIA = auto()
    KOINONIPHOBIA = auto()
    KOLONIAPHOBIA = auto()
    KONSENTOPHOBIA = auto()
    KOSMEMOPHOBIA = auto()
    KOUMPIPHOBIA = auto()
    KOUNIAPHOBIA = auto()
    KOUVAPHOBIA = auto()
    KOUZIPHOBIA = auto()
    KREMASTRAPHOBIA = auto()
    KYPELLOPHOBIA = auto()
    K2NQIPHOBIA = auto()
    LADDERPHOBIA = auto()
    LAGOUMIPHOBIA = auto()
    LAMPAPHOBIA = auto()
    LASTICHOPHOBIA = auto()
    LATERIPHOBIA = auto()
    LECHOPHOBIA = auto()
    LENTOPHOBIA = auto()
    LEVOPHOBIA = auto()
    LIGAMENTOPHOBIA = auto()
    LIGHTERPHOBIA = auto()
    LIGYROPHOBIA = auto()
    LIMNIPHOBIA = auto()
    LINONOPHOBIA = auto()
    LINYUPHOBIA = auto()
    LOCKERPHOBIA = auto()
    LODICULAPHOBIA = auto()
    LOGICOMECHANIBIOPHOBIA = auto()
    LOGOCRISIAPHOBIA = auto()
    LOUTROPHOBIA = auto()
    LRASHAPHOBIA = auto()
    LUMENOPHOBIA = auto()
    LUODOPHOBIA = auto()
    LYSBRYTOPHOBIA = auto()
    MAGEIREIOPHOBIA = auto()
    MAIKBANPHOBIA = auto()
    MONOXEIDIOANTHRAKAPHOBIA = auto()
    MAGEIACHALIPHOBIA = auto()
    MAGIKORAVDIPHOBIA = auto()
    MAGNITOFONOPHOBIA = auto()
    MANHOLEPHOBIA = auto()
    MANUSSICCUSPHOBIA = auto()
    MAPPOPHOBIA = auto()
    MARKADOROPHOBIA = auto()
    MATTERPHOBIA = auto()
    MECHANOPHOBIA = auto()
    MEDIAPHOBIA = auto()
    MEGALOPHOBIA = auto()
    MEGAPHONOPHOBIA = auto()
    MELOPHOBIA = auto()
    MEMEPHOBIA = auto()
    MEMEOPHOBIA = auto()
    MENOPHOBIA = auto()
    METAZODEPHOBIA = auto()
    MICROPHONOPHOBIA = auto()
    MINICELAROPHOBIA = auto()
    MYSOPHOBIA = auto()
    METROPHOBIA = auto()
    MICROPHOBIA = auto()
    MYCROPHOBIA = auto()
    MICROSCOPOPHOBIA = auto()
    MICROVOPHOBIA = auto()
    MLAFENPHOBIA = auto()
    MNEMOPHOBIA = auto()
    MRNPHOBIA = auto()
    MOLYVIPHOBIA = auto()
    MUNJINGPHOBIA = auto()
    MYKITAPHOBIA = auto()
    MYTHOPHOBIA = auto()
    NAITOSUTANDOPHOBIA = auto()
    NECROPHOBIA = auto()
    NEOPHOBIA = auto()
    NICKELPHOBIA = auto()
    NIJOONGPHOBIA = auto()
    NLAIGUPHOBIA = auto()
    NINTENDOPHOBIA = auto()
    NOJESCENTROPHOBIA = auto()
    NOTOPHOBIA = auto()
    NRASOBPHOBIA = auto()
    NUCLEOMITUPHOBIA = auto()
    NWUMPOPHOBIA = auto()
    N☽MWUPHOBIA = auto()
    OBJECTSHOWPHOBIA = auto()
    OCTAGONPHOBIA = auto()
    OIKOPHOBIA = auto()
    OMNIPHOBIA = auto()
    ONEHUNDREDBOTTLESOFBEERPHOBIA = auto()
    OPINATOPHOBIA = auto()
    OPIOPHOBIA = auto()
    ORATOPAROPHOBIA = auto()
    ORDCLAVIPHOBIA = auto()
    ORTHOPHOBIA = auto()
    OSMOPHOBIA = auto()
    OSOURIPHOBIA = auto()
    OTASPIDAPHOBIA = auto()
    OULINOPHOBIA = auto()
    OURITIRIOPHOBIA = auto()
    OVALPHOBIA = auto()
    PACTORBOPHOBIA = auto()
    PAGOPHOBIA = auto()
    PAMPHOBIA = auto()
    PANOPHOBIA = auto()
    PANPHOBIA = auto()
    PANTELONIPHOBIA = auto()
    PANTOPHOBIA = auto()
    PAPOUTSIPHOBIA = auto()
    PAPYROPHOBIA = auto()
    PAYPHONOPHOBIA = auto()
    PATROIOPHOBIA = auto()
    PECCATOPHOBIA = auto()
    PECTUSSPEMOPHOBIA = auto()
    PEDIOPHOBIA = auto()
    PENCILLOPHOBIA = auto()
    PENNYPHOBIA = auto()
    PERSTILBOSPHERPHOBIA = auto()
    PEZODROMIOPHOBIA = auto()
    PHILOSOPHOBIA = auto()
    PHONOPHOBIA = auto()
    PHOTOAUGLIAPHOBIA = auto()
    PHOTOGRAPHOPHOBIA = auto()
    PHOTOPHOBIA = auto()
    PIATOPHOBIA = auto()
    PICTOPHOBIA = auto()
    PINGBOPHOBIA = auto()
    PINGPONGPHOBIA = auto()
    PISTOTIKIKARTAPHOBIA = auto()
    PITHANOPHOBIA = auto()
    PLACOPHOBIA = auto()
    PLAKIDIOPHOBIA = auto()
    PLANOPHOBIA = auto()
    PLASTOPHOBIA = auto()
    PLYNTIPHOBIA = auto()
    POLYPHOBIA = auto()
    POOLPHOBIA = auto()
    PORTBANKAZPHOBIA = auto()
    POSTALPHOBIA = auto()
    POTAMOPHOBIA = auto()
    POUKAMISOPHOBIA = auto()
    PRAGMATICOPHOBIA = auto()
    PRAXIPHOBIA = auto()
    PRINTERPHOBIA = auto()
    PROPHETOPHOBIA = auto()
    PROSOPHOBIA = auto()
    P🎈GRONPHOBIA = auto()
    PSALIDIPHOBIA = auto()
    PSICHAPHOBIA = auto()
    PSYCHOPHOBIA = auto()
    PSYGEPHOBIA = auto()
    PUMPPUPHOBIA = auto()
    PUPAPHOBIA = auto()
    PURINSUMPHOBIA = auto()
    PURGAMENTOPHOBIA = auto()
    PYLIPHOBIA = auto()
    PYROPHOBIA = auto()
    PYROTECHNOPHOBIA = auto()
    PYRSOPHOBIA = auto()
    P🐟XMOPHOBIA = auto()
    P3NSOPHOBIA = auto()
    QAGAZUSAQPHOBIA = auto()
    QIEDJINGPHOBIA = auto()
    QUARTERPHOBIA = auto()
    RADIOPHOBIA = auto()
    RASEMAPHOBIA = auto()
    RAVDIPHOBIA = auto()
    R🚦CREBPHOBIA = auto()
    RECEIPTPHOBIA = auto()
    RECREATIONPHOBIA = auto()
    RELAXATIONPHOBIA = auto()
    REMINDERPHOBIA = auto()
    REMMIÐOPHOBIA = auto()
    RENWUPHOBIA = auto()
    REQIQIUPHOBIA = auto()
    RESHUIQIPHOBIA = auto()
    RETAINERPHOBIA = auto()
    REVMAGRAMMIPHOBIA = auto()
    RINGOPHOBIA = auto()
    RLERROPHOBIA = auto()
    ROBOPHOBIA = auto()
    ROLLERSKATEPHOBIA = auto()
    ROLLATOPHOBIA = auto()
    ROLOIPHOBIA = auto()
    R🚗ZNONPHOBIA = auto()
    RWECONPHOBIA = auto()
    SAKIDIOPHOBIA = auto()
    SAKOULAPHOBIA = auto()
    SANTAKIPHOBIA = auto()
    SAXOPHONOPHOBIA = auto()
    SCATOPHOBIA = auto()
    SCHARAPHOBIA = auto()
    SCIOPHOBIA = auto()
    SCOTOMAPHOBIA = auto()
    SCRINIAPHOBIA = auto()
    SEIRINAPHOBIA = auto()
    SEPLOPHOBIA = auto()
    SENOƩUPHOBIA = auto()
    SFAIRAPHOBIA = auto()
    SFOUNGARISTRAPHOBIA = auto()
    SFYRIPHOBIA = auto()
    SHUICAOPHOBIA = auto()
    SH5DOPHOBIA = auto()
    SIMAPHOBIA = auto()
    SINISTROPHOBIA = auto()
    SIXFLAGSPHOBIA = auto()
    SHIJIPHOBIA = auto()
    SHOEBOXPHOBIA = auto()
    SHWNPHOBIA = auto()
    SH☀GMOPHOBIA = auto()
    SKATEBOARDPHOBIA = auto()
    SKOUPAPHOBIA = auto()
    SNEROLAKOPHOBIA = auto()
    SOLOIPHOBIA = auto()
    SOTERIOPHOBIA = auto()
    SPACESUITPHOBIA = auto()
    SPASMENAGALIAPHOBIA = auto()
    SPEEDOMOPHOBIA = auto()
    SPHYGMOMANOPHOBIA = auto()
    SPIRTOPHOBIA = auto()
    SPRINKLERPHOBIA = auto()
    SRANDUOPHOBIA = auto()
    STAUROPHOBIA = auto()
    STAVRODROMIPHOBIA = auto()
    STENOPHOBIA = auto()
    STETHOSCOPEPHOBIA = auto()
    STICKERPHOBIA = auto()
    STOCKINGPHOBIA = auto()
    STOPSIGNPHOBIA = auto()
    STRANCAPHOBIA = auto()
    STRANTOPHOBIA = auto()
    STREETLIGHTPHOBIA = auto()
    STROVOPHOBIA = auto()
    STYLOPHOBIA = auto()
    ST📹PROPHOBIA = auto()
    SUBMECHANOPHOBIA = auto()
    SURFBOARDPHOBIA = auto()
    SYMBOLOPHOBIA = auto()
    SYNDETIRAPHOBIA = auto()
    SYNTRIVANIPHOBIA = auto()
    SYSKEVIPHOBIA = auto()
    S🐦GMOPHOBIA = auto()
    TABULATOPHOBIA = auto()
    TAILLIGHTPHOBIA = auto()
    FDS_HFKDSHFKJHSDKJFHSDKJFHDSKJFHSKJFHSDKJPHOBIA = auto()
    TAIÞUPHOBIA = auto()
    TAMEIOPHOBIA = auto()
    TAPETSARIAPHOBIA = auto()
    TAPHOSPHOBIA = auto()
    TECHNOPHOBIA = auto()
    TECTOPHOBIA = auto()
    TEGOPHOBIA = auto()
    TELEOPHOBIA = auto()
    TELEPHONOPHOBIA = auto()
    TELESCOPOPHOBIA = auto()
    TERRAMOPHOBIA = auto()
    TERRORPHOBIA = auto()
    TEXTOPHOBIA = auto()
    THAUMATOPHOBIA = auto()
    THEOLOGICOPHOBIA = auto()
    THEOPHOBIA = auto()
    THERMOMOPHOBIA = auto()
    THERMOSTATPHOBIA = auto()
    THESAUROPHOBIA = auto()
    TIGANIPHOBIA = auto()
    TILECHEIRISTIRIOPHOBIA = auto()
    TINGCHECHANGPHOBIA = auto()
    TINGCHECHEKUPHOBIA = auto()
    TLINGHUPHOBIA = auto()
    TOASTERPHOBIA = auto()
    TOICHOPHOBIA = auto()
    TOPOPHOBIA = auto()
    TOUALETAPHOBIA = auto()
    TOUVLOPHOBIA = auto()
    TRAGOUDIPHOBIA = auto()
    TRAPEZAPHOBIA = auto()
    TROKHOPHOBIA = auto()
    TROMPETAPHOBIA = auto()
    TROPHOPHOBIA = auto()
    TRƐDNOPHOBIA = auto()
    TRYPANOPHOBIA = auto()
    TRYPOPHOBIA = auto()
    TR✈️GMOPHOBIA = auto()
    TURRIPHOBIA = auto()
    TYCHOPHOBIA = auto()
    TYMPANOPHOBIA = auto()
    TƜDROPHOBIA = auto()
    UMBRAPHOBIA = auto()
    UMBRELLAPHOBIA = auto()
    VAGONIPHOBIA = auto()
    VALANTIOPHOBIA = auto()
    VALITSAPHOBIA = auto()
    VERKEINTRIPHOBIA = auto()
    VESTIPHOBIA = auto()
    VIEMAPHOBIA = auto()
    VIDEOCASSETTOPHOBIA = auto()
    VINITOPHOBIA = auto()
    VIOLIPHOBIA = auto()
    VOEDSEPHOBIA = auto()
    VOIDOPHOBIA = auto()
    VOLANPHOBIA = auto()
    VORRAPHOBIA = auto()
    VOTHROPHOBIA = auto()
    VOULISIPHOBIA = auto()
    VINYLOPHOBIA = auto()
    V🚫SHROPHOBIA = auto()
    WANJUWUPHOBIA = auto()
    WHEELCHAIRPHOBIA = auto()
    WICCAPHOBIA = auto()
    WLANOPHOBIA = auto()
    XAFNIASMAPHOBIA = auto()
    X!MZOPHOBIA = auto()
    XINXIANGPHOBIA = auto()
    XYLOPHONOPHOBIA = auto()
    XYPNITIRIPHOBIA = auto()
    XYROPHOBIA = auto()
    W@NOPHOBIA = auto()
    YEDANSHUPHOBIA = auto()
    YEDENGPHOBIA = auto()
    YGROPHOBIA = auto()
    YINJIPHOBIA = auto()
    YINSHUIJIPHOBIA = auto()
    YLOPHOBIA = auto()
    YROUXPHOBIA = auto()
    YPNODOMATIOPHOBIA = auto()
    YUPENPHOBIA = auto()
    YUSHIXISHOPHOBIA = auto()
    YUSHUAPHOBIA = auto()
    YWAOHUPHOBIA = auto()
    Y∞GOMPHOBIA = auto()
    ZAPSAULPHOBIA = auto()
    ZARIPHOBIA = auto()
    ZHAOQINPHOBIA = auto()
    ZHINCHAPHOBIA = auto()
    ZHUOJPHOBIA = auto()
    ZIDONGSHOPHOBIA = auto()
    ZIZANMEPHOBIA = auto()
    ZLOQINGPHOBIA = auto()
    Z📷MROTPHOBIA = auto()
    ZONIASFALEIAPHOBIA = auto()
    ZRAIDOPHOBIA = auto()
    ZUIGERPHOBIA = auto()
    ZWUQIPHOBIA = auto()
    ZYGARIAPHOBIA = auto()


THINGS_PHOBIAS_NAMES_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    ThingsPhobias.ADIAFANOPHOBIA: {
        Languages.ENGLISH: "Adiafanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ADVERTISEMENTPHOBIA: {
        Languages.ENGLISH: "Advertisementphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.AEROSAKAPHOBIA: {
        Languages.ENGLISH: "Aerosakaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.AICHMOPHOBIA: {
        Languages.ENGLISH: "Aichmophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.AIRCOPHOBIA: {
        Languages.ENGLISH: "Aircophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.AIRPODAPHOBIA: {
        Languages.ENGLISH: "Airpodaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ALARMOPHOBIA: {
        Languages.ENGLISH: "Alarmophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ALLODOXAPHOBIA: {
        Languages.ENGLISH: "Allodoxaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ALTOCELAROPHOBIA: {
        Languages.ENGLISH: "Altocelarophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ANEMISTIRAPHOBIA: {
        Languages.ENGLISH: "Anemistiraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ANIMAPHOBIA: {
        Languages.ENGLISH: "Animaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ANTANAKLOPHOBIA: {
        Languages.ENGLISH: "Antanaklophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ANTENNAPHOBIA: {
        Languages.ENGLISH: "Antennaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.APEIROPHOBIA: {
        Languages.ENGLISH: "Apeirophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.APOSTASIPHOBIA: {
        Languages.ENGLISH: "Apostasiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.APPLETVAPHOBIA: {
        Languages.ENGLISH: "Appletvaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.AQUAMECHANOPHOBIA: {
        Languages.ENGLISH: "Aquamechanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ARACHTOPHOBIA: {
        Languages.ENGLISH: "Arachtophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ARCHEIOTHIKIPHOBIA: {
        Languages.ENGLISH: "Archeiothikiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ARMAROPHOBIA: {
        Languages.ENGLISH: "Armarophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ARPAPHOBIA: {
        Languages.ENGLISH: "Arpaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ARTEMOPHOBIA: {
        Languages.ENGLISH: "Artemophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.AULOPHOBIA: {
        Languages.ENGLISH: "Aulophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.AUTOKERAPHOBIA: {
        Languages.ENGLISH: "Autokeraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.AUTOPLENOPHOBIA: {
        Languages.ENGLISH: "Autoplenophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.AUTOMATONOPHOBIA: {
        Languages.ENGLISH: "Automatonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BACOPHOBIA: {
        Languages.ENGLISH: "Bacophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BAHNUBOPHOBIA: {
        Languages.ENGLISH: "Bahnubophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BALLISTOPHOBIA: {
        Languages.ENGLISH: "Ballistophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BALTEUSPHOBIA: {
        Languages.ENGLISH: "Balteusphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BALTICOPHOBIA: {
        Languages.ENGLISH: "Balticophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BANDZOPHOBIA: {
        Languages.ENGLISH: "Bandzophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BANMAXIANPHOBIA: {
        Languages.ENGLISH: "Banmaxianphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BAROPHOBIA: {
        Languages.ENGLISH: "Barophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BASSOLOPHOBIA: {
        Languages.ENGLISH: "Bassolophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BATHMOPHOBIA: {
        Languages.ENGLISH: "Bathmophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BATHROBEPHOBIA: {
        Languages.ENGLISH: "Bathrobephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BATTEROPHOBIA: {
        Languages.ENGLISH: "Batterophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BEEPOPHOBIA: {
        Languages.ENGLISH: "Beepophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BELONEPHOBIA: {
        Languages.ENGLISH: "Belonephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BIBLIOPHOBIA: {
        Languages.ENGLISH: "Bibliophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BILLBOARDPHOBIA: {
        Languages.ENGLISH: "Billboardphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BIJIXPHOBIA: {
        Languages.ENGLISH: "Bijixphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BINOCULOPHOBIA: {
        Languages.ENGLISH: "Binoculophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BLEIMPNOPHOBIA: {
        Languages.ENGLISH: "Bleimpnophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BLEMENSAPHOBIA: {
        Languages.ENGLISH: "Blemensaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BLENDERPHOBIA: {
        Languages.ENGLISH: "Blenderphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BLOWERPEELPHOBIA: {
        Languages.ENGLISH: "Blowerpeelphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BRACESPHOBIA: {
        Languages.ENGLISH: "Bracesphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BRUGNOPHOBIA: {
        Languages.ENGLISH: "Brugnophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BODENSTANDOPHOBIA: {
        Languages.ENGLISH: "Bodenstandophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BONOCKOPHOBIA: {
        Languages.ENGLISH: "Bonockophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BOOGIEBOARDPHOBIA: {
        Languages.ENGLISH: "Boogieboardphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BOWERPHOBIA: {
        Languages.ENGLISH: "Bowerphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BOWPHOBIA: {
        Languages.ENGLISH: "Bowphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BRIEFSHIEPHOBIA: {
        Languages.ENGLISH: "Briefshiephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BUHUAJIPHOBIA: {
        Languages.ENGLISH: "Buhuajiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BUZZOPHOBIA: {
        Languages.ENGLISH: "Buzzophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BWAOPIPHOBIA: {
        Languages.ENGLISH: "Bwaopiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.BWAUKPHOBIA: {
        Languages.ENGLISH: "Bwaukphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CABLEPHOBIA: {
        Languages.ENGLISH: "Cablephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CAELOPHOBIA: {
        Languages.ENGLISH: "Caelophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CALCULAPHOBIA: {
        Languages.ENGLISH: "Calculaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CAMCORDERPHOBIA: {
        Languages.ENGLISH: "Camcorderphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CAMERAPHOBIA: {
        Languages.ENGLISH: "Cameraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CAPILLUSSETISPHOBIA: {
        Languages.ENGLISH: "Capillussetisphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CASSETTOPHOBIA: {
        Languages.ENGLISH: "Cassettophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CATASTOLEPHOBIA: {
        Languages.ENGLISH: "Catastolephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CATHEDRAPHOBIA: {
        Languages.ENGLISH: "Cathedraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CATOPTROPHOBIA: {
        Languages.ENGLISH: "Catoptrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CELAROPHOBIA: {
        Languages.ENGLISH: "Celarophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CENOSILICAPHOBIA: {
        Languages.ENGLISH: "Cenosilicaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CHARAKAPHOBIA: {
        Languages.ENGLISH: "Charakaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CHARTIPHOBIA: {
        Languages.ENGLISH: "Chartiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CHEDOANGPHOBIA: {
        Languages.ENGLISH: "Chedoangphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CHEKUXISHOPHOBIA: {
        Languages.ENGLISH: "Chekuxishophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CHIONOFYSOPHOBIA: {
        Languages.ENGLISH: "Chionofysophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CHLOEPHOBIA: {
        Languages.ENGLISH: "Chloephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CHREOSTIKIKARTAPHOBIA: {
        Languages.ENGLISH: "Chreostikikartaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CHROMETOPHOBIA: {
        Languages.ENGLISH: "Chrometophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CHRONOMENTROPHOBIA: {
        Languages.ENGLISH: "Chronomentrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CHUFXISHOPHOBIA: {
        Languages.ENGLISH: "Chufxishophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CISTULAPHOBIA: {
        Languages.ENGLISH: "Cistulaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CITHARAPHOBIA: {
        Languages.ENGLISH: "Citharaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CLAPPERPHOBIA: {
        Languages.ENGLISH: "Clapperphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CLEITHROPHOBIA: {
        Languages.ENGLISH: "Cleithrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CLINEPHOBIA: {
        Languages.ENGLISH: "Clinephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CLOACAPHOBIA: {
        Languages.ENGLISH: "Cloacaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.COGOMBOPHOBIA: {
        Languages.ENGLISH: "Cogombophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.COLIMBOPHOBIA: {
        Languages.ENGLISH: "Colimbophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.COMMERCIALPHOBIA: {
        Languages.ENGLISH: "Commercialphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.COMPASSPHOBIA: {
        Languages.ENGLISH: "Compassphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CONFETTIPHOBIA: {
        Languages.ENGLISH: "Confettiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CONSECOTALEOPHOBIA: {
        Languages.ENGLISH: "Consecotaleophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CONTROSOFFITTOPHOBIA: {
        Languages.ENGLISH: "Controsoffittophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.COZAMPIOPHOBIA: {
        Languages.ENGLISH: "Cozampiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CRANOPHOBIA: {
        Languages.ENGLISH: "Cranophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CREMNOPHOBIA: {
        Languages.ENGLISH: "Cremnophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CRUSRUMBLOPHOBIA: {
        Languages.ENGLISH: "Crusrumblophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CUPROLAMINOPHOBIA: {
        Languages.ENGLISH: "Cuprolaminophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CYBERPHOBIA: {
        Languages.ENGLISH: "Cyberphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.CYMOPHOBIA: {
        Languages.ENGLISH: "Cymophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DACHOINGPHOBIA: {
        Languages.ENGLISH: "Dachoingphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DARTBOARDPHOBIA: {
        Languages.ENGLISH: "Dartboardphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DARTOPHOBIA: {
        Languages.ENGLISH: "Dartophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DEFENESTRAPHOBIA: {
        Languages.ENGLISH: "Defenestraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DEKANIKIPHOBIA: {
        Languages.ENGLISH: "Dekanikiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DELEOPHOBIA: {
        Languages.ENGLISH: "Deleophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DENGPAOPHOBIA: {
        Languages.ENGLISH: "Dengpaophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DENTODRAPANOPHOBIA: {
        Languages.ENGLISH: "Dentodrapanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DENTUREPHOBIA: {
        Languages.ENGLISH: "Denturephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DEXTROPHOBIA: {
        Languages.ENGLISH: "Dextrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DIAFANOPHOBIA: {
        Languages.ENGLISH: "Diafanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DIANZIFANKUIPHOBIA: {
        Languages.ENGLISH: "Dianzifankuiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DIAPERPHOBIA: {
        Languages.ENGLISH: "Diaperphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DIAPHIMISTICOPHOBIA: {
        Languages.ENGLISH: "Diaphimisticophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DIASTIMAPHOBIA: {
        Languages.ENGLISH: "Diastimaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DIATHLASOPHOBIA: {
        Languages.ENGLISH: "Diathlasophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DICLEBGOPHOBIA: {
        Languages.ENGLISH: "Diclebgophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DIETHNESYSTIMAMONADONOPHOBIA: {
        Languages.ENGLISH: "Diethnesystimamonadonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DIKEPHOBIA: {
        Languages.ENGLISH: "Dikephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DIMEPHOBIA: {
        Languages.ENGLISH: "Dimephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DINGOPHOBIA: {
        Languages.ENGLISH: "Dingophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DINOPHOBIA: {
        Languages.ENGLISH: "Dinophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DISHLEPROPHOBIA: {
        Languages.ENGLISH: "Dishleprophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DIZOANGPHOBIA: {
        Languages.ENGLISH: "Dizoangphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DLITOPHOBIA: {
        Languages.ENGLISH: "Dlitophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DOMINEATHERPHOBIA: {
        Languages.ENGLISH: "Domineatherphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DOORBELLPHOBIA: {
        Languages.ENGLISH: "Doorbellphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DORAPHOBIA: {
        Languages.ENGLISH: "Doraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DORNGOPHOBIA: {
        Languages.ENGLISH: "Dorngophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DORYFORIKOCHARTIPHOBIA: {
        Languages.ENGLISH: "Doryforikochartiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DOTTOPHOBIA: {
        Languages.ENGLISH: "Dottophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DRAPANOPHOBIA: {
        Languages.ENGLISH: "Drapanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DRIKRONPHOBIA: {
        Languages.ENGLISH: "Drikronphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DROGERPHOBIA: {
        Languages.ENGLISH: "Drogerphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DROMUSEPHOBIA: {
        Languages.ENGLISH: "Dromusephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DULUNCHEPHOBIA: {
        Languages.ENGLISH: "Dulunchephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DUMASAPHOBIA: {
        Languages.ENGLISH: "Dumasaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DUMPSTERPHOBIA: {
        Languages.ENGLISH: "Dumpsterphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DUOPHOBIA: {
        Languages.ENGLISH: "Duophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.DVDPHOBIA: {
        Languages.ENGLISH: "Dvdphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.EAPALLIOPHOBIA: {
        Languages.ENGLISH: "Eapalliophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.EARMUFFPHOBIA: {
        Languages.ENGLISH: "Earmuffphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.EBULLIOPHOBIA: {
        Languages.ENGLISH: "Ebulliophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.OIKOPHOBIA: {
        Languages.ENGLISH: "Oikophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.EIFFELTURRIPHOBIA: {
        Languages.ENGLISH: "Eiffelturriphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.EISOPTROPHOBIA: {
        Languages.ENGLISH: "Eisoptrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ELECTROPHOBIA: {
        Languages.ENGLISH: "Electrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ELEVATOPHOBIA: {
        Languages.ENGLISH: "Elevatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ELEVAPHOBIA: {
        Languages.ENGLISH: "Elevaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.EMAILPHOBIA: {
        Languages.ENGLISH: "Emailphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ENERGYPHOBIA: {
        Languages.ENGLISH: "Energyphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ENISSOPHOBIA: {
        Languages.ENGLISH: "Enissophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ENTAMAPHOBIA: {
        Languages.ENGLISH: "Entamaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ENYDREIOPHOBIA: {
        Languages.ENGLISH: "Enydreiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.EPIPLAPHOBIA: {
        Languages.ENGLISH: "Epiplaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.EPISTOLAPHOBIA: {
        Languages.ENGLISH: "Epistolaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.EPISTEMOPHOBIA: {
        Languages.ENGLISH: "Epistemophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ERGALEIOPHOBIA: {
        Languages.ENGLISH: "Ergaleiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ERYTHOPHOBIA: {
        Languages.ENGLISH: "Erythophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.EREUTHOPHOBIA: {
        Languages.ENGLISH: "Ereuthophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ESCALAPHOBIA: {
        Languages.ENGLISH: "Escalaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ROLTRAPHOBIA: {
        Languages.ENGLISH: "Roltraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ESCALATOPHOBIA: {
        Languages.ENGLISH: "Escalatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ESOROUCHAPHOBIA: {
        Languages.ENGLISH: "Esorouchaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ETHISMOSOPHOBIA: {
        Languages.ENGLISH: "Ethismosophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.EUPHOBIA: {
        Languages.ENGLISH: "Euphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.EUPISTOPHOBIA: {
        Languages.ENGLISH: "Eupistophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.EVODIAPHOBIA: {
        Languages.ENGLISH: "Evodiaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FADCHOONGPHOBIA: {
        Languages.ENGLISH: "Fadchoongphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FASCIOLISPHOBIA: {
        Languages.ENGLISH: "Fasciolisphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FAKELOPHOBIA: {
        Languages.ENGLISH: "Fakelophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FAKOSPHOBIA: {
        Languages.ENGLISH: "Fakosphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FANARIPHOBIA: {
        Languages.ENGLISH: "Fanariphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FARASIPHOBIA: {
        Languages.ENGLISH: "Farasiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FENBANPHOBIA: {
        Languages.ENGLISH: "Fenbanphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FERETROPHOBIA: {
        Languages.ENGLISH: "Feretrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FERROPHOBIA: {
        Languages.ENGLISH: "Ferrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FICTOPHOBIA: {
        Languages.ENGLISH: "Fictophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FILICOPHOBIA: {
        Languages.ENGLISH: "Filicophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FILOPHOBIA: {
        Languages.ENGLISH: "Filophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FIREHYDRANTPHOBIA: {
        Languages.ENGLISH: "Firehydrantphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FLASCIPHOBIA: {
        Languages.ENGLISH: "Flasciphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FLITZANIPHOBIA: {
        Languages.ENGLISH: "Flitzaniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FLITZANISAGIOUPHOBIA: {
        Languages.ENGLISH: "Flitzanisagiouphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FOCOPHOBIA: {
        Languages.ENGLISH: "Focophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FOONIPHOBIA: {
        Languages.ENGLISH: "Fooniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FOREMAPHOBIA: {
        Languages.ENGLISH: "Foremaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FORMIDOPHOBIA: {
        Languages.ENGLISH: "Formidophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FORNACIPHOBIA: {
        Languages.ENGLISH: "Fornaciphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FORUMPHOBIA: {
        Languages.ENGLISH: "Forumphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FOSSILPHOBIA: {
        Languages.ENGLISH: "Fossilphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FOURNOPHOBIA: {
        Languages.ENGLISH: "Fournophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FOUSTAPHOBIA: {
        Languages.ENGLISH: "Foustaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FRACHTIPHOBIA: {
        Languages.ENGLISH: "Frachtiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FRAGMAPHOBIA: {
        Languages.ENGLISH: "Fragmaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FREARPHOBIA: {
        Languages.ENGLISH: "Frearphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FRENOPHOBIA: {
        Languages.ENGLISH: "Frenophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FR%PLOPHOBIA: {
        Languages.ENGLISH: "Fr%Plophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FUMIPHOBIA: {
        Languages.ENGLISH: "Fumiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FURNGZUPHOBIA: {
        Languages.ENGLISH: "Furngzuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FWAUTPHOBIA: {
        Languages.ENGLISH: "Fwautphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FWONGIPHOBIA: {
        Languages.ENGLISH: "Fwongiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FYLLOFYSOPHOBIA: {
        Languages.ENGLISH: "Fyllofysophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GAKKIPHOBIA: {
        Languages.ENGLISH: "Gakkiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GASGAUGEPHOBIA: {
        Languages.ENGLISH: "Gasgaugephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GASPEDALPHOBIA: {
        Languages.ENGLISH: "Gaspedalphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GELIOPHOBIA: {
        Languages.ENGLISH: "Geliophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GERAPHOBIA: {
        Languages.ENGLISH: "Geraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GEUMAPHOBIA: {
        Languages.ENGLISH: "Geumaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GATNOBPHOBIA: {
        Languages.ENGLISH: "Gatnobphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GLEYMOPHOBIA: {
        Languages.ENGLISH: "Gleymophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GLOBOPHOBIA: {
        Languages.ENGLISH: "Globophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GL÷NDOPHOBIA: {
        Languages.ENGLISH: "Gl÷Ndophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GOOGLEPHOBIA: {
        Languages.ENGLISH: "Googlephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GOUWUCHEPHOBIA: {
        Languages.ENGLISH: "Gouwuchephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GRAFEIOPHOBIA: {
        Languages.ENGLISH: "Grafeiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GRAFFITIPHOBIA: {
        Languages.ENGLISH: "Graffitiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GRAMMATOSIMOPHOBIA: {
        Languages.ENGLISH: "Grammatosimophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GRANDSLAMWICHPHOBIA: {
        Languages.ENGLISH: "Grandslamwichphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GR?SOPHOBIA: {
        Languages.ENGLISH: "Gr?Sophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.GYALIAILIOUPHOBIA: {
        Languages.ENGLISH: "Gyaliailiouphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.G4GOPHOBIA: {
        Languages.ENGLISH: "G4Gophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HAGIOPHOBIA: {
        Languages.ENGLISH: "Hagiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HANDCUFFPHOBIA: {
        Languages.ENGLISH: "Handcuffphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HEADLIGHTPHOBIA: {
        Languages.ENGLISH: "Headlightphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HEADPHONOPHOBIA: {
        Languages.ENGLISH: "Headphonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HEARINGAIDPHOBIA: {
        Languages.ENGLISH: "Hearingaidphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HEDGETROPHOBIA: {
        Languages.ENGLISH: "Hedgetrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HEIZGEPHOBIA: {
        Languages.ENGLISH: "Heizgephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HERESYPHOBIA: {
        Languages.ENGLISH: "Heresyphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HEREIOPHOBIA: {
        Languages.ENGLISH: "Hereiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HERPETOPHOBIA: {
        Languages.ENGLISH: "Herpetophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HIBERNICAPHOBIA: {
        Languages.ENGLISH: "Hibernicaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HIEROPHOBIA: {
        Languages.ENGLISH: "Hierophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HLEGUPHOBIA: {
        Languages.ENGLISH: "Hleguphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HMOSHGOPHOBIA: {
        Languages.ENGLISH: "Hmoshgophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HNIRSHUNPHOBIA: {
        Languages.ENGLISH: "Hnirshunphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HOCKEYPHOBIA: {
        Languages.ENGLISH: "Hockeyphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HOPLOPHOBIA: {
        Languages.ENGLISH: "Hoplophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HOSEPHOBIA: {
        Languages.ENGLISH: "Hosephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HRONGYOPHOBIA: {
        Languages.ENGLISH: "Hrongyophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HUMORPHOBIA: {
        Languages.ENGLISH: "Humorphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HYELOPHOBIA: {
        Languages.ENGLISH: "Hyelophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HYGROPHOBIA: {
        Languages.ENGLISH: "Hygrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HYLEPHOBIA: {
        Languages.ENGLISH: "Hylephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.HYPENGYOPHOBIA: {
        Languages.ENGLISH: "Hypengyophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.H8POPHOBIA: {
        Languages.ENGLISH: "H8Pophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ICONOPHOBIA: {
        Languages.ENGLISH: "Iconophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.IDEOPHOBIA: {
        Languages.ENGLISH: "Ideophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.IMEROLOGIOPHOBIA: {
        Languages.ENGLISH: "Imerologiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.INTERCOMPHOBIA: {
        Languages.ENGLISH: "Intercomphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.INTERNETPHOBIA: {
        Languages.ENGLISH: "Internetphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.JIJINGPHOBIA: {
        Languages.ENGLISH: "Jijingphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.JUKEBOXOPHOBIA: {
        Languages.ENGLISH: "Jukeboxophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.JULELOPHOBIA: {
        Languages.ENGLISH: "Julelophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.J9DOBPHOBIA: {
        Languages.ENGLISH: "J9Dobphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KAFETIPHOBIA: {
        Languages.ENGLISH: "Kafetiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KALATHIPHOBIA: {
        Languages.ENGLISH: "Kalathiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KALTSAPHOBIA: {
        Languages.ENGLISH: "Kaltsaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KAMARAKIPHOBIA: {
        Languages.ENGLISH: "Kamarakiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KAMPANAPHOBIA: {
        Languages.ENGLISH: "Kampanaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KANAYAPHOBIA: {
        Languages.ENGLISH: "Kanayaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KAPELAPHOBIA: {
        Languages.ENGLISH: "Kapelaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KARAZPHOBIA: {
        Languages.ENGLISH: "Karazphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KARAZPORTANOICHTIRIPHOBIA: {
        Languages.ENGLISH: "Karazportanoichtiriphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KARAZPORTAPHOBIA: {
        Languages.ENGLISH: "Karazportaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KARFIPHOBIA: {
        Languages.ENGLISH: "Karfiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KAROTSAKIPHOBIA: {
        Languages.ENGLISH: "Karotsakiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KASSAPHOBIA: {
        Languages.ENGLISH: "Kassaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KASONIPHOBIA: {
        Languages.ENGLISH: "Kasoniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KATAGELOPHOBIA: {
        Languages.ENGLISH: "Katagelophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KATSAVIDIPHOBIA: {
        Languages.ENGLISH: "Katsavidiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KATARRAKTIPHOBIA: {
        Languages.ENGLISH: "Katarraktiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KEFIPHOBIA: {
        Languages.ENGLISH: "Kefiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KENOPHOBIA: {
        Languages.ENGLISH: "Kenophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KERAPHOBIA: {
        Languages.ENGLISH: "Keraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KERASOPHOBIA: {
        Languages.ENGLISH: "Kerasophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KERIPHOBIA: {
        Languages.ENGLISH: "Keriphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KIFNAPHOBIA: {
        Languages.ENGLISH: "Kifnaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KILNPHOBIA: {
        Languages.ENGLISH: "Kilnphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KINZODOPHOBIA: {
        Languages.ENGLISH: "Kinzodophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KIROMPIGIAPHOBIA: {
        Languages.ENGLISH: "Kirompigiaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KLEIDARIAPHOBIA: {
        Languages.ENGLISH: "Kleidariaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KLEIDIPHOBIA: {
        Languages.ENGLISH: "Kleidiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KLƐBZEENPHOBIA: {
        Languages.ENGLISH: "Klɛbzeenphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KOINONIPHOBIA: {
        Languages.ENGLISH: "Koinoniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KOLONIAPHOBIA: {
        Languages.ENGLISH: "Koloniaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KONSENTOPHOBIA: {
        Languages.ENGLISH: "Konsentophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KOSMEMOPHOBIA: {
        Languages.ENGLISH: "Kosmemophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KOUMPIPHOBIA: {
        Languages.ENGLISH: "Koumpiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KOUNIAPHOBIA: {
        Languages.ENGLISH: "Kouniaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KOUVAPHOBIA: {
        Languages.ENGLISH: "Kouvaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KOUZIPHOBIA: {
        Languages.ENGLISH: "Kouziphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KREMASTRAPHOBIA: {
        Languages.ENGLISH: "Kremastraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.KYPELLOPHOBIA: {
        Languages.ENGLISH: "Kypellophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.K2NQIPHOBIA: {
        Languages.ENGLISH: "K2Nqiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LADDERPHOBIA: {
        Languages.ENGLISH: "Ladderphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LAGOUMIPHOBIA: {
        Languages.ENGLISH: "Lagoumiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LAMPAPHOBIA: {
        Languages.ENGLISH: "Lampaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LASTICHOPHOBIA: {
        Languages.ENGLISH: "Lastichophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LATERIPHOBIA: {
        Languages.ENGLISH: "Lateriphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LECHOPHOBIA: {
        Languages.ENGLISH: "Lechophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LENTOPHOBIA: {
        Languages.ENGLISH: "Lentophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LEVOPHOBIA: {
        Languages.ENGLISH: "Levophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LIGAMENTOPHOBIA: {
        Languages.ENGLISH: "Ligamentophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LIGHTERPHOBIA: {
        Languages.ENGLISH: "Lighterphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LIGYROPHOBIA: {
        Languages.ENGLISH: "Ligyrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LIMNIPHOBIA: {
        Languages.ENGLISH: "Limniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LINONOPHOBIA: {
        Languages.ENGLISH: "Linonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LINYUPHOBIA: {
        Languages.ENGLISH: "Linyuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LOCKERPHOBIA: {
        Languages.ENGLISH: "Lockerphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LODICULAPHOBIA: {
        Languages.ENGLISH: "Lodiculaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LOGICOMECHANIBIOPHOBIA: {
        Languages.ENGLISH: "Logicomechanibiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LOGOCRISIAPHOBIA: {
        Languages.ENGLISH: "Logocrisiaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LOUTROPHOBIA: {
        Languages.ENGLISH: "Loutrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LRASHAPHOBIA: {
        Languages.ENGLISH: "Lrashaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LUMENOPHOBIA: {
        Languages.ENGLISH: "Lumenophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LUODOPHOBIA: {
        Languages.ENGLISH: "Luodophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.LYSBRYTOPHOBIA: {
        Languages.ENGLISH: "Lysbrytophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MAGEIREIOPHOBIA: {
        Languages.ENGLISH: "Mageireiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MAIKBANPHOBIA: {
        Languages.ENGLISH: "Maikbanphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MONOXEIDIOANTHRAKAPHOBIA: {
        Languages.ENGLISH: "Monoxeidioanthrakaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MAGEIACHALIPHOBIA: {
        Languages.ENGLISH: "Mageiachaliphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MAGIKORAVDIPHOBIA: {
        Languages.ENGLISH: "Magikoravdiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MAGNITOFONOPHOBIA: {
        Languages.ENGLISH: "Magnitofonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MANHOLEPHOBIA: {
        Languages.ENGLISH: "Manholephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MANUSSICCUSPHOBIA: {
        Languages.ENGLISH: "Manussiccusphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MAPPOPHOBIA: {
        Languages.ENGLISH: "Mappophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MARKADOROPHOBIA: {
        Languages.ENGLISH: "Markadorophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MATTERPHOBIA: {
        Languages.ENGLISH: "Matterphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MECHANOPHOBIA: {
        Languages.ENGLISH: "Mechanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MEDIAPHOBIA: {
        Languages.ENGLISH: "Mediaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MEGALOPHOBIA: {
        Languages.ENGLISH: "Megalophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MEGAPHONOPHOBIA: {
        Languages.ENGLISH: "Megaphonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MELOPHOBIA: {
        Languages.ENGLISH: "Melophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MEMEPHOBIA: {
        Languages.ENGLISH: "Memephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MEMEOPHOBIA: {
        Languages.ENGLISH: "Memeophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MENOPHOBIA: {
        Languages.ENGLISH: "Menophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.METAZODEPHOBIA: {
        Languages.ENGLISH: "Metazodephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MICROPHONOPHOBIA: {
        Languages.ENGLISH: "Microphonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MINICELAROPHOBIA: {
        Languages.ENGLISH: "Minicelarophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MYSOPHOBIA: {
        Languages.ENGLISH: "Mysophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.METROPHOBIA: {
        Languages.ENGLISH: "Metrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MICROPHOBIA: {
        Languages.ENGLISH: "Microphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MYCROPHOBIA: {
        Languages.ENGLISH: "Mycrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MICROSCOPOPHOBIA: {
        Languages.ENGLISH: "Microscopophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MICROVOPHOBIA: {
        Languages.ENGLISH: "Microvophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MLAFENPHOBIA: {
        Languages.ENGLISH: "Mlafenphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MNEMOPHOBIA: {
        Languages.ENGLISH: "Mnemophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MRNPHOBIA: {
        Languages.ENGLISH: "Mrnphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MOLYVIPHOBIA: {
        Languages.ENGLISH: "Molyviphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MUNJINGPHOBIA: {
        Languages.ENGLISH: "Munjingphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MYKITAPHOBIA: {
        Languages.ENGLISH: "Mykitaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.MYTHOPHOBIA: {
        Languages.ENGLISH: "Mythophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.NAITOSUTANDOPHOBIA: {
        Languages.ENGLISH: "Naitosutandophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.NECROPHOBIA: {
        Languages.ENGLISH: "Necrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.NEOPHOBIA: {
        Languages.ENGLISH: "Neophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.NICKELPHOBIA: {
        Languages.ENGLISH: "Nickelphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.NIJOONGPHOBIA: {
        Languages.ENGLISH: "Nijoongphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.NLAIGUPHOBIA: {
        Languages.ENGLISH: "Nlaiguphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.NINTENDOPHOBIA: {
        Languages.ENGLISH: "Nintendophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.NOJESCENTROPHOBIA: {
        Languages.ENGLISH: "Nojescentrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.NOTOPHOBIA: {
        Languages.ENGLISH: "Notophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.NRASOBPHOBIA: {
        Languages.ENGLISH: "Nrasobphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.NUCLEOMITUPHOBIA: {
        Languages.ENGLISH: "Nucleomituphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.NWUMPOPHOBIA: {
        Languages.ENGLISH: "Nwumpophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.N☽MWUPHOBIA: {
        Languages.ENGLISH: "N☽Mwuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.OBJECTSHOWPHOBIA: {
        Languages.ENGLISH: "Objectshowphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.OCTAGONPHOBIA: {
        Languages.ENGLISH: "Octagonphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.OIKOPHOBIA: {
        Languages.ENGLISH: "Oikophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.OMNIPHOBIA: {
        Languages.ENGLISH: "Omniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ONEHUNDREDBOTTLESOFBEERPHOBIA: {
        Languages.ENGLISH: "Onehundredbottlesofbeerphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.OPINATOPHOBIA: {
        Languages.ENGLISH: "Opinatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.OPIOPHOBIA: {
        Languages.ENGLISH: "Opiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ORATOPAROPHOBIA: {
        Languages.ENGLISH: "Oratoparophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ORDCLAVIPHOBIA: {
        Languages.ENGLISH: "Ordclaviphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ORTHOPHOBIA: {
        Languages.ENGLISH: "Orthophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.OSMOPHOBIA: {
        Languages.ENGLISH: "Osmophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.OSOURIPHOBIA: {
        Languages.ENGLISH: "Osouriphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.OTASPIDAPHOBIA: {
        Languages.ENGLISH: "Otaspidaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.OULINOPHOBIA: {
        Languages.ENGLISH: "Oulinophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.OURITIRIOPHOBIA: {
        Languages.ENGLISH: "Ouritiriophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.OVALPHOBIA: {
        Languages.ENGLISH: "Ovalphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PACTORBOPHOBIA: {
        Languages.ENGLISH: "Pactorbophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PAGOPHOBIA: {
        Languages.ENGLISH: "Pagophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PAMPHOBIA: {
        Languages.ENGLISH: "Pamphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PANOPHOBIA: {
        Languages.ENGLISH: "Panophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PANPHOBIA: {
        Languages.ENGLISH: "Panphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PANTELONIPHOBIA: {
        Languages.ENGLISH: "Panteloniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PANTOPHOBIA: {
        Languages.ENGLISH: "Pantophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PAPOUTSIPHOBIA: {
        Languages.ENGLISH: "Papoutsiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PAPYROPHOBIA: {
        Languages.ENGLISH: "Papyrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PAYPHONOPHOBIA: {
        Languages.ENGLISH: "Payphonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PATROIOPHOBIA: {
        Languages.ENGLISH: "Patroiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PECCATOPHOBIA: {
        Languages.ENGLISH: "Peccatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PECTUSSPEMOPHOBIA: {
        Languages.ENGLISH: "Pectusspemophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PEDIOPHOBIA: {
        Languages.ENGLISH: "Pediophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PENCILLOPHOBIA: {
        Languages.ENGLISH: "Pencillophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PENNYPHOBIA: {
        Languages.ENGLISH: "Pennyphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PERSTILBOSPHERPHOBIA: {
        Languages.ENGLISH: "Perstilbospherphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PEZODROMIOPHOBIA: {
        Languages.ENGLISH: "Pezodromiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PHILOSOPHOBIA: {
        Languages.ENGLISH: "Philosophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PHONOPHOBIA: {
        Languages.ENGLISH: "Phonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PHOTOAUGLIAPHOBIA: {
        Languages.ENGLISH: "Photoaugliaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PHOTOGRAPHOPHOBIA: {
        Languages.ENGLISH: "Photographophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PHOTOPHOBIA: {
        Languages.ENGLISH: "Photophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PIATOPHOBIA: {
        Languages.ENGLISH: "Piatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PICTOPHOBIA: {
        Languages.ENGLISH: "Pictophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PINGBOPHOBIA: {
        Languages.ENGLISH: "Pingbophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PINGPONGPHOBIA: {
        Languages.ENGLISH: "Pingpongphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PISTOTIKIKARTAPHOBIA: {
        Languages.ENGLISH: "Pistotikikartaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PITHANOPHOBIA: {
        Languages.ENGLISH: "Pithanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PLACOPHOBIA: {
        Languages.ENGLISH: "Placophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PLAKIDIOPHOBIA: {
        Languages.ENGLISH: "Plakidiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PLANOPHOBIA: {
        Languages.ENGLISH: "Planophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PLASTOPHOBIA: {
        Languages.ENGLISH: "Plastophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PLYNTIPHOBIA: {
        Languages.ENGLISH: "Plyntiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.POLYPHOBIA: {
        Languages.ENGLISH: "Polyphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.POOLPHOBIA: {
        Languages.ENGLISH: "Poolphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PORTBANKAZPHOBIA: {
        Languages.ENGLISH: "Portbankazphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.POSTALPHOBIA: {
        Languages.ENGLISH: "Postalphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.POTAMOPHOBIA: {
        Languages.ENGLISH: "Potamophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.POUKAMISOPHOBIA: {
        Languages.ENGLISH: "Poukamisophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PRAGMATICOPHOBIA: {
        Languages.ENGLISH: "Pragmaticophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PRAXIPHOBIA: {
        Languages.ENGLISH: "Praxiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PRINTERPHOBIA: {
        Languages.ENGLISH: "Printerphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PROPHETOPHOBIA: {
        Languages.ENGLISH: "Prophetophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PROSOPHOBIA: {
        Languages.ENGLISH: "Prosophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.P🎈GRONPHOBIA: {
        Languages.ENGLISH: "P🎈Gronphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PSALIDIPHOBIA: {
        Languages.ENGLISH: "Psalidiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PSICHAPHOBIA: {
        Languages.ENGLISH: "Psichaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PSYCHOPHOBIA: {
        Languages.ENGLISH: "Psychophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PSYGEPHOBIA: {
        Languages.ENGLISH: "Psygephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PUMPPUPHOBIA: {
        Languages.ENGLISH: "Pumppuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PUPAPHOBIA: {
        Languages.ENGLISH: "Pupaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PURINSUMPHOBIA: {
        Languages.ENGLISH: "Purinsumphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PURGAMENTOPHOBIA: {
        Languages.ENGLISH: "Purgamentophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PYLIPHOBIA: {
        Languages.ENGLISH: "Pyliphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PYROPHOBIA: {
        Languages.ENGLISH: "Pyrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PYROTECHNOPHOBIA: {
        Languages.ENGLISH: "Pyrotechnophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.PYRSOPHOBIA: {
        Languages.ENGLISH: "Pyrsophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.P🐟XMOPHOBIA: {
        Languages.ENGLISH: "P🐟Xmophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.P3NSOPHOBIA: {
        Languages.ENGLISH: "P3Nsophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.QAGAZUSAQPHOBIA: {
        Languages.ENGLISH: "Qagazusaqphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.QIEDJINGPHOBIA: {
        Languages.ENGLISH: "Qiedjingphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.QUARTERPHOBIA: {
        Languages.ENGLISH: "Quarterphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.RADIOPHOBIA: {
        Languages.ENGLISH: "Radiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.RASEMAPHOBIA: {
        Languages.ENGLISH: "Rasemaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.RAVDIPHOBIA: {
        Languages.ENGLISH: "Ravdiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.R🚦CREBPHOBIA: {
        Languages.ENGLISH: "R🚦Crebphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.RECEIPTPHOBIA: {
        Languages.ENGLISH: "Receiptphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.RECREATIONPHOBIA: {
        Languages.ENGLISH: "Recreationphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.RELAXATIONPHOBIA: {
        Languages.ENGLISH: "Relaxationphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.REMINDERPHOBIA: {
        Languages.ENGLISH: "Reminderphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.REMMIÐOPHOBIA: {
        Languages.ENGLISH: "Remmiðophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.RENWUPHOBIA: {
        Languages.ENGLISH: "Renwuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.REQIQIUPHOBIA: {
        Languages.ENGLISH: "Reqiqiuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.RESHUIQIPHOBIA: {
        Languages.ENGLISH: "Reshuiqiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.RETAINERPHOBIA: {
        Languages.ENGLISH: "Retainerphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.REVMAGRAMMIPHOBIA: {
        Languages.ENGLISH: "Revmagrammiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.RINGOPHOBIA: {
        Languages.ENGLISH: "Ringophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.RLERROPHOBIA: {
        Languages.ENGLISH: "Rlerrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ROBOPHOBIA: {
        Languages.ENGLISH: "Robophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ROLLERSKATEPHOBIA: {
        Languages.ENGLISH: "Rollerskatephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ROLLATOPHOBIA: {
        Languages.ENGLISH: "Rollatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ROLOIPHOBIA: {
        Languages.ENGLISH: "Roloiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.R🚗ZNONPHOBIA: {
        Languages.ENGLISH: "R🚗Znonphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.RWECONPHOBIA: {
        Languages.ENGLISH: "Rweconphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SAKIDIOPHOBIA: {
        Languages.ENGLISH: "Sakidiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SAKOULAPHOBIA: {
        Languages.ENGLISH: "Sakoulaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SANTAKIPHOBIA: {
        Languages.ENGLISH: "Santakiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SAXOPHONOPHOBIA: {
        Languages.ENGLISH: "Saxophonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SCATOPHOBIA: {
        Languages.ENGLISH: "Scatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SCHARAPHOBIA: {
        Languages.ENGLISH: "Scharaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SCIOPHOBIA: {
        Languages.ENGLISH: "Sciophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SCOTOMAPHOBIA: {
        Languages.ENGLISH: "Scotomaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SCRINIAPHOBIA: {
        Languages.ENGLISH: "Scriniaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SEIRINAPHOBIA: {
        Languages.ENGLISH: "Seirinaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SEPLOPHOBIA: {
        Languages.ENGLISH: "Seplophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SENOƩUPHOBIA: {
        Languages.ENGLISH: "Senoʃuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SFAIRAPHOBIA: {
        Languages.ENGLISH: "Sfairaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SFOUNGARISTRAPHOBIA: {
        Languages.ENGLISH: "Sfoungaristraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SFYRIPHOBIA: {
        Languages.ENGLISH: "Sfyriphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SHUICAOPHOBIA: {
        Languages.ENGLISH: "Shuicaophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SH5DOPHOBIA: {
        Languages.ENGLISH: "Sh5Dophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SIMAPHOBIA: {
        Languages.ENGLISH: "Simaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SINISTROPHOBIA: {
        Languages.ENGLISH: "Sinistrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SIXFLAGSPHOBIA: {
        Languages.ENGLISH: "Sixflagsphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SHIJIPHOBIA: {
        Languages.ENGLISH: "Shijiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SHOEBOXPHOBIA: {
        Languages.ENGLISH: "Shoeboxphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SHWNPHOBIA: {
        Languages.ENGLISH: "Shwnphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SH☀GMOPHOBIA: {
        Languages.ENGLISH: "Sh☀Gmophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SKATEBOARDPHOBIA: {
        Languages.ENGLISH: "Skateboardphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SKOUPAPHOBIA: {
        Languages.ENGLISH: "Skoupaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SNEROLAKOPHOBIA: {
        Languages.ENGLISH: "Snerolakophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SOLOIPHOBIA: {
        Languages.ENGLISH: "Soloiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SOTERIOPHOBIA: {
        Languages.ENGLISH: "Soteriophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SPACESUITPHOBIA: {
        Languages.ENGLISH: "Spacesuitphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SPASMENAGALIAPHOBIA: {
        Languages.ENGLISH: "Spasmenagaliaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SPEEDOMOPHOBIA: {
        Languages.ENGLISH: "Speedomophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SPHYGMOMANOPHOBIA: {
        Languages.ENGLISH: "Sphygmomanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SPIRTOPHOBIA: {
        Languages.ENGLISH: "Spirtophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SPRINKLERPHOBIA: {
        Languages.ENGLISH: "Sprinklerphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SRANDUOPHOBIA: {
        Languages.ENGLISH: "Sranduophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.STAUROPHOBIA: {
        Languages.ENGLISH: "Staurophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.STAVRODROMIPHOBIA: {
        Languages.ENGLISH: "Stavrodromiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.STENOPHOBIA: {
        Languages.ENGLISH: "Stenophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.STETHOSCOPEPHOBIA: {
        Languages.ENGLISH: "Stethoscopephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.STICKERPHOBIA: {
        Languages.ENGLISH: "Stickerphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.STOCKINGPHOBIA: {
        Languages.ENGLISH: "Stockingphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.STOPSIGNPHOBIA: {
        Languages.ENGLISH: "Stopsignphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.STRANCAPHOBIA: {
        Languages.ENGLISH: "Strancaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.STRANTOPHOBIA: {
        Languages.ENGLISH: "Strantophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.STREETLIGHTPHOBIA: {
        Languages.ENGLISH: "Streetlightphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.STROVOPHOBIA: {
        Languages.ENGLISH: "Strovophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.STYLOPHOBIA: {
        Languages.ENGLISH: "Stylophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ST📹PROPHOBIA: {
        Languages.ENGLISH: "St📹Prophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SUBMECHANOPHOBIA: {
        Languages.ENGLISH: "Submechanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SURFBOARDPHOBIA: {
        Languages.ENGLISH: "Surfboardphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SYMBOLOPHOBIA: {
        Languages.ENGLISH: "Symbolophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SYNDETIRAPHOBIA: {
        Languages.ENGLISH: "Syndetiraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SYNTRIVANIPHOBIA: {
        Languages.ENGLISH: "Syntrivaniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.SYSKEVIPHOBIA: {
        Languages.ENGLISH: "Syskeviphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.S🐦GMOPHOBIA: {
        Languages.ENGLISH: "S🐦Gmophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TABULATOPHOBIA: {
        Languages.ENGLISH: "Tabulatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TAILLIGHTPHOBIA: {
        Languages.ENGLISH: "Taillightphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.FDS_HFKDSHFKJHSDKJFHSDKJFHDSKJFHSKJFHSDKJPHOBIA: {
        Languages.ENGLISH: "Fds Hfkdshfkjhsdkjfhsdkjfhdskjfhskjfhsdkjphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TAIÞUPHOBIA: {
        Languages.ENGLISH: "Taiþuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TAMEIOPHOBIA: {
        Languages.ENGLISH: "Tameiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TAPETSARIAPHOBIA: {
        Languages.ENGLISH: "Tapetsariaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TAPHOSPHOBIA: {
        Languages.ENGLISH: "Taphosphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TECHNOPHOBIA: {
        Languages.ENGLISH: "Technophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TECTOPHOBIA: {
        Languages.ENGLISH: "Tectophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TEGOPHOBIA: {
        Languages.ENGLISH: "Tegophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TELEOPHOBIA: {
        Languages.ENGLISH: "Teleophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TELEPHONOPHOBIA: {
        Languages.ENGLISH: "Telephonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TELESCOPOPHOBIA: {
        Languages.ENGLISH: "Telescopophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TERRAMOPHOBIA: {
        Languages.ENGLISH: "Terramophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TERRORPHOBIA: {
        Languages.ENGLISH: "Terrorphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TEXTOPHOBIA: {
        Languages.ENGLISH: "Textophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.THAUMATOPHOBIA: {
        Languages.ENGLISH: "Thaumatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.THEOLOGICOPHOBIA: {
        Languages.ENGLISH: "Theologicophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.THEOPHOBIA: {
        Languages.ENGLISH: "Theophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.THERMOMOPHOBIA: {
        Languages.ENGLISH: "Thermomophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.THERMOSTATPHOBIA: {
        Languages.ENGLISH: "Thermostatphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.THESAUROPHOBIA: {
        Languages.ENGLISH: "Thesaurophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TIGANIPHOBIA: {
        Languages.ENGLISH: "Tiganiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TILECHEIRISTIRIOPHOBIA: {
        Languages.ENGLISH: "Tilecheiristiriophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TINGCHECHANGPHOBIA: {
        Languages.ENGLISH: "Tingchechangphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TINGCHECHEKUPHOBIA: {
        Languages.ENGLISH: "Tingchechekuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TLINGHUPHOBIA: {
        Languages.ENGLISH: "Tlinghuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TOASTERPHOBIA: {
        Languages.ENGLISH: "Toasterphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TOICHOPHOBIA: {
        Languages.ENGLISH: "Toichophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TOPOPHOBIA: {
        Languages.ENGLISH: "Topophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TOUALETAPHOBIA: {
        Languages.ENGLISH: "Toualetaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TOUVLOPHOBIA: {
        Languages.ENGLISH: "Touvlophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TRAGOUDIPHOBIA: {
        Languages.ENGLISH: "Tragoudiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TRAPEZAPHOBIA: {
        Languages.ENGLISH: "Trapezaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TROKHOPHOBIA: {
        Languages.ENGLISH: "Trokhophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TROMPETAPHOBIA: {
        Languages.ENGLISH: "Trompetaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TROPHOPHOBIA: {
        Languages.ENGLISH: "Trophophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TRƐDNOPHOBIA: {
        Languages.ENGLISH: "Trɛdnophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TRYPANOPHOBIA: {
        Languages.ENGLISH: "Trypanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TRYPOPHOBIA: {
        Languages.ENGLISH: "Trypophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TR✈️GMOPHOBIA: {
        Languages.ENGLISH: "Tr✈️Gmophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TURRIPHOBIA: {
        Languages.ENGLISH: "Turriphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TYCHOPHOBIA: {
        Languages.ENGLISH: "Tychophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TYMPANOPHOBIA: {
        Languages.ENGLISH: "Tympanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.TƜDROPHOBIA: {
        Languages.ENGLISH: "Tɯdrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.UMBRAPHOBIA: {
        Languages.ENGLISH: "Umbraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.UMBRELLAPHOBIA: {
        Languages.ENGLISH: "Umbrellaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VAGONIPHOBIA: {
        Languages.ENGLISH: "Vagoniphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VALANTIOPHOBIA: {
        Languages.ENGLISH: "Valantiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VALITSAPHOBIA: {
        Languages.ENGLISH: "Valitsaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VERKEINTRIPHOBIA: {
        Languages.ENGLISH: "Verkeintriphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VESTIPHOBIA: {
        Languages.ENGLISH: "Vestiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VIEMAPHOBIA: {
        Languages.ENGLISH: "Viemaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VIDEOCASSETTOPHOBIA: {
        Languages.ENGLISH: "Videocassettophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VINITOPHOBIA: {
        Languages.ENGLISH: "Vinitophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VIOLIPHOBIA: {
        Languages.ENGLISH: "Violiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VOEDSEPHOBIA: {
        Languages.ENGLISH: "Voedsephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VOIDOPHOBIA: {
        Languages.ENGLISH: "Voidophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VOLANPHOBIA: {
        Languages.ENGLISH: "Volanphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VORRAPHOBIA: {
        Languages.ENGLISH: "Vorraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VOTHROPHOBIA: {
        Languages.ENGLISH: "Vothrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VOULISIPHOBIA: {
        Languages.ENGLISH: "Voulisiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.VINYLOPHOBIA: {
        Languages.ENGLISH: "Vinylophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.V🚫SHROPHOBIA: {
        Languages.ENGLISH: "V🚫Shrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.WANJUWUPHOBIA: {
        Languages.ENGLISH: "Wanjuwuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.WHEELCHAIRPHOBIA: {
        Languages.ENGLISH: "Wheelchairphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.WICCAPHOBIA: {
        Languages.ENGLISH: "Wiccaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.WLANOPHOBIA: {
        Languages.ENGLISH: "Wlanophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.XAFNIASMAPHOBIA: {
        Languages.ENGLISH: "Xafniasmaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.X!MZOPHOBIA: {
        Languages.ENGLISH: "X!Mzophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.XINXIANGPHOBIA: {
        Languages.ENGLISH: "Xinxiangphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.XYLOPHONOPHOBIA: {
        Languages.ENGLISH: "Xylophonophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.XYPNITIRIPHOBIA: {
        Languages.ENGLISH: "Xypnitiriphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.XYROPHOBIA: {
        Languages.ENGLISH: "Xyrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.W@NOPHOBIA: {
        Languages.ENGLISH: "W@Nophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.YEDANSHUPHOBIA: {
        Languages.ENGLISH: "Yedanshuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.YEDENGPHOBIA: {
        Languages.ENGLISH: "Yedengphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.YGROPHOBIA: {
        Languages.ENGLISH: "Ygrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.YINJIPHOBIA: {
        Languages.ENGLISH: "Yinjiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.YINSHUIJIPHOBIA: {
        Languages.ENGLISH: "Yinshuijiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.YLOPHOBIA: {
        Languages.ENGLISH: "Ylophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.YROUXPHOBIA: {
        Languages.ENGLISH: "Yrouxphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.YPNODOMATIOPHOBIA: {
        Languages.ENGLISH: "Ypnodomatiophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.YUPENPHOBIA: {
        Languages.ENGLISH: "Yupenphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.YUSHIXISHOPHOBIA: {
        Languages.ENGLISH: "Yushixishophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.YUSHUAPHOBIA: {
        Languages.ENGLISH: "Yushuaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.YWAOHUPHOBIA: {
        Languages.ENGLISH: "Ywaohuphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.Y∞GOMPHOBIA: {
        Languages.ENGLISH: "Y∞Gomphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ZAPSAULPHOBIA: {
        Languages.ENGLISH: "Zapsaulphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ZARIPHOBIA: {
        Languages.ENGLISH: "Zariphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ZHAOQINPHOBIA: {
        Languages.ENGLISH: "Zhaoqinphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ZHINCHAPHOBIA: {
        Languages.ENGLISH: "Zhinchaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ZHUOJPHOBIA: {
        Languages.ENGLISH: "Zhuojphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ZIDONGSHOPHOBIA: {
        Languages.ENGLISH: "Zidongshophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ZIZANMEPHOBIA: {
        Languages.ENGLISH: "Zizanmephobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ZLOQINGPHOBIA: {
        Languages.ENGLISH: "Zloqingphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.Z📷MROTPHOBIA: {
        Languages.ENGLISH: "Z📷Mrotphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ZONIASFALEIAPHOBIA: {
        Languages.ENGLISH: "Zoniasfaleiaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ZRAIDOPHOBIA: {
        Languages.ENGLISH: "Zraidophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ZUIGERPHOBIA: {
        Languages.ENGLISH: "Zuigerphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ZWUQIPHOBIA: {
        Languages.ENGLISH: "Zwuqiphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobias.ZYGARIAPHOBIA: {
        Languages.ENGLISH: "Zygariaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}


class ThingsPhobiasDescriptions(Enum):
    """
    Things Phobias Descriptions
    """
    ADIAFANOPHOBIA = auto()
    ADVERTISEMENTPHOBIA = auto()
    AEROSAKAPHOBIA = auto()
    AICHMOPHOBIA = auto()
    AIRCOPHOBIA = auto()
    AIRPODAPHOBIA = auto()
    ALARMOPHOBIA = auto()
    ALLODOXAPHOBIA = auto()
    ALTOCELAROPHOBIA = auto()
    ANEMISTIRAPHOBIA = auto()
    ANIMAPHOBIA = auto()
    ANTANAKLOPHOBIA = auto()
    ANTENNAPHOBIA = auto()
    APEIROPHOBIA = auto()
    APOSTASIPHOBIA = auto()
    APPLETVAPHOBIA = auto()
    AQUAMECHANOPHOBIA = auto()
    ARACHTOPHOBIA = auto()
    ARCHEIOTHIKIPHOBIA = auto()
    ARMAROPHOBIA = auto()
    ARPAPHOBIA = auto()
    ARTEMOPHOBIA = auto()
    AULOPHOBIA = auto()
    AUTOKERAPHOBIA = auto()
    AUTOPLENOPHOBIA = auto()
    AUTOMATONOPHOBIA = auto()
    BACOPHOBIA = auto()
    BAHNUBOPHOBIA = auto()
    BALLISTOPHOBIA = auto()
    BALTEUSPHOBIA = auto()
    BALTICOPHOBIA = auto()
    BANDZOPHOBIA = auto()
    BANMAXIANPHOBIA = auto()
    BAROPHOBIA = auto()
    BASSOLOPHOBIA = auto()
    BATHMOPHOBIA = auto()
    BATHROBEPHOBIA = auto()
    BATTEROPHOBIA = auto()
    BEEPOPHOBIA = auto()
    BELONEPHOBIA = auto()
    BIBLIOPHOBIA = auto()
    BILLBOARDPHOBIA = auto()
    BIJIXPHOBIA = auto()
    BINOCULOPHOBIA = auto()
    BLEIMPNOPHOBIA = auto()
    BLEMENSAPHOBIA = auto()
    BLENDERPHOBIA = auto()
    BLOWERPEELPHOBIA = auto()
    BRACESPHOBIA = auto()
    BRUGNOPHOBIA = auto()
    BODENSTANDOPHOBIA = auto()
    BONOCKOPHOBIA = auto()
    BOOGIEBOARDPHOBIA = auto()
    BOWERPHOBIA = auto()
    BOWPHOBIA = auto()
    BRIEFSHIEPHOBIA = auto()
    BUHUAJIPHOBIA = auto()
    BUZZOPHOBIA = auto()
    BWAOPIPHOBIA = auto()
    BWAUKPHOBIA = auto()
    CABLEPHOBIA = auto()
    CAELOPHOBIA = auto()
    CALCULAPHOBIA = auto()
    CAMCORDERPHOBIA = auto()
    CAMERAPHOBIA = auto()
    CAPILLUSSETISPHOBIA = auto()
    CASSETTOPHOBIA = auto()
    CATASTOLEPHOBIA = auto()
    CATHEDRAPHOBIA = auto()
    CATOPTROPHOBIA = auto()
    CELAROPHOBIA = auto()
    CENOSILICAPHOBIA = auto()
    CHARAKAPHOBIA = auto()
    CHARTIPHOBIA = auto()
    CHEDOANGPHOBIA = auto()
    CHEKUXISHOPHOBIA = auto()
    CHIONOFYSOPHOBIA = auto()
    CHLOEPHOBIA = auto()
    CHREOSTIKIKARTAPHOBIA = auto()
    CHROMETOPHOBIA = auto()
    CHRONOMENTROPHOBIA = auto()
    CHUFXISHOPHOBIA = auto()
    CISTULAPHOBIA = auto()
    CITHARAPHOBIA = auto()
    CLAPPERPHOBIA = auto()
    CLEITHROPHOBIA = auto()
    CLINEPHOBIA = auto()
    CLOACAPHOBIA = auto()
    COGOMBOPHOBIA = auto()
    COLIMBOPHOBIA = auto()
    COMMERCIALPHOBIA = auto()
    COMPASSPHOBIA = auto()
    CONFETTIPHOBIA = auto()
    CONSECOTALEOPHOBIA = auto()
    CONTROSOFFITTOPHOBIA = auto()
    COZAMPIOPHOBIA = auto()
    CRANOPHOBIA = auto()
    CREMNOPHOBIA = auto()
    CRUSRUMBLOPHOBIA = auto()
    CUPROLAMINOPHOBIA = auto()
    CYBERPHOBIA = auto()
    CYMOPHOBIA = auto()
    DACHOINGPHOBIA = auto()
    DARTBOARDPHOBIA = auto()
    DARTOPHOBIA = auto()
    DEFENESTRAPHOBIA = auto()
    DEKANIKIPHOBIA = auto()
    DELEOPHOBIA = auto()
    DENGPAOPHOBIA = auto()
    DENTODRAPANOPHOBIA = auto()
    DENTUREPHOBIA = auto()
    DEXTROPHOBIA = auto()
    DIAFANOPHOBIA = auto()
    DIANZIFANKUIPHOBIA = auto()
    DIAPERPHOBIA = auto()
    DIAPHIMISTICOPHOBIA = auto()
    DIASTIMAPHOBIA = auto()
    DIATHLASOPHOBIA = auto()
    DICLEBGOPHOBIA = auto()
    DIETHNESYSTIMAMONADONOPHOBIA = auto()
    DIKEPHOBIA = auto()
    DIMEPHOBIA = auto()
    DINGOPHOBIA = auto()
    DINOPHOBIA = auto()
    DISHLEPROPHOBIA = auto()
    DIZOANGPHOBIA = auto()
    DLITOPHOBIA = auto()
    DOMINEATHERPHOBIA = auto()
    DOORBELLPHOBIA = auto()
    DORAPHOBIA = auto()
    DORNGOPHOBIA = auto()
    DORYFORIKOCHARTIPHOBIA = auto()
    DOTTOPHOBIA = auto()
    DRAPANOPHOBIA = auto()
    DRIKRONPHOBIA = auto()
    DROGERPHOBIA = auto()
    DROMUSEPHOBIA = auto()
    DULUNCHEPHOBIA = auto()
    DUMASAPHOBIA = auto()
    DUMPSTERPHOBIA = auto()
    DUOPHOBIA = auto()
    DVDPHOBIA = auto()
    EAPALLIOPHOBIA = auto()
    EARMUFFPHOBIA = auto()
    EBULLIOPHOBIA = auto()
    OIKOPHOBIA = auto()
    EIFFELTURRIPHOBIA = auto()
    EISOPTROPHOBIA = auto()
    ELECTROPHOBIA = auto()
    ELEVATOPHOBIA = auto()
    ELEVAPHOBIA = auto()
    EMAILPHOBIA = auto()
    ENERGYPHOBIA = auto()
    ENISSOPHOBIA = auto()
    ENTAMAPHOBIA = auto()
    ENYDREIOPHOBIA = auto()
    EPIPLAPHOBIA = auto()
    EPISTOLAPHOBIA = auto()
    EPISTEMOPHOBIA = auto()
    ERGALEIOPHOBIA = auto()
    ERYTHOPHOBIA = auto()
    EREUTHOPHOBIA = auto()
    ESCALAPHOBIA = auto()
    ROLTRAPHOBIA = auto()
    ESCALATOPHOBIA = auto()
    ESOROUCHAPHOBIA = auto()
    ETHISMOSOPHOBIA = auto()
    EUPHOBIA = auto()
    EUPISTOPHOBIA = auto()
    EVODIAPHOBIA = auto()
    FADCHOONGPHOBIA = auto()
    FASCIOLISPHOBIA = auto()
    FAKELOPHOBIA = auto()
    FAKOSPHOBIA = auto()
    FANARIPHOBIA = auto()
    FARASIPHOBIA = auto()
    FENBANPHOBIA = auto()
    FERETROPHOBIA = auto()
    FERROPHOBIA = auto()
    FICTOPHOBIA = auto()
    FILICOPHOBIA = auto()
    FILOPHOBIA = auto()
    FIREHYDRANTPHOBIA = auto()
    FLASCIPHOBIA = auto()
    FLITZANIPHOBIA = auto()
    FLITZANISAGIOUPHOBIA = auto()
    FOCOPHOBIA = auto()
    FOONIPHOBIA = auto()
    FOREMAPHOBIA = auto()
    FORMIDOPHOBIA = auto()
    FORNACIPHOBIA = auto()
    FORUMPHOBIA = auto()
    FOSSILPHOBIA = auto()
    FOURNOPHOBIA = auto()
    FOUSTAPHOBIA = auto()
    FRACHTIPHOBIA = auto()
    FRAGMAPHOBIA = auto()
    FREARPHOBIA = auto()
    FRENOPHOBIA = auto()
    FR%PLOPHOBIA = auto()
    FUMIPHOBIA = auto()
    FURNGZUPHOBIA = auto()
    FWAUTPHOBIA = auto()
    FWONGIPHOBIA = auto()
    FYLLOFYSOPHOBIA = auto()
    GAKKIPHOBIA = auto()
    GASGAUGEPHOBIA = auto()
    GASPEDALPHOBIA = auto()
    GELIOPHOBIA = auto()
    GERAPHOBIA = auto()
    GEUMAPHOBIA = auto()
    GATNOBPHOBIA = auto()
    GLEYMOPHOBIA = auto()
    GLOBOPHOBIA = auto()
    GL÷NDOPHOBIA = auto()
    GOOGLEPHOBIA = auto()
    GOUWUCHEPHOBIA = auto()
    GRAFEIOPHOBIA = auto()
    GRAFFITIPHOBIA = auto()
    GRAMMATOSIMOPHOBIA = auto()
    GRANDSLAMWICHPHOBIA = auto()
    GR?SOPHOBIA = auto()
    GYALIAILIOUPHOBIA = auto()
    G4GOPHOBIA = auto()
    HAGIOPHOBIA = auto()
    HANDCUFFPHOBIA = auto()
    HEADLIGHTPHOBIA = auto()
    HEADPHONOPHOBIA = auto()
    HEARINGAIDPHOBIA = auto()
    HEDGETROPHOBIA = auto()
    HEIZGEPHOBIA = auto()
    HERESYPHOBIA = auto()
    HEREIOPHOBIA = auto()
    HERPETOPHOBIA = auto()
    HIBERNICAPHOBIA = auto()
    HIEROPHOBIA = auto()
    HLEGUPHOBIA = auto()
    HMOSHGOPHOBIA = auto()
    HNIRSHUNPHOBIA = auto()
    HOCKEYPHOBIA = auto()
    HOPLOPHOBIA = auto()
    HOSEPHOBIA = auto()
    HRONGYOPHOBIA = auto()
    HUMORPHOBIA = auto()
    HYELOPHOBIA = auto()
    HYGROPHOBIA = auto()
    HYLEPHOBIA = auto()
    HYPENGYOPHOBIA = auto()
    H8POPHOBIA = auto()
    ICONOPHOBIA = auto()
    IDEOPHOBIA = auto()
    IMEROLOGIOPHOBIA = auto()
    INTERCOMPHOBIA = auto()
    INTERNETPHOBIA = auto()
    JIJINGPHOBIA = auto()
    JUKEBOXOPHOBIA = auto()
    JULELOPHOBIA = auto()
    J9DOBPHOBIA = auto()
    KAFETIPHOBIA = auto()
    KALATHIPHOBIA = auto()
    KALTSAPHOBIA = auto()
    KAMARAKIPHOBIA = auto()
    KAMPANAPHOBIA = auto()
    KANAYAPHOBIA = auto()
    KAPELAPHOBIA = auto()
    KARAZPHOBIA = auto()
    KARAZPORTANOICHTIRIPHOBIA = auto()
    KARAZPORTAPHOBIA = auto()
    KARFIPHOBIA = auto()
    KAROTSAKIPHOBIA = auto()
    KASSAPHOBIA = auto()
    KASONIPHOBIA = auto()
    KATAGELOPHOBIA = auto()
    KATSAVIDIPHOBIA = auto()
    KATARRAKTIPHOBIA = auto()
    KEFIPHOBIA = auto()
    KENOPHOBIA = auto()
    KERAPHOBIA = auto()
    KERASOPHOBIA = auto()
    KERIPHOBIA = auto()
    KIFNAPHOBIA = auto()
    KILNPHOBIA = auto()
    KINZODOPHOBIA = auto()
    KIROMPIGIAPHOBIA = auto()
    KLEIDARIAPHOBIA = auto()
    KLEIDIPHOBIA = auto()
    KLƐBZEENPHOBIA = auto()
    KOINONIPHOBIA = auto()
    KOLONIAPHOBIA = auto()
    KONSENTOPHOBIA = auto()
    KOSMEMOPHOBIA = auto()
    KOUMPIPHOBIA = auto()
    KOUNIAPHOBIA = auto()
    KOUVAPHOBIA = auto()
    KOUZIPHOBIA = auto()
    KREMASTRAPHOBIA = auto()
    KYPELLOPHOBIA = auto()
    K2NQIPHOBIA = auto()
    LADDERPHOBIA = auto()
    LAGOUMIPHOBIA = auto()
    LAMPAPHOBIA = auto()
    LASTICHOPHOBIA = auto()
    LATERIPHOBIA = auto()
    LECHOPHOBIA = auto()
    LENTOPHOBIA = auto()
    LEVOPHOBIA = auto()
    LIGAMENTOPHOBIA = auto()
    LIGHTERPHOBIA = auto()
    LIGYROPHOBIA = auto()
    LIMNIPHOBIA = auto()
    LINONOPHOBIA = auto()
    LINYUPHOBIA = auto()
    LOCKERPHOBIA = auto()
    LODICULAPHOBIA = auto()
    LOGICOMECHANIBIOPHOBIA = auto()
    LOGOCRISIAPHOBIA = auto()
    LOUTROPHOBIA = auto()
    LRASHAPHOBIA = auto()
    LUMENOPHOBIA = auto()
    LUODOPHOBIA = auto()
    LYSBRYTOPHOBIA = auto()
    MAGEIREIOPHOBIA = auto()
    MAIKBANPHOBIA = auto()
    MONOXEIDIOANTHRAKAPHOBIA = auto()
    MAGEIACHALIPHOBIA = auto()
    MAGIKORAVDIPHOBIA = auto()
    MAGNITOFONOPHOBIA = auto()
    MANHOLEPHOBIA = auto()
    MANUSSICCUSPHOBIA = auto()
    MAPPOPHOBIA = auto()
    MARKADOROPHOBIA = auto()
    MATTERPHOBIA = auto()
    MECHANOPHOBIA = auto()
    MEDIAPHOBIA = auto()
    MEGALOPHOBIA = auto()
    MEGAPHONOPHOBIA = auto()
    MELOPHOBIA = auto()
    MEMEPHOBIA = auto()
    MEMEOPHOBIA = auto()
    MENOPHOBIA = auto()
    METAZODEPHOBIA = auto()
    MICROPHONOPHOBIA = auto()
    MINICELAROPHOBIA = auto()
    MYSOPHOBIA = auto()
    METROPHOBIA = auto()
    MICROPHOBIA = auto()
    MYCROPHOBIA = auto()
    MICROSCOPOPHOBIA = auto()
    MICROVOPHOBIA = auto()
    MLAFENPHOBIA = auto()
    MNEMOPHOBIA = auto()
    MRNPHOBIA = auto()
    MOLYVIPHOBIA = auto()
    MUNJINGPHOBIA = auto()
    MYKITAPHOBIA = auto()
    MYTHOPHOBIA = auto()
    NAITOSUTANDOPHOBIA = auto()
    NECROPHOBIA = auto()
    NEOPHOBIA = auto()
    NICKELPHOBIA = auto()
    NIJOONGPHOBIA = auto()
    NLAIGUPHOBIA = auto()
    NINTENDOPHOBIA = auto()
    NOJESCENTROPHOBIA = auto()
    NOTOPHOBIA = auto()
    NRASOBPHOBIA = auto()
    NUCLEOMITUPHOBIA = auto()
    NWUMPOPHOBIA = auto()
    N☽MWUPHOBIA = auto()
    OBJECTSHOWPHOBIA = auto()
    OCTAGONPHOBIA = auto()
    OIKOPHOBIA = auto()
    OMNIPHOBIA = auto()
    ONEHUNDREDBOTTLESOFBEERPHOBIA = auto()
    OPINATOPHOBIA = auto()
    OPIOPHOBIA = auto()
    ORATOPAROPHOBIA = auto()
    ORDCLAVIPHOBIA = auto()
    ORTHOPHOBIA = auto()
    OSMOPHOBIA = auto()
    OSOURIPHOBIA = auto()
    OTASPIDAPHOBIA = auto()
    OULINOPHOBIA = auto()
    OURITIRIOPHOBIA = auto()
    OVALPHOBIA = auto()
    PACTORBOPHOBIA = auto()
    PAGOPHOBIA = auto()
    PAMPHOBIA = auto()
    PANOPHOBIA = auto()
    PANPHOBIA = auto()
    PANTELONIPHOBIA = auto()
    PANTOPHOBIA = auto()
    PAPOUTSIPHOBIA = auto()
    PAPYROPHOBIA = auto()
    PAYPHONOPHOBIA = auto()
    PATROIOPHOBIA = auto()
    PECCATOPHOBIA = auto()
    PECTUSSPEMOPHOBIA = auto()
    PEDIOPHOBIA = auto()
    PENCILLOPHOBIA = auto()
    PENNYPHOBIA = auto()
    PERSTILBOSPHERPHOBIA = auto()
    PEZODROMIOPHOBIA = auto()
    PHILOSOPHOBIA = auto()
    PHONOPHOBIA = auto()
    PHOTOAUGLIAPHOBIA = auto()
    PHOTOGRAPHOPHOBIA = auto()
    PHOTOPHOBIA = auto()
    PIATOPHOBIA = auto()
    PICTOPHOBIA = auto()
    PINGBOPHOBIA = auto()
    PINGPONGPHOBIA = auto()
    PISTOTIKIKARTAPHOBIA = auto()
    PITHANOPHOBIA = auto()
    PLACOPHOBIA = auto()
    PLAKIDIOPHOBIA = auto()
    PLANOPHOBIA = auto()
    PLASTOPHOBIA = auto()
    PLYNTIPHOBIA = auto()
    POLYPHOBIA = auto()
    POOLPHOBIA = auto()
    PORTBANKAZPHOBIA = auto()
    POSTALPHOBIA = auto()
    POTAMOPHOBIA = auto()
    POUKAMISOPHOBIA = auto()
    PRAGMATICOPHOBIA = auto()
    PRAXIPHOBIA = auto()
    PRINTERPHOBIA = auto()
    PROPHETOPHOBIA = auto()
    PROSOPHOBIA = auto()
    P🎈GRONPHOBIA = auto()
    PSALIDIPHOBIA = auto()
    PSICHAPHOBIA = auto()
    PSYCHOPHOBIA = auto()
    PSYGEPHOBIA = auto()
    PUMPPUPHOBIA = auto()
    PUPAPHOBIA = auto()
    PURINSUMPHOBIA = auto()
    PURGAMENTOPHOBIA = auto()
    PYLIPHOBIA = auto()
    PYROPHOBIA = auto()
    PYROTECHNOPHOBIA = auto()
    PYRSOPHOBIA = auto()
    P🐟XMOPHOBIA = auto()
    P3NSOPHOBIA = auto()
    QAGAZUSAQPHOBIA = auto()
    QIEDJINGPHOBIA = auto()
    QUARTERPHOBIA = auto()
    RADIOPHOBIA = auto()
    RASEMAPHOBIA = auto()
    RAVDIPHOBIA = auto()
    R🚦CREBPHOBIA = auto()
    RECEIPTPHOBIA = auto()
    RECREATIONPHOBIA = auto()
    RELAXATIONPHOBIA = auto()
    REMINDERPHOBIA = auto()
    REMMIÐOPHOBIA = auto()
    RENWUPHOBIA = auto()
    REQIQIUPHOBIA = auto()
    RESHUIQIPHOBIA = auto()
    RETAINERPHOBIA = auto()
    REVMAGRAMMIPHOBIA = auto()
    RINGOPHOBIA = auto()
    RLERROPHOBIA = auto()
    ROBOPHOBIA = auto()
    ROLLERSKATEPHOBIA = auto()
    ROLLATOPHOBIA = auto()
    ROLOIPHOBIA = auto()
    R🚗ZNONPHOBIA = auto()
    RWECONPHOBIA = auto()
    SAKIDIOPHOBIA = auto()
    SAKOULAPHOBIA = auto()
    SANTAKIPHOBIA = auto()
    SAXOPHONOPHOBIA = auto()
    SCATOPHOBIA = auto()
    SCHARAPHOBIA = auto()
    SCIOPHOBIA = auto()
    SCOTOMAPHOBIA = auto()
    SCRINIAPHOBIA = auto()
    SEIRINAPHOBIA = auto()
    SEPLOPHOBIA = auto()
    SENOƩUPHOBIA = auto()
    SFAIRAPHOBIA = auto()
    SFOUNGARISTRAPHOBIA = auto()
    SFYRIPHOBIA = auto()
    SHUICAOPHOBIA = auto()
    SH5DOPHOBIA = auto()
    SIMAPHOBIA = auto()
    SINISTROPHOBIA = auto()
    SIXFLAGSPHOBIA = auto()
    SHIJIPHOBIA = auto()
    SHOEBOXPHOBIA = auto()
    SHWNPHOBIA = auto()
    SH☀GMOPHOBIA = auto()
    SKATEBOARDPHOBIA = auto()
    SKOUPAPHOBIA = auto()
    SNEROLAKOPHOBIA = auto()
    SOLOIPHOBIA = auto()
    SOTERIOPHOBIA = auto()
    SPACESUITPHOBIA = auto()
    SPASMENAGALIAPHOBIA = auto()
    SPEEDOMOPHOBIA = auto()
    SPHYGMOMANOPHOBIA = auto()
    SPIRTOPHOBIA = auto()
    SPRINKLERPHOBIA = auto()
    SRANDUOPHOBIA = auto()
    STAUROPHOBIA = auto()
    STAVRODROMIPHOBIA = auto()
    STENOPHOBIA = auto()
    STETHOSCOPEPHOBIA = auto()
    STICKERPHOBIA = auto()
    STOCKINGPHOBIA = auto()
    STOPSIGNPHOBIA = auto()
    STRANCAPHOBIA = auto()
    STRANTOPHOBIA = auto()
    STREETLIGHTPHOBIA = auto()
    STROVOPHOBIA = auto()
    STYLOPHOBIA = auto()
    ST📹PROPHOBIA = auto()
    SUBMECHANOPHOBIA = auto()
    SURFBOARDPHOBIA = auto()
    SYMBOLOPHOBIA = auto()
    SYNDETIRAPHOBIA = auto()
    SYNTRIVANIPHOBIA = auto()
    SYSKEVIPHOBIA = auto()
    S🐦GMOPHOBIA = auto()
    TABULATOPHOBIA = auto()
    TAILLIGHTPHOBIA = auto()
    FDS_HFKDSHFKJHSDKJFHSDKJFHDSKJFHSKJFHSDKJPHOBIA = auto()
    TAIÞUPHOBIA = auto()
    TAMEIOPHOBIA = auto()
    TAPETSARIAPHOBIA = auto()
    TAPHOSPHOBIA = auto()
    TECHNOPHOBIA = auto()
    TECTOPHOBIA = auto()
    TEGOPHOBIA = auto()
    TELEOPHOBIA = auto()
    TELEPHONOPHOBIA = auto()
    TELESCOPOPHOBIA = auto()
    TERRAMOPHOBIA = auto()
    TERRORPHOBIA = auto()
    TEXTOPHOBIA = auto()
    THAUMATOPHOBIA = auto()
    THEOLOGICOPHOBIA = auto()
    THEOPHOBIA = auto()
    THERMOMOPHOBIA = auto()
    THERMOSTATPHOBIA = auto()
    THESAUROPHOBIA = auto()
    TIGANIPHOBIA = auto()
    TILECHEIRISTIRIOPHOBIA = auto()
    TINGCHECHANGPHOBIA = auto()
    TINGCHECHEKUPHOBIA = auto()
    TLINGHUPHOBIA = auto()
    TOASTERPHOBIA = auto()
    TOICHOPHOBIA = auto()
    TOPOPHOBIA = auto()
    TOUALETAPHOBIA = auto()
    TOUVLOPHOBIA = auto()
    TRAGOUDIPHOBIA = auto()
    TRAPEZAPHOBIA = auto()
    TROKHOPHOBIA = auto()
    TROMPETAPHOBIA = auto()
    TROPHOPHOBIA = auto()
    TRƐDNOPHOBIA = auto()
    TRYPANOPHOBIA = auto()
    TRYPOPHOBIA = auto()
    TR✈️GMOPHOBIA = auto()
    TURRIPHOBIA = auto()
    TYCHOPHOBIA = auto()
    TYMPANOPHOBIA = auto()
    TƜDROPHOBIA = auto()
    UMBRAPHOBIA = auto()
    UMBRELLAPHOBIA = auto()
    VAGONIPHOBIA = auto()
    VALANTIOPHOBIA = auto()
    VALITSAPHOBIA = auto()
    VERKEINTRIPHOBIA = auto()
    VESTIPHOBIA = auto()
    VIEMAPHOBIA = auto()
    VIDEOCASSETTOPHOBIA = auto()
    VINITOPHOBIA = auto()
    VIOLIPHOBIA = auto()
    VOEDSEPHOBIA = auto()
    VOIDOPHOBIA = auto()
    VOLANPHOBIA = auto()
    VORRAPHOBIA = auto()
    VOTHROPHOBIA = auto()
    VOULISIPHOBIA = auto()
    VINYLOPHOBIA = auto()
    V🚫SHROPHOBIA = auto()
    WANJUWUPHOBIA = auto()
    WHEELCHAIRPHOBIA = auto()
    WICCAPHOBIA = auto()
    WLANOPHOBIA = auto()
    XAFNIASMAPHOBIA = auto()
    X!MZOPHOBIA = auto()
    XINXIANGPHOBIA = auto()
    XYLOPHONOPHOBIA = auto()
    XYPNITIRIPHOBIA = auto()
    XYROPHOBIA = auto()
    W@NOPHOBIA = auto()
    YEDANSHUPHOBIA = auto()
    YEDENGPHOBIA = auto()
    YGROPHOBIA = auto()
    YINJIPHOBIA = auto()
    YINSHUIJIPHOBIA = auto()
    YLOPHOBIA = auto()
    YROUXPHOBIA = auto()
    YPNODOMATIOPHOBIA = auto()
    YUPENPHOBIA = auto()
    YUSHIXISHOPHOBIA = auto()
    YUSHUAPHOBIA = auto()
    YWAOHUPHOBIA = auto()
    Y∞GOMPHOBIA = auto()
    ZAPSAULPHOBIA = auto()
    ZARIPHOBIA = auto()
    ZHAOQINPHOBIA = auto()
    ZHINCHAPHOBIA = auto()
    ZHUOJPHOBIA = auto()
    ZIDONGSHOPHOBIA = auto()
    ZIZANMEPHOBIA = auto()
    ZLOQINGPHOBIA = auto()
    Z📷MROTPHOBIA = auto()
    ZONIASFALEIAPHOBIA = auto()
    ZRAIDOPHOBIA = auto()
    ZUIGERPHOBIA = auto()
    ZWUQIPHOBIA = auto()
    ZYGARIAPHOBIA = auto()


THINGS_PHOBIAS_DESCRIPTIONS_LANGUAGE_STRINGS: Dict[
    Enum, Dict[Languages, Optional[str]]] = {
    ThingsPhobiasDescriptions.ADIAFANOPHOBIA: {
        Languages.ENGLISH: "Fear of opaque objects",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ADVERTISEMENTPHOBIA: {
        Languages.ENGLISH: "Fear of advertisements",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.AEROSAKAPHOBIA: {
        Languages.ENGLISH: "Fear of airbags",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.AICHMOPHOBIA: {
        Languages.ENGLISH: "Fear of sharp or pointed objects (such as a needle or knife)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.AIRCOPHOBIA: {
        Languages.ENGLISH: "Fear of air conditioners, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.AIRPODAPHOBIA: {
        Languages.ENGLISH: "Fear of airpods",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ALARMOPHOBIA: {
        Languages.ENGLISH: "Fear of alarms",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ALLODOXAPHOBIA: {
        Languages.ENGLISH: "Fear of different people's opinions",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ALTOCELAROPHOBIA: {
        Languages.ENGLISH: "Fear of high ceilings, branch of celarophobia (fear of ceilings",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ANEMISTIRAPHOBIA: {
        Languages.ENGLISH: "Fear of fans, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ANIMAPHOBIA: {
        Languages.ENGLISH: "Fear of souls",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ANTANAKLOPHOBIA: {
        Languages.ENGLISH: "Fear of reflections",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ANTENNAPHOBIA: {
        Languages.ENGLISH: "Fear of antennae",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.APEIROPHOBIA: {
        Languages.ENGLISH: "Fear of infinity or eternity",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.APOSTASIPHOBIA: {
        Languages.ENGLISH: "Fear of distances",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.APPLETVAPHOBIA: {
        Languages.ENGLISH: "Fear of apple tv",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.AQUAMECHANOPHOBIA: {
        Languages.ENGLISH: "Fear of machines that have to involve water (branch of submechanophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ARACHTOPHOBIA: {
        Languages.ENGLISH: "Fear of artificial intelligence",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ARCHEIOTHIKIPHOBIA: {
        Languages.ENGLISH: "Fear of file cabinets",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ARMAROPHOBIA: {
        Languages.ENGLISH: "Fear of cupboards, branch of epiplaphobia (fear of furnitures)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ARPAPHOBIA: {
        Languages.ENGLISH: "Fear of harps, branch of gakkiphobia (fear of musical instruments)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ARTEMOPHOBIA: {
        Languages.ENGLISH: "Fear of art",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.AULOPHOBIA: {
        Languages.ENGLISH: "Fear of flutes, branch of gakkiphobia (fear of musical instruments)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.AUTOKERAPHOBIA: {
        Languages.ENGLISH: "Fear of car horns",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.AUTOPLENOPHOBIA: {
        Languages.ENGLISH: "Fear of car washes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.AUTOMATONOPHOBIA: {
        Languages.ENGLISH: "Fear of humanoid figures",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BACOPHOBIA: {
        Languages.ENGLISH: "Fear of pizza cutters",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BAHNUBOPHOBIA: {
        Languages.ENGLISH: "Fear of railroad crossings",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BALLISTOPHOBIA: {
        Languages.ENGLISH: "Fear of missles and bullets",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BALTEUSPHOBIA: {
        Languages.ENGLISH: "Fear of belts",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BALTICOPHOBIA: {
        Languages.ENGLISH: "Fear of photocopiers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BANDZOPHOBIA: {
        Languages.ENGLISH: "Fear of blow torches",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BANMAXIANPHOBIA: {
        Languages.ENGLISH: "Fear of crosswalks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BAROPHOBIA: {
        Languages.ENGLISH: "Fear of gravity",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BASSOLOPHOBIA: {
        Languages.ENGLISH: "Fear of bass instruments",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BATHMOPHOBIA: {
        Languages.ENGLISH: "Fear of stairs or steep slopes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BATHROBEPHOBIA: {
        Languages.ENGLISH: "Fear of bath robes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BATTEROPHOBIA: {
        Languages.ENGLISH: "Fear of batteries",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BEEPOPHOBIA: {
        Languages.ENGLISH: "Fear of beeping sounds",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BELONEPHOBIA: {
        Languages.ENGLISH: "Fear of pins and needles (branch of aichmophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BIBLIOPHOBIA: {
        Languages.ENGLISH: "Fear of books",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BILLBOARDPHOBIA: {
        Languages.ENGLISH: "Fear of billboards",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BIJIXPHOBIA: {
        Languages.ENGLISH: "Fear of laptops computers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BINOCULOPHOBIA: {
        Languages.ENGLISH: "Fear of binoculars",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BLEIMPNOPHOBIA: {
        Languages.ENGLISH: "Fear of empty boxes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BLEMENSAPHOBIA: {
        Languages.ENGLISH: "Fear of blue table",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BLENDERPHOBIA: {
        Languages.ENGLISH: "Fear of blenders",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BLOWERPEELPHOBIA: {
        Languages.ENGLISH: "Fear of sex dolls",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BRACESPHOBIA: {
        Languages.ENGLISH: "Fear of dental braces",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BRUGNOPHOBIA: {
        Languages.ENGLISH: "Fear of icemakers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BODENSTANDOPHOBIA: {
        Languages.ENGLISH: "Fear of grandfather clocks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BONOCKOPHOBIA: {
        Languages.ENGLISH: "Fear of skeleton keys",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BOOGIEBOARDPHOBIA: {
        Languages.ENGLISH: "Fear of boogieboards",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BOWERPHOBIA: {
        Languages.ENGLISH: "Fear of bowers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BOWPHOBIA: {
        Languages.ENGLISH: "Fear of bows",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BRIEFSHIEPHOBIA: {
        Languages.ENGLISH: "Fear of secret documents",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BUHUAJIPHOBIA: {
        Languages.ENGLISH: "Fear of walkie-talkies",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BUZZOPHOBIA: {
        Languages.ENGLISH: "Fear of buzzing sounds",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BWAOPIPHOBIA: {
        Languages.ENGLISH: "Fear of x-ray machines",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.BWAUKPHOBIA: {
        Languages.ENGLISH: "Fear of library books",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CABLEPHOBIA: {
        Languages.ENGLISH: "Fear of cables",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CAELOPHOBIA: {
        Languages.ENGLISH: "Fear of the sky",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CALCULAPHOBIA: {
        Languages.ENGLISH: "Fear of calculators",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CAMCORDERPHOBIA: {
        Languages.ENGLISH: "Fear of camcorders",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CAMERAPHOBIA: {
        Languages.ENGLISH: "Fear of cameras",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CAPILLUSSETISPHOBIA: {
        Languages.ENGLISH: "Fear of hairbrushes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CASSETTOPHOBIA: {
        Languages.ENGLISH: "Fear of cassette tapes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CATASTOLEPHOBIA: {
        Languages.ENGLISH: "Fear of repression or repressive culture/countries",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CATHEDRAPHOBIA: {
        Languages.ENGLISH: "Fear of chairs, branch of epiplaphobia (fear of furnitures)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CATOPTROPHOBIA: {
        Languages.ENGLISH: "Fear of mirrors, branch of oikophobia (fear of home surroundings)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CELAROPHOBIA: {
        Languages.ENGLISH: "Fear of ceilings",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CENOSILICAPHOBIA: {
        Languages.ENGLISH: "Fear of empty glasses",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CHARAKAPHOBIA: {
        Languages.ENGLISH: "Fear of rulers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CHARTIPHOBIA: {
        Languages.ENGLISH: "Fear of charts",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CHEDOANGPHOBIA: {
        Languages.ENGLISH: "Fear of driveways",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CHEKUXISHOPHOBIA: {
        Languages.ENGLISH: "Fear of garage sinks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CHIONOFYSOPHOBIA: {
        Languages.ENGLISH: "Fear of snow blowers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CHLOEPHOBIA: {
        Languages.ENGLISH: "Fear of newspapers (branch of papyrophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CHREOSTIKIKARTAPHOBIA: {
        Languages.ENGLISH: "Fear of debit cards",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CHROMETOPHOBIA: {
        Languages.ENGLISH: "Fear of money",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CHRONOMENTROPHOBIA: {
        Languages.ENGLISH: "Fear of clocks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CHUFXISHOPHOBIA: {
        Languages.ENGLISH: "Fear of kitchen sinks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CISTULAPHOBIA: {
        Languages.ENGLISH: "Fear of cabinets, branch of oikophobia (fear of home surroundings)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CITHARAPHOBIA: {
        Languages.ENGLISH: "Fear of guitars, branch of gakkiphobia (fear of musical instruments)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CLAPPERPHOBIA: {
        Languages.ENGLISH: "Fear of the clapper",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CLEITHROPHOBIA: {
        Languages.ENGLISH: "Fear of being trapped, branch of claustrophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CLINEPHOBIA: {
        Languages.ENGLISH: "Fear of beds, branch of epiplaphobia (fear of furnitures)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CLOACAPHOBIA: {
        Languages.ENGLISH: "Fear of sewers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.COGOMBOPHOBIA: {
        Languages.ENGLISH: "Fear of cardboard boxes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.COLIMBOPHOBIA: {
        Languages.ENGLISH: "Fear of swimming pools, branch of aquaphobia (fear of water)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.COMMERCIALPHOBIA: {
        Languages.ENGLISH: "Fear of commercials",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.COMPASSPHOBIA: {
        Languages.ENGLISH: "Fear of compasses",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CONFETTIPHOBIA: {
        Languages.ENGLISH: "Fear of confetti",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CONSECOTALEOPHOBIA: {
        Languages.ENGLISH: "Fear of chopsticks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CONTROSOFFITTOPHOBIA: {
        Languages.ENGLISH: "Fear of counter tops  ",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.COZAMPIOPHOBIA: {
        Languages.ENGLISH: "Fear of body pillows",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CRANOPHOBIA: {
        Languages.ENGLISH: "Fear of helmets",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CREMNOPHOBIA: {
        Languages.ENGLISH: "Fear of cliffs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CRUSRUMBLOPHOBIA: {
        Languages.ENGLISH: "Fear of cookie jars",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CUPROLAMINOPHOBIA: {
        Languages.ENGLISH: "Fear of coins",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CYBERPHOBIA: {
        Languages.ENGLISH: "Fear of computers, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.CYMOPHOBIA: {
        Languages.ENGLISH: "Fear of waves or wave-like motions",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DACHOINGPHOBIA: {
        Languages.ENGLISH: "Fear of power tools",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DARTBOARDPHOBIA: {
        Languages.ENGLISH: "Fear of dartboards",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DARTOPHOBIA: {
        Languages.ENGLISH: "Fear of darts",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DEFENESTRAPHOBIA: {
        Languages.ENGLISH: "Fear of windows",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DEKANIKIPHOBIA: {
        Languages.ENGLISH: "Fear of crutches",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DELEOPHOBIA: {
        Languages.ENGLISH: "Fear of erasers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DENGPAOPHOBIA: {
        Languages.ENGLISH: "Fear of light bulbs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DENTODRAPANOPHOBIA: {
        Languages.ENGLISH: "Fear of dental drills",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DENTUREPHOBIA: {
        Languages.ENGLISH: "Fear of dentures",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DEXTROPHOBIA: {
        Languages.ENGLISH: "Fear of objects at the right side of the body",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DIAFANOPHOBIA: {
        Languages.ENGLISH: "Fear of transparent objects",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DIANZIFANKUIPHOBIA: {
        Languages.ENGLISH: "Fear of electronic feedback",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DIAPERPHOBIA: {
        Languages.ENGLISH: "Fear of diapers, branch of vestiphobia (fear of clothing)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DIAPHIMISTICOPHOBIA: {
        Languages.ENGLISH: "Fear of commercials",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DIASTIMAPHOBIA: {
        Languages.ENGLISH: "Fear of physical space",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DIATHLASOPHOBIA: {
        Languages.ENGLISH: "Fear of refractions",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DICLEBGOPHOBIA: {
        Languages.ENGLISH: "Fear of teabags",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DIETHNESYSTIMAMONADONOPHOBIA: {
        Languages.ENGLISH: "Fear of the metric system",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DIKEPHOBIA: {
        Languages.ENGLISH: "Fear of justice",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DIMEPHOBIA: {
        Languages.ENGLISH: "Fear of dimes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DINGOPHOBIA: {
        Languages.ENGLISH: "Fear of dinging sounds",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DINOPHOBIA: {
        Languages.ENGLISH: "Fear of dizziness or whirlpools",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DISHLEPROPHOBIA: {
        Languages.ENGLISH: "Fear of dishwashers, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DIZOANGPHOBIA: {
        Languages.ENGLISH: "Fear of electric generators",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DLITOPHOBIA: {
        Languages.ENGLISH: "Fear of gas grills",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DOMINEATHERPHOBIA: {
        Languages.ENGLISH: "Fear of collars that can control people",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DOORBELLPHOBIA: {
        Languages.ENGLISH: "Fear of doorbells",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DORAPHOBIA: {
        Languages.ENGLISH: "Fear of fur or skins of animals",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DORNGOPHOBIA: {
        Languages.ENGLISH: "Fear of plasma globes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DORYFORIKOCHARTIPHOBIA: {
        Languages.ENGLISH: "Fear of satelite maps",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DOTTOPHOBIA: {
        Languages.ENGLISH: "Fear of dots",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DRAPANOPHOBIA: {
        Languages.ENGLISH: "Fear of drills",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DRIKRONPHOBIA: {
        Languages.ENGLISH: "Fear of dark walls",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DROGERPHOBIA: {
        Languages.ENGLISH: "Fear of clothes dryers, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DROMUSEPHOBIA: {
        Languages.ENGLISH: "Fear of dropper rides",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DULUNCHEPHOBIA: {
        Languages.ENGLISH: "Fear of wheelbarrows",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DUMASAPHOBIA: {
        Languages.ENGLISH: "Fear of stupid things",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DUMPSTERPHOBIA: {
        Languages.ENGLISH: "Fear of dumpsters",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DUOPHOBIA: {
        Languages.ENGLISH: "Fear of pairs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.DVDPHOBIA: {
        Languages.ENGLISH: "Fear of dvds",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.EAPALLIOPHOBIA: {
        Languages.ENGLISH: "Fear of rugs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.EARMUFFPHOBIA: {
        Languages.ENGLISH: "Fear of earmuffs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.EBULLIOPHOBIA: {
        Languages.ENGLISH: "Fear of bubbles",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.OIKOPHOBIA: {
        Languages.ENGLISH: "Fear of home surroundings",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.EIFFELTURRIPHOBIA: {
        Languages.ENGLISH: "Fear of eiffel tower, branch of turriphobia (fear of towers)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.EISOPTROPHOBIA: {
        Languages.ENGLISH: "Fear of your own reflection in a mirror",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ELECTROPHOBIA: {
        Languages.ENGLISH: "Fear of electricity",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ELEVATOPHOBIA: {
        Languages.ENGLISH: "Fear of elevators",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ELEVAPHOBIA: {
        Languages.ENGLISH: "Same as elevatophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.EMAILPHOBIA: {
        Languages.ENGLISH: "Fear of email",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ENERGYPHOBIA: {
        Languages.ENGLISH: "Fear of energy",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ENISSOPHOBIA: {
        Languages.ENGLISH: "Fear of criticism",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ENTAMAPHOBIA: {
        Languages.ENGLISH: "Fear of doors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ENYDREIOPHOBIA: {
        Languages.ENGLISH: "Fear of fishtanks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.EPIPLAPHOBIA: {
        Languages.ENGLISH: "Fear of furnitures, branch of oikophobia (fear of home surroundings)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.EPISTOLAPHOBIA: {
        Languages.ENGLISH: "Fear of epistles",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.EPISTEMOPHOBIA: {
        Languages.ENGLISH: "Fear of knowledge",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ERGALEIOPHOBIA: {
        Languages.ENGLISH: "Fear of tools",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ERYTHOPHOBIA: {
        Languages.ENGLISH: "Fear of redlights",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.EREUTHOPHOBIA: {
        Languages.ENGLISH: "Same as erythophobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ESCALAPHOBIA: {
        Languages.ENGLISH: "Fear of escalators",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ROLTRAPHOBIA: {
        Languages.ENGLISH: "Same as escalaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ESCALATOPHOBIA: {
        Languages.ENGLISH: "Same as escalaphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ESOROUCHAPHOBIA: {
        Languages.ENGLISH: "Fear of underwear, branch of vestiphobia (fear of clothing)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ETHISMOSOPHOBIA: {
        Languages.ENGLISH: "Fear of addiction",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.EUPHOBIA: {
        Languages.ENGLISH: "Fear of good news",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.EUPISTOPHOBIA: {
        Languages.ENGLISH: "Fear of faith",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.EVODIAPHOBIA: {
        Languages.ENGLISH: "Fear of pleasant smell, branch of osmophobia (fear of smells or odors)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FADCHOONGPHOBIA: {
        Languages.ENGLISH: "Fear of power plants",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FASCIOLISPHOBIA: {
        Languages.ENGLISH: "Fear of hoses",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FAKELOPHOBIA: {
        Languages.ENGLISH: "Fear of envelopes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FAKOSPHOBIA: {
        Languages.ENGLISH: "Fear of flashlights",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FANARIPHOBIA: {
        Languages.ENGLISH: "Fear of traffic lights",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FARASIPHOBIA: {
        Languages.ENGLISH: "Fear of dustpans",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FENBANPHOBIA: {
        Languages.ENGLISH: "Fear of chalkboards",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FERETROPHOBIA: {
        Languages.ENGLISH: "Fear of caskets",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FERROPHOBIA: {
        Languages.ENGLISH: "Fear of iron",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FICTOPHOBIA: {
        Languages.ENGLISH: "Fear of fiction",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FILICOPHOBIA: {
        Languages.ENGLISH: "Fear of filicology",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FILOPHOBIA: {
        Languages.ENGLISH: "Fear of wires",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FIREHYDRANTPHOBIA: {
        Languages.ENGLISH: "Fear of fire hydrants",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FLASCIPHOBIA: {
        Languages.ENGLISH: "Fear of bottles",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FLITZANIPHOBIA: {
        Languages.ENGLISH: "Fear of cups",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FLITZANISAGIOUPHOBIA: {
        Languages.ENGLISH: "Fear of teacups",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FOCOPHOBIA: {
        Languages.ENGLISH: "Fear of fireplaces, branch of oikophobia (fear of home surroundings)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FOONIPHOBIA: {
        Languages.ENGLISH: "Fear of blow-dryers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FOREMAPHOBIA: {
        Languages.ENGLISH: "Fear of dresses",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FORMIDOPHOBIA: {
        Languages.ENGLISH: "Fear of scarecrows",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FORNACIPHOBIA: {
        Languages.ENGLISH: "Fear of furnaces, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FORUMPHOBIA: {
        Languages.ENGLISH: "Fear of internet forums",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FOSSILPHOBIA: {
        Languages.ENGLISH: "Fear of fossils",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FOURNOPHOBIA: {
        Languages.ENGLISH: "Fear of ovens, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FOUSTAPHOBIA: {
        Languages.ENGLISH: "Fear of skirts",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FRACHTIPHOBIA: {
        Languages.ENGLISH: "Fear of fences",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FRAGMAPHOBIA: {
        Languages.ENGLISH: "Fear of dams",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FREARPHOBIA: {
        Languages.ENGLISH: "Fear of wells",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FRENOPHOBIA: {
        Languages.ENGLISH: "Fear of brakes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FR%PLOPHOBIA: {
        Languages.ENGLISH: "Fear of styrofoam cups",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FUMIPHOBIA: {
        Languages.ENGLISH: "Fear of smoke",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FURNGZUPHOBIA: {
        Languages.ENGLISH: "Fear of kitchen tables",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FWAUTPHOBIA: {
        Languages.ENGLISH: "Fear of foot massagers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FWONGIPHOBIA: {
        Languages.ENGLISH: "Fear of public swimming pools",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FYLLOFYSOPHOBIA: {
        Languages.ENGLISH: "Fear of leaf blowers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GAKKIPHOBIA: {
        Languages.ENGLISH: "Fear of musical instruments  ",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GASGAUGEPHOBIA: {
        Languages.ENGLISH: "Fear of gas gauges",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GASPEDALPHOBIA: {
        Languages.ENGLISH: "Fear of gas pedals",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GELIOPHOBIA: {
        Languages.ENGLISH: "Fear of laughter",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GERAPHOBIA: {
        Languages.ENGLISH: "Fear of metal straws",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GEUMAPHOBIA: {
        Languages.ENGLISH: "Fear of taste",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GATNOBPHOBIA: {
        Languages.ENGLISH: "Fear of long hallways",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GLEYMOPHOBIA: {
        Languages.ENGLISH: "Fear of eyeglasses",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GLOBOPHOBIA: {
        Languages.ENGLISH: "Fear of balloons",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GL÷NDOPHOBIA: {
        Languages.ENGLISH: "Fear of tin cans",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GOOGLEPHOBIA: {
        Languages.ENGLISH: "Fear of search engines",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GOUWUCHEPHOBIA: {
        Languages.ENGLISH: "Fear of shopping carts",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GRAFEIOPHOBIA: {
        Languages.ENGLISH: "Fear of desks, branch of epiplaphobia (fear of furnitures)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GRAFFITIPHOBIA: {
        Languages.ENGLISH: "Fear of graffiti",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GRAMMATOSIMOPHOBIA: {
        Languages.ENGLISH: "Fear of postal stamps",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GRANDSLAMWICHPHOBIA: {
        Languages.ENGLISH: "Fear of grand slamwich",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GR?SOPHOBIA: {
        Languages.ENGLISH: "Fear of circular saws",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.GYALIAILIOUPHOBIA: {
        Languages.ENGLISH: "Fear of sunglasses",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.G4GOPHOBIA: {
        Languages.ENGLISH: "Fear of air horns",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HAGIOPHOBIA: {
        Languages.ENGLISH: "Fear of holy things",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HANDCUFFPHOBIA: {
        Languages.ENGLISH: "Fear of handcuffs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HEADLIGHTPHOBIA: {
        Languages.ENGLISH: "Fear of headlights",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HEADPHONOPHOBIA: {
        Languages.ENGLISH: "Fear of headphones",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HEARINGAIDPHOBIA: {
        Languages.ENGLISH: "Fear of hearing aids",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HEDGETROPHOBIA: {
        Languages.ENGLISH: "Fear of hedge trimmers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HEIZGEPHOBIA: {
        Languages.ENGLISH: "Fear of heaters, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HERESYPHOBIA: {
        Languages.ENGLISH: "Fear of challenges to official doctrine or of radical deviation",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HEREIOPHOBIA: {
        Languages.ENGLISH: "Same as heresyphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HERPETOPHOBIA: {
        Languages.ENGLISH: "Fear of creepy, crawly things",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HIBERNICAPHOBIA: {
        Languages.ENGLISH: "Fear of carpets, branch of oikophobia (fear of home surroundings)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HIEROPHOBIA: {
        Languages.ENGLISH: "Fear of sacred thin",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HLEGUPHOBIA: {
        Languages.ENGLISH: "Fear of black lights",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HMOSHGOPHOBIA: {
        Languages.ENGLISH: "Fear of laundry",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HNIRSHUNPHOBIA: {
        Languages.ENGLISH: "Fear of dirty dishes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HOCKEYPHOBIA: {
        Languages.ENGLISH: "Fear of hockey",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HOPLOPHOBIA: {
        Languages.ENGLISH: "Fear of weapons, specifically firearms",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HOSEPHOBIA: {
        Languages.ENGLISH: "Fear of hoses",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HRONGYOPHOBIA: {
        Languages.ENGLISH: "Fear of lava lamps",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HUMORPHOBIA: {
        Languages.ENGLISH: "Fear of humor",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HYELOPHOBIA: {
        Languages.ENGLISH: "Fear of glass",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HYGROPHOBIA: {
        Languages.ENGLISH: "Fear of liquids, dampness, or moisture",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HYLEPHOBIA: {
        Languages.ENGLISH: "Fear of materialism",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.HYPENGYOPHOBIA: {
        Languages.ENGLISH: "Fear of responsibility",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.H8POPHOBIA: {
        Languages.ENGLISH: "Fear of flamethrowers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ICONOPHOBIA: {
        Languages.ENGLISH: "Fear of icons",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.IDEOPHOBIA: {
        Languages.ENGLISH: "Fear of intellect",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.IMEROLOGIOPHOBIA: {
        Languages.ENGLISH: "Fear of calendars",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.INTERCOMPHOBIA: {
        Languages.ENGLISH: "Fear of intercoms",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.INTERNETPHOBIA: {
        Languages.ENGLISH: "Fear of the internet",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.JIJINGPHOBIA: {
        Languages.ENGLISH: "Fear of car alarms",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.JUKEBOXOPHOBIA: {
        Languages.ENGLISH: "Fear of jukeboxes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.JULELOPHOBIA: {
        Languages.ENGLISH: "Fear of christmas lights",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.J9DOBPHOBIA: {
        Languages.ENGLISH: "Fear of hot tubs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KAFETIPHOBIA: {
        Languages.ENGLISH: "Fear of coffeemakers, branch of syskeviphobia (fear of appliance",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KALATHIPHOBIA: {
        Languages.ENGLISH: "Fear of baskets",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KALTSAPHOBIA: {
        Languages.ENGLISH: "Fear of socks, branch of vestiphobia (fear of clothing)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KAMARAKIPHOBIA: {
        Languages.ENGLISH: "Fear of closets",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KAMPANAPHOBIA: {
        Languages.ENGLISH: "Fear of bells",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KANAYAPHOBIA: {
        Languages.ENGLISH: "Fear of chainsaws",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KAPELAPHOBIA: {
        Languages.ENGLISH: "Fear of hats, branch of vestiphobia (fear of clothing)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KARAZPHOBIA: {
        Languages.ENGLISH: "Fear of garages",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KARAZPORTANOICHTIRIPHOBIA: {
        Languages.ENGLISH: "Fear of garage door openers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KARAZPORTAPHOBIA: {
        Languages.ENGLISH: "Fear of garage doors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KARFIPHOBIA: {
        Languages.ENGLISH: "Fear of nails",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KAROTSAKIPHOBIA: {
        Languages.ENGLISH: "Fear of strollers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KASSAPHOBIA: {
        Languages.ENGLISH: "Fear of cash registers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KASONIPHOBIA: {
        Languages.ENGLISH: "Fear of boxes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KATAGELOPHOBIA: {
        Languages.ENGLISH: "Fear of ridicule",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KATSAVIDIPHOBIA: {
        Languages.ENGLISH: "Fear of screwdrivers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KATARRAKTIPHOBIA: {
        Languages.ENGLISH: "Fear of waterfalls",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KEFIPHOBIA: {
        Languages.ENGLISH: "Fear of fun",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KENOPHOBIA: {
        Languages.ENGLISH: "Fear of voids or empty spaces",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KERAPHOBIA: {
        Languages.ENGLISH: "Fear of horns",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KERASOPHOBIA: {
        Languages.ENGLISH: "Same as keraphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KERIPHOBIA: {
        Languages.ENGLISH: "Fear of candles",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KIFNAPHOBIA: {
        Languages.ENGLISH: "Fear of drones",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KILNPHOBIA: {
        Languages.ENGLISH: "Fear of kilns",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KINZODOPHOBIA: {
        Languages.ENGLISH: "Fear of handheld metal detectors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KIROMPIGIAPHOBIA: {
        Languages.ENGLISH: "Fear of crayons",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KLEIDARIAPHOBIA: {
        Languages.ENGLISH: "Fear of locks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KLEIDIPHOBIA: {
        Languages.ENGLISH: "Fear of keys",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KLƐBZEENPHOBIA: {
        Languages.ENGLISH: "Fear of flat tires",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KOINONIPHOBIA: {
        Languages.ENGLISH: "Fear of rooms",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KOLONIAPHOBIA: {
        Languages.ENGLISH: "Fear of colognes and perfumes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KONSENTOPHOBIA: {
        Languages.ENGLISH: "Fear of electric outlets  ",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KOSMEMOPHOBIA: {
        Languages.ENGLISH: "Fear of jewelry",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KOUMPIPHOBIA: {
        Languages.ENGLISH: "Fear of buttons",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KOUNIAPHOBIA: {
        Languages.ENGLISH: "Fear of swings",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KOUVAPHOBIA: {
        Languages.ENGLISH: "Fear of buckets",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KOUZIPHOBIA: {
        Languages.ENGLISH: "Fear of stoves, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KREMASTRAPHOBIA: {
        Languages.ENGLISH: "Fear of coat hangers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.KYPELLOPHOBIA: {
        Languages.ENGLISH: "Fear of mugs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.K2NQIPHOBIA: {
        Languages.ENGLISH: "Fear of space heaters",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LADDERPHOBIA: {
        Languages.ENGLISH: "Fear of ladders",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LAGOUMIPHOBIA: {
        Languages.ENGLISH: "Fear of rabbit holes, branch of trypophobia (fear of holes)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LAMPAPHOBIA: {
        Languages.ENGLISH: "Fear of lamps, branch of oikophobia (fear of home surroundings)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LASTICHOPHOBIA: {
        Languages.ENGLISH: "Fear of tires",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LATERIPHOBIA: {
        Languages.ENGLISH: "Fear of legos (branch of ludilophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LECHOPHOBIA: {
        Languages.ENGLISH: "Fear of couches, branch of epiplaphobia (fear of furnitures)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LENTOPHOBIA: {
        Languages.ENGLISH: "Fear of contact lenses",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LEVOPHOBIA: {
        Languages.ENGLISH: "Fear of things to the left side of the body",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LIGAMENTOPHOBIA: {
        Languages.ENGLISH: "Fear of ribbons",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LIGHTERPHOBIA: {
        Languages.ENGLISH: "Fear of lighters",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LIGYROPHOBIA: {
        Languages.ENGLISH: "Fear of loud noises (psychological phobia) (branch of phonophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LIMNIPHOBIA: {
        Languages.ENGLISH: "Fear of lakes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LINONOPHOBIA: {
        Languages.ENGLISH: "Fear of strings",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LINYUPHOBIA: {
        Languages.ENGLISH: "Fear of showers, branch of oikophobia (fear of home surroundings)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LOCKERPHOBIA: {
        Languages.ENGLISH: "Fear of lockers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LODICULAPHOBIA: {
        Languages.ENGLISH: "Fear of blankets",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LOGICOMECHANIBIOPHOBIA: {
        Languages.ENGLISH: "Fear of artificial life (robots, drones, cyborgs)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LOGOCRISIAPHOBIA: {
        Languages.ENGLISH: "Fear of censorship",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LOUTROPHOBIA: {
        Languages.ENGLISH: "Fear of bathrooms",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LRASHAPHOBIA: {
        Languages.ENGLISH: "Fear of massage chairs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LUMENOPHOBIA: {
        Languages.ENGLISH: "Fear of light fixtures",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LUODOPHOBIA: {
        Languages.ENGLISH: "Fear of floor lamps",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.LYSBRYTOPHOBIA: {
        Languages.ENGLISH: "Fear of light-switches  ",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MAGEIREIOPHOBIA: {
        Languages.ENGLISH: "Fear of kitchens",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MAIKBANPHOBIA: {
        Languages.ENGLISH: "Fear of whiteboards",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MONOXEIDIOANTHRAKAPHOBIA: {
        Languages.ENGLISH: "Fear of carbon monoxide",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MAGEIACHALIPHOBIA: {
        Languages.ENGLISH: "Fear of magic carpets",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MAGIKORAVDIPHOBIA: {
        Languages.ENGLISH: "Fear of magic wands",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MAGNITOFONOPHOBIA: {
        Languages.ENGLISH: "Fear of tape recorders",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MANHOLEPHOBIA: {
        Languages.ENGLISH: "Fear of manholes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MANUSSICCUSPHOBIA: {
        Languages.ENGLISH: "Fear of hand dryers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MAPPOPHOBIA: {
        Languages.ENGLISH: "Fear of maps",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MARKADOROPHOBIA: {
        Languages.ENGLISH: "Fear of markers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MATTERPHOBIA: {
        Languages.ENGLISH: "Fear of matter",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MECHANOPHOBIA: {
        Languages.ENGLISH: "Fear of machines",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MEDIAPHOBIA: {
        Languages.ENGLISH: "Fear of media",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MEGALOPHOBIA: {
        Languages.ENGLISH: "Fear of large things",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MEGAPHONOPHOBIA: {
        Languages.ENGLISH: "Fear of megaphones",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MELOPHOBIA: {
        Languages.ENGLISH: "Fear of music (branch of phonophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MEMEPHOBIA: {
        Languages.ENGLISH: "Fear of internet memes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MEMEOPHOBIA: {
        Languages.ENGLISH: "Fear of memes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MENOPHOBIA: {
        Languages.ENGLISH: "Fear of menstruation",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.METAZODEPHOBIA: {
        Languages.ENGLISH: "Fear of metazodes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MICROPHONOPHOBIA: {
        Languages.ENGLISH: "Fear of microphones",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MINICELAROPHOBIA: {
        Languages.ENGLISH: "Fear of low ceilings (branch of celarophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MYSOPHOBIA: {
        Languages.ENGLISH: "Fear of dirt (rupophobia) or contamination",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.METROPHOBIA: {
        Languages.ENGLISH: "Fear of poetry",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MICROPHOBIA: {
        Languages.ENGLISH: "Fear of small things",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MYCROPHOBIA: {
        Languages.ENGLISH: "Same as microphobia",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MICROSCOPOPHOBIA: {
        Languages.ENGLISH: "Fear of microscopes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MICROVOPHOBIA: {
        Languages.ENGLISH: "Fear of microwave ovens, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MLAFENPHOBIA: {
        Languages.ENGLISH: "Fear of coffee grinders",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MNEMOPHOBIA: {
        Languages.ENGLISH: "Fear of memories",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MRNPHOBIA: {
        Languages.ENGLISH: "Fear of charcoal grills",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MOLYVIPHOBIA: {
        Languages.ENGLISH: "Fear of pencils",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MUNJINGPHOBIA: {
        Languages.ENGLISH: "Fear of emergency exit door alarms",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MYKITAPHOBIA: {
        Languages.ENGLISH: "Fear of fungus",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.MYTHOPHOBIA: {
        Languages.ENGLISH: "Fear of myths, stories or false statements",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.NAITOSUTANDOPHOBIA: {
        Languages.ENGLISH: "Fear of nightstands, branch of epiplaphobia (fear of furnitures)  ",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.NECROPHOBIA: {
        Languages.ENGLISH: "Fear of dead things",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.NEOPHOBIA: {
        Languages.ENGLISH: "Fear of newness",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.NICKELPHOBIA: {
        Languages.ENGLISH: "Fear of nickels",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.NIJOONGPHOBIA: {
        Languages.ENGLISH: "Fear of yearbooks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.NLAIGUPHOBIA: {
        Languages.ENGLISH: "Fear of can openers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.NINTENDOPHOBIA: {
        Languages.ENGLISH: "Fear of nintendo",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.NOJESCENTROPHOBIA: {
        Languages.ENGLISH: "Fear of entertainment centers, branch of epiplaphobia (fear of furnitures)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.NOTOPHOBIA: {
        Languages.ENGLISH: "Fear of south",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.NRASOBPHOBIA: {
        Languages.ENGLISH: "Fear of cheese graters",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.NUCLEOMITUPHOBIA: {
        Languages.ENGLISH: "Fear of nuclear weapons (branch of hoplophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.NWUMPOPHOBIA: {
        Languages.ENGLISH: "Fear of electric mixers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.N☽MWUPHOBIA: {
        Languages.ENGLISH: "Fear of milk jugs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.OBJECTSHOWPHOBIA: {
        Languages.ENGLISH: "Fear of object shows",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.OCTAGONPHOBIA: {
        Languages.ENGLISH: "Fear of octagons",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.OIKOPHOBIA: {
        Languages.ENGLISH: "Fear of home surroundings",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.OMNIPHOBIA: {
        Languages.ENGLISH: "Fear of all and when you have every fear",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ONEHUNDREDBOTTLESOFBEERPHOBIA: {
        Languages.ENGLISH: "Fear of 100 bottles of beer on the wall",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.OPINATOPHOBIA: {
        Languages.ENGLISH: "Fear of imagination",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.OPIOPHOBIA: {
        Languages.ENGLISH: "Fear of doctor's experience of prescribing needed pain medications for patients",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ORATOPAROPHOBIA: {
        Languages.ENGLISH: "Fear of speakers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ORDCLAVIPHOBIA: {
        Languages.ENGLISH: "Fear of computer keyboards",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ORTHOPHOBIA: {
        Languages.ENGLISH: "Fear of property",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.OSMOPHOBIA: {
        Languages.ENGLISH: "Fear of smells",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.OSOURIPHOBIA: {
        Languages.ENGLISH: "Fear of computer mice",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.OTASPIDAPHOBIA: {
        Languages.ENGLISH: "Fear of earplugs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.OULINOPHOBIA: {
        Languages.ENGLISH: "Fear of scars",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.OURITIRIOPHOBIA: {
        Languages.ENGLISH: "Fear of urinals",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.OVALPHOBIA: {
        Languages.ENGLISH: "Fear of ovals",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PACTORBOPHOBIA: {
        Languages.ENGLISH: "Fear of cds",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PAGOPHOBIA: {
        Languages.ENGLISH: "Fear of ice or frost",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PAMPHOBIA: {
        Languages.ENGLISH: "Fear of an unknown cause",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PANOPHOBIA: {
        Languages.ENGLISH: "Fear of everything (branch of panphobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PANPHOBIA: {
        Languages.ENGLISH: "Fear of all (branch of pantophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PANTELONIPHOBIA: {
        Languages.ENGLISH: "Fear of pants, branch of vestiphobia (fear of clothing)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PANTOPHOBIA: {
        Languages.ENGLISH: "Fear of everything or all",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PAPOUTSIPHOBIA: {
        Languages.ENGLISH: "Fear of shoes, branch of vestiphobia (fear of clothing)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PAPYROPHOBIA: {
        Languages.ENGLISH: "Fear of paper",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PAYPHONOPHOBIA: {
        Languages.ENGLISH: "Fear of payphones",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PATROIOPHOBIA: {
        Languages.ENGLISH: "Fear of heredity",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PECCATOPHOBIA: {
        Languages.ENGLISH: "Fear of imaginary crimes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PECTUSSPEMOPHOBIA: {
        Languages.ENGLISH: "Fear of hope chests, branch of epiplaphobia (fear of furnitures)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PEDIOPHOBIA: {
        Languages.ENGLISH: "Fear of dolls (branch of automatonophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PENCILLOPHOBIA: {
        Languages.ENGLISH: "Fear of pencils",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PENNYPHOBIA: {
        Languages.ENGLISH: "Fear of pennies",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PERSTILBOSPHERPHOBIA: {
        Languages.ENGLISH: "Fear of mirror balls",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PEZODROMIOPHOBIA: {
        Languages.ENGLISH: "Fear of sidewalks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PHILOSOPHOBIA: {
        Languages.ENGLISH: "Fear of philosophy",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PHONOPHOBIA: {
        Languages.ENGLISH: "Fear of loud noise (branch of (ligyrophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PHOTOAUGLIAPHOBIA: {
        Languages.ENGLISH: "Fear of glaring lights (branch of photophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PHOTOGRAPHOPHOBIA: {
        Languages.ENGLISH: "Fear of photography",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PHOTOPHOBIA: {
        Languages.ENGLISH: "Fear of light",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PIATOPHOBIA: {
        Languages.ENGLISH: "Fear of dishes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PICTOPHOBIA: {
        Languages.ENGLISH: "Fear of pictures",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PINGBOPHOBIA: {
        Languages.ENGLISH: "Fear of tablet computers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PINGPONGPHOBIA: {
        Languages.ENGLISH: "Fear of ping pong",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PISTOTIKIKARTAPHOBIA: {
        Languages.ENGLISH: "Fear of credit cards",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PITHANOPHOBIA: {
        Languages.ENGLISH: "Fear of probabilities",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PLACOPHOBIA: {
        Languages.ENGLISH: "Fear of tombstones",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PLAKIDIOPHOBIA: {
        Languages.ENGLISH: "Fear of tiles",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PLANOPHOBIA: {
        Languages.ENGLISH: "Fear of piano, branch of gakkiphobia (fear of musical instruments)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PLASTOPHOBIA: {
        Languages.ENGLISH: "Fear of plastic bags",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PLYNTIPHOBIA: {
        Languages.ENGLISH: "Fear of washing machines, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.POLYPHOBIA: {
        Languages.ENGLISH: "Fear of many things",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.POOLPHOBIA: {
        Languages.ENGLISH: "Fear of pool games",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PORTBANKAZPHOBIA: {
        Languages.ENGLISH: "Fear of car trunks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.POSTALPHOBIA: {
        Languages.ENGLISH: "Fear of mail",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.POTAMOPHOBIA: {
        Languages.ENGLISH: "Fear of rivers or running water",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.POUKAMISOPHOBIA: {
        Languages.ENGLISH: "Fear of shirts, branch of vestiphobia (fear of clothing)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PRAGMATICOPHOBIA: {
        Languages.ENGLISH: "Fear of reality",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PRAXIPHOBIA: {
        Languages.ENGLISH: "Fear of actions",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PRINTERPHOBIA: {
        Languages.ENGLISH: "Fear of printers, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PROPHETOPHOBIA: {
        Languages.ENGLISH: "Fear of prophecies",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PROSOPHOBIA: {
        Languages.ENGLISH: "Fear of progress",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.P🎈GRONPHOBIA: {
        Languages.ENGLISH: "Fear of paper bags",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PSALIDIPHOBIA: {
        Languages.ENGLISH: "Fear of scissors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PSICHAPHOBIA: {
        Languages.ENGLISH: "Fear of crumbs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PSYCHOPHOBIA: {
        Languages.ENGLISH: "Fear of mind",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PSYGEPHOBIA: {
        Languages.ENGLISH: "Fear of refrigerators, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PUMPPUPHOBIA: {
        Languages.ENGLISH: "Fear of sump pump, branch of syskeviphobia (fear of appliances)  ",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PUPAPHOBIA: {
        Languages.ENGLISH: "Fear of puppets (branch of automatonophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PURINSUMPHOBIA: {
        Languages.ENGLISH: "Fear of trash cans",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PURGAMENTOPHOBIA: {
        Languages.ENGLISH: "Fear of garbage",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PYLIPHOBIA: {
        Languages.ENGLISH: "Fear of gates",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PYROPHOBIA: {
        Languages.ENGLISH: "Fear of fire",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PYROTECHNOPHOBIA: {
        Languages.ENGLISH: "Fear of fireworks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.PYRSOPHOBIA: {
        Languages.ENGLISH: "Fear of torches",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.P🐟XMOPHOBIA: {
        Languages.ENGLISH: "Fear of pizza boxes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.P3NSOPHOBIA: {
        Languages.ENGLISH: "Fear of spray guns",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.QAGAZUSAQPHOBIA: {
        Languages.ENGLISH: "Fear of paper airplanes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.QIEDJINGPHOBIA: {
        Languages.ENGLISH: "Fear of burglar alarms",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.QUARTERPHOBIA: {
        Languages.ENGLISH: "Fear of quarters",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.RADIOPHOBIA: {
        Languages.ENGLISH: "Fear of radioactivity or x-rays",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.RASEMAPHOBIA: {
        Languages.ENGLISH: "Fear of lawn mowers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.RAVDIPHOBIA: {
        Languages.ENGLISH: "Fear of walking canes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.R🚦CREBPHOBIA: {
        Languages.ENGLISH: "Fear of cracked tiles",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.RECEIPTPHOBIA: {
        Languages.ENGLISH: "Fear of receipts",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.RECREATIONPHOBIA: {
        Languages.ENGLISH: "Fear of recreation",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.RELAXATIONPHOBIA: {
        Languages.ENGLISH: "Fear of relaxation",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.REMINDERPHOBIA: {
        Languages.ENGLISH: "Fear of reminders",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.REMMIÐOPHOBIA: {
        Languages.ENGLISH: "Fear of christmas tree lights",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.RENWUPHOBIA: {
        Languages.ENGLISH: "Fear of action figures (branch of automatonophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.REQIQIUPHOBIA: {
        Languages.ENGLISH: "Fear of hot air balloons",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.RESHUIQIPHOBIA: {
        Languages.ENGLISH: "Fear of water heaters, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.RETAINERPHOBIA: {
        Languages.ENGLISH: "Fear of dental retainers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.REVMAGRAMMIPHOBIA: {
        Languages.ENGLISH: "Fear of power lines",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.RINGOPHOBIA: {
        Languages.ENGLISH: "Fear of ringing sounds",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.RLERROPHOBIA: {
        Languages.ENGLISH: "Fear of patio chairs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ROBOPHOBIA: {
        Languages.ENGLISH: "Fear of robots",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ROLLERSKATEPHOBIA: {
        Languages.ENGLISH: "Fear of rollerskates",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ROLLATOPHOBIA: {
        Languages.ENGLISH: "Fear of walking frames",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ROLOIPHOBIA: {
        Languages.ENGLISH: "Fear of watches",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.R🚗ZNONPHOBIA: {
        Languages.ENGLISH: "Fear of revolving doors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.RWECONPHOBIA: {
        Languages.ENGLISH: "Fear of picnic tables",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SAKIDIOPHOBIA: {
        Languages.ENGLISH: "Fear of backpacks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SAKOULAPHOBIA: {
        Languages.ENGLISH: "Fear of bags",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SANTAKIPHOBIA: {
        Languages.ENGLISH: "Fear of purses",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SAXOPHONOPHOBIA: {
        Languages.ENGLISH: "Fear of saxophones, branch of gakkiphobia (fear of musical instruments)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SCATOPHOBIA: {
        Languages.ENGLISH: "Fear of fecal matter",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SCHARAPHOBIA: {
        Languages.ENGLISH: "Fear of grills",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SCIOPHOBIA: {
        Languages.ENGLISH: "Fear of shadows",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SCOTOMAPHOBIA: {
        Languages.ENGLISH: "Fear of blindness in visual field",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SCRINIAPHOBIA: {
        Languages.ENGLISH: "Fear of bookcases, branch of epiplaphobia (fear of furnitures)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SEIRINAPHOBIA: {
        Languages.ENGLISH: "Fear of sirens",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SEPLOPHOBIA: {
        Languages.ENGLISH: "Fear of decaying matter",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SENOƩUPHOBIA: {
        Languages.ENGLISH: "Fear of birthday cake candles",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SFAIRAPHOBIA: {
        Languages.ENGLISH: "Fear of globes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SFOUNGARISTRAPHOBIA: {
        Languages.ENGLISH: "Fear of mops",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SFYRIPHOBIA: {
        Languages.ENGLISH: "Fear of hammers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SHUICAOPHOBIA: {
        Languages.ENGLISH: "Fear of sinks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SH5DOPHOBIA: {
        Languages.ENGLISH: "Fear of paper shredders",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SIMAPHOBIA: {
        Languages.ENGLISH: "Fear of signs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SINISTROPHOBIA: {
        Languages.ENGLISH: "Fear of things to the left or left-handed",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SIXFLAGSPHOBIA: {
        Languages.ENGLISH: "Fear of six flags",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SHIJIPHOBIA: {
        Languages.ENGLISH: "Fear of television sets, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SHOEBOXPHOBIA: {
        Languages.ENGLISH: "Fear of shoeboxes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SHWNPHOBIA: {
        Languages.ENGLISH: "Fear of food processors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SH☀GMOPHOBIA: {
        Languages.ENGLISH: "Fear of two-liter bottles",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SKATEBOARDPHOBIA: {
        Languages.ENGLISH: "Fear of skateboards",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SKOUPAPHOBIA: {
        Languages.ENGLISH: "Fear of brooms",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SNEROLAKOPHOBIA: {
        Languages.ENGLISH: "Fear of ponds",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SOLOIPHOBIA: {
        Languages.ENGLISH: "Fear of watches, branch of vestiphobia (fear of clothing)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SOTERIOPHOBIA: {
        Languages.ENGLISH: "Fear of dependence on others",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SPACESUITPHOBIA: {
        Languages.ENGLISH: "Fear of spacesuits",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SPASMENAGALIAPHOBIA: {
        Languages.ENGLISH: "Fear of broken glass (branch of nelophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SPEEDOMOPHOBIA: {
        Languages.ENGLISH: "Fear of speedometers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SPHYGMOMANOPHOBIA: {
        Languages.ENGLISH: "Fear of sphygmomanometers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SPIRTOPHOBIA: {
        Languages.ENGLISH: "Fear of matches",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SPRINKLERPHOBIA: {
        Languages.ENGLISH: "Fear of sprinklers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SRANDUOPHOBIA: {
        Languages.ENGLISH: "Fear of crockpots",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.STAUROPHOBIA: {
        Languages.ENGLISH: "Fear of crosses or the crucifix",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.STAVRODROMIPHOBIA: {
        Languages.ENGLISH: "Fear of crossroads",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.STENOPHOBIA: {
        Languages.ENGLISH: "Fear of narrow things or places",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.STETHOSCOPEPHOBIA: {
        Languages.ENGLISH: "Fear of stethoscopes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.STICKERPHOBIA: {
        Languages.ENGLISH: "Fear of stickers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.STOCKINGPHOBIA: {
        Languages.ENGLISH: "Fear of stockings",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.STOPSIGNPHOBIA: {
        Languages.ENGLISH: "Fear of stop signs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.STRANCAPHOBIA: {
        Languages.ENGLISH: "Fear of cold fire",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.STRANTOPHOBIA: {
        Languages.ENGLISH: "Fear of the stratosphere",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.STREETLIGHTPHOBIA: {
        Languages.ENGLISH: "Fear of streetlights",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.STROVOPHOBIA: {
        Languages.ENGLISH: "Fear of strobe lights",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.STYLOPHOBIA: {
        Languages.ENGLISH: "Fear of pens",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ST📹PROPHOBIA: {
        Languages.ENGLISH: "Fear of soda cans",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SUBMECHANOPHOBIA: {
        Languages.ENGLISH: "Fear of submerged man-made objects",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SURFBOARDPHOBIA: {
        Languages.ENGLISH: "Fear of surfboards",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SYMBOLOPHOBIA: {
        Languages.ENGLISH: "Fear of symbols and symbolism",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SYNDETIRAPHOBIA: {
        Languages.ENGLISH: "Fear of paperclips",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SYNTRIVANIPHOBIA: {
        Languages.ENGLISH: "Fear of fountains",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.SYSKEVIPHOBIA: {
        Languages.ENGLISH: "Fear of appliances, branch of panophobia (fear of everything)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.S🐦GMOPHOBIA: {
        Languages.ENGLISH: "Fear of toolboxes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TABULATOPHOBIA: {
        Languages.ENGLISH: "Fear of floors (branch of terramophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TAILLIGHTPHOBIA: {
        Languages.ENGLISH: "Fear of taillights",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.FDS_HFKDSHFKJHSDKJFHSDKJFHDSKJFHSKJFHSDKJPHOBIA: {
        Languages.ENGLISH: "Fear of typing",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TAIÞUPHOBIA: {
        Languages.ENGLISH: "Fear of sunroofs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TAMEIOPHOBIA: {
        Languages.ENGLISH: "Fear of store checkouts",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TAPETSARIAPHOBIA: {
        Languages.ENGLISH: "Fear of wallpaper",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TAPHOSPHOBIA: {
        Languages.ENGLISH: "Fear of the grave",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TECHNOPHOBIA: {
        Languages.ENGLISH: "Fear of technology",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TECTOPHOBIA: {
        Languages.ENGLISH: "Fear of roofs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TEGOPHOBIA: {
        Languages.ENGLISH: "Fear of rooftops",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TELEOPHOBIA: {
        Languages.ENGLISH: "Fear of definite plans",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TELEPHONOPHOBIA: {
        Languages.ENGLISH: "Fear of telephones, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TELESCOPOPHOBIA: {
        Languages.ENGLISH: "Fear of telescopes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TERRAMOPHOBIA: {
        Languages.ENGLISH: "Fear of the ground",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TERRORPHOBIA: {
        Languages.ENGLISH: "Fear of terrorism",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TEXTOPHOBIA: {
        Languages.ENGLISH: "Fear of certain fabrics",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.THAUMATOPHOBIA: {
        Languages.ENGLISH: "Fear of miracles",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.THEOLOGICOPHOBIA: {
        Languages.ENGLISH: "Fear of theology",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.THEOPHOBIA: {
        Languages.ENGLISH: "Fear of religion",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.THERMOMOPHOBIA: {
        Languages.ENGLISH: "Fear of thermometers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.THERMOSTATPHOBIA: {
        Languages.ENGLISH: "Fear of thermostats",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.THESAUROPHOBIA: {
        Languages.ENGLISH: "Fear of treasure chests",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TIGANIPHOBIA: {
        Languages.ENGLISH: "Fear of frying pans",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TILECHEIRISTIRIOPHOBIA: {
        Languages.ENGLISH: "Fear of remote controls",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TINGCHECHANGPHOBIA: {
        Languages.ENGLISH: "Fear of parking lots",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TINGCHECHEKUPHOBIA: {
        Languages.ENGLISH: "Fear of parking garages",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TLINGHUPHOBIA: {
        Languages.ENGLISH: "Fear of campfires",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TOASTERPHOBIA: {
        Languages.ENGLISH: "Fear of toasters, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TOICHOPHOBIA: {
        Languages.ENGLISH: "Fear of walls",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TOPOPHOBIA: {
        Languages.ENGLISH: "Fear of certain places or situations, such as stage fright",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TOUALETAPHOBIA: {
        Languages.ENGLISH: "Fear of toilets, branch of oikophobia (fear of home surroundings)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TOUVLOPHOBIA: {
        Languages.ENGLISH: "Fear of bricks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TRAGOUDIPHOBIA: {
        Languages.ENGLISH: "Fear of songs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TRAPEZAPHOBIA: {
        Languages.ENGLISH: "Fear of tables, branch of epiplaphobia (fear of furnitures)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TROKHOPHOBIA: {
        Languages.ENGLISH: "Fear of wheels",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TROMPETAPHOBIA: {
        Languages.ENGLISH: "Fear of trumpets, branch of gakkiphobia (fear of musical instruments)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TROPHOPHOBIA: {
        Languages.ENGLISH: "Fear of trophies",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TRƐDNOPHOBIA: {
        Languages.ENGLISH: "Fear of electric razors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TRYPANOPHOBIA: {
        Languages.ENGLISH: "Fear of needles (belonephobia) or injections (trypanophobia) (branch of aichmophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TRYPOPHOBIA: {
        Languages.ENGLISH: "Fear of holes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TR✈️GMOPHOBIA: {
        Languages.ENGLISH: "Fear of skylights",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TURRIPHOBIA: {
        Languages.ENGLISH: "Fear of towers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TYCHOPHOBIA: {
        Languages.ENGLISH: "Fear of randomness",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TYMPANOPHOBIA: {
        Languages.ENGLISH: "Fear of drums, branch of gakkiphobia (fear of musical instruments)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.TƜDROPHOBIA: {
        Languages.ENGLISH: "Fear of 3d movies",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.UMBRAPHOBIA: {
        Languages.ENGLISH: "Fear of shadows",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.UMBRELLAPHOBIA: {
        Languages.ENGLISH: "Fear of umbrellas",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VAGONIPHOBIA: {
        Languages.ENGLISH: "Fear of wagons",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VALANTIOPHOBIA: {
        Languages.ENGLISH: "Fear of wallets",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VALITSAPHOBIA: {
        Languages.ENGLISH: "Fear of suitcases",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VERKEINTRIPHOBIA: {
        Languages.ENGLISH: "Fear of traffic tickets",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VESTIPHOBIA: {
        Languages.ENGLISH: "Fear of clothing",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VIEMAPHOBIA: {
        Languages.ENGLISH: "Fear of drains",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VIDEOCASSETTOPHOBIA: {
        Languages.ENGLISH: "Fear of vhs tapes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VINITOPHOBIA: {
        Languages.ENGLISH: "Fear of dressers, branch of epiplaphobia (fear of furnitures)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VIOLIPHOBIA: {
        Languages.ENGLISH: "Fear of violins, branch of gakkiphobia (fear of musical instruments)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VOEDSEPHOBIA: {
        Languages.ENGLISH: "Fear of garbage disposals",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VOIDOPHOBIA: {
        Languages.ENGLISH: "Fear of the void",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VOLANPHOBIA: {
        Languages.ENGLISH: "Fear of steering wheels",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VORRAPHOBIA: {
        Languages.ENGLISH: "Fear of north",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VOTHROPHOBIA: {
        Languages.ENGLISH: "Fear of cesspool",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VOULISIPHOBIA: {
        Languages.ENGLISH: "Fear of the will to do things",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.VINYLOPHOBIA: {
        Languages.ENGLISH: "Fear of vinyl records",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.V🚫SHROPHOBIA: {
        Languages.ENGLISH: "Fear of wet floors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.WANJUWUPHOBIA: {
        Languages.ENGLISH: "Fear of dollhouses (branch of automatonophobia)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.WHEELCHAIRPHOBIA: {
        Languages.ENGLISH: "Fear of wheelchairs",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.WICCAPHOBIA: {
        Languages.ENGLISH: "Fear of witchcraft",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.WLANOPHOBIA: {
        Languages.ENGLISH: "Fear of candy machines",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.XAFNIASMAPHOBIA: {
        Languages.ENGLISH: "Fear of surprises",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.X!MZOPHOBIA: {
        Languages.ENGLISH: "Fear of heart monitors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.XINXIANGPHOBIA: {
        Languages.ENGLISH: "Fear of mailboxes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.XYLOPHONOPHOBIA: {
        Languages.ENGLISH: "Fear of xylophones, branch of gakkiphobia (fear of musical instruments)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.XYPNITIRIPHOBIA: {
        Languages.ENGLISH: "Fear of alarm clocks, branch of syskeviphobia (fear of appliances)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.XYROPHOBIA: {
        Languages.ENGLISH: "Fear of razors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.W@NOPHOBIA: {
        Languages.ENGLISH: "Fear of pressure washers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.YEDANSHUPHOBIA: {
        Languages.ENGLISH: "Fear of christmas trees",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.YEDENGPHOBIA: {
        Languages.ENGLISH: "Fear of nightlights",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.YGROPHOBIA: {
        Languages.ENGLISH: "Fear of liquid",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.YINJIPHOBIA: {
        Languages.ENGLISH: "Fear of radio receivers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.YINSHUIJIPHOBIA: {
        Languages.ENGLISH: "Fear of drinking fountains",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.YLOPHOBIA: {
        Languages.ENGLISH: "Fear of wood",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.YROUXPHOBIA: {
        Languages.ENGLISH: "Fear of gumball machines",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.YPNODOMATIOPHOBIA: {
        Languages.ENGLISH: "Fear of bedrooms",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.YUPENPHOBIA: {
        Languages.ENGLISH: "Fear of bathtubs, branch of oikophobia (fear of home surroundings)",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.YUSHIXISHOPHOBIA: {
        Languages.ENGLISH: "Fear of bathroom sinks",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.YUSHUAPHOBIA: {
        Languages.ENGLISH: "Fear of windshield wipers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.YWAOHUPHOBIA: {
        Languages.ENGLISH: "Fear of slot machines",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.Y∞GOMPHOBIA: {
        Languages.ENGLISH: "Fear of popcorn poppers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ZAPSAULPHOBIA: {
        Languages.ENGLISH: "Fear of gas pumps",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ZARIPHOBIA: {
        Languages.ENGLISH: "Fear of dice",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ZHAOQINPHOBIA: {
        Languages.ENGLISH: "Fear of store exit anti-theft alarms",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ZHINCHAPHOBIA: {
        Languages.ENGLISH: "Fear of walkthrough metal detectors",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ZHUOJPHOBIA: {
        Languages.ENGLISH: "Fear of desktop computers",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ZIDONGSHOPHOBIA: {
        Languages.ENGLISH: "Fear of vending machines",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ZIZANMEPHOBIA: {
        Languages.ENGLISH: "Fear of weed eaters",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ZLOQINGPHOBIA: {
        Languages.ENGLISH: "Fear of paintball guns",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.Z📷MROTPHOBIA: {
        Languages.ENGLISH: "Fear of old shoes",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ZONIASFALEIAPHOBIA: {
        Languages.ENGLISH: "Fear of seatbelts",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ZRAIDOPHOBIA: {
        Languages.ENGLISH: "Fear of table lamps",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ZUIGERPHOBIA: {
        Languages.ENGLISH: "Fear of vacuum cleaners",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ZWUQIPHOBIA: {
        Languages.ENGLISH: "Fear of squirt guns",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
    ThingsPhobiasDescriptions.ZYGARIAPHOBIA: {
        Languages.ENGLISH: "Fear of weighing scales",
        Languages.HEBREW: None,
        Languages.ARAB: None,
        Languages.ITALIAN: None, },
}
