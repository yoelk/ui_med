from typing import List


class Meridian(object):
    """A Meridian
    """

    def __init__(self, name: str) -> None:
        """
        Initialize
        :param name: The name
        :return: Nothing
        """
        self.name: str = name


MERIDIANS: List[Meridian] = [
    Meridian(name="Lungs"),
    Meridian(name="Large Intestine"),
    Meridian(name="Stomach"),
    Meridian(name="Spleen"),
    Meridian(name="Heart"),
    Meridian(name="Small Intestine"),
    Meridian(name="Urinary Bladder"),
    Meridian(name="Kidneys"),
    Meridian(name="Pericard"),
    Meridian(name="Triple Burner"),
    Meridian(name="Gallbladder"),
    Meridian(name="Liver"),

]
