
__author__ = 'Denver'

import sys


sys.path.append('/home/denver/Documents/ODM2PythonAPI')
from src.api.ODM2.services.createService import createResults
from src.api.ODMconnection import dbconnection
from src.api.ODM2.services.readService import readCore

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

        print "Connected!"
        print "Server: ", Credentials.host
        print "Database: ", Credentials.db_name
        print "User: ", Credentials.uid
        
        return True


    def write(self, data):
        '''
        write is a public method that is used to write data to an 
        ODM2 database. This method should only be called once a valid
        database connection has been established.
        '''
        cr = createResults(self.session_factory)
        if cr.createTimeSeriesResultValues(data) is None:
            return False
        return True

    def getNoDataValues(self, resultID):
        rc = readCore(self.session_factory)
        result = rc.getResultByID(resultID)
        
        return result.VariableObj.NoDataValue
