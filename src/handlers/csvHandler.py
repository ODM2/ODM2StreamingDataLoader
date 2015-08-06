import os
import urllib2
import pandas as pd
import tempfile
import logging
from StringIO import StringIO

from controllers.FileSizeReader import FileSizeReader

logger = logging.getLogger('SDL_logger')

class CSVReader():
    '''
    Reads and analyzes CSV/TSV files.

    '''
    
    def dataFrameReader(self, filepath, header=0, sep=None, dataBegin=0):
        
        if filepath.startswith('http://'):
            response = urllib2.urlopen(filepath)
            data = response.read()
            filepath = StringIO(data)
        
        df = pd.read_csv(filepath, header=(header - 1), sep=sep)
        df = df.ix[(dataBegin - header) - 1:]
        return df

    def getData(self, df):
        return df.applymap(unicode).values.tolist()
    
    def getColumnNames(self, df):
        return df.columns.values.tolist()
    

    def byteReader(self, filepath, start_byte, datecol, header=0, sep=None, dataBegin=0):
    #def byteReader(self, filepath, start_byte, sep, datecol, skip=0):
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
        try:
            if filepath.startswith('http://'):
                response = urllib2.urlopen(filepath)
                data = response.read()
                #filepath = StringIO(data)

                temp = tempfile.NamedTemporaryFile()
                try:
                    temp.write(data)
                    temp.seek(0)
                finally:
                    print temp.name
                    df = self.byteReader(temp.name, start_byte, datecol, header, sep, dataBegin)
                    temp.close()
                    return df
                #return self.byteReader(filepath, start_byte, datecol, header, sep, dataBegin)
        except AttributeError:
            print 'not a text'

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
                    for i in range(header):
                        header_names = f.next()

                    f.seek(int(start_byte))
                    new_data = f.read()
                    print 'new_data', new_data 
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
                                        header=(header - 1),
                                        sep=str(sep),
                                        engine='python')
                    df = df.ix[(dataBegin - header) - 1:]
                    df.set_index(datecol, inplace=True)

        
        except IOError as e:
            logger.error('Skipping "%s" because of %s' % (filepath, e))
        except Exception as e2:
            # TODO: There is something fishy because if I don't
            # watch for an Exception, Pandas freaks out about
            # something. Figure out why that is.
            logger.error('Exception: %s' % e2.message)

        return df
    

