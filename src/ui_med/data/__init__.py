import os


def get_data_resource(relpath: str) -> str:
    """
    :param relpath: The relative path in the data resources
    :return: The file's full path
    """
    return os.path.join(os.path.dirname(__file__), "resources", relpath)
