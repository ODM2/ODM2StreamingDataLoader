"""
    File Parser

    Handles reading both CSV & TSV data
"""

import pandas as pd


class CSVReader():
    """Reads and analyizes CSV/TSV files"""

    def __init__(self):
        pass

    def csv_reader(self, filepath, sep, datetime=None, skip=0):
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

    def getPandasObjectFromFile(self, filepath, sep, skip=0):
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
            raise "FilePath cannot be null"
        if not sep:
            sep = ','

        try:
            data = pd.read_csv(filepath, sep=sep, index_col=0, parse_dates=True, skiprows=skip)
            return data.sort()
        except:
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

        if not data:
            raise "Data cannot be None"
        if not column:
            raise "Column cannot be None"
        if not datetime:
            raise "datetime cannot be None"

        col = data[column]
        sortedData = col.sort()
        try:
            start = sortedData.index.searchsorted(datetime)
            return sortedData[start:]
        except:
            return None










