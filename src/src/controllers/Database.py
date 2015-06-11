
__author__ = 'Denver'

import sys
sys.path.append('/home/denver/Documents/ODM2PythonAPI')

from src.api.ODM2.services.createService import createResults

from src.api.ODMconnection import dbconnection

class Database:
    def __init__(self):
        self.createConnection()
        pass
    
    def createConnection(self, db='mysql', server='jws.uwrl.usu.edu',
                            db_name='odm2', uid='ODM', pwd='ODM123!!'):
        self.session_factory = dbconnection.createConnection(db, server,
                                                        db_name, uid,
                                                        pwd)
        if not self.session_factory:
            return False

        print "Connected!"
        print "Server: ", server
        print "Database: ", db_name
        print "User: ", uid

    def write(self, data):
        print data.columns.tolist()[0]
        
        cr = createResults(self.session_factory)
        cr.createTimeSeriesResultValues(data)

        
