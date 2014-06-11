from collections import namedtuple

__author__ = 'Jacob'

import json


class JsonHandler():
    """Reads and Writes Json files, generate objects from json

    """

    def __init__(self):
        pass

    def readJsonFile(self, file):
        """

        :param file:
            :type String:
        :return:
            :type json.load object:
        """

        if not file:
            raise "readJsonFile cannot read the file you provided"

        f = open(file)
        load = json.load(f)
        f.close()
        if load:
            return load
        else:
            return None

    def writeJsonFile(self, load, outputName):
        """

        :param outputName:
            :type String:
        :param load:
            :type json.Load Object:
        :return:
            :type boolean:
        """

        if not load:
            raise "writeJsonFile cannot work because json.Loads object is None"
        if not outputName:
            outputName = "unknown"
        try:
            dump = json.dumps(load, indent=4, separators=(',', ': '), sort_keys=True)
            f = open(outputName, 'w')
            f.write(dump)
            f.close()
            return True
        except:
            return False



    def toConfigObject(self, jsonLoadedObject):
        """

        :param jsonLoadedObject:
            :type jsonLoadedObject instance
        :return:
            :type list of namedtuple
        :return:
            :type ConfigObject namedtuple
        """
        if isinstance(jsonLoadedObject, list):
            listOfObjects = []
            for x in jsonLoadedObject:
                listOfObjects.append(namedtuple('ID_%s' % x['ID'], x)(**x))
            return listOfObjects
        else:
            x = jsonLoadedObject
            return namedtuple('ID_%s' % x['ID'], x)(**x)



        #ConfigObject = namedtuple('Object', **jsonLoadedObject)

