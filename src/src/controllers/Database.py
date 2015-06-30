
__author__ = 'Denver'

import sys


sys.path.append('/home/denver/Documents/ODM2PythonAPI')
from src.api.ODM2.services.createService import CreateODM2
from src.api.ODMconnection import dbconnection
from src.api.ODM2.services.readService import ReadODM2

#sys.path.insert(0, '/Users/stephanie/DEV/ODM2PythonAPI/src')
#from api.ODM2.services.createService import createResults
#from api.ODMconnection import dbconnection


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
        #print Credentials.host
        self.session_factory = \
            dbconnection.createConnection('mysql', Credentials.host,
                                            Credentials.db_name,
                                            Credentials.uid,
                                            Credentials.pwd)
        if not self.session_factory:
            return False

        print "[INFO] Connected!"
        print "\tHost:", Credentials.host
        print "\tDatabase: ", Credentials.db_name
        print "\tUser: ", Credentials.uid
        
        return True


    def write(self, data):
        '''
        write is a public method that is used to write data to an 
        ODM2 database. This method should only be called once a valid
        database connection has been established.
        '''
        cr = CreateODM2(self.session_factory)
        
        # TODO: Check if data is already in the database.

        if cr.createTimeSeriesResultValues(data) is None:
            return False
        return True

    def getNoDataValue(self, resultID):
        rc = ReadODM2(self.session_factory)
        result = rc.getResultByID(int(resultID))
        return result.VariableObj.NoDataValue
