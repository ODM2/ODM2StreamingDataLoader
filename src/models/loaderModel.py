import logging
import pandas as pd
import pprint
import os.path
__author__ = 'Jacob'

#from ..handlers.jsonHandler import JsonHandler as json
from ..handlers.yamlHandler import YAMLHandler as yaml
from ..handlers.csvHandler import CSVReader as csv

from ..common.logger import LoggerTool

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
        """
        if config.endswith('.json'):
            self.jsonFile = config
            if not self.jsonFile:
                logger.debug("json configuration file couldn't be found")
                raise RuntimeError("json configuration file couldn't be found")
        """
        if config.endswith('.yaml'):
            self.yamlFile = config
            if not self.yamlFile:
                logger.debug("yaml configuration file couldn't be found")
                raise RuntimeError("yaml configuration file couldn't be found")
        self.yaml = yaml()
        
        #self.js = json()
        self.csv = csv()
        self.readData(self.readYamlConfig())

        # read yamlFile
        # self.readYamlConfig(yamlConfig=self.yamlFile)

    def readData(self, yamlConfigObject):
        pprint.pprint(yamlConfigObject)
        # loop for each config file inside of the yaml file
        for fileConfig in yamlConfigObject:
            filePath = yamlConfigObject[fileConfig]['Settings']['FileLocation']
            if (os.path.isfile(filePath)):
                print self.csv.reader(filePath, '\t')
            else:
                print filePath + " does not exist."
        
        return None

    def readYamlConfig(self, yamlConfig=None):
        """
        Read YAML configuration

        :param yamlConfig:
        :return config:
            :type dictionary:
        """
        if not yamlConfig:
            yamlConfig = self.yamlFile
        
        self.config = self.yaml.read_yaml(yamlConfig)
        if not self.config:
            logger.debug("yaml configuration couldn't be extracted.")
            raise RuntimeError("yaml configuration couldn't be extracted.")

        self.yamlConfigObjectList = self.yaml.toConfigObject(self.config)
        if not self.yamlConfigObjectList:
            logger.debug("yamlConfigObjectList is null.")
            raise RuntimeError("yamlConfigObjectList is null, this cannot happen.")
        return self.yamlConfigObjectList

    def readJsonConfig(self, jsonConfig=None):
        """Read Json configuration

        :param jsonConfig:
        :return config:
            :type namedtuple:
        """

        if not jsonConfig:
            jsonConfig = self.jsonFile

        self.config = self.js.read_json(jsonConfig)
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
            configFile = self.yamlConfigObjectList

        extractedData = self.csv.reader(self.yamlConfigObjectList.strip("'"), '\t')
        return extractedData
        """
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
        if isinstance(extractedData, pd.DataFrame):
            if extractedData.empty:
                print("Unable to extract data based on the configuration provided")
        else:
            if not extractedData:
                print("Unable to extract data based on the configuration provided")


        ## return extractedData
        return extractedData
        """
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
