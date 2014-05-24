"""
    File Parser

    Handles reading both CSV & TSV data
"""

from os import listdir
from os.path import isfile, join

import pandas as pd


class FileReader():
    """Reads and analyizes CSV/TSV files"""

    def __init__(self, path):
        self.path = path

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
        print("Analyzing...'{file}'\n".format(file=filepath))

        if not data.empty:
            if datetime:
                try:
                    data.sort()
                    parsedData = data[datetime:]
                    return parsedData
                except KeyError:
                    # TODO make an approximation if the date isn't in the list.
                    # https://stackoverflow.com/questions/
                    # 16175874/python-pandas-dataframe-slicing-by-date-conditions
                    return data

            else:
                return data
        return None

    ## Debugging
    def returnFiles(self):
        """Collects a list of files within a file

        :rtype: list
        """
        if self.path:
            onlyFiles = [join(self.path, f) for f in listdir(self.path) if isfile(join(self.path, f))]
            print("onlyFiles: ", onlyFiles)
            return onlyFiles
        return None


