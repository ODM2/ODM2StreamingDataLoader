"""
    Streaming Data Loader Python

"""
import os

#this_file = os.path.realpath(__file__)
#directory = os.path.dirname(os.path.dirname(this_file))
#sys.path.insert(0, directory)
#print directory

from src.common import SystemController

if __name__ == "__main__":
    sys = SystemController()
    sys.startSystem()

