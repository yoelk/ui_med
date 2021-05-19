from typing import List, Optional, Tuple


def python_filename_to_names_enum_class_name(name: str) -> str:
    """
    :param name: The name
    :return: The names' enum class name
    """
    return name.rstrip(".py").replace("_", " ").title().replace(" ", "")


def python_filename_to_names_enum_class_docstring(name: str) -> str:
    """
    :param name: The name
    :return: The names' enum class docstring
    """
    return f'{name.rstrip(".py").replace("_", " ").title()} Names'


def python_filename_to_descriptions_enum_class_name(name: str) -> str:
    """
    :param name: The name
    :return: The descriptions enum class name
    """
    return f'{name.rstrip(".py").replace("_", " ").title().replace(" ", "")}Descriptions'


def python_filename_to_descriptions_enum_class_docstring(name: str) -> str:
    """
    :param name: The name
    :return: The descriptions' enum class docstring
    """
    return f'{name.rstrip(".py").replace("_", " ").title()} Descriptions'


def entry_name_to_enum_entry_name(name: str) -> str:
    """
    :param name: The file name
    :return: The enum entry name
    """
    return name.upper().replace(" ", "_")


def python_filename_to_names_enum_strings_dict_name(name: str) -> str:
    """
    :param name: The file name
    :return: The names enum strings dictionary name
    """
    return f"{name.rstrip('.py').upper()}_NAMES_LANGUAGE_STRINGS"


def python_filename_to_descriptions_enum_strings_dict_name(name: str) -> str:
    """
    :param name: The file name
    :return: The descriptions enum strings dictionary name
    """
    return f"{name.rstrip('.py').upper()}_DESCRIPTIONS_LANGUAGE_STRINGS"


def split_entry_line(line: str) -> Tuple[str, str]:
    """
    Split an entry line
    :param line: The line
    :return: A tuple of the item's name and its description
    """
    name, desc = line.split(sep=" - ", maxsplit=1)
    return name.title(), desc.capitalize()


def write_phobias_python_file(filename: str, entry_lines: List[str]):
    """
    Write a phobias python file
    :param filename: The file name
    :param entry_lines: The lines of the entries to be added to the file
    :return: Nothing
    """
    print(f"Writing {filename} with {len(entry_lines)} entries")
    with open(filename, "w") as fh:
        # Header
        fh.write('''from enum import Enum, auto
from typing import Dict, Optional

from ui_med.model.enums import Languages


''')
        # Names enum
        fh.write(f'''class {python_filename_to_names_enum_class_name(name=filename)}(Enum):
    """
    {python_filename_to_names_enum_class_docstring(name=filename)}
    """
''')
        names_and_descs: List[Tuple[str, str]] = [split_entry_line(line=line)
                                                  for line in entry_lines]
        for name, _ in names_and_descs:
            fh.write(f"    {entry_name_to_enum_entry_name(name=name)} = auto()\n")
        fh.write("\n\n")

        # Names enum strings
        fh.write(
            f"""{python_filename_to_names_enum_strings_dict_name(name=filename)}: Dict[
    Enum, Dict[Languages, Optional[str]]] = {{\n""")
        for name, _ in names_and_descs:
            fh.write(
                f"    {python_filename_to_names_enum_class_name(name=filename)}.{entry_name_to_enum_entry_name(name=name)}: {{\n")
            fh.write(f'        Languages.ENGLISH: "{name}",\n')
            fh.write(f"        Languages.HEBREW: None,\n")
            fh.write(f"        Languages.ARAB: None,\n")
            fh.write(f"        Languages.ITALIAN: None, }},\n")
        fh.write("}\n")
        fh.write("\n\n")

        # Descriptions enum
        fh.write(f'''class {python_filename_to_descriptions_enum_class_name(name=filename)}(Enum):
    """
    {python_filename_to_descriptions_enum_class_docstring(name=filename)}
    """
''')
        for name, _ in names_and_descs:
            fh.write(f"    {entry_name_to_enum_entry_name(name=name)} = auto()\n")
        fh.write("\n\n")

        # Descriptions enum strings
        fh.write(
            f"""{python_filename_to_descriptions_enum_strings_dict_name(name=filename)}: Dict[
    Enum, Dict[Languages, Optional[str]]] = {{\n""")
        for name, desc in names_and_descs:
            fh.write(
                f"    {python_filename_to_descriptions_enum_class_name(name=filename)}.{entry_name_to_enum_entry_name(name=name)}: {{\n")
            fh.write(f'        Languages.ENGLISH: "{desc}",\n')
            fh.write(f"        Languages.HEBREW: None,\n")
            fh.write(f"        Languages.ARAB: None,\n")
            fh.write(f"        Languages.ITALIAN: None, }},\n")
        fh.write("}\n")


if __name__ == '__main__':
    with open("all_phobias.txt", "r", encoding="utf-8") as fh:
        lines: List[str] = fh.read().split('\n')

    cur_filename: Optional[str] = None
    entry_lines: List[str] = []
    for line in lines:
        line = line.strip(" ")

        # Skip empty lines
        if not line:
            continue

        # Open a new python file to contain the next lines
        if ".py" in line:
            if cur_filename is not None:
                write_phobias_python_file(filename=cur_filename, entry_lines=entry_lines)

            cur_filename = line
            entry_lines = []

        else:
            entry_lines.append(line)

    if cur_filename is not None:
        write_phobias_python_file(filename=cur_filename, entry_lines=entry_lines)
        cur_filename = None

# TODO(joel):
#  - Create classes for each phobia
#  - Make connections between phobias and their parents / synonims
#  - Take care of duplicate entries from different files
#  - Concentrate all of the strings' dictionaries in a single place