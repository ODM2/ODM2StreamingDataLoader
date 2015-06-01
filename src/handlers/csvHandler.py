"""
    File Parser

    Handles reading both CSV & TSV data
"""
import logging

import pandas as pd
from ..common.logger import LoggerTool


tool = LoggerTool()
logger = tool.setupLogger(__name__, __name__ + '.log', 'w', logging.DEBUG)


class CSVReader():
    """Reads and analyzes CSV/TSV files"""

    def __init__(self):
        pass
    '''
    def reader(self, filepath, sep, datetime=None, skip=0):
        """Reads csv into pandas object

        Parameters
        ----------
        filepath : string
            path to csv file
        datetime : datetime
            limits output to dates occurring after specified date
        skip : int
            indicates the skip amount to begin reading

        Returns
        -------
            pandas.core.frame.DataFrame
        """

        if not filepath:
            raise "FilePath cannot be null"


        data = pd.read_csv(filepath, sep=sep, index_col=0, parse_dates=True, skiprows=skip)
        # print("Analyzing...'{file}'\n".format(file=filepath))

        if not data.empty:
            sortedData = data.sort()
            if datetime:
                try:
                    return sortedData[datetime:]
                except KeyError:
                    start = sortedData.index.searchsorted(datetime)
                    return sortedData[start:]

            else:
                return sortedData
        return None
    '''
    def reader(self, filepath, sep, skip=0):
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
        print ("READER PATH: ", filepath)
        if not filepath:
            raise RuntimeError("FilePath cannot be null")

        logger.debug("filepath: %s" % filepath)
        logger.debug("sep: %s" % sep)
        logger.debug("skiprows: %s" % skip)

        try:
            df = pd.read_csv(filepath, header=0, sep=str(sep))
            #df = pd.concat(data)
            df.set_index(['DateTime'], inplace=True)
            logger.debug("dataframe: %s" % df)
            return df

        except Exception as e:
            print e
            logger.fatal(e)
            return None

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












