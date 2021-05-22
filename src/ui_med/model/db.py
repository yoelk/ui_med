from enum import IntEnum
from typing import Any, List, Optional

from kivy.storage.dictstore import DictStore
from ui_med.app_base import get_logger
from ui_med.model.people import Person


class DbKeys(object):
    """
    Keys for storage access
    """
    VALUE: str = "value"
    VERSION: str = "version"
    PEOPLE: str = "people"


class DbVersions(IntEnum):
    """
    Known DB versions
    """

    # V0: The DB is empty    
    V0 = 0

    # V1: The people list was added
    V1 = 1

    # V2: phobias was added to Person
    V2 = 2


class Db(object):
    """
    Our database
    """

    _DB_STORAGE_FILENAME: str = "ui_med_app_storage"
    """The database storage filename 
    """

    _CODE_VERSION: int = DbVersions.V2
    """The DB version in the code
    """

    def __init__(self) -> None:
        """
        Initialize
        :return: Nothing
        """
        self._store: DictStore = DictStore(filename=self._DB_STORAGE_FILENAME)
        self._store.store_load()
        self._migrate_up_if_needed()

    def _migrate_up_if_needed(self) -> None:
        """
        Migrate the current data up to the current code version
        :return: Nothing
        """
        read_db_version: int = self.version
        assert read_db_version <= self._CODE_VERSION
        if read_db_version == self._CODE_VERSION:
            # No migration needed
            return
        
        if read_db_version <= DbVersions.V1:
            # Init the people list
            if DbKeys.PEOPLE not in self._keys():
                self.people = []

        if read_db_version <= DbVersions.V2:
            # Add "phobias" field to Person class
            people: List[Person] = self.people
            for person in people:
                if not hasattr(person, "phobias"):
                    person.phobias = []
            self.people = people

        # Update the new db version
        self.version = self._CODE_VERSION
        get_logger().info(f"Db version updated: {read_db_version}->{self.version}")

    # Store wrappers
    def _put(self, key: str, value: Any) -> None:
        """
        Put a value in the database
        :param key: The key
        :param value: The value
        :return: Nothing
        """
        get_logger().info(f"Db._put: {key}, {value}")
        self._store.put(key, **{DbKeys.VALUE: value})

    def _get(self, key: str) -> Optional[Any]:
        """
        :param key: The key
        :return: A value from the database if it exists, else None
        """
        try:
            return self._store.get(key)[DbKeys.VALUE]

        except KeyError:
            return None

    def _keys(self) -> List[Any]:
        """
        :return: Our DB keys
        """
        return self._store.keys()

    # Access methods for DB parts
    @property
    def version(self) -> int:
        """
        :return: The current DB version
        """
        version: Optional[int] = self._get(key=DbKeys.VERSION)
        return version if version is not None else DbVersions.V0

    @version.setter
    def version(self, value: int) -> None:
        """
        :param value: The value to set
        :return: Nothing
        """
        self._put(key=DbKeys.VERSION, value=value)

    @property
    def people(self) -> Optional[List[Person]]:
        """
        :return: The people list
        """
        return self._get(key=DbKeys.PEOPLE)

    @people.setter
    def people(self, value: List[Person]) -> None:
        """
        :param value: The value to set
        :return: Nothing
        """
        self._put(key=DbKeys.PEOPLE, value=value)
