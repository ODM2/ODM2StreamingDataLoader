__author__ = 'Denver'

import yaml

class YamlConfiguration():
    """ YAML Config file model """

    def __init__(self, configFilePath):
        self.yamlDict = {}
        self.yamlDict = self.readFile(configFilePath)
        

    def readFile(self, path):
        
        if not path:
            print "Cannot read the file provided."
            return None

        try:
            f = open(path)
            load = yaml.load(f)
            f.close()

            if load:
                return load

        except IOError as e:
            print e
            return None


    def get(self):
        fileDictList = []
        for fileDict in self.yamlDict.keys():
            fileDictList.append(self.yamlDict[fileDict])
        return fileDictList
