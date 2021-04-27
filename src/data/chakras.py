from typing import List


class Chakra(object):
    """A Chakra
    """

    def __init__(self, number: int, color_name: str, life_domain: str,
                 gland_name: str) -> None:
        """
        Initialize
        :param number: The number
        :param color_name: The color's name
        :param life_domain: The life domain
        :param gland_name: The gland's name
        :return: Nothing
        """
        self.number: int = number
        self.color_name: str = color_name
        self.life_domain: str = life_domain
        self.gland_name: str = gland_name


CHAKRAS: List[Chakra] = [
    Chakra(number=1,
           color_name="Red",
           life_domain="Territory",
           gland_name="Adrenal gland"),
    Chakra(number=2,
           color_name="Orange",
           life_domain="Sex",
           gland_name="Ovaries and Testis"),
    Chakra(number=3,
           color_name="Yellow",
           life_domain="Society",
           gland_name="Pancreas"),
    Chakra(number=4,
           color_name="Green",
           life_domain="Family",
           gland_name="Thymus gland"),
    Chakra(number=5,
           color_name="Blue",
           life_domain="Profession",
           gland_name="Thyroid gland"),
    Chakra(number=6,
           color_name="Violet",
           life_domain="Life path",
           gland_name="Hypofisis gland"),
    Chakra(number=7,
           color_name="Crimson",
           life_domain="Relation with God",
           gland_name="Pineal gland"),
]
