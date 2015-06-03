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
        for col in self.mapping:
            print 'col', col
            """tempdf = self.table[col]
            #DataValue, ValueDateTime
            tempdf["ResultID"] = \
                col['Mappings']['AirTemperature-C']['ResultID']
            tempdf["ValueDateTimeUTCOffset"] = \
                col['Settings']['UTCOffset']
            tempdf["CensorCodeCV"] = "Not Censored"
            tempdf["QualityCodeCV"] = 0
            if not col.calcint:
                tempdf["TimeAggregationInterval"] = col.aggint
                tempdf["TimeAggregationIntervalUnitsID"] = \
                    col.aggintunit
            else:
                #calculate the aggregation interval based on distance
                #between points
                tempdf["TimeAggregationInterval"] = 0
                tempdf["TimeAggregationIntervalUnitsID"] = 0
            """
        print 'tempdf', tempdf

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
        print self.rawData
        return self.table

