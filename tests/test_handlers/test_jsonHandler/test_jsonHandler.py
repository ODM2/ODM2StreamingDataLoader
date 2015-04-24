# !/usr/bin/python
from __future__ import print_function
import json
from os import listdir, getcwd, remove
from os.path import join, isfile

from src.handlers.jsonHandler import JsonHandler as js


class TestJsonHandler:
    def setup(self):
        self.path = join(getcwd(), 'test_handlers', 'test_jsonHandler', 'jsonFiles')
        assert self.path
        self.json = js()
        assert self.json
        self.files = returnFiles(self.path)
        assert self.files
        assert len(self.files) > 0
        self.load = self.json.readJsonFile(self.files[0])


    def test_readJsonFile(self):
        assert self.load
        cmpValue = getTestJsonExample()
        assert cmpValue
        if self.load == cmpValue:
            assert True
        else:
            from warnings import warn

            warn("Didn't pass the readJsonFile. File format could have changed!!!!", UserWarning)

    def test_writeJsonFile(self):
        assert self.load
        output = 'test'
        assert output
        result = self.json.writeJsonFile(self.load, output)
        if result:
            assert True
            remove(output)
        else:
            assert False

    def test_toConfigObject(self):
        load = self.json.readJsonFile(self.files[0])
        assert load
        load2 = self.json.readJsonFile(self.files[1])
        assert load2

        obj = self.json.toConfigObject(load)
        for x in obj:
            assert isnamedtupleinstance(x)

        obj2 = self.json.toConfigObject(load2)
        for x in obj2:
            assert isnamedtupleinstance(x)

        print("Object: ", obj[0]._fields)
        field = obj[0]._asdict()
        print("type Field: ", type(field))

        print(field['DataSeriesMapping'])

        # get each mapping
        for k, v in field['DataSeriesMapping'].items():
            print(k, ": ", v)
        print()


def isnamedtupleinstance(x):
    t = type(x)
    b = t.__bases__
    if len(b) != 1 or b[0] != tuple: 
        return False
    f = getattr(t, '_fields', None)
    if not isinstance(f, tuple): 
        return False
    return all(type(n) == str for n in f)


def returnFiles(path):
    """Collects a list of files within a file

    :rtype: list
    """
    if path:
        onlyFiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
        # print("onlyFiles: ", onlyFiles)
        return onlyFiles
        # print("Path: ", listdir(path))
    return None


def getTestJsonExample():
    """

    :return:
    """
    path = 'C:\\Users\\Jacob\\Documents\\StreamDataLoader\\tests\\test_common\\test_filereader\\csvFiles\\Treeline_HrlySummary_2014.csv'

    test = """
    {
    "File": [
      {
        "ID": "3",
        "DataRowPosition": "21",
        "DataSeriesMapping": [
          {
            "DatabaseStartOfInterval": "True",
            "FileStartOfInterval": "True",
            "IntervalLength": "00:00:00",
            "MethodID": "32",
            "OffsetTypeID": "2",
            "OffsetValue": "0",
            "QualityControlLevelID": "-9999",
            "SiteID": "1",
            "SourceID": "1",
            "ValueColumnName": "Precipitation-mm",
            "VariableID": "4"
          },
          {
            "DatabaseStartOfInterval": "True",
            "FileStartOfInterval": "True",
            "IntervalLength": "00:00:00",
            "MethodID": "32",
            "OffsetTypeID": "2",
            "OffsetValue": "0",
            "QualityControlLevelID": "1",
            "SiteID": "3",
            "SourceID": "9",
            "ValueColumnName": "AirTemperature-C",
            "VariableID": "85"
          },
          {
            "DatabaseStartOfInterval": "True",
            "FileStartOfInterval": "True",
            "IntervalLength": "00:00:00",
            "MethodID": "31",
            "OffsetTypeID": "2",
            "OffsetValue": "0",
            "QualityControlLevelID": "1",
            "SiteID": "13",
            "SourceID": "1",
            "ValueColumnName": "SolarRadiation-Watts/m2",
            "VariableID": "90"
          },
          {
            "DatabaseStartOfInterval": "True",
            "FileStartOfInterval": "True",
            "IntervalLength": "00:00:00",
            "MethodID": "1",
            "OffsetTypeID": "2",
            "OffsetValue": "0",
            "QualityControlLevelID": "-9999",
            "SiteID": "3",
            "SourceID": "1",
            "ValueColumnName": "NetRadiation-Watts/m2",
            "VariableID": "1"
          },
          {
            "DatabaseStartOfInterval": "True",
            "FileStartOfInterval": "True",
            "IntervalLength": "00:00:00",
            "MethodID": "1",
            "OffsetTypeID": "2",
            "OffsetValue": "0",
            "QualityControlLevelID": "-9999",
            "SiteID": "24",
            "SourceID": "1",
            "ValueColumnName": "RelativeHumidity-%%",
            "VariableID": "1"
          },
          {
            "DatabaseStartOfInterval": "True",
            "FileStartOfInterval": "True",
            "IntervalLength": "00:00:00",
            "MethodID": "1",
            "OffsetTypeID": "2",
            "OffsetValue": "0",
            "QualityControlLevelID": "-9999",
            "SiteID": "24",
            "SourceID": "1",
            "ValueColumnName": "WindDirection-Degree",
            "VariableID": "1"
          },
          {
            "DatabaseStartOfInterval": "True",
            "FileStartOfInterval": "True",
            "IntervalLength": "00:00:00",
            "MethodID": "1",
            "OffsetTypeID": "2",
            "OffsetValue": "0",
            "QualityControlLevelID": "-9999",
            "SiteID": "4",
            "SourceID": "1",
            "ValueColumnName": "WindSpeed-m/s",
            "VariableID": "2"
          },
          {
            "DatabaseStartOfInterval": "True",
            "FileStartOfInterval": "True",
            "IntervalLength": "00:00:00",
            "MethodID": "1",
            "OffsetTypeID": "2",
            "OffsetValue": "0",
            "QualityControlLevelID": "-9999",
            "SiteID": "17",
            "SourceID": "7",
            "ValueColumnName": "SnowDepth-cm",
            "VariableID": "5"
          }
        ],
        "DatabaseName": "TestODM",
        "DateTimeColumnName": "None",
        "DaylightSavingsTime": "False",
        "Delimiter": "<Comma Delimited>",
        "FileLocation": "%r",
        "FileLocationType": "Local",
        "HeaderRowPosition": "20",
        "IncludeOldData": "False",
        "LastUpdate": "1/1/0001 12:00:00 AM",
        "Pword": "odm",
        "ScheduleBeginning": "6/18/2014 10:00:00 AM",
        "SchedulePeriod": "1 minutes",
        "ServerAddress": "arroyo.uwrl.usu.edu",
        "TimeZone": "None",
        "UTCDateTimeColumnName": "DateTime",
        "UserName": "ODM"
      }
    ]
} """ % path

    return json.loads(test)
