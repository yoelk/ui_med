import os
import shutil


def recreate_folder(path: str) -> None:
    """
    Recreate a folder
    :param path: The folder path
    :return: Nothing
    """
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)