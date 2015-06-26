__author__ = 'stephanie'
import pandas as pd
from collections import namedtuple
from handlers.csvHandler import CSVReader

class Mapping():
    '''
    Model class representing a mapped pandas dataframe object.
    
    Attributes:
        rawData : pandas.core.frame.DataFrame - Raw CSV data from the
                                                given file.
        tables : pandas.core.frame.DataFrame - The finnished tables to
                                                write to the database.
        mapping : dict - The YAML configuration mapping.
    '''
    def __init__(self, configDict):
        self.tables = [] # Empty
        self.mapping = configDict
        self.rawData = pd.DataFrame # Empty

    def map(self):
        '''
        This public method begins the process of mapping the data
        into something that we can write to the database. First,
        the file is read from the config file (mapping), if that
        works, we begin to build a new Pandas dataframe. 
        '''
        if self._readFile(self.mapping['Settings']['FileLocation']):
            self._buildTables()
            return True
        return False

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

                # Calculate the aggregation interval based on distance
                # between points.

                df['TimeAggregationInterval'] = 0
                df['TimeAggregationIntervalUnitsID'] = 0

            else:
                df['TimeAggregationInterval'] = series['IntendedTimeSpacing']
                df['TimeAggregationIntervalUnitsID'] = series['IntendedTimeSpacingUnitID']

            #df['QualityCodeCV'] = 'None'
            df['QualityCodeCV'] = 'SDL Test Data'
            df['CensorCodeCV'] = 'Unknown'
            df['ResultID'] = series['ResultID']
            df['ValueDateTimeUTCOffset'] = self.mapping['Settings']['UTCOffset']

            #df.set_index(['DateTime'], inplace=True)
            df.ValueDateTime = pd.to_datetime(\
                                pd.Series(df.ValueDateTime))
            self.tables.append((col, df))

    def _getStartByte(self):
        '''
        getStartByte is a private method which determines the smallest
        byte number of the given columns.
        '''
        m = [value['LastByteRead'] for key,value in \
            self.mapping['Mappings'].items()]
        
        return min(m)


    def _readFile(self, path):
        '''
        readFile gathers the raw data (rawData) from the given CSV
        file (path). If rawData ends up being empty, we return False,
        otherwise we return as True.
        '''
        reader = CSVReader()

        # Collect the smallest 'LastByteRead' in the file.
        byte = self._getStartByte()

        print "Beginning from byte number", byte
        
        self.rawData = reader.byteReader(path,
                start_byte=byte,
                sep=self.mapping['Settings']['Delimiter'],
                datecol=self.mapping['Settings']['DateTimeColumnName'],
                skip=self.mapping['Settings']['HeaderRowPosition'] - 1)

        if self.rawData.empty:
            return False
        else:
            return True

    def getTables(self):
        '''
        getTables is a public method that returns a Pandas dataframe.
        It should be called after a mapping has been made.
        '''
        return self.tables
    
    def getDatabase(self):
        '''
        getDatabase is a public method that should be called before
        interacting with the database. It snatches up the database
        credentials from the YAML file object (mapping) and returns
        a named-tuple called Credentials.
        '''
        Credentials = namedtuple('Credentials', 'host, db_name,\
                                    uid, pwd')
        return Credentials(self.mapping['Database']['Address'],
                            self.mapping['Database']['DatabaseName'],
                            self.mapping['Database']['UserName'],
                            self.mapping['Database']['Password'])

