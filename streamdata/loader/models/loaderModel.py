import logging

__author__ = 'Jacob'

from streamdata.handlers.jsonHandler import JsonHandler as json
from streamdata.handlers.csvHandler import CSVReader as csv

from streamdata.common.logger import LoggerTool

tool = LoggerTool()
logger = tool.setupLogger(__name__, __name__ + '.log', 'w', logging.DEBUG)


class LoaderModel():
    """Model for Loader"""

    def __init__(self, config):
        """
        :param config:
            :type config String:
        :return:
        """
        self.jsonFile = config
        if not self.jsonFile:
            logger.debug("json configuration file couldn't be found")
            raise RuntimeError("json configuration file couldn't be found")

        self.js = json()
        self.csv = csv()

        # read jsonFile
        # self.readJsonConfig(jsonConfig=self.jsonFile)

    def readJsonConfig(self, jsonConfig=None):
        """Read Json configuration

        :param jsonConfig:
        :return config:
            :type namedtuple:
        """

        if not jsonConfig:
            jsonConfig = self.jsonFile

        self.config = self.js.readJsonFile(jsonConfig)
        if not self.config:
            logger.debug('json configuration couldn\'t be extracted')
            raise RuntimeError('json configuration couldn\'t be extracted')

        self.jsonConfigObjectList = self.js.toConfigObject(self.config)
        if not self.jsonConfigObjectList:
            logger.debug('jsonConfigObjectList is null')
            raise RuntimeError('jsonConfigObjectList is null, this cannot happen')

        return self.jsonConfigObjectList

    def readDataFileFromConfig(self, selectedId, configFile=None):
        """Read dataFile

        :param configFile:
        :type configFile Object:
        :return:
        """

        if not configFile:
            configFile = self.jsonConfigObjectList

        ## Obtain correct configuration file filtered by selectedId
        config = self.queryBasedOnId(selectedId, configFile)
        if not config:
            raise RuntimeError("Unable to find the specified id: %s" % selectedId)
        if not config.FileLocation:
            raise RuntimeError("Unable to find the FileLocation to load from the configuration")
        if not config.DataRowPosition:
            raise RuntimeError("Unable to find the DataRowPosition from the configuration")
        if not config.Delimiter:
            raise RuntimeError("Unable to find the Delimiter")

        sep = (',' if config.Delimiter == "<Comma Delimited>" else '\t')

        ## read csv using the parameters from the configuration file
        extractedData = self.csv.reader(config.FileLocation.strip("'"), sep, config.DataRowPosition)
        if extractedData.empty:
            #print ("FileLocation ", config.FileLocation[1:-1])
            raise RuntimeError("Unable to extract data based on the configuration provided")

        ## return extractedData
        return extractedData

    def queryBasedOnId(self, selectedId, configFile=None):
        """

        :param selectedId:
            :type selectedId String:
        :param dataFile:
            :type dataFile namedtuple:
        :return:
        """

        if not configFile:
            configFile = self.jsonConfigObjectList
        result = [t for t in configFile if t.ID == str(selectedId)][0]
        return result