__author__ = 'Denver'

import yaml
import os
import csv
import datetime
import logging
import urllib2
import tempfile

from src.models.Mapping import Mapping

logger = logging.getLogger('SDL_logger')

class YamlConfiguration():
    '''
    YAML Config file model

    This class represents a YAML configuration file. It does things
    like loading and writing data to the file, and handles all 
    interaction to the YAML configuration file.

    yamlDict - A dictionary containing the same data that's inside
                the YAML file.
    yamlFilePath - The path to the YAML configuration file.
    dataFile - An optional path to one specific CSV file provided by
                the user.
    '''
    def __init__(self, configFilePath=None,
                dataFile=None, ignoreBytes=False):
        if not configFilePath:
            #self.yamlDict = self._createNew()
            self.yamlDict = {}
            self.dataFile = dataFile
            #self.yamlDict = self.get(yamlDict=self.yamlDict)
            return

        self.yamlFilePath = configFilePath
        self.yamlDict = {}
        self.yamlDict = self._readFile(self.yamlFilePath)
        #self._remoteFileMagic()
        self.dataFile = dataFile


        # If we are running in restart mode, ignore the 
        # 'LastByteRead' parameter in the YAML file.
        if ignoreBytes:
            logger.info('Restart mode enabled - Ignoring last byte read.')
            # Loop through to set just one of the values to -1
            # so that the mapper performs duplicate value checks.
            for fileConfig in self.yamlDict.keys():
                for variable in self.yamlDict[fileConfig]['Mappings'].keys():
                    self.yamlDict[fileConfig]\
                                 ['Mappings']\
                                 [variable]\
                                 ['LastByteRead'] = '-1'
                    break


    def _remoteFileMagic(self):
        for chunk in self.yamlDict.keys():
            print chunk

    def _readFile(self, path):
        '''
        _readFile takes a string argument, which is the path to
        the YAML configuration file to be mapped to a python dict.
        '''
        # Attempt to read from the given path. Data is returned if
        # the opporation is successful, None is returned if there is
        # some sort of IO Error.
        try:
            with open(path) as f:
                logger.info("Loading configuration file: '%s'..." % path)
                load = yaml.load(f)
                if load:
                    logger.info("...load successful.")
                return load
                
        except IOError as e:
            logger.error("Cannot read the file provided. Exception: %s" % e)
            return None


    def get(self, yamlDict=None):
        '''
        The YAML file is divided up according to different CSV data
        files. This method returns a list of the configuration
        parameters for each CSV file in the YAML configuration file.

        The list is in this format: [('file_id',{parameter_dict}), ('file_id',{parameter_dict})]
        '''
        fileDictList = []

        if not yamlDict:
            yamlDict = self.yamlDict
        
        for fileDict in yamlDict.keys():
            # If the user specified a single data file to use.
            if self.dataFile is not None:
                # Look for the matching data file.
                if self.yamlDict[fileDict]['Settings']['FileLocation'] == self.dataFile:
                    # only use the one file configuration.
                    fileDictList.append(Mapping((fileDict, self.yamlDict[fileDict])))
            
            # Collect all of the configurations.
            else:
                fileDictList.append(Mapping((fileDict, self.yamlDict[fileDict])))

        return fileDictList

    def updateLastRead(self, configFileDict, columnName):
        '''
        updateLastRead is a public method which updates the
        'LastByteRead' parameter for the given column.
        
        These changes are not reflected in the actual file
        until the rebase method is called.
        '''
        
        try:
            fileSize = os.path.getsize(configFileDict.asTuple()[1]['Settings']\
                                                     ['FileLocation'])
        except OSError:
            response = urllib2.urlopen(configFileDict.asTuple()[1]['Settings']\
                ['FileLocation'])
            data = response.read()
            temp = tempfile.NamedTemporaryFile()
            try:
                temp.write(data)
                temp.seek(0)
            finally:
                fileSize = os.path.getsize(temp.name)
                configFileDict.asTuple()[1]['Mappings'][columnName]\
                    ['LastByteRead'] = str(fileSize)
                temp.close()
                return configFileDict
        
        configFileDict.asTuple()[1]['Mappings'][columnName]\
                      ['LastByteRead'] = str(fileSize)
        
        return configFileDict


    def rebase(self, configFileDictList):
        '''
        A public method which writes the changes made in memory
        to the YAML configuration file.
        '''
        newContent = {}
        for i,d in reversed([l.asTuple() for l in configFileDictList]):
            newContent[i] = d
        with open(self.yamlFilePath, 'w') as f:
            f.write('## Configuration file\n## Last modified: %s\n---\n' %\
                    (str(datetime.date.today()) +\
                    ' ' +\
                    str(datetime.datetime.now().hour) +\
                    ':' +\
                    str(datetime.datetime.now().minute)))
            f.write(yaml.dump(newContent, default_flow_style=False, allow_unicode=True,))


    def save(self, path=''):
        if path == '' and self.yamlFilePath == '':
            raise ValueError('Cannot save to empty path')
            return
        logger.info("Writing to '%s'" % path)

        #if self.yamlFilePath == '':
        self.yamlFilePath = path
        self.rebase(self.get())

    def addMapping(self, mapping):
        '''
        Add a new mapping to self.yamlDict
        Used by the wizard.
        '''
        self.yamlDict[mapping[0]] = mapping[1]
    
    def deleteMapping(self, mapping):
        '''
        Delete a mapping from self.yamlDict
        Used by the wizard.
        '''
        del self.yamlDict[mapping.asTuple()[0]]
    
    def deleteMappings(self):
        '''
        Delete all mappings from self.yamlDict
        Used by the wizard.
        '''
        self.yamlDict = {}

