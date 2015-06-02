__author__ = 'stephanie'
import pandas as pd

from src.handlers.csvHandler import CSVReader


class Mapping():
    '''
    Model class representing a mapped pandas dataframe object.

    rawData : pandas.core.frame.DataFrame
    table : pandas.core.frame.DataFrame
    mapping : dict - The YAML configuration mapping.
    '''
    def __init__(self, configDict):
        self.table = pd.DataFrame
        self.mapping = configDict
        self.rawData = pd.DataFrame
        self.readFile(self.mapping['Settings']['FileLocation'])
        #self.buildTable()

    def buildTable(self):
        tempdf = {}
        for col in self.mapping:
            tempdf = self.table[col]
            #DataValue, ValueDateTime
            tempdf["ResultID"] = \
                col['Mappings']['AirTemperature-C']['ResultID']
            tempdf["ValueDateTimeUTCOffset"] = col['Settings']['UTCOffset']
            tempdf["CensorCodeCV"] = "Not Censored"
            tempdf["QualityCodeCV"] = 0
            if not col.calcint:
                tempdf["TimeAggregationInterval"] = col.aggint
                tempdf["TimeAggregationIntervalUnitsID"] = col.aggintunit
            else:
                #calculate the aggregation interval based on distance between points
                tempdf["TimeAggregationInterval"] = 0
                tempdf["TimeAggregationIntervalUnitsID"] = 0
        print tempdf

    def readFile(self, path):
        reader = CSVReader()
        self.rawData = reader.reader(path, sep=',', skip=0)
        #read csv into pandas
        if self.rawData.empty:
            return False
        else:
            return True

    def get(self):
        print self.rawData
        return self.table

