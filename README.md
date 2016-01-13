ODM2StreamingDataLoader
======================

A program for streaming continuous sensor data into an instance of Version 2 of the Observations Data Model (ODM2). The ODM2 Streaming Data Loader is written in Python and our goal is to make sure that it is compatible with Windows, Mac, and Linux platforms. The ODM2 Streaming Data Loader consists of two programs:

1. An executable data loader that reads a configuration file, performs the work of loading the data, and can be scheduled according to a user-defined schedule.
2. A graphical user interface wizard that enables users to map a delimited datalogger text file to an ODM2 database and create a configuration file.

### Setup

## Mac/OSX

1. Download and install the latest installer package: https://github.com/ODM2/ODM2StreamingDataLoader/releases
2. To schedule the Streaming Data Loader to run periodically, create a new cron job. Open a terminal window and enter the following command:  
```
crontab -e
```  
This will open a special file where you can create tasks that run automatically. The syntax for the file is as follows:  
Argument 1: Minute (0 - 59)
Argument 2: Hour (0 - 23)
Argument 3: Day of Month (1 - 31)
Argument 4: Month (1-12)
Argument 5: Day of Week (0 - 6) Sunday = 0
Argument 6: Command  
This is an example entry which will run the Streaming Data Loader every minute:  
```
* * * * * /Applications/SDLLoader.app/Contents/MacOS/SDLLoader -c /Users/denversmith/Desktop/newb.yaml -v >/dev/null 2>&1
```

### Credits

This work was supported by National Science Foundation Grants [EAR-1224638](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1224638) and [ACI-1339834](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1339834). Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation. 
