from __future__ import print_function
from argparse import ArgumentParser
from os import listdir, getcwd
from os.path import join, isfile

__author__ = 'Jacob'

from src.models.loaderModel import LoaderModel


class TestStreamingDataLoader():
    def setup(self):
        parser = ArgumentParser(description="StreamDataLoader")
        parser.add_argument('-c', '--config', dest="jsonFile", help="Json config file", required=True, action="store")
        parser.add_argument('-d', '--data', dest="dataFile", help="CSV/TSV formatted file", required=False,
                            action="store")
        jsonSamplePath = join(getcwd(), 'test_app', 'configFile')
        print("Return Files: ", returnFiles(jsonSamplePath))
        assert jsonSamplePath
        self.args = parser.parse_args(['-c', returnFiles(jsonSamplePath)[0]])
        assert self.args
        assert self.args.jsonFile
        self.model = LoaderModel(config=self.args.jsonFile)
        assert self.model
        assert self.model.jsonFile

    def test_readJsonConfig(self):
        ## parse json configuration file
        model = self.model
        configObj = model.readJsonConfig()
        assert configObj
        assert model.config
        configObj = model.readJsonConfig(model.jsonFile)
        assert configObj
        assert model.config

    def test_queringBasedOnId(self):
        model = self.model
        assert model
        configObj = model.readJsonConfig()
        assert configObj
        result = model.queryBasedOnId(1, configObj)
        assert result
        assert result.ID == "1"
        result = model.queryBasedOnId(2, configObj)
        assert result
        assert result.ID == "2"
        result = model.queryBasedOnId(3, configObj)
        assert result
        assert result.ID == "3"

    def test_extractDataBasedOnJsonFile(self):
        model = self.model
        configObj = model.readJsonConfig()
        ## extract data from the specified datafile based on the json configuration provided
        extractedData = model.readDataFileFromConfig(1)
        extractedData = model.readDataFileFromConfig(2, configObj)
        extractedData = model.readDataFileFromConfig(3, configObj)

    def debug(self, model):
        for i in model.jsonConfigObjectList:
            print('Fields: ', i._fields)
            print()
            d = i._asdict()
            print("Dumping items in: ", d["ID"])
            for k, v in d.items():
                print(k, ": ", v)
            print()

            print("Printing file contents: ")
            print("ID: ", i.ID)
            print("File", i.FileLocation)

        id = [t for t in model.jsonConfigObjectList if t.ID == '2']
        print("Queried ID: ", id)


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

