from enum import Enum
from typing import Any, List, Optional, Type


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


def enum_from_value(enum_cls: Type[Enum], value: Any) -> Optional[Enum]:
    """
    :param enum_cls: The enum class
    :param value: The enum value
    :return: The enum that corresponds to the given value
    """
    for e in enum_cls:
        if e.value == value:
            return e

    return None
