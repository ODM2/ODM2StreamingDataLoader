# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Denver'

from argparse import ArgumentParser
import pprint

from models.YamlConfiguration import YamlConfiguration

from controllers.Mapping import Mapping

def main(arguments):
    
    print "[INFO] Using '%s' as YAML configuration." % arguments.yamlFile

    # Create an object to represent the yaml coniguration
    # file.
    yamlModel = YamlConfiguration(arguments.yamlFile)

    # List to hold any changes made to the config file to be
    # saved when the program has completed.
    configParamsList = []
    failureList = []

    # Loop through each file given in the YAML configuration.
    for configParams in yamlModel.get():
        updatedParams = configParams 
        dataMapModel = Mapping(configParams)
        
        if dataMapModel.getDatabase():

            if dataMapModel.map():

                for table in dataMapModel.getTables():
                    
                    print "[INFO] Trying to write", table[0]
                    print table[1]
                    if dataMapModel.save(table[1]):
                        
                        print "\t...Success!"
                        updatedParams = yamlModel.updateLastRead(\
                                            configParams, table[0])
                    
                    else:
                        
                        failureList.append(table[0])
        
        configParamsList.append(updatedParams)
    
    yamlModel.rebase(configParamsList)

    if failureList:
        print "[INFO] These columns were not added to the database:"
        for fail in failureList:
            print "\t", fail

# Application entry point.
if __name__ == "__main__":
    parser = ArgumentParser(description="StreamDataLoader")
    parser.add_argument('-c', '--config', dest="yamlFile",\
        help="YAML config file", required=True, action="store")
    args = parser.parse_args()
    main(args)


