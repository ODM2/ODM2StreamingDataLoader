"""Creates a factory logging method to be used within any class"""

import logging
import os


class LoggerTool():
    """Logging Tool that simplifies the logging process for each module."""

    def __init__(self):
        self.formatString = '%(asctime)s - %(levelname)s - %(name)s.%(funcName)s() (%(lineno)d): %(message)s'
        self.formatString1 = '%(asctime)s (%(levelname)s) %(module)s:%(funcName)s.%(name)s(%(lineno)d) - %(message)s'

    def setupLogger(self, loggerName, logFile, m='w', level=logging.INFO):
        """Creates a logging instance and initializes handlers, format, log file path, etc

        :param loggerName:
        :param logFile:
        :param m:
        :param level:
        :return logging Object:
        """
        l = logging.getLogger(loggerName)
        # formatter = logging.Formatter('%(asctime)s : %(message)s')
        formatter = logging.Formatter(self.formatString)

        # logPath = os.path.abspath(os.path.dirname("../../"))
        # logPath += '/log/'
        # if not os.path.exists(logPath):
        #     os.mkdir(logPath, 755)
        # fileHandler = logging.FileHandler(logPath + logFile, mode=m)
        # fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        l.setLevel(level)
        # l.addHandler(fileHandler)
        l.addHandler(streamHandler)

        # solves issues where logging would duplicate its logging message to the root logger
        # https://stackoverflow.com/questions/21127360/python-2-7-log-displayed-twice-when-logging-module-is-used-in-two-python-scri
        l.propagate = False

        return l

