# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Denver'

from argparse import ArgumentParser
import pprint

from models.YamlConfiguration import YamlConfiguration

from controllers.Mapping import Mapping
from controllers.Database import Database

def main(arguments):
    
    print "Using %s as YAML configuration." % arguments.yamlFile

    yamlModel = YamlConfiguration(arguments.yamlFile)
    dbWriter = Database()

    configParamsList = []

    # Loop through each file given in the YAML configuration.
    for configParams in yamlModel.get():
        
        dataMapModel = Mapping(configParams)
        if dataMapModel.map():
            dbCredentials = dataMapModel.getDatabase()
            if dbWriter.createConnection(dbCredentials):
                #for table in dataMapModel.getTables():
                #    dbWriter.write(table)
                updatedParams = yamlModel.updateLastRead(configParams)
            else:
                updatedParams = configParams    
        else:
            updatedParams = configParams
        
        configParamsList.append(updatedParams)
    
    yamlModel.rebase(configParamsList)

if __name__ == "__main__":
    parser = ArgumentParser(description="StreamDataLoader")
    parser.add_argument('-c', '--config', dest="yamlFile",\
        help="YAML config file", required=True, action="store")
    args = parser.parse_args()
    main(args)


