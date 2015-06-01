__author__ = 'stephanie'
import pandas as pd
from src.handlers.csvHandler import CSVReader


class Mapping():
    '''
    Model class representing a mapped pandas dataframe object.
    '''
    def __init__(self, config):
        self.table = pd.DataFrame
        self.mapping = config
        self.rawData= None
        self.readFile()
        self.buildTable()

    def buildTable(self):
        for col in self.mapping.cols:
            tempdf = self.table[col]
            #DataValue, ValueDateTime
            tempdf["ResultID"] = col.ResultID
            tempdf["ValueDateTimeUTCOffset"] = col.offset
            tempdf["CensorCodeCV"] = "Not Censored"
            tempdf["QualityCodeCV"] = 0
            if not col.calcint:
                tempdf["TimeAggregationInterval"] = col.aggint
                tempdf["TimeAggregationIntervalUnitsID"] = col.aggintunit
            else:
                #calculate the aggregation interval based on distance between points
                tempdf["TimeAggregationInterval"] = 0
                tempdf["TimeAggregationIntervalUnitsID"] = 0


    def readFile(self, path):
        reader = CSVReader()
        self.rawData=reader.reader(path, ',', 0)
        #read csv into pandas
        if self.rawData:
            return True
        else:
            return False

    def get(self):
        return self.table

