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
    print "dataFile: ", arguments.dataFile

    dbWriter = Database()

    yamlModel = YamlConfiguration(arguments.yamlFile)
    for configParams in yamlModel.get():
        #pprint.pprint(configParams)
        dataMapModel = Mapping(configParams)
        dataMapModel.get()
        
        for table in dataMapModel.get():
            dbWriter.write(table)


if __name__ == "__main__":
    parser = ArgumentParser(description="StreamDataLoader")
    parser.add_argument('-c', '--config', dest="yamlFile",\
        help="YAML config file", required=True, action="store")
    parser.add_argument('-d', '--data', dest="dataFile",\
        help="CSV/TSV formatted file", required=False, action="store")
    args = parser.parse_args()
    main(args)


