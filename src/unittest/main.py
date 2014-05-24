"""Streaming Data Loader Python
                      *     .--.
                           /# /  `
          +               |# |
                 '         \# \__,
             *          +   '--'  *
                 +   /\
    +              .'  '.   *
           *      /======\      +
                 ;:.  _   ;
                 |:. (_)  |
                 |:.  _   |
       +         |:. (_)  |          *
                 ;:.      ;
               .' \:.    / `.
              / .-'':._.'`-. \
              |/    /||\    \|
            _..---/-```***--.._
      _.-'``                    ``'-._
    -'                                '-

"""

from __future__ import print_function
from datetime import date, datetime

from src.FileReader import FileReader


if __name__ == "__main__":
    c = FileReader(path='../csvFiles/')
    #files = c.returnFiles()

    ## SDLTest.csv
    data = c.csv_reader('../csvFiles/SDLTest.csv', ',', datetime(day=3, month=4, year=2011))
    if data.empty:
        print("../csvFiles/SDLTest.csv")

    ## random TSV style document example 2013/08/18
    data = c.csv_reader('../csvFiles/sampleTSV.txt', '\t', datetime(day=18, month=8, year=2013))
    if data.empty:
        print("../csvFiles/sampleTSV.txt failed")

    ## Treeline_HrlySummary_2014.csv
    data = c.csv_reader('../csvFiles/Treeline_HrlySummary_2014.csv', ',', datetime(day=2, month=2, year=2014), 19)
    if data.empty:
        print("../csvFiles/Treeline_HrlySummary_2014.csv failed")

    print("Done!")

    #print(files[1], " Result: ", data.count()) if data and not data.empty else ""
