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

    # Create an object to represent the yaml coniguration
    # file.
    yamlModel = YamlConfiguration(arguments.yamlFile)
    # Create an object to handle interactions with the database
    # and ODM2 API.
    dbWriter = Database()

    # List to hold any changes made to the config file to be
    # saved when the program has completed.
    configParamsList = []

    # Loop through each file given in the YAML configuration.
    for configParams in yamlModel.get():
        
        dataMapModel = Mapping(configParams)
        # If we are able to create a mapping...
        if dataMapModel.map():
            # Get the database connection credentials.
            dbCredentials = dataMapModel.getDatabase()
            # If we are able to connect to the database with
            # the credentials...
            if dbWriter.createConnection(dbCredentials):
                # For each of the tables in the mapping...
                #for table in dataMapModel.getTables():
                #    # Write the table to the database.
                #    dbWriter.write(table)
                # Update the config file to match what was
                # most recently read.
                updatedParams = yamlModel.updateLastRead(configParams)
            # If not able to connect to the database with the
            # given credentials, then the config file does not
            # need to be updated.
            else:
                updatedParams = configParams    
        # If not able to create a mapping, then the config file
        # does not need to be updated.
        else:
            updatedParams = configParams
        
        # Add any changes to the config file to the list to be
        # updated when finished reading the config file.
        configParamsList.append(updatedParams)
    
    # Update the config file with any parameters that have
    # changed since the last time the program was ran.
    yamlModel.rebase(configParamsList)

# Application entry point.
if __name__ == "__main__":
    parser = ArgumentParser(description="StreamDataLoader")
    parser.add_argument('-c', '--config', dest="yamlFile",\
        help="YAML config file", required=True, action="store")
    args = parser.parse_args()
    main(args)


