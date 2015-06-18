"""
    File Parser

    Handles reading both CSV & TSV data
"""
import logging

import pandas as pd
from common.logger import LoggerTool
#from src.common.logger import LoggerTool

import os

tool = LoggerTool()
logger = tool.setupLogger(__name__, __name__ + '.log', 'w', logging.DEBUG)

from controllers.FileSizeReader import FileSizeReader

class CSVReader():
    """Reads and analyzes CSV/TSV files"""

    def __init__(self):
        pass
    
    def reader(self, filepath, sep, datecol, skip=0):
        """Reads csv into pandas object

        Parameters
        ----------
        filepath : string
            path to csv file
        skip : int
            indicates the skip amount to begin reading

        Returns
        -------
            pandas.core.frame.DataFrame
        """
        if not filepath:
            raise RuntimeError("FilePath cannot be null")

        try:

            df = pd.read_csv(filepath, header=skip,
                                sep=str(sep), engine='python')
            df.set_index(datecol, inplace=True)

            return df

        except Exception as e:
            print e
            #logger.fatal(e)
            return pd.DataFrame

    
    def byteReader(self, filepath, sep, datecol, skip=0):
        """
            byteReader -- Reads a CSV file beginning from the
                            end of the last time it was read.
        """

        fsr = FileSizeReader('./fileSize.dat')

        # Get the size of the file last time we read the data.
        size_last_read = fsr.getSizeByName(filepath)

        with open(filepath, 'rb') as f:
            # Jump to the new part of the file.
            f.seek(int(size_last_read))
            # Read the new data.
            data = f.read()
            print data


        # Store the file size including the new data.
        fsr.setSizeByName(filepath)
    
    
    def getColumn(self, data, column, datetime):
        """Obtain a specified column from the most recent datetime

        :param data:
            :type pandas.core.frame.DataFrame:
        :param column:
            :type pandas.core.index.Index:
        :param datetime:
            :type datetime object:
        :return :
        """

        if data.empty:
            raise RuntimeError("Data cannot be None")
        if not column:
            raise RuntimeError("Column cannot be None")
        if not datetime:
            raise RuntimeError("datetime cannot be None")

        col = data[column]
        sortedData = col.sort()
        try:
            start = sortedData.index.searchsorted(datetime)
            return sortedData[start:]
        except:
            return None

    def getLatestDataFrameByDate(self, data, dt_value):
        """

        :param data:
            :type pandas.core.frame.DataFrame:
        :param dt_value:
            :type datetime object:
        :return:
            pandas DataFrame
        """

        if data.empty:
            raise RuntimeError("Data cannot be None")
        if not dt_value:
            raise RuntimeError("datetime cannot be None")












