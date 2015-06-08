__author__ = 'stephanie'
import pandas as pd

from src.handlers.csvHandler import CSVReader


class Mapping():
    '''
    Model class representing a mapped pandas dataframe object.

    rawData : pandas.core.frame.DataFrame - Raw CSV data from the
                                            given file.
    table : pandas.core.frame.DataFrame - The finnished table to
                                            write to the database.
    mapping : dict - The YAML configuration mapping.
    '''
    def __init__(self, configDict):
        self.table = pd.DataFrame # Empty
        self.mapping = configDict
        self.rawData = pd.DataFrame # Empty
        if self.readFile(self.mapping['Settings']['FileLocation']):
            self.buildTable()

    def buildTable(self):
        tempdf = {}
        for col in self.mapping['Mappings']:
            print '$%$%$%$%$ col $%$%$%$%$', col
            tempdf = {'DataValue': self.rawData[col].values}
            df = pd.DataFrame(dict([ (k, pd.Series(v)) for k,v in tempdf.iteritems() ]))
            if self.mapping['Mappings'][col]['CalculateAggInterval']:
                # Calculate the aggregation interval based on distance
                # between points.

                df['AggregationInterval'] = 0;
                df['AggregationIntervalUnitsID'] = 0

            else:
                df['AggregationInterval'] = self.mapping['Mappings'][col]['IntendedTimeSpacing'];
                df['AggregationIntervalUnitsID'] = self.mapping['Mappings'][col]['IntendedTimeSpacingUnitID'];
                
            df['DateTime'] = self.rawData.index.values
            df['QualityCode'] = 'None'
            df['CensorCode'] = 'Unknown'
            df['ResultID'] = self.mapping['Mappings'][col]['ResultID']
            df['UTCOffset'] = self.mapping['Settings']['UTCOffset']
            
            df.set_index(['DateTime'], inplace=True)
            
            print df


    def readFile(self, path):
        reader = CSVReader()
        self.rawData = reader.reader(path,\
            sep=self.mapping['Settings']['Delimiter'],\
            skip=self.mapping['Settings']['HeaderRowPosition'] - 1)
        #read csv into pandas
        if self.rawData.empty:
            return False
        else:
            return True

    def get(self):
        return self.table

