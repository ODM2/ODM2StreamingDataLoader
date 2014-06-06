from __future__ import print_function

from src.handlers.jsonHandler import JsonHandler as js
from os import listdir, getcwd
from os.path import join, isfile

class TestJsonHandler:
    def setup(self):
        self.path = join(getcwd(), 'test_handlers', 'test_jsonHandler', 'jsonFiles')
        self.json = js

    def test_readJsonFile(self):
        self.json.readJsonFile(path=self.path)
        pass

    def test_writeJsonFile(self):
        pass

    def test_toConfigObject(self):
        pass

