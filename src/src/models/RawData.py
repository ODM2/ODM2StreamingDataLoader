
import pandas as pd
import logging

from common.logger import LoggerTool

tool = LoggerTool()
logger = tool.setupLogger(__name__, __name__ + '.log', 'w', logging.DEBUG)

class RawData():
    """ Raw CSV/TSV data model """

    def __init__(self, filePath):
        self.rawData = None
        if not self.readFile(filePath):
            logger.fatal("Could not read data file.")


    def readFile(self, path):
        try:
            self.rawData = pd.read_csv(path)
        except Exception as e:
            logger.fatal(e)
            return False
        return True
    
    def get(self):
        return self.rawData
