# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jacob'

""" Loader """

from argparse import ArgumentParser
from src.loader.models.loaderModel import LoaderModel

if __name__ == "__main__":
    parser = ArgumentParser(description="StreamDataLoader")
    parser.add_argument('-c', '--config', dest="jsonFile", help="Json config file", required=True, action="store")
    parser.add_argument('-d', '--data', dest="dataFile", help="csv/tsv data file", required=True, action="store")
    args = parser.parse_args()

    if args:
        print "jsonFile: ", args.jsonFile
        print "dataFile: ", args.dataFile

    model = LoaderModel(args)



