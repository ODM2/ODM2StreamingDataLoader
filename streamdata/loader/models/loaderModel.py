__author__ = 'Jacob'

from streamdata.handlers.jsonHandler import JsonHandler as json
from streamdata.handlers.csvHandler import CSVReader as csv

class LoaderModel():
    """Model for Loader"""
    def __init__(self, args):
        """

        :param args:
            :type ArgumentParser:
        :return:
        """
        self.jsonFile = args.jsonFile
        if not self.jsonFile:
            raise "json configuration file couldn't be found"

        self.dataFile = args.dataFile

        # read jsonFile
        self.readJsonConfig(jsonConfig=self.jsonFile)

    def readJsonConfig(self, jsonConfig):
        """Read Json configuration

        :param jsonConfig:
        :return config:
            :type namedtuple:
        """

        self.config = json.readJsonFile(self.jsonFile)
        if not self.config:
            raise "json configuration returned None"

        self.jsonConfigObject = json.toConfigObject(self.config)
        if not self.jsonConfigObject:
            raise "json config object returned None"

    def readDataFile(self, dataFile=None):
        """Read dataFile

        :param dataFile:
        :type dataFile String:
        :return:
        """

        sep = self.jsonConfigObject

        #if dataFile:
        #    self.data = csv.csv_reader(dataFile)


    def _validateJsonFile(self):
        pass

    def _validateCSVFile(self):
        pass



