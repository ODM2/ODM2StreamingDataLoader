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
    #read jsonfile
    #loop through files
        #canirun()
        #createpandatable(datafile)
        # object namedtuple
        #set up db connection
        #loop through Mappings
            # loop through object.DataSeriesMapping
            # get max(localdatetime) for seriesmapping
            # TODO: change csvHandler to read entire csv then add another function that will return a specified column after a datetime
            # get panda column (DataseriesMapping.columnname, localdatetime )
            #does this series exist?
                #if no return error
            #createmapping(DataSeriesMapping, namedtuple, pandacolumn)
            #savemapping
            #update value count in the Results Table # if save is successful

    #createresult
        #Result
        #TimeSeriesResult
        # TODO create the result and timeSeriesResult in the wizard and pass the resultid we will assume the user has already created the series




    #createmapping
        # get TimeSeriesResultValue create skeleton(template)
        #fill in the template with info from the DAtaSEriesMapping







