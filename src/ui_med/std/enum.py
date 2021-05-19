from enum import Enum
from typing import Any, List, Type


def enum_names(enum_cls: Type[Enum]) -> List[str]:
    """
    :param enum_cls: The enum class
    :return: The names of the enum entries
    """
    return [e.name for e in enum_cls]


def enum_values(enum_cls: Type[Enum]) -> List[Any]:
    """
    :param enum_cls: The enum class
    :return: The values of the enum entries
    """
    return [e.value for e in enum_cls]
