from genericpath import isfile
from os import listdir
from os.path import join

__author__ = 'jmeline'

def returnFiles(path):
    """Collects a list of files within a file

    :rtype: list
    """
    if path:
        onlyFiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
        # print("onlyFiles: ", onlyFiles)
        return onlyFiles
        # print("Path: ", listdir(path))
    return None