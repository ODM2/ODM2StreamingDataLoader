
__author__ = 'Denver'

import sys
import logging



#sys.path.append('/home/denver/Documents/ODM2PythonAPI')
sys.path.append('/Users/stephanie/Dev/ODM2PythonAPI')
#import src
#from src.api.ODM2.services.createService import CreateODM2
from src.api.ODMconnection import dbconnection
#from src.api.ODM2.services.readService import ReadODM2
from src.api.ODM2.services import *

#sys.path.insert(0, '/Users/stephanie/DEV/ODM2PythonAPI/src')
#from api.ODM2.services.createService import createResults
#from api.ODMconnection import dbconnection

logger = logging.getLogger('SDL_logger')

class Database:
    '''
    This class uses the ODM2 API to connect and interact with an
    ODM2 database.
    '''
    
    def createConnection(self, Credentials):
        '''
        createConnection is a public method that should be called 
        after obtaining login credentials (Credentials) and is used
        to set up a new connection to an ODM2 database.
        '''
        self.session_factory = \
            dbconnection.createConnection('mysql', Credentials.host,
                                            Credentials.db_name,
                                            Credentials.uid,
                                            Credentials.pwd)
        if not self.session_factory:
            return False
        
        return True


    def write(self, data, duplicateValuesCheck):
        '''
        write is a public method that is used to write data to an 
        ODM2 database. This method should only be called once a valid
        database connection has been established.
        '''
        cr = CreateODM2(self.session_factory)
        
        finished_data = data

        if duplicateValuesCheck == True:
            logger.info('Performing duplicate database value check. (This affects performance).')
            # Check if data is already in the database.
            rc = ReadODM2(self.session_factory)
            dt = rc.getResultValidDateTime(data['ResultID'][0])
            finished_data = data[data['ValueDateTime'] > dt[0]]

        if cr.createTimeSeriesResultValues(finished_data) is None:
            return False
        return True

    def getNoDataValue(self, resultID):
        '''
        getNoDataValue querys the ODM2 API and returns
        the "No data value" for the given ResultID.
        '''

        rc = ReadODM2(self.session_factory)
        result = rc.getResultByID(int(resultID))
        return result.VariableObj.NoDataValue

    def updateDateTime(self, seriesId, dateTime):
        '''
        updateDateTime uses the ODM2 API to update the latest
        date time added to the database.
        '''
        cr = UpdateODM2(self.session_factory)
        cr.updateResultValidDateTime(seriesId, dateTime)
        return True
