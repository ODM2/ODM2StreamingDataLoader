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
            print("readJsonFile cannot read the file you provided")
            raise

        try:
            f = open(file)
            load = json.load(f)
            f.close()
            if load:
                return load['File']
            else:
                return None
        except IOError as e:
            print e
            return None


    def writeJsonFile(self, load, outputName=None):
        """

        :param outputName:
            :type String:
        :param load:
            :type json.Load Object:
        :return:
            :type boolean:
        """

        if not load:
            print ("json.Loads object is None")
            raise
        try:
            dump = json.dumps(load, indent=4, separators=(',', ': '), sort_keys=True)
            if outputName:
                f = open(outputName, 'w')
                f.write(dump)
                f.close()
            return dump
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

        if not jsonLoadedObject:
            print("json.Load object cannot be null")
            raise

        if isinstance(jsonLoadedObject, list):
            listOfObjects = []
            for x in jsonLoadedObject:
                listOfObjects.append(namedtuple('ID_%s' % x['ID'], x)(**x))
            return listOfObjects
        else:
            x = jsonLoadedObject
            return namedtuple('ID_%s' % x['ID'], x)(**x)
