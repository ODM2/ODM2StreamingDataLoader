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

        myList = load['File']
        myList2 = load2['File']

        obj = self.json.toConfigObject(myList)
        for x in obj:
            assert isnamedtupleinstance(x)

        obj = self.json.toConfigObject(myList2)
        for x in obj:
            assert isnamedtupleinstance(x)

        #print ()
        #for x in obj[0]._fields:
        #    print(x, ": ", getattr(obj[0], x))



def isnamedtupleinstance(x):
    t = type(x)
    b = t.__bases__
    if len(b) != 1 or b[0] != tuple: return False
    f = getattr(t, '_fields', None)
    if not isinstance(f, tuple): return False
    return all(type(n) == str for n in f)


def returnFiles(path):
    """Collects a list of files within a file

    :rtype: list
    """
    if path:
        try:
            onlyFiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
            # print("onlyFiles: ", onlyFiles)
            return onlyFiles
        except WindowsError:
            pass
            # print("Path: ", listdir(path))
    return None


def getTestJsonExample():
    """

    :return:
    """
    path = 'C:\\Users\\Jacob\\Documents\\StreamDataLoader\\tests\\test_common\\test_filereader\\csvFiles\\Treeline_HrlySummary_2014.csv'

    test = """{
        "File": [
          {
            "ID": "1",
            "ServerAddress": "Arroyo.uwrl.usu.edu",
            "DatabaseName": "TestODM2",
            "UserName": "ODM",
            "Pword": "odm",
            "FileLocationType": "Local",
            "FileLocation": "%r",
            "Delimiter": "<Comma Delimited>",
            "HeaderRowPosition": "20",
            "DataRowPosition": "21",
            "SchedulePeriod": "1 minutes",
            "ScheduleBeginning": "6/4/2014 11:00:00 AM",
            "UTCDateTimeColumnName": "DateTime",
            "DaylightSavingsTime": "False",
            "IncludeOldData": "False",
            "LastUpdate": "1/1/0001 12:00:00 AM",
            "ValueColumnName": "Precipitation-mm",
            "Site": {
              "ID" : "",
              "Code" : ""
              },
            "SamplingFeature" : {
              "ID" : "",
              "Code" : ""
              },
            "Variable": {
              "ID" : "",
              "Code" : ""
              },
            "OffsetTypeID": "2",
            "OffsetValue": "5",
            "Method": {
                "ID" : "",
                "Code" : ""
              },
            "DeploymentAction": {
              "ID" : "",
              "Code" : ""
              },
            "ProcessingLevel": {
              "ID" : "",
              "Code" : ""
              },
              "FileStartOfInterval": "True",
              "DatabaseStartOfInterval": "True",
              "IntervalLength": "00:00:00"
          }
        ]
    }""" % (path)

    return json.loads(test)
