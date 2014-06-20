"""Unittests for file reader"""

from __future__ import print_function
from datetime import datetime
from os import listdir, getcwd
from os.path import join, isfile

from streamdata.handlers.csvHandler import CSVReader


class TestFileReader:
    def setup(self):
        self.path = join(getcwd(), 'test_handlers', 'test_csvHandler', 'csvFiles')
        #print ("Path at Setup: ", self.path)
        self.fileReader = CSVReader()
        assert self.path is not None
        self.files = returnFiles(self.path)
        assert self.files is not None
        assert len(self.files) > 0

    def test_readCSV(self):
        ## SDLTest.csv
        #data = self.fileReader.reader(self.files[1], ',', datetime(day=3, month=4, year=2011))
        data = self.fileReader.reader(self.files[1], ',')
        if data.empty:
            assert False
        assert data is not None
        assert len(data) > 0

    def test_readTSV(self):
        ## random TSV style document example 2013/08/18
        data = None
        assert data is None
        #data = self.fileReader.reader(self.files[0], '\t', datetime(day=19, month=6, year=2013))
        data = self.fileReader.reader(self.files[0], '\t')
        if data.empty:
            assert False
        #data2 = self.fileReader.reader(self.files[0], '\t', datetime(day=3, month=4, year=2013))
        data2 = self.fileReader.reader(self.files[0], '\t')
        if data2.empty:
            assert False
        assert data is not None
        assert len(data) > 0 and len(data2) > 0

    def test_readCSV_example1(self):
        ## Treeline_HrlySummary_2014.csv
        #data = self.fileReader.reader(self.files[2], ',', datetime(day=15, month=3, year=2014), 19)
        data = self.fileReader.reader(self.files[2], ',', 19)
        if data.empty:
            assert False
        assert data is not None
        assert len(data) == 439 or len(data) > 0

    def test_readCSV_example2(self):
        ## Treeline_HrlySummary_2014_2.csv
        #data = self.fileReader.reader(self.files[3], ',', datetime(day=22, month=1, year=2014), 19)
        data = self.fileReader.reader(self.files[3], ',', 19)
        if data.empty:
            assert False
        assert data is not None
        assert len(data) == 7 or len(data) > 0


## Debugging
def returnFiles(path):
    """Collects a list of files within a file

    :rtype: list
    """
    if path:
        try:
            onlyFiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
            #print("onlyFiles: ", onlyFiles)
            return onlyFiles
        except WindowsError:
            pass
            #print("Path: ", listdir(path))
    return None