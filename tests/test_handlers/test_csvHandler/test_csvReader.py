"""Unittests for file reader"""

from __future__ import print_function
import datetime
import os
from os import listdir, getcwd
from os.path import join, isfile

from src.handlers.csvHandler import CSVReader


class TestFileReader:
    def setup(self):
        self.example_path = os.path.join(os.getcwd(), 'test_handlers', 
                                 'test_csvHandler', 'csvFiles')
        self.fileReader = CSVReader()

    def test_readCSV(self):
        ## SDLTest.csv
        #data = self.fileReader.reader(self.files[1], ',', datetime(day=3, month=4, year=2011))
        SDLTest = os.path.join(self.example_path, 'SDLTest.csv')
        assert SDLTest
        data = self.fileReader.reader(SDLTest, ',')
        if data.empty:
            assert False
        assert data is not None
        assert len(data) > 0

    def test_readTSV(self):
        ## random TSV style document example 2013/08/18
        data = None
        assert data is None
        #data = self.fileReader.reader(self.files[0], '\t', datetime(day=19, month=6, year=2013))
        SampleTSV = os.path.join(self.example_path, 'sampleTSV.txt')

        assert SampleTSV
        data = self.fileReader.reader(SampleTSV, '\t')
        if data.empty:
            assert False
        #data2 = self.fileReader.reader(self.files[0], '\t', datetime(day=3, month=4, year=2013))
        data2 = self.fileReader.reader(SampleTSV, '\t')
        if data2.empty:
            assert False
        assert data2 is not None
        assert len(data) > 0 and len(data2) > 0

    def test_readCSV_example1(self):
        ## Treeline_HrlySummary_2014.csv
        #data = self.fileReader.reader(self.files[2], ',', datetime(day=15, month=3, year=2014), 19)
        TreeLine_1 = os.path.join(self.example_path, 'Treeline_HrlySummary_2014.csv')
        assert TreeLine_1
        data = self.fileReader.reader(TreeLine_1, ',', 19)
        if data.empty:
            assert False
        assert data is not None
        assert len(data) == 439 or len(data) > 0

    def test_readCSV_example2(self):
        ## Treeline_HrlySummary_2014_2.csv
        #data = self.fileReader.reader(self.files[3], ',', datetime(day=22, month=1, year=2014), 19)
        TreeLine_2 = os.path.join(self.example_path, 'Treeline_HrlySummary_2014_2.csv')
        assert TreeLine_2
        data = self.fileReader.reader(TreeLine_2, ',', 19)
        if data.empty:
            assert False
        assert data is not None
        assert len(data) == 7 or len(data) > 0

    def test_getColumn(self):
        TreeLine_1 = os.path.join(self.example_path, 'Treeline_HrlySummary_2014.csv')
        assert TreeLine_1
        data = self.fileReader.reader(TreeLine_1, ',', 19)
        # print ("Data: ", data)
        if data.empty:
            assert False
        dt = datetime.datetime(2014, 3, 23)
        # print (dt)
        # self.fileReader.getColumn(data, 'DateTime', dt)

    def test_load_giga_csv(self):
        import timeit

        start = timeit.default_timer()
        GigaCSV = os.path.join(self.example_path, 'Treeline_HrlySummary_2014_giga.csv')
        assert GigaCSV
        data = self.fileReader.reader(GigaCSV, ',', 19)
        end = timeit.default_timer() - start
        print ("TimeTaken: ", end)

        if data.empty:
            assert False
        # print (data[:10])






### Debugging
#def returnFiles(path):
#    """Collects a list of files within a file
#
#    :rtype: list
#    """
#    if path:
#        onlyFiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
#        #print("onlyFiles: ", onlyFiles)
#        return onlyFiles
#    return None
