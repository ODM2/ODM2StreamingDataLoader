# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Denver'

from argparse import ArgumentParser
import pprint

from models.YamlConfiguration import YamlConfiguration

from controllers.Mapping import Mapping
from controllers.Database import Database

def main(arguments):
    
    print "yamlFile: ", arguments.yamlFile

    yamlModel = YamlConfiguration(arguments.yamlFile)
    dbWriter = Database()

    for configParams in yamlModel.get():
        
        dataMapModel = Mapping(configParams)
        dbCredentials = dataMapModel.getDatabase()
        
        if dbWriter.createConnection(dbCredentials):

            for table in dataMapModel.getTables():
                dbWriter.write(table)

if __name__ == "__main__":
    parser = ArgumentParser(description="StreamDataLoader")
    parser.add_argument('-c', '--config', dest="yamlFile",\
        help="YAML config file", required=True, action="store")
    args = parser.parse_args()
    main(args)


