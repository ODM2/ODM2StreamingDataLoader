__author__ = 'Denver'

import yaml
import os
import csv

import pprint
import datetime

class YamlConfiguration():
    '''
    YAML Config file model
    '''

    def __init__(self, configFilePath):
        self.yamlFilePath = configFilePath
        self.yamlDict = {}
        self.yamlDict = self._readFile(self.yamlFilePath)

    def _readFile(self, path):
        '''
        _readFile takes a string argument, which is the path to
        the YAML configuration file to be mapped to a python dict.
        '''
        # If the given path does not exist then return None.
        if not path:
            print "Cannot read the file provided."
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
            print e
            return None


    def get(self):
        '''
        The YAML file is divided up according to different CSV data
        files. This method returns a list of the configuration
        parameters for each CSV file in the YAML configuration file.
        '''
        fileDictList = []
        for fileDict in self.yamlDict.keys():
            fileDictList.append(self.yamlDict[fileDict])
        return fileDictList

    def updateLastRead(self, configFileDict):
        
        fileSize = os.path.getsize(configFileDict['Settings']['FileLocation'])
        configFileDict['Settings']['LastByteRead'] = str(fileSize)

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

