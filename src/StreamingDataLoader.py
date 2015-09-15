# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Denver'

from argparse import ArgumentParser
import logging

from models.YamlConfiguration import YamlConfiguration
from controllers.Mapping import Mapping
from lib.Appdirs.appdirs import user_config_dir

import numpy as np
import os
import glob

def _get_file(filename):
        #fn = util.resource_path('connection.config')
        fn = os.path.join(user_config_dir("SDL", "UCHIC"), filename)
        print fn

        return fn

def main(arguments):

    # Create logger.
    LOG_FILENAME = _get_file('logfile.txt')
    logger = logging.getLogger('SDL_logger')
    
    # Set logging verbosity to either DEBUG or INFO.
    if arguments.verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Set up logger to log to a file.
    handler = logging.FileHandler(LOG_FILENAME)

    # Set up the formatting of the log strings.
    formatter = logging.Formatter("[%(asctime)s %(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    
    logger.info('\n\nBeginning execution.')
    logger.debug("Using '%s' as YAML configuration." % arguments.yamlFile)

    if arguments.csvFile:
        logger.info('Using only the specified data file: %s' % arguments.csvFile)

    for arg, i in zip(arguments.yamlFile, range(len(arguments.yamlFile))):
        if os.path.isdir(arg):
            arguments.yamlFile[i] += "/*.yaml"

        else:
            if not arg.endswith('.yaml'):
                arguments.yamlFile[i] = ""
                logger.error("Invalid configuration file (must be .yaml).")

    print [r for r in arguments.yamlFile]
    for arg in arguments.yamlFile:
        for filepath in glob.glob(arg):
            # Create an object to represent the yaml coniguration
            # file.
            yamlModel = YamlConfiguration(filepath,\
                (arguments.csvFile if arguments.csvFile is not None else None),\
                (arguments.restart if arguments.restart is not False else False))

            # List to hold any changes made to the config file to be
            # saved when the program has completed.
            configParamsList = []
            failureList = []

            # Loop through each file given in the YAML configuration.
            files = yamlModel.get()
            for configParams in files:
                # Declare updatedParams to preserve scope.
                updatedParams = configParams 
                print configParams
                dataMapModel = Mapping(configParams[1])
                # If able to connect to the database...
                if dataMapModel.getDatabase():
                    # If able to perform a mapping...
                    if dataMapModel.map():
                        # Loop through the tables in the mapping. 
                        for table in dataMapModel.getTables():
                            logger.debug('Writing %s...' % table[0])
                            # If able to save table to database...
                            if dataMapModel.save(table[1]):
                                # Update the latest date time for the table.
                                dataMapModel.updateDateTime(table[1]['ResultID'][0], np.max(table[1]['ValueDateTime'])) 
                                logger.debug('...Success!')
                                # Update the last byte read.
                                updatedParams = yamlModel.updateLastRead(\
                                                    configParams, table[0])
                            # If not able to save to database.
                            else:
                                # Add table to list of failures
                                failureList.append(table[0])
                configParamsList.append(updatedParams)
            # Error with either YAML or CSV file path given on command line.
            if not files:
                logger.error('No matching configuration found using configuration file "%s" and data file "%s".' % (arguments.yamlFile, arguments.csvFile))
            # No errors. Update the config file with what the app has done.
            else:
                yamlModel.rebase(configParamsList)
            # If any failures exist, write them to the log file.
            if failureList:
                for fail in failureList:
                    logger.info('%s not added to the database.' % fail)

    for arg in arguments.yamlFile:
        if not glob.glob(arg):
            logger.error("No configuration files could be found given directory: '%s'" % arg)
            #print "[error] No configuration files could be found given directory: '%s'" % arguments.yamlFile

    logger.info('Completed execution.')



# Application entry point.
if __name__ == "__main__":
    parser = ArgumentParser(description="StreamingDataLoader")
    parser.add_argument('-r', '--restart',\
        action='store_true', help="Read the entire CSV file to ensure that data is correct and accounted for. This option affects performance. While the integrity of the data is checked each time the program executes, it is still recommended to use this option if you have manually modified your data file between executions.")
    parser.add_argument('-v', '--verbose',\
        action='store_true', help="Enable more verbose logging in the logfile.")
    parser.add_argument('-c', '--config', nargs='+', dest="yamlFile",\
        help="Specify a YAML configuration file in the form of one of these formats:\n1. A single YAML (.yaml) file.\n2. A list of YAML files (.yaml), deliminated by white space.\n3. A directory containing multiple YAML (.yaml) files.", required=True, action="store")
    parser.add_argument('-f', '--file', dest="csvFile",\
        help="Specify a single CSV data file to target instead of the one listed in the configuration file.", required=False, action="store")
    args = parser.parse_args()

    main(args)


