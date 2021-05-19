from enum import Enum, auto
from typing import List, Optional


# TODO(joel): create phobias lists, with reference to duplications and parent phobias
#  gather their language dicts into a single one in language.py

class PlantPhobias(Enum):
    AGROSTOPHOBIA = auto()
    ANTHOPHOBIA = auto()
    BOTANOPHOBIA = auto()
    CITAROPHOBIA = auto()
    DENDROPHOBIA = auto()
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


class MicroorganismPhobias(Enum):
    ANOPHELIPHOBIA = auto()
    BACILLOPHOBIA = auto()
    BACTERIOPHOBIA = auto()
    CHOLEROPHOBIA = auto()
    EBOLAPHOBIA = auto()
    MICROBIOPHOBIA = auto()
    VERMINOPHOBIA = auto()
    VIROPHOBIA = auto()


class BodyPhobias(Enum):
Aftiphobia – fear of ears
Agkonaphobia – fear of elbows
Anatomophobia – is the fear of the human body
Antikheirphobia – fear of thumbs
Binastrophobia – fear of big brains
Bromidrosiphobia – fear of body odors (branch of osmophobia)
Cardiophobia – fear of the heart
Carpophobia – fear of wrists
Cartilogenophobia – fear of bones
Chaetophobia – fear of hair
Cheilophobia – fear of lips
Chirophobia – fear of hands
Coprophobia – fear of feces
Corporiphobia – fear of ones body
Cryohemophobia – fear of frozen blood
Dakruphobia – fear of tears
Dakulophobia – fear of fingers
Dermatophobia – fear of skin
Digitusphobia – fear of toes
Enkefalophobia – fear of brains
Eurotophobia – fear of female genitalia
Geniphobia – fear of chins
Genuphobia – fear of knees
Glossaphobia – fear of tongues
Gonatophobia – fear of knees
Halitophobia – fear of bad breath (branch of osmophobia)
Hidrophobia – fear of sweat
Kefaliphobia – fear of heads
Kolpophobia – fear of genitals
Kypselidaphobia – fear of earwax
Mammophobia – fear of mammary glands
Mytiphobia – fear of noses
Maschaliphobia – fear of underarms
Mastrophobia – fear of breasts
Nakusophobia – fear of boogers
Namizuphobia – fear of snot
Nefrophobia – fear of kidneys
Nevophobia – fear of moles on skin
Paruresis – fear of urinating in the presence of others
Pnevmonaphobia – fear of lungs
Odontophobia – fear of teeth
Ommetaphobia – fear of eyes
Omphalophobia – fear of belly buttons
Onuxophobia – fear of fingernails and toenails
Osmophobia – fear of odors
Parasitophobia – fear of parasites
Parthenophobia – fear of virgins
Phallophobia – fear of willies
Pharyphobia – fear of pharynx
Pnevmonaphobia – fear of lungs
Podophobia – fear of feet
Pogonophobia – fear of beards
Proctophobia – fear of rectums
Prosopophobia – fear of faces
Pugophobia – fear of buttocks
Queunliskanphobia – fear of saliva
Rhytiphobia – fear of wrinkles
Stomaphobia – fear of mouths
Sinistrophobia - fear of left handedness
Stomachphobia – fear of stomachs
Thelephobia - fear of nipples
Urophobia – fear of urine
Venephobia - fear of veins


class FearNames(Enum):
    """
    Fear names
    """
Acarophobia – fear of ticks and mites (Branch of Zoophobia)
Acinonyxphobia – fear of cheetahs (branch of zoophobia)
Aerozoophobia – fear of flying animals (branch of zoophobia)
Aetophobia – fear of eagles (branch of zoophobia and aerozoophobia)
Agerozoophobia –fear of farm animals (Branch of zoophobia and domestievzoophobia)
Agrizoophobia – fear of wild animals (Branch of zoophobia)
Ailurophobia – fear of cats (Branch of zoophobia)
Aligatoraphobia – fear of alligators (branch of zoophobia)
Alkiphobia – fear of moose (Branch of zoophobia)
Ankylosaurophobia – fear of Ankylosaurs (Branch of zoophobia)
Anopheliphobia – fear of Mosquitos (branch of zoophobia and aerozoophobia)
Arachnophobia – fear of spiders (Branch of zoophobia)
Arkoudaphobia – fear of bears (branch of zoophobia)
Astakophobia – fear of lobsters (branch of zoophobia)
Asteriaphobia – fear of starfish (Brnach of zoophobia)
Bakaliarophobia – fear of cod (branch of zoophobia)
Batrachophobia – fear of amphibians (branch of zoophobia)
Bettaphobia – fear of bettas (branch of zoophobia)
Bloodhoundphobia – fear of bloodhounds (branch of zoophobia)
Bluebirdphobia – fear of bluebirds (branch of zoophobia and aerozoophobia)
Bovinophobia – fear of cattle (branch of zoophoiba and agerozoohobia)
Brontosaurusphobia – fear of brontosauruses (branch of zoophobia)
Bufonophobia – fear of toads (branch of batrachophobia & zoophobia)
Bulldogphobia – fear of bulldogs (branch of zoophobia and cynophobia)
Caballiophobia – fear of ponies (branch of zoophobia and agerozoophobia)
Capraphobia – fear of goats (branch of zoophobia and agerozoophobia)
Chapodiphobia – fear of octopi (branch of zoophobia)
Chauliophobia – fear of viperfish (branch of zoophobia)
Cheliphobia – fear of eels (branch of zoophobia)
Chelonaphobia – fear of turtles (branch of herpetophobia & zoophobia)
Chihuahuaphobia – fear of chihuahuas (branch of zoophobia)
Chimpatsiphobia – fear of chimpanzees (branch of zoophobia)
Chinchillaphobia – fear of chinchillas (branch of zoophobia)
Chipmunkphobia – fear of chipmunks (branch of zoophobia)
Chiroptophobia – fear of bats (branch of zoophobia and aerozoophobia)
Chrysopsarophobia – fear of goldfish (branch of zoophobia)
Coccinellidaephobia – fear of ladybugs (branch of zoophobia)
Cockophobia – fear of chickens (branch of zoophobia and Agerozoophobia)
Coyotephobia – fear of coyotes (branch of zoophobia)
Crappiephobia – fear of crappies (branch of zoophobia)
Cynophobia – fear of dogs (branch of zoophobia)
Cyprinodon diabolisphobia – fear of devil holespupfish (branch of zoophobia)
Deinophobia – fear of dinosaurs (branch of zoophobia)
Delfiniphobia – fear of dolphins (branch of zoophobia)
Didelphiphobia – fear of opossums (branch of zoophobia)
Digkophobia – fear of dingoes (branch of cynophobia & zoophobia)
Dobermanphobia – fear of doberman pinschers (branch of zoophobia and cynophobia)
Dodophobia – fear of dodoes (branch of zoophobia)
Domestozoophobia – fear of domestic animals (branch of zoophobia)
Dragoferophobia – fear of dragonflies (branch of zoophobia)
Elafiphobia – fear of deer (branch of zoophobia)
Emuphobia – fear of emus (branch of zoophobia)
Entomophobia – fear of insects (branch of zoophobia and aerozoophobia)
Equinophobia – fear of horses (branch of zoophobia)
Falainaphobia – fear of whales (branch of zoophobia and agerozoophobia)
Fennecaphobia – fear of foxes (branch of zoophobia)
Fimsophobia – fear of gorillas (branch of zoophobia)
Flamingophobia – fear of flamingoes (branch of zoophobia and aerozoophobia)
Gaidouriphobia – fear of donkeys (branch of zoophobia and agerozoophobia)
Galeophobia – fear of sharks
Garidaphobia – fear of shrimp (branch of zoophobia)
Gatakiphobia – fear of kittens (branch of zoophobia)
Gibbonphobia – fear of gibbons (branch of zoophobia)
Goldenretrieverphobia – fear of Golden Retrievers (branch of cynophobia & zoophobia)
Hadrosaurphobia – fear of hadrosaurs (branch of zoophobia)
Hamsterphobia – fear of hamsters (branch of zoophobia)
Herpetophobia – fear of reptiles (branch of zoophobia)
Hippophobia – fear of horses (branch of zoophobia and agerozoophobia)
Hippopotamophobia – fear of hippopotamuses (branch of zoophobia)
Hominidphobia – fear of humans and great apes (hominids) (branch of zoophobia)
Hominoidphobia – fear of humans and apes (hominoids) (branch of zoophobia)
Iagouarophobia – fear of jaguars (branch of zoophobia)
Ichthyosaurphobia – fear of ichthyosaurs (branch of deinophobia & zoophobia)
Isopterophobia – fear of termites (branch of entomophobia & zoophobia)
Indikochoiridiophobia – fear of guinea pigs (branch of zoophobia)
Kagkourophobia – fear of kangaroos (branch of zoophobia)
Kamilaphobia – fear of camels (branch of zoophobia)
Kamilopardaliphobia – fear of giraffes (branch of zoophobia)
Kanariniphobia – fear of canaries (branch of zoophobia and aerozoophobia)
Kanmengphobia – fear of guard dogs (branch of zoophobia)
Kastoraphobia – fear of beavers (branch of zoophobia)
Katsaridaphobia – fear of cockroaches (branch of entomophobia & zoophobia)
Kavouriphobia – fear of crabs (branch of zoophobia)
Khenphobia – fear of geese (branch of zoophobia and aerozoophobia)
Kogiotphobia – fear of coyotes (branch of zoophobia)
Kolimpriphobia – fear of hummingbirds (branch of zoophobia and aerozoophobia)
Kotsyfiphobia – fear of blackbirds (branch of zoophobia and aerozoophobia)
Krokodeilophobia – fear of crocodiles (branch of zoophobia)
Kyknophobia – fear of swans (branch of zoophobia and aerozoophobia)
Lemurphobia – fear of lemurs (branch of zoophobia)
Lepidopterophobia – fear of butterflies (branch of zoophobia and aerozoophobia)
Lepidoptophobia – fear of flying insects (branch of aerozoophobia & zoophobia)
Leopardaliphobia – fear of leopards (branch of zoophobia)
Leophobia, Liontariphobia – fear of lions (branch of zoophobia)
Llamaphobia – fear of llamas (branch of zoophobia)
Lupophobia – fear of wolves (branch of agrizoophobia & zoophobia)
Lutraphobia – fear of otters (branch of zoophobia)
Mammothphobia – fear of mammoths (branch of zoophobia)
Mavrogatphobia – fear of black cats (branch of felinophobia & zoophobia)
Medousaphobia – fear of jellyfish (branch of zoophobia)
Mefitidaphobia – fear of skunks (branch of zoophobia)
Mahidolamistakophobia – fear of mahi mahi (branch of zoophobia)
Melissaphobia – fear of bees (branch of entomophobia & zoophobia and aerozoophobia)
Mephitophobia – fear of skunks (again, branch of zoophobia)
Metazoibphobia – fear of humans and animals (metazoibs) (branch of zoophobia)
Agrostophobia – fear of grass (branch of boranophobia)
Anthophobia – fear of flowers (branch of botanophobia)
Botanophobia – fear of plants (branch of pantophobia)
Citarophobia – fear of citrus (branch of botanophobia)
Dendrophobia – fear of trees (branch of Botanophobia)
Distlephobia – fear of thistles (branch of botanopgobia)
Dogwoodphobia - fear of dogwood trees (branch of dendrophobia)
Drusophobia - fear of oak trees (branch of dendrophobia)
Grasartophobia – fear of tumbleweeds (branch of botanophobia)
Kactosophobia - fear of cacti (branch of botanophobia)
Pefkophobia - fear of pine trees (branch of dendrophobia)
Phyllophobia – fear of leaves (branch of botanophobia)
Mapleleafaphobia - fear of maple leaves (branch of Phyllophobia)
Pteridophobia – fear of ferns (branch of botanophobia)
Viriditaphobia - fear of weeds (branch of botanophobia)
Anopheliphobia – fear of malaria (branch of micobiophobia)
bacillophobia – fear of bacillus (branch of microbiophobia)
Bacteriophobia – fear of bacteria (branch of microbiophobia)
Cholerophobia – fear of Vibreo cholerae (the bacteria that causes cholera) (branch of microbiophobia)
EbolaPhobia – fear of the Ebola Virus (branch of virophobia)
Microbiophobia – fear of micro-organisms (branch of pantophobia)
Verminophobia – fear of germs (branch of microbiophobia)
Virophobia – fear of viruses (not the ones on computers) (branch of microbiophobia)
Aftiphobia – fear of ears
Agkonaphobia – fear of elbows
Anatomophobia – is the fear of the human body
Antikheirphobia – fear of thumbs
Binastrophobia – fear of big brains
Bromidrosiphobia – fear of body odors (branch of osmophobia)
Cardiophobia – fear of the heart
Carpophobia – fear of wrists
Cartilogenophobia – fear of bones
Chaetophobia – fear of hair
Cheilophobia – fear of lips
Chirophobia – fear of hands
Coprophobia – fear of feces
Corporiphobia – fear of ones body
Cryohemophobia – fear of frozen blood
Dakruphobia – fear of tears
Dakulophobia – fear of fingers
Dermatophobia – fear of skin
Digitusphobia – fear of toes
Enkefalophobia – fear of brains
Eurotophobia – fear of female genitalia
Geniphobia – fear of chins
Genuphobia – fear of knees
Glossaphobia – fear of tongues
Gonatophobia – fear of knees
Halitophobia – fear of bad breath (branch of osmophobia)
Hidrophobia – fear of sweat
Kefaliphobia – fear of heads
Kolpophobia – fear of genitals
Kypselidaphobia – fear of earwax
Mammophobia – fear of mammary glands
Mytiphobia – fear of noses
Maschaliphobia – fear of underarms
Mastrophobia – fear of breasts
Nakusophobia – fear of boogers
Namizuphobia – fear of snot
Nefrophobia – fear of kidneys
Nevophobia – fear of moles on skin
Paruresis – fear of urinating in the presence of others
Pnevmonaphobia – fear of lungs
Odontophobia – fear of teeth
Ommetaphobia – fear of eyes
Omphalophobia – fear of belly buttons
Onuxophobia – fear of fingernails and toenails
Osmophobia – fear of odors
Parasitophobia – fear of parasites
Parthenophobia – fear of virgins
Phallophobia – fear of willies
Pharyphobia – fear of pharynx
Pnevmonaphobia – fear of lungs
Podophobia – fear of feet
Pogonophobia – fear of beards
Proctophobia – fear of rectums
Prosopophobia – fear of faces
Pugophobia – fear of buttocks
Queunliskanphobia – fear of saliva
Rhytiphobia – fear of wrinkles
Stomaphobia – fear of mouths
Sinistrophobia - fear of left handedness
Stomachphobia – fear of stomachs
Thelephobia - fear of nipples
Urophobia – fear of urine
Venephobia - fear of veins











class FearNames2(Enum):
    """
    Fear names
    """
    ACHLUOPHOBIA = "ACHLUOPHOBIA_NAME"
    ACROPHOBIA = "ACROPHOBIA_NAME"
    AEROPHOBIA = "AEROPHOBIA_NAME"
    ALGOPHOBIA = "ALGOPHOBIA_NAME"
    AGORAPHOBIA = "AGORAPHOBIA_NAME"
    AICHMOPHOBIA = "AICHMOPHOBIA_NAME"
    AMAXOPHOBIA = "AMAXOPHOBIA_NAME"
    ANDROPHOBIA = "ANDROPHOBIA_NAME"
    ANGINOPHOBIA = "ANGINOPHOBIA_NAME"
    ANTHROPHOBIA = "ANTHROPHOBIA_NAME"
    ANTHROPOPHOBIA = "ANTHROPOPHOBIA_NAME"
    APHENPHOSMPHOBIA = "APHENPHOSMPHOBIA_NAME"
    ARACHIBUTYROPHOBIA = "ARACHIBUTYROPHOBIA_NAME"
    ARACHNOPHOBIA = "ARACHNOPHOBIA_NAME"
    ARITHMOPHOBIA = "ARITHMOPHOBIA_NAME"
    ASTRAPHOBIA = "ASTRAPHOBIA_NAME"
    ATAXOPHOBIA = "ATAXOPHOBIA_NAME"
    ATELOPHOBIA = "ATELOPHOBIA_NAME"
    ATYCHIPHOBIA = "ATYCHIPHOBIA_NAME"
    AUTOMATONOPHOBIA = "AUTOMATONOPHOBIA_NAME"
    AUTOMYSOPHOBIA = "AUTOMYSOPHOBIA_NAME"
    AUTOPHOBIA = "AUTOPHOBIA_NAME"
    BACTERIOPHOBIA = "BACTERIOPHOBIA_NAME"
    BAROPHOBIA = "BAROPHOBIA_NAME"
    BATHMOPHOBIA = "BATHMOPHOBIA_NAME"
    BATRACHOPHOBIA = "BATRACHOPHOBIA_NAME"
    BELONEPHOBIA = "BELONEPHOBIA_NAME"
    BIBLIOPHOBIA = "BIBLIOPHOBIA_NAME"
    BOTANOPHOBIA = "BOTANOPHOBIA_NAME"
    CACOPHOBIA = "CACOPHOBIA_NAME"
    CATAGELOPHOBIA = "CATAGELOPHOBIA_NAME"
    CATOPTROPHOBIA = "CATOPTROPHOBIA_NAME"
    CHIONOPHOBIA = "CHIONOPHOBIA_NAME"
    CHROMOPHOBIA = "CHROMOPHOBIA_NAME"
    CHRONOMENTROPHOBIA = "CHRONOMENTROPHOBIA_NAME"
    CHRONOPHOBIA = "CHRONOPHOBIA_NAME"
    CLAUSTROPHOBIA = "CLAUSTROPHOBIA_NAME"
    COULROPHOBIA = "COULROPHOBIA_NAME"
    CYBERPHOBIA = "CYBERPHOBIA_NAME"
    CYNOPHOBIA = "CYNOPHOBIA_NAME"
    DENDROPHOBIA = "DENDROPHOBIA_NAME"
    DENTOPHOBIA = "DENTOPHOBIA_NAME"
    DOMATOPHOBIA = "DOMATOPHOBIA_NAME"
    DYSTYCHIPHOBIA = "DYSTYCHIPHOBIA_NAME"
    ECOPHOBIA = "ECOPHOBIA_NAME"
    ELUROPHOBIA = "ELUROPHOBIA_NAME"
    ENTOMOPHOBIA = "ENTOMOPHOBIA_NAME"
    EPHEBIPHOBIA = "EPHEBIPHOBIA_NAME"
    EQUINOPHOBIA = "EQUINOPHOBIA_NAME"
    GAMOPHOBIA = "GAMOPHOBIA_NAME"
    GENUPHOBIA = "GENUPHOBIA_NAME"
    GLOSSOPHOBIA = "GLOSSOPHOBIA_NAME"
    GYNOPHOBIA = "GYNOPHOBIA_NAME"
    HAPHEPHOBIA = "HAPHEPHOBIA_NAME"
    HELIOPHOBIA = "HELIOPHOBIA_NAME"
    HEMOPHOBIA = "HEMOPHOBIA_NAME"
    HERPETOPHOBIA = "HERPETOPHOBIA_NAME"
    HIPPOPOTOMONSTROSESQUIPEDALIOPHOBIA = "HIPPOPOTOMONSTROSESQUIPEDALIOPHOBIA_NAME"
    HYDROPHOBIA = "HYDROPHOBIA_NAME"
    HYPOCHONDRIA = "HYPOCHONDRIA_NAME"
    IATROPHOBIA = "IATROPHOBIA_NAME"
    INSECTOPHOBIA = "INSECTOPHOBIA_NAME"
    KOINONIPHOBIA = "KOINONIPHOBIA_NAME"
    KOUMPOUNOPHOBIA = "KOUMPOUNOPHOBIA_NAME"
    LEUKOPHOBIA = "LEUKOPHOBIA_NAME"
    LILAPSOPHOBIA = "LILAPSOPHOBIA_NAME"
    LOCKIOPHOBIA = "LOCKIOPHOBIA_NAME"
    MAGEIROCOPHOBIA = "MAGEIROCOPHOBIA_NAME"
    MEGALOPHOBIA = "MEGALOPHOBIA_NAME"
    MENOPHOBIA = "MENOPHOBIA_NAME"
    MELANOPHOBIA = "MELANOPHOBIA_NAME"
    MICROPHOBIA = "MICROPHOBIA_NAME"
    MYSOPHOBIA = "MYSOPHOBIA_NAME"
    NECROPHOBIA = "NECROPHOBIA_NAME"
    NOCTIPHOBIA = "NOCTIPHOBIA_NAME"
    NOSOCOMEPHOBIA = "NOSOCOMEPHOBIA_NAME"
    NYCTOPHOBIA = "NYCTOPHOBIA_NAME"
    OBESOPHOBIA = "OBESOPHOBIA_NAME"
    OCTOPHOBIA = "OCTOPHOBIA_NAME"
    OMBROPHOBIA = "OMBROPHOBIA_NAME"
    OMPHALOPHOBIA = "OMPHALOPHOBIA_NAME"
    OPHIDIOPHOBIA = "OPHIDIOPHOBIA_NAME"
    ORNITHOPHOBIA = "ORNITHOPHOBIA_NAME"
    PAPYROPHOBIA = "PAPYROPHOBIA_NAME"
    PARAPHOBIA = "PARAPHOBIA_NAME"
    PARTHENOPHOBIA = "PARTHENOPHOBIA_NAME"
    PARURESIS = "PARURESIS_NAME"
    PATHOPHOBIA = "PATHOPHOBIA_NAME"
    PEDOPHOBIA = "PEDOPHOBIA_NAME"
    PHILEMATOPHOBIA = "PHILEMATOPHOBIA_NAME"
    PHILOPHOBIA = "PHILOPHOBIA_NAME"
    PHOBOPHOBIA = "PHOBOPHOBIA_NAME"
    PODOPHOBIA = "PODOPHOBIA_NAME"
    PORPHYROPHOBIA = "PORPHYROPHOBIA_NAME"
    PTERIDOPHOBIA = "PTERIDOPHOBIA_NAME"
    PTEROMERHANOPHOBIA = "PTEROMERHANOPHOBIA_NAME"
    PUEROPHOBIA = "PUEROPHOBIA_NAME"
    PYROPHOBIA = "PYROPHOBIA_NAME"
    SAMHAINOPHOBIA = "SAMHAINOPHOBIA_NAME"
    SCOLIONOPHOBIA = "SCOLIONOPHOBIA_NAME"
    SCOPTOPHOBIA = "SCOPTOPHOBIA_NAME"
    SCYPHOPHOBIA = "SCYPHOPHOBIA_NAME"
    SELENOPHOBIA = "SELENOPHOBIA_NAME"
    SOCIOPHOBIA = "SOCIOPHOBIA_NAME"
    SOMNIPHOBIA = "SOMNIPHOBIA_NAME"
    TACHOPHOBIA = "TACHOPHOBIA_NAME"
    TECHNOPHOBIA = "TECHNOPHOBIA_NAME"
    TONITROPHOBIA = "TONITROPHOBIA_NAME"
    TRYPANOPHOBIA = "TRYPANOPHOBIA_NAME"
    TRYPOPHOBIA = "TRYPOPHOBIA_NAME"
    VENUSTRAPHOBIA = "VENUSTRAPHOBIA_NAME"
    VERMINOPHOBIA = "VERMINOPHOBIA_NAME"
    WICCAPHOBIA = "WICCAPHOBIA_NAME"
    XENOPHOBIA = "XENOPHOBIA_NAME"
    ZOOPHOBIA = "ZOOPHOBIA_NAME"


class FearDescriptions(Enum):
    """
    Fear descriptions
    """
    ACHLUOPHOBIA = "ACHLUOPHOBIA_DESC"
    ACROPHOBIA = "ACROPHOBIA_DESC"
    AEROPHOBIA = "AEROPHOBIA_DESC"
    ALGOPHOBIA = "ALGOPHOBIA_DESC"
    AGORAPHOBIA = "AGORAPHOBIA_DESC"
    AICHMOPHOBIA = "AICHMOPHOBIA_DESC"
    AMAXOPHOBIA = "AMAXOPHOBIA_DESC"
    ANDROPHOBIA = "ANDROPHOBIA_DESC"
    ANGINOPHOBIA = "ANGINOPHOBIA_DESC"
    ANTHROPHOBIA = "ANTHROPHOBIA_DESC"
    ANTHROPOPHOBIA = "ANTHROPOPHOBIA_DESC"
    APHENPHOSMPHOBIA = "APHENPHOSMPHOBIA_DESC"
    ARACHIBUTYROPHOBIA = "ARACHIBUTYROPHOBIA_DESC"
    ARACHNOPHOBIA = "ARACHNOPHOBIA_DESC"
    ARITHMOPHOBIA = "ARITHMOPHOBIA_DESC"
    ASTRAPHOBIA = "ASTRAPHOBIA_DESC"
    ATAXOPHOBIA = "ATAXOPHOBIA_DESC"
    ATELOPHOBIA = "ATELOPHOBIA_DESC"
    ATYCHIPHOBIA = "ATYCHIPHOBIA_DESC"
    AUTOMATONOPHOBIA = "AUTOMATONOPHOBIA_DESC"
    AUTOMYSOPHOBIA = "AUTOMYSOPHOBIA_DESC"
    AUTOPHOBIA = "AUTOPHOBIA_DESC"
    BACTERIOPHOBIA = "BACTERIOPHOBIA_DESC"
    BAROPHOBIA = "BAROPHOBIA_DESC"
    BATHMOPHOBIA = "BATHMOPHOBIA_DESC"
    BATRACHOPHOBIA = "BATRACHOPHOBIA_DESC"
    BELONEPHOBIA = "BELONEPHOBIA_DESC"
    BIBLIOPHOBIA = "BIBLIOPHOBIA_DESC"
    BOTANOPHOBIA = "BOTANOPHOBIA_DESC"
    CACOPHOBIA = "CACOPHOBIA_DESC"
    CATAGELOPHOBIA = "CATAGELOPHOBIA_DESC"
    CATOPTROPHOBIA = "CATOPTROPHOBIA_DESC"
    CHIONOPHOBIA = "CHIONOPHOBIA_DESC"
    CHROMOPHOBIA = "CHROMOPHOBIA_DESC"
    CHRONOMENTROPHOBIA = "CHRONOMENTROPHOBIA_DESC"
    CHRONOPHOBIA = "CHRONOPHOBIA_DESC"
    CLAUSTROPHOBIA = "CLAUSTROPHOBIA_DESC"
    COULROPHOBIA = "COULROPHOBIA_DESC"
    CYBERPHOBIA = "CYBERPHOBIA_DESC"
    CYNOPHOBIA = "CYNOPHOBIA_DESC"
    DENDROPHOBIA = "DENDROPHOBIA_DESC"
    DENTOPHOBIA = "DENTOPHOBIA_DESC"
    DOMATOPHOBIA = "DOMATOPHOBIA_DESC"
    DYSTYCHIPHOBIA = "DYSTYCHIPHOBIA_DESC"
    ECOPHOBIA = "ECOPHOBIA_DESC"
    ELUROPHOBIA = "ELUROPHOBIA_DESC"
    ENTOMOPHOBIA = "ENTOMOPHOBIA_DESC"
    EPHEBIPHOBIA = "EPHEBIPHOBIA_DESC"
    EQUINOPHOBIA = "EQUINOPHOBIA_DESC"
    GAMOPHOBIA = "GAMOPHOBIA_DESC"
    GENUPHOBIA = "GENUPHOBIA_DESC"
    GLOSSOPHOBIA = "GLOSSOPHOBIA_DESC"
    GYNOPHOBIA = "GYNOPHOBIA_DESC"
    HAPHEPHOBIA = "HAPHEPHOBIA_DESC"
    HELIOPHOBIA = "HELIOPHOBIA_DESC"
    HEMOPHOBIA = "HEMOPHOBIA_DESC"
    HERPETOPHOBIA = "HERPETOPHOBIA_DESC"
    HIPPOPOTOMONSTROSESQUIPEDALIOPHOBIA = "HIPPOPOTOMONSTROSESQUIPEDALIOPHOBIA_DESC"
    HYDROPHOBIA = "HYDROPHOBIA_DESC"
    HYPOCHONDRIA = "HYPOCHONDRIA_DESC"
    IATROPHOBIA = "IATROPHOBIA_DESC"
    INSECTOPHOBIA = "INSECTOPHOBIA_DESC"
    KOINONIPHOBIA = "KOINONIPHOBIA_DESC"
    KOUMPOUNOPHOBIA = "KOUMPOUNOPHOBIA_DESC"
    LEUKOPHOBIA = "LEUKOPHOBIA_DESC"
    LILAPSOPHOBIA = "LILAPSOPHOBIA_DESC"
    LOCKIOPHOBIA = "LOCKIOPHOBIA_DESC"
    MAGEIROCOPHOBIA = "MAGEIROCOPHOBIA_DESC"
    MEGALOPHOBIA = "MEGALOPHOBIA_DESC"
    MENOPHOBIA = "MENOPHOBIA_DESC"
    MELANOPHOBIA = "MELANOPHOBIA_DESC"
    MICROPHOBIA = "MICROPHOBIA_DESC"
    MYSOPHOBIA = "MYSOPHOBIA_DESC"
    NECROPHOBIA = "NECROPHOBIA_DESC"
    NOCTIPHOBIA = "NOCTIPHOBIA_DESC"
    NOSOCOMEPHOBIA = "NOSOCOMEPHOBIA_DESC"
    NYCTOPHOBIA = "NYCTOPHOBIA_DESC"
    OBESOPHOBIA = "OBESOPHOBIA_DESC"
    OCTOPHOBIA = "OCTOPHOBIA_DESC"
    OMBROPHOBIA = "OMBROPHOBIA_DESC"
    OMPHALOPHOBIA = "OMPHALOPHOBIA_DESC"
    OPHIDIOPHOBIA = "OPHIDIOPHOBIA_DESC"
    ORNITHOPHOBIA = "ORNITHOPHOBIA_DESC"
    PAPYROPHOBIA = "PAPYROPHOBIA_DESC"
    PARAPHOBIA = "PARAPHOBIA_DESC"
    PARTHENOPHOBIA = "PARTHENOPHOBIA_DESC"
    PARURESIS = "PARURESIS_DESC"
    PATHOPHOBIA = "PATHOPHOBIA_DESC"
    PEDOPHOBIA = "PEDOPHOBIA_DESC"
    PHILEMATOPHOBIA = "PHILEMATOPHOBIA_DESC"
    PHILOPHOBIA = "PHILOPHOBIA_DESC"
    PHOBOPHOBIA = "PHOBOPHOBIA_DESC"
    PODOPHOBIA = "PODOPHOBIA_DESC"
    PORPHYROPHOBIA = "PORPHYROPHOBIA_DESC"
    PTERIDOPHOBIA = "PTERIDOPHOBIA_DESC"
    PTEROMERHANOPHOBIA = "PTEROMERHANOPHOBIA_DESC"
    PUEROPHOBIA = "PUEROPHOBIA_DESC"
    PYROPHOBIA = "PYROPHOBIA_DESC"
    SAMHAINOPHOBIA = "SAMHAINOPHOBIA_DESC"
    SCOLIONOPHOBIA = "SCOLIONOPHOBIA_DESC"
    SCOPTOPHOBIA = "SCOPTOPHOBIA_DESC"
    SCYPHOPHOBIA = "SCYPHOPHOBIA_DESC"
    SELENOPHOBIA = "SELENOPHOBIA_DESC"
    SOCIOPHOBIA = "SOCIOPHOBIA_DESC"
    SOMNIPHOBIA = "SOMNIPHOBIA_DESC"
    TACHOPHOBIA = "TACHOPHOBIA_DESC"
    TECHNOPHOBIA = "TECHNOPHOBIA_DESC"
    TONITROPHOBIA = "TONITROPHOBIA_DESC"
    TRYPANOPHOBIA = "TRYPANOPHOBIA_DESC"
    TRYPOPHOBIA = "TRYPOPHOBIA_DESC"
    VENUSTRAPHOBIA = "VENUSTRAPHOBIA_DESC"
    VERMINOPHOBIA = "VERMINOPHOBIA_DESC"
    WICCAPHOBIA = "WICCAPHOBIA_DESC"
    XENOPHOBIA = "XENOPHOBIA_DESC"
    ZOOPHOBIA = "ZOOPHOBIA_DESC"


class FearTypes(Enum):
    """
    Fear types
    """
    PEOPLE_RELATED_TO_TRAUMA_AND_PUNISHMENT = "PEOPLE_RELATED_TO_TRAUMA_AND_PUNISHMENT"
    PAST_LIFE_TRAUMA = "PAST_LIFE_TRAUMA"
    INNOCENT_STIMULUS = "INNOCENT_STIMULUS"
    LOWER_SPIRITUAL_WORLD = "LOWER_SPIRITUAL_WORLD"
    SPIRITUAL_WORLD = "SPIRITUAL_WORLD"
    OBSESSION_AND_POSSESSION = "OBSESSION_AND_POSSESSION"
    LACK_OF_ENERGY = "LACK_OF_ENERGY"
    ABANDONMENT = "ABANDONMENT"
    SEPARATION_AND_LOVE = "SEPARATION_AND_LOVE"
    BODILY_HURT_AND_DISEASE = "BODILY_HURT_AND_DISEASE"
    DISEASE = "DISEASE"
    SEXUAL_ABUSE_AND_TRAUMA = "SEXUAL_ABUSE_AND_TRAUMA"
    GENITAL_SECRETION = "GENITAL_SECRETION"


class Fear(object):
    """A type of fear
    """

    def __init__(self, name_enum: FearNames, desc_enum: FearDescriptions,
                 type_enum: FearTypes) -> None:
        """
        Initialize
        :param name_enum: The name enum
        :param desc_enum: The description enum
        :param type_enum: The type enum
        :return: Nothing
        """
        self.name_enum: FearNames = name_enum
        self.desc_enum: FearDescriptions = desc_enum
        self.type_enum: FearTypes = type_enum

    def __eq__(self, other: 'Fear') -> bool:
        """
        :param other: Another instance
        :return: True if we are equal to other, else False
        """
        return self.name_enum == other.name_enum


# TODO(joel): add all of the types and phobias that are in the hebrew list but not here
FEARS: List[Fear] = [
    Fear(name_enum=FearNames.ACHLUOPHOBIA,
         desc_enum=FearDescriptions.ACHLUOPHOBIA),
    Fear(name_enum=FearNames.ACROPHOBIA,
         desc_enum=FearDescriptions.ACROPHOBIA),
    Fear(name_enum=FearNames.AEROPHOBIA,
         desc_enum=FearDescriptions.AEROPHOBIA),
    Fear(name_enum=FearNames.ALGOPHOBIA,
         desc_enum=FearDescriptions.ALGOPHOBIA),
    Fear(name_enum=FearNames.AGORAPHOBIA,
         desc_enum=FearDescriptions.AGORAPHOBIA),
    Fear(name_enum=FearNames.AICHMOPHOBIA,
         desc_enum=FearDescriptions.AICHMOPHOBIA),
    Fear(name_enum=FearNames.AMAXOPHOBIA,
         desc_enum=FearDescriptions.AMAXOPHOBIA),
    Fear(name_enum=FearNames.ANDROPHOBIA,
         desc_enum=FearDescriptions.ANDROPHOBIA),
    Fear(name_enum=FearNames.ANGINOPHOBIA,
         desc_enum=FearDescriptions.ANGINOPHOBIA),
    Fear(name_enum=FearNames.ANTHROPHOBIA,
         desc_enum=FearDescriptions.ANTHROPHOBIA),
    Fear(name_enum=FearNames.ANTHROPOPHOBIA,
         desc_enum=FearDescriptions.ANTHROPOPHOBIA),
    Fear(name_enum=FearNames.APHENPHOSMPHOBIA,
         desc_enum=FearDescriptions.APHENPHOSMPHOBIA),
    Fear(name_enum=FearNames.ARACHIBUTYROPHOBIA,
         desc_enum=FearDescriptions.ARACHIBUTYROPHOBIA),
    Fear(name_enum=FearNames.ARACHNOPHOBIA,
         desc_enum=FearDescriptions.ARACHNOPHOBIA),
    Fear(name_enum=FearNames.ARITHMOPHOBIA,
         desc_enum=FearDescriptions.ARITHMOPHOBIA),
    Fear(name_enum=FearNames.ASTRAPHOBIA,
         desc_enum=FearDescriptions.ASTRAPHOBIA),
    Fear(name_enum=FearNames.ATAXOPHOBIA,
         desc_enum=FearDescriptions.ATAXOPHOBIA),
    Fear(name_enum=FearNames.ATELOPHOBIA,
         desc_enum=FearDescriptions.ATELOPHOBIA),
    Fear(name_enum=FearNames.ATYCHIPHOBIA,
         desc_enum=FearDescriptions.ATYCHIPHOBIA),
    Fear(name_enum=FearNames.AUTOMATONOPHOBIA,
         desc_enum=FearDescriptions.AUTOMATONOPHOBIA),
    Fear(name_enum=FearNames.AUTOMYSOPHOBIA,
         desc_enum=FearDescriptions.AUTOMYSOPHOBIA,
         type_enum=FearTypes.GENITAL_SECRETION),
    Fear(name_enum=FearNames.AUTOPHOBIA,
         desc_enum=FearDescriptions.AUTOPHOBIA),
    Fear(name_enum=FearNames.BACTERIOPHOBIA,
         desc_enum=FearDescriptions.BACTERIOPHOBIA),
    Fear(name_enum=FearNames.BAROPHOBIA,
         desc_enum=FearDescriptions.BAROPHOBIA),
    Fear(name_enum=FearNames.BATHMOPHOBIA,
         desc_enum=FearDescriptions.BATHMOPHOBIA),
    Fear(name_enum=FearNames.BATRACHOPHOBIA,
         desc_enum=FearDescriptions.BATRACHOPHOBIA),
    Fear(name_enum=FearNames.BELONEPHOBIA,
         desc_enum=FearDescriptions.BELONEPHOBIA),
    Fear(name_enum=FearNames.BIBLIOPHOBIA,
         desc_enum=FearDescriptions.BIBLIOPHOBIA),
    Fear(name_enum=FearNames.BOTANOPHOBIA,
         desc_enum=FearDescriptions.BOTANOPHOBIA),
    Fear(name_enum=FearNames.CACOPHOBIA,
         desc_enum=FearDescriptions.CACOPHOBIA,
         type_enum=FearTypes.GENITAL_SECRETION),
    Fear(name_enum=FearNames.CATAGELOPHOBIA,
         desc_enum=FearDescriptions.CATAGELOPHOBIA),
    Fear(name_enum=FearNames.CATOPTROPHOBIA,
         desc_enum=FearDescriptions.CATOPTROPHOBIA),
    Fear(name_enum=FearNames.CHIONOPHOBIA,
         desc_enum=FearDescriptions.CHIONOPHOBIA),
    Fear(name_enum=FearNames.CHROMOPHOBIA,
         desc_enum=FearDescriptions.CHROMOPHOBIA),
    Fear(name_enum=FearNames.CHRONOMENTROPHOBIA,
         desc_enum=FearDescriptions.CHRONOMENTROPHOBIA),
    Fear(name_enum=FearNames.CHRONOPHOBIA,
         desc_enum=FearDescriptions.CHRONOPHOBIA),
    Fear(name_enum=FearNames.CLAUSTROPHOBIA,
         desc_enum=FearDescriptions.CLAUSTROPHOBIA),
    Fear(name_enum=FearNames.COULROPHOBIA,
         desc_enum=FearDescriptions.COULROPHOBIA),
    Fear(name_enum=FearNames.CYBERPHOBIA,
         desc_enum=FearDescriptions.CYBERPHOBIA),
    Fear(name_enum=FearNames.CYNOPHOBIA,
         desc_enum=FearDescriptions.CYNOPHOBIA),
    Fear(name_enum=FearNames.DENDROPHOBIA,
         desc_enum=FearDescriptions.DENDROPHOBIA),
    Fear(name_enum=FearNames.DENTOPHOBIA,
         desc_enum=FearDescriptions.DENTOPHOBIA),
    Fear(name_enum=FearNames.DOMATOPHOBIA,
         desc_enum=FearDescriptions.DOMATOPHOBIA),
    Fear(name_enum=FearNames.DYSTYCHIPHOBIA,
         desc_enum=FearDescriptions.DYSTYCHIPHOBIA),
    Fear(name_enum=FearNames.ECOPHOBIA,
         desc_enum=FearDescriptions.ECOPHOBIA),
    Fear(name_enum=FearNames.ELUROPHOBIA,
         desc_enum=FearDescriptions.ELUROPHOBIA),
    Fear(name_enum=FearNames.ENTOMOPHOBIA,
         desc_enum=FearDescriptions.ENTOMOPHOBIA),
    Fear(name_enum=FearNames.EPHEBIPHOBIA,
         desc_enum=FearDescriptions.EPHEBIPHOBIA),
    Fear(name_enum=FearNames.EQUINOPHOBIA,
         desc_enum=FearDescriptions.EQUINOPHOBIA),
    Fear(name_enum=FearNames.GAMOPHOBIA,
         desc_enum=FearDescriptions.GAMOPHOBIA),
    Fear(name_enum=FearNames.GENUPHOBIA,
         desc_enum=FearDescriptions.GENUPHOBIA),
    Fear(name_enum=FearNames.GLOSSOPHOBIA,
         desc_enum=FearDescriptions.GLOSSOPHOBIA),
    Fear(name_enum=FearNames.GYNOPHOBIA,
         desc_enum=FearDescriptions.GYNOPHOBIA),
    Fear(name_enum=FearNames.HAPHEPHOBIA,
         desc_enum=FearDescriptions.HAPHEPHOBIA),
    Fear(name_enum=FearNames.HELIOPHOBIA,
         desc_enum=FearDescriptions.HELIOPHOBIA),
    Fear(name_enum=FearNames.HEMOPHOBIA,
         desc_enum=FearDescriptions.HEMOPHOBIA),
    Fear(name_enum=FearNames.HERPETOPHOBIA,
         desc_enum=FearDescriptions.HERPETOPHOBIA),
    Fear(name_enum=FearNames.HIPPOPOTOMONSTROSESQUIPEDALIOPHOBIA,
         desc_enum=FearDescriptions.HIPPOPOTOMONSTROSESQUIPEDALIOPHOBIA),
    Fear(name_enum=FearNames.HYDROPHOBIA,
         desc_enum=FearDescriptions.HYDROPHOBIA),
    Fear(name_enum=FearNames.HYPOCHONDRIA,
         desc_enum=FearDescriptions.HYPOCHONDRIA),
    Fear(name_enum=FearNames.IATROPHOBIA,
         desc_enum=FearDescriptions.IATROPHOBIA),
    Fear(name_enum=FearNames.INSECTOPHOBIA,
         desc_enum=FearDescriptions.INSECTOPHOBIA),
    Fear(name_enum=FearNames.KOINONIPHOBIA,
         desc_enum=FearDescriptions.KOINONIPHOBIA),
    Fear(name_enum=FearNames.KOUMPOUNOPHOBIA,
         desc_enum=FearDescriptions.KOUMPOUNOPHOBIA),
    Fear(name_enum=FearNames.LEUKOPHOBIA,
         desc_enum=FearDescriptions.LEUKOPHOBIA),
    Fear(name_enum=FearNames.LILAPSOPHOBIA,
         desc_enum=FearDescriptions.LILAPSOPHOBIA),
    Fear(name_enum=FearNames.LOCKIOPHOBIA,
         desc_enum=FearDescriptions.LOCKIOPHOBIA),
    Fear(name_enum=FearNames.MAGEIROCOPHOBIA,
         desc_enum=FearDescriptions.MAGEIROCOPHOBIA),
    Fear(name_enum=FearNames.MEGALOPHOBIA,
         desc_enum=FearDescriptions.MEGALOPHOBIA),
    Fear(name_enum=FearNames.MENOPHOBIA,
         desc_enum=FearDescriptions.MENOPHOBIA,
         type_enum=FearTypes.GENITAL_SECRETION),
    Fear(name_enum=FearNames.MELANOPHOBIA,
         desc_enum=FearDescriptions.MELANOPHOBIA),
    Fear(name_enum=FearNames.MICROPHOBIA,
         desc_enum=FearDescriptions.MICROPHOBIA),
    Fear(name_enum=FearNames.MYSOPHOBIA,
         desc_enum=FearDescriptions.MYSOPHOBIA,
         type_enum=FearTypes.GENITAL_SECRETION),
    Fear(name_enum=FearNames.NECROPHOBIA,
         desc_enum=FearDescriptions.NECROPHOBIA),
    Fear(name_enum=FearNames.NOCTIPHOBIA,
         desc_enum=FearDescriptions.NOCTIPHOBIA),
    Fear(name_enum=FearNames.NOSOCOMEPHOBIA,
         desc_enum=FearDescriptions.NOSOCOMEPHOBIA),
    Fear(name_enum=FearNames.NYCTOPHOBIA,
         desc_enum=FearDescriptions.NYCTOPHOBIA),
    Fear(name_enum=FearNames.OBESOPHOBIA,
         desc_enum=FearDescriptions.OBESOPHOBIA),
    Fear(name_enum=FearNames.OCTOPHOBIA,
         desc_enum=FearDescriptions.OCTOPHOBIA),
    Fear(name_enum=FearNames.OMBROPHOBIA,
         desc_enum=FearDescriptions.OMBROPHOBIA),
    Fear(name_enum=FearNames.OMPHALOPHOBIA,
         desc_enum=FearDescriptions.OMPHALOPHOBIA,
         type_enum=FearTypes.SEXUAL_ABUSE_AND_TRAUMA),
    Fear(name_enum=FearNames.OPHIDIOPHOBIA,
         desc_enum=FearDescriptions.OPHIDIOPHOBIA),
    Fear(name_enum=FearNames.ORNITHOPHOBIA,
         desc_enum=FearDescriptions.ORNITHOPHOBIA),
    Fear(name_enum=FearNames.PAPYROPHOBIA,
         desc_enum=FearDescriptions.PAPYROPHOBIA),
    Fear(name_enum=FearNames.PARAPHOBIA,
         desc_enum=FearDescriptions.PARAPHOBIA,
         type_enum=FearTypes.SEXUAL_ABUSE_AND_TRAUMA),
    Fear(name_enum=FearNames.PARTHENOPHOBIA,
         desc_enum=FearDescriptions.PARTHENOPHOBIA,
         type_enum=FearTypes.SEXUAL_ABUSE_AND_TRAUMA),
    Fear(name_enum=FearNames.PARURESIS,
         desc_enum=FearDescriptions.PARURESIS,
         type_enum=FearTypes.GENITAL_SECRETION),
    Fear(name_enum=FearNames.PATHOPHOBIA,
         desc_enum=FearDescriptions.PATHOPHOBIA),
    Fear(name_enum=FearNames.PEDOPHOBIA,
         desc_enum=FearDescriptions.PEDOPHOBIA),
    Fear(name_enum=FearNames.PHILEMATOPHOBIA,
         desc_enum=FearDescriptions.PHILEMATOPHOBIA),
    Fear(name_enum=FearNames.PHILOPHOBIA,
         desc_enum=FearDescriptions.PHILOPHOBIA),
    Fear(name_enum=FearNames.PHOBOPHOBIA,
         desc_enum=FearDescriptions.PHOBOPHOBIA),
    Fear(name_enum=FearNames.PODOPHOBIA,
         desc_enum=FearDescriptions.PODOPHOBIA),
    Fear(name_enum=FearNames.PORPHYROPHOBIA,
         desc_enum=FearDescriptions.PORPHYROPHOBIA),
    Fear(name_enum=FearNames.PTERIDOPHOBIA,
         desc_enum=FearDescriptions.PTERIDOPHOBIA),
    Fear(name_enum=FearNames.PTEROMERHANOPHOBIA,
         desc_enum=FearDescriptions.PTEROMERHANOPHOBIA),
    Fear(name_enum=FearNames.PUEROPHOBIA,
         desc_enum=FearDescriptions.PUEROPHOBIA,
         type_enum=FearTypes.SEXUAL_ABUSE_AND_TRAUMA),
    Fear(name_enum=FearNames.PYROPHOBIA,
         desc_enum=FearDescriptions.PYROPHOBIA),
    Fear(name_enum=FearNames.SAMHAINOPHOBIA,
         desc_enum=FearDescriptions.SAMHAINOPHOBIA),
    Fear(name_enum=FearNames.SCOLIONOPHOBIA,
         desc_enum=FearDescriptions.SCOLIONOPHOBIA),
    Fear(name_enum=FearNames.SCOPTOPHOBIA,
         desc_enum=FearDescriptions.SCOPTOPHOBIA),
    Fear(name_enum=FearNames.SCYPHOPHOBIA,
         desc_enum=FearDescriptions.SCYPHOPHOBIA,
         type_enum=FearTypes.GENITAL_SECRETION),
    Fear(name_enum=FearNames.SELENOPHOBIA,
         desc_enum=FearDescriptions.SELENOPHOBIA),
    Fear(name_enum=FearNames.SOCIOPHOBIA,
         desc_enum=FearDescriptions.SOCIOPHOBIA),
    Fear(name_enum=FearNames.SOMNIPHOBIA,
         desc_enum=FearDescriptions.SOMNIPHOBIA),
    Fear(name_enum=FearNames.TACHOPHOBIA,
         desc_enum=FearDescriptions.TACHOPHOBIA),
    Fear(name_enum=FearNames.TECHNOPHOBIA,
         desc_enum=FearDescriptions.TECHNOPHOBIA),
    Fear(name_enum=FearNames.TONITROPHOBIA,
         desc_enum=FearDescriptions.TONITROPHOBIA),
    Fear(name_enum=FearNames.TRYPANOPHOBIA,
         desc_enum=FearDescriptions.TRYPANOPHOBIA),
    Fear(name_enum=FearNames.TRYPOPHOBIA,
         desc_enum=FearDescriptions.TRYPOPHOBIA),
    Fear(name_enum=FearNames.VENUSTRAPHOBIA,
         desc_enum=FearDescriptions.VENUSTRAPHOBIA),
    Fear(name_enum=FearNames.VERMINOPHOBIA,
         desc_enum=FearDescriptions.VERMINOPHOBIA),
    Fear(name_enum=FearNames.WICCAPHOBIA,
         desc_enum=FearDescriptions.WICCAPHOBIA),
    Fear(name_enum=FearNames.XENOPHOBIA,
         desc_enum=FearDescriptions.XENOPHOBIA),
    Fear(name_enum=FearNames.ZOOPHOBIA,
         desc_enum=FearDescriptions.ZOOPHOBIA),
]
"""All of the phobias
"""
