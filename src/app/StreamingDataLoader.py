# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jacob'

""" Loader """

from argparse import ArgumentParser
import sys
import os
this_file = os.path.realpath(__file__)
print "this_file: ", this_file, os.path.dirname(this_file)
directory = os.path.dirname(os.path.dirname(this_file))
print "directory: ", directory
if not directory in sys.path:
    sys.path.insert(0, directory)
for i in sys.path:
    print i

from loader.models.loaderModel import LoaderModel

if __name__ == "__main__":
    parser = ArgumentParser(description="StreamDataLoader")
    parser.add_argument('-c', '--config', dest="jsonFile", help="Json config file", required=True, action="store")
    parser.add_argument('-d', '--data', dest="dataFile", help="CSV/TSV formatted file", required=False, action="store")
    args = parser.parse_args()

    if args:
        print "jsonFile: ", args.jsonFile
        print "dataFile: ", args.dataFile

    model = LoaderModel(args)



