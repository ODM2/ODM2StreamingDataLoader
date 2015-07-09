__author__ = 'Denver'

import yaml
import os
import csv

import datetime
import logging

logger = logging.getLogger('SDL_logger')

class YamlConfiguration():
    '''
    YAML Config file model
    '''

    def __init__(self, configFilePath, dataFile=None):
        self.yamlFilePath = configFilePath
        self.yamlDict = {}
        self.yamlDict = self._readFile(self.yamlFilePath)
        self.dataFile = dataFile

    def _readFile(self, path):
        '''
        _readFile takes a string argument, which is the path to
        the YAML configuration file to be mapped to a python dict.
        '''
        # If the given path does not exist then return None.
        # TODO: This this case even possible?
        if not path:
            return None

        # Attempt to read from the given path. Data is returned if
        # the opporation is successful, None is returned if there is
        # some sort of IO Error.
        try:
            with open(path) as f:
                load = yaml.load(f)
                if load:
                    return load
        except IOError as e:
            logger.error("Cannot read the file provided. Exception: %s" % e)
            return None


    def get(self):
        '''
        The YAML file is divided up according to different CSV data
        files. This method returns a list of the configuration
        parameters for each CSV file in the YAML configuration file.
        '''
        fileDictList = []

        for fileDict in self.yamlDict.keys():
            # If the user specified a single data file to use.
            if self.dataFile is not None:
                # Look for the matching data file.
                if self.yamlDict[fileDict]['Settings']['FileLocation'] == self.dataFile:
                    # only use the one file configuration.
                    fileDictList.append(self.yamlDict[fileDict])
            
            # Collect all of the configurations.
            else:
                fileDictList.append(self.yamlDict[fileDict])

        return fileDictList

    def updateLastRead(self, configFileDict, columnName):
        '''
        updateLastRead is a public method which updates the
        'LastByteRead' parameter for the given column.
        '''
        fileSize = os.path.getsize(configFileDict['Settings']\
                                                 ['FileLocation'])
        configFileDict['Mappings'][columnName]\
                      ['LastByteRead'] = str(fileSize)
        
        return configFileDict


    def rebase(self, configFileDictList):
        newContent = {}
        for i,d in enumerate(reversed(configFileDictList)):
            newContent['File_%d' % i] = d
        
        with open(self.yamlFilePath, 'w') as f:
            f.write('## Configuration file\n## Last modified: %s\n---\n' %\
                    (str(datetime.date.today()) +\
                    ' ' +\
                    str(datetime.datetime.now().hour) +\
                    ':' +\
                    str(datetime.datetime.now().minute)))
            f.write(yaml.dump(newContent, default_flow_style=False, allow_unicode=True,))

