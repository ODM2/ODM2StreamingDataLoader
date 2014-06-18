__author__ = 'Jacob'

from handlers.jsonHandler import JsonHandler as json
from handlers.csvHandler import CSVReader as csv

class LoaderModel():
    """Model for Loader"""
    def __init__(self, args):
        """

        :param args:
            :type ArgumentParser:
        :return:
        """
        self.jsonFile = args.jsonFile
        self.dataFile = args.dataFile

    def _validateJsonFile(self):
        pass

    def _validateCSVFile(self):
        pass



