__author__ = 'jmeline'


import yaml

class YAMLHandler:
    def __init__(self):
        pass

    def read_yaml(self, filename):
        """ Takes in a filename, parses yaml
        :param filename:
        :return:
        """

        if not filename:
            print("read_yaml cannot read the file you provided")
            raise

        try:
            f = open(filename)
            load = yaml.load(f)
            f.close()
            if load:
                return load
            else:
                return None
        except IOError as e:
            print(e)
            return None

    def write_yaml(self, load, outputName=None):
        """

        :param outputName:
            :type String:
        :param load:
            :type json.Load Object:
        :return:
            :type boolean:
        """

        if not load:
            print ("yaml.Load object is None")
            raise
        try:
            dump = yaml.dump(load, indent=4, separators=(',', ': '), sort_keys=True)
            if outputName:
                f = open(outputName, 'w')
                f.write(dump)
                f.close()
            return dump
        except Exception as e:
            print (e)
            return False

    def toConfigObject(self, yamlLoadedObject):
        """

        :param yamlLoadedObject instance
        :type configFile Object:
        :return:
        """
        return None
