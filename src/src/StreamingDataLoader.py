# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Denver'

from argparse import ArgumentParser
import pprint
import logging

from models.YamlConfiguration import YamlConfiguration
from controllers.Mapping import Mapping

import numpy as np

def main(arguments):
    

    # Setup logging.
    LOG_FILENAME = 'logfile.txt'
    logger = logging.getLogger('SDL_logger')
    if arguments.verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(asctime)s %(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
    handler = logging.FileHandler(LOG_FILENAME)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    

    logger.info("Using '%s' as YAML configuration." % arguments.yamlFile)

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
                    logger.debug('Writing %s...' % table[0])
                    if dataMapModel.save(table[1]):
                        
                        dataMapModel.updateDateTime(table[1]['ResultID'][0], np.max(table[1]['ValueDateTime'])) 
                        
                        logger.debug('...Success!')
                        updatedParams = yamlModel.updateLastRead(\
                                            configParams, table[0])
                    
                    else:
                        
                        failureList.append(table[0])
        
        configParamsList.append(updatedParams)
    
    yamlModel.rebase(configParamsList)

    if failureList:
        for fail in failureList:
            logger.info('%s not added to the database.' % fail)

# Application entry point.
if __name__ == "__main__":
    parser = ArgumentParser(description="StreamDataLoader")
    parser.add_argument('-v', '--verbose',\
        action='store_true', help="Verbose logging mode.")
    parser.add_argument('-c', '--config', dest="yamlFile",\
        help="YAML config file", required=True, action="store")
    args = parser.parse_args()
    main(args)


