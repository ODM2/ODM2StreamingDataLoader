__author__ = 'Jacob'

import json

class JsonHandler():
    """Reads and Writes Json files, generate objects from json

    """
    def __init__(self):
        pass

    def readJsonFile(self, path):
        """

        :param path:
            :type String:
        :return:
            :type json.dump object:
        """

        load = json.loads(path)

    def writeJsonFile(self, outputName):
        """

        :param outputName:
            :type String:
        :return:
            :type boolean:
        """
        pass

    def toConfigObject(self, jsonDump):
        """

        :param jsonDump:
            :type jsonDump.dumps instance
        :return:
            :type Configuration
        """
        pass
