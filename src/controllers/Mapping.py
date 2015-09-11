__author__ = 'stephanie, denver'
import pandas as pd
import numpy as np
from collections import namedtuple
import logging

from handlers.csvHandler import CSVReader
from controllers.Database import Database

logger = logging.getLogger('SDL_logger')

class Mapping():
    '''
    Model class representing a mapped pandas dataframe object.
    
    Attributes:
        rawData : pandas.core.frame.DataFrame - Raw CSV data from the
                                                given file.
        tables : pandas.core.frame.DataFrame - The finnished tables to
                                                write to the database.
        mapping : dict - The YAML configuration mapping.
        dbWriter : Database - The database object that will be used.
    '''
    
    
    
    def __init__(self, configDict):
        self.tables = [] # Empty
        self.mapping = configDict
        self.rawData = pd.DataFrame # Empty

        self.dbWriter = Database()
        self.performDuplicateValueChecks = False
    
    
    def getDatabase(self):
        '''
        getDatabase is a public method that should be called before
        interacting with the database. It snatches up the database
        credentials from the YAML file object (mapping) and returns
        a named-tuple called Credentials.
        '''
        Credentials = namedtuple('Credentials', 'host, db_name,\
                                    uid, pwd')
        return self.dbWriter.createConnection(Credentials(\
                            self.mapping['Database']['Address'],
                            self.mapping['Database']['DatabaseName'],
                            self.mapping['Database']['UserName'],
                            self.mapping['Database']['Password']))
    
    
    
    def map(self):
        '''
        This public method begins the process of mapping the data
        into something that we can write to the database. First,
        the file is read from the config file (mapping), if that
        works, we begin to build a new Pandas dataframe.
        '''
        #if self._readFile(self.mapping['Settings']['FileLocation']):
        try:
            if self._readFile(self.mapping['Settings']['FileLocation']):
                self._buildTables()
            #self._buildTables()
        except KeyError:
            logger.error("Unable to create mapping. Check your data & configuration files.")
            return False
        return True
    
    
    
    def _readFile(self, path):
        '''
        readFile gathers the raw data (rawData) from the given CSV
        file (path). If rawData ends up being empty, we return False,
        otherwise we return as True.
        '''
        
        reader = CSVReader()

        # Collect the smallest 'LastByteRead' in the file.
        byte = self._getStartByte()
        
        logger.debug('Last successful byte read: %s' % byte)
       
        logger.info("Data file location: '%s'" % path)
        self.rawData = reader.byteReader(path,
                start_byte=byte,
                datecol=self.mapping['Settings']['DateTimeColumnName'],
                sep=self.mapping['Settings']['Delimiter'],
                header=self.mapping['Settings']['HeaderRowPosition'],
                dataBegin=self.mapping['Settings']['DataRowPosition'])

        if self.rawData.empty:
            return False
        else:
            return True
    
    
    
    def _getStartByte(self):
        '''
        getStartByte is a private method which determines the smallest
        byte number of the given columns.
        '''
        m = [value['LastByteRead'] for key,value in \
            self.mapping['Mappings'].items()]
        
        # If all of the bytes are the same, don't do a
        # duplicate values check when writing to database.
        self.performDuplicateValueChecks = not len(set(m)) <= 1

        # Starting byte will be the lowest value.
        startByte = int(min(m))
        
        # But if it's less than 0 (AKA running in restart mode)
        # then just set it to 0.
        if startByte < 0:
            startByte = 0
        
        return startByte
    
    
    
    def _buildTables(self):
        '''
        buildTables creates a brand new Pandas dataframe (tables),
        gathering the needed columns from the YAML file (mapping)
        and raw data (rawData).
        '''
        for col, series in self.mapping['Mappings'].iteritems():
            df = self.rawData[col].reset_index()
            df.columns = ['ValueDateTime', 'DataValue']
            
            if series['CalculateAggInterval']:

                df['TimeAggregationInterval'] = 0
                df['TimeAggregationIntervalUnitsID'] = 0

            else:
                df['TimeAggregationInterval'] = series['IntendedTimeSpacing']
                df['TimeAggregationIntervalUnitsID'] = series['IntendedTimeSpacingUnitID']

            df['QualityCodeCV'] = 'None'
            #df['QualityCodeCV'] = 'SDL Test Data'
            df['CensorCodeCV'] = 'Unknown'
            df['ResultID'] = series['ResultID']
            df['ValueDateTimeUTCOffset'] = self.mapping['Settings']['UTCOffset']

            noDataValue = self._getNoDataValue(df['ResultID'][0])
            
            df = df.replace(to_replace=[np.nan, '-INF'],
                            value=[noDataValue, noDataValue],
                            regex=True)
            
            replaced = df.isin([noDataValue]).sum().sum()

            df.ValueDateTime = pd.to_datetime(\
                                pd.Series(df.ValueDateTime))
            self.tables.append((col, df))
            
            logger.info('Result: %s Total Values: %d, Non-data Values: %d' % (col, len(df), replaced))
    
    def _getNoDataValue(self, resultID):
        '''
        _getNoDataValue is a wrapper method to the database object's
        getNoDataValue method.
        '''
        return self.dbWriter.getNoDataValue(resultID)
    
    
    
    def getTables(self):
        '''
        getTables is a public method that returns a Pandas dataframe.
        It should be called after a mapping has been made.
        '''
        return self.tables
    
    
    
    def save(self, data):
        '''
        save is a public method that wraps the Database.write method.
        '''
        return self.dbWriter.write(data,
            self.performDuplicateValueChecks)

    def updateDateTime(self, seriesId, dateTime):
        '''
        updateDateTime is a public method that wraps the
        Database.updateDateTime method. It's part of this module
        because the database connection is only accessable through
        here.
        '''
        return self.dbWriter.updateDateTime(seriesId, dateTime)      


