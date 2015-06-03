# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Denver'


from argparse import ArgumentParser
import pprint

from src.models.YamlConfiguration import YamlConfiguration
from src.controllers.Mapping import Mapping

def main(arguments):
    
    print "yamlFile: ", arguments.yamlFile
    print "dataFile: ", arguments.dataFile

    yamlModel = YamlConfiguration(arguments.yamlFile)
    for configParams in yamlModel.get():
        #pprint.pprint(configParams)
        dataMapModel = Mapping(configParams)
        #dataMapModel.get()
        #Write to database


if __name__ == "__main__":
    parser = ArgumentParser(description="StreamDataLoader")
    parser.add_argument('-c', '--config', dest="yamlFile",\
        help="YAML config file", required=True, action="store")
    parser.add_argument('-d', '--data', dest="dataFile",\
        help="CSV/TSV formatted file", required=False, action="store")
    args = parser.parse_args()
    main(args)


