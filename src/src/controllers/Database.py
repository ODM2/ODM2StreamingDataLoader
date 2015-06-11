
__author__ = 'Denver'

import sys

sys.path.append('/home/denver/Documents/ODM2PythonAPI')

from src.api.ODM2.services.createService import createResults
from src.api.ODMconnection import dbconnection

class Database:
    
    def createConnection(self, Credentials):
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
        #print data.columns.tolist()[0]
        #print data
        cr = createResults(self.session_factory)
        cr.createTimeSeriesResultValues(data)

        
