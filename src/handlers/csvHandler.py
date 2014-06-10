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
        print("Analyzing...'{file}'\n".format(file=filepath))

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




