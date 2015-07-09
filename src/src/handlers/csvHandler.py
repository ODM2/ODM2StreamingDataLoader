import os
import pandas as pd
import logging
from StringIO import StringIO

from controllers.FileSizeReader import FileSizeReader

logger = logging.getLogger('SDL_logger')

class CSVReader():
    """Reads and analyzes CSV/TSV files"""

    '''
    def reader(self, filepath, sep, datecol, skip=0, columns= None):

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
            df = pd.read_csv(filepath, header=skip, sep=str(sep), engine='c', index_col = datecol, usecols= [datecol]+columns, parse_dates = True)
    #skiprows : list-like or integer Row numbers to skip (0-indexed) or number of rows to skip (int) at the start of the file
            #df.set_index(datecol, inplace=True)
            #logger.debug("dataframe: %s" % df)

            return df

        except Exception as e:
            print e
            #logger.fatal(e)
            return pd.DataFrame
    '''
    
    def byteReader(self, filepath, start_byte, sep, datecol, skip=0):
        '''
        byteReader reads from a given file (filepath) beginning at the
        given byte (start_byte). This method returns an empty Pandas
        dataframe on failure, and a populated Pandas dataframe on
        success.

        Other Parameters:

        sep - A string of characters to use as separators when reading
            the CSV file.
        datecol - The column name which contains the dates in the CSV
                file.
        skip - the number of lines to skip, i.e. where the data begins
             in the CSV file.
        '''

        df = pd.DataFrame
        
        logger.debug('File size: %d bytes.' % os.path.getsize(filepath))
        logger.debug('Start byte: %d.' % start_byte)

        # Check if the data has been modified.
        if int(os.path.getsize(filepath)) < start_byte:
            logger.info('Previous data has been modified.')
            start_byte = 0
        
        try:

            with open(filepath, 'rb') as f:
                
                logger.info('Reading from byte %d.' % start_byte)
                # If we are going to skip to the new location, we need
                # to make sure and grab the header for Pandas.
                if start_byte > 0:
                    header_names = ''
                    # Read lines from the file until we get the 
                    # CSV headers. This loop should not be too
                    # expensive because the headers are almost
                    # always gaurenteed to be within about 100
                    # lines.
                    for i in range(skip+1):
                        header_names = f.next()

                    f.seek(int(start_byte))
                    new_data = f.read()
                
                    finished_data = header_names + new_data
                    
                    if new_data:
                        logger.info('New Data:\n%s' % finished_data)
                    else:
                        logger.info('No new data.')

                    df = pd.read_csv(StringIO(finished_data),
                                        sep=str(sep),
                                        engine='python')
                    df.set_index(datecol, inplace=True)
                else:
                    # Just begin at the start of the file.
                    f.seek(0)
                    finished_data = f.read()
                    
                    logger.info('New data:\n%s' % finished_data)
                    
                    df = pd.read_csv(StringIO(finished_data),
                                        header=skip,
                                        sep=str(sep),
                                        engine='python')
                    df.set_index(datecol, inplace=True)

        
        except IOError as e:
            logger.error('Skipping "%s" because of %s' % (filepath, e))
        except Exception as e2:
            # TODO: There is something fishy because if I don't
            # watch for an Exception, Pandas freaks out about
            # something. Figure out why that is.
            logger.error('Exception: %s' % e2.message)

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












