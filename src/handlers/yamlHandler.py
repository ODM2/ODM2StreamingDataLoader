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
            print("read_json cannot read the file you provided")
            raise

        try:
            f = open(filename)
            load = yaml.load(f)
            f.close()
            if load:
                return load['File']
            else:
                return None
        except IOError as e:
            print(e)
            return None