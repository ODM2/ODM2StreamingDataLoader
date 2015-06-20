"""
    File Parser

    Handles reading both CSV & TSV data
"""
import logging

import pandas as pd
from common.logger import LoggerTool
#from src.common.logger import LoggerTool

import os
from StringIO import StringIO

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

    
    def byteReader(self, filepath, start_byte, sep, datecol, skip=0):
        """
        byteReader reads from a given file (filepath) beginning at the given
        byte (start_byte). This method returns an empty Pandas dataframe on 
        failure, and a populated Pandas dataframe on success.

        Other Parameters:

        sep - A string of characters to use as separators when reading the CSV file.
        datecol - The column name which contains the dates in the CSV file.
        skip - the number of lines to skip, i.e. where the data begins in the CSV file.
        """

        df = pd.DataFrame

        try:

            with open(filepath, 'rb') as f:
                data = ''
                # If we are going to skip to the new location, we need
                # to make sure and grab the header for Pandas.
                if start_byte > 0:
                    skip = 1
                    # Without reading the whole file first, search each line
                    # for the column names. This could potentially go wrong.
                    # We should think of some better way to locate the column names.
                    line = f.next()
                    while (str(datecol + ',') not in line):
                        skip = skip + 1
                        line = f.next()
                    print "Column names are on line %d" % skip
                    data = line
                
                # Jump to the new part of the file.
                f.seek(int(start_byte))
                # Read the new data.
                data_vals = f.read()
                data = data + data_vals
                print "New Data:\n\n", data
                return None
                df = pd.read_csv(StringIO(data), header=skip,
                                    sep=str(sep), engine='python')
                df.set_index(datecol, inplace=True)
        
        except IOError as e:
            print "Skipping '%s' because of %s" % (filepath, e)
        except Exception as e2:
            # TODO: There is something fishy because if I don't watch for an Exception,
            # pandas freaks out about something. Figure out why that is.
            print e2

        return df
    
    
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












