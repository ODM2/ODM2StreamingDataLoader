from os import getcwd
from os.path import join
from src.handlers.yamlHandler import YAMLHandler
from tests.test_utils import returnFiles
__author__ = 'jmeline'

class TestYAMLHandler:
    def setup(self):
        self.path = join(getcwd(), 'test_handlers', 'test_yamlHandler', 'yamlFiles')
        assert self.path
        self.yaml = YAMLHandler()
        assert self.yaml
        self.files = returnFiles(self.path)
        assert self.files

    def test_read_yaml(self):
        load = self.yaml.read_yaml(self.files[0])
        assert load

    def test_write_yaml(self):
        load = self.yaml.read_yaml(self.files[0])
        assert load

        result = self.yaml.write_yaml(load, 'test.yaml')
        print(result)



