# url
# url + '/data.proto.bin' + '/list.proto.bin' + '/model.py'

from abc import ABC, abstractmethod
from typing import Dict
from importlib.machinery import SourceFileLoader
  
# imports the module from the given path

class Parser(ABC):
    @abstractmethod
    def extract(self, bytes) -> Dict:
        pass

class Downloader:
    def __init__(self, url, cache, model = "model.py"):
        self.endpoints = {
            'data': url + '/data.proto.bin',
            'list': url + '/list.proto.bin',
            'model': url + '/' + model
        }
        self.cache = cache
        # https://www.geeksforgeeks.org/how-to-import-a-python-module-given-the-full-path/
        self.parser = SourceFileLoader("gfg","articles/gfg.py").load_module()

    def __download(file, part_count=None, part_start=None, part_end=None):
        return b'Hello world'

    def _download_data_use_cache(self, name, bucket):
        return b'Hello world'

    def classes_with_bucket_count(self):
        list = self.__download(self.endpoints['list'])
        # extract with list.proto.py
        # return list.classes
        return {'train/n04562935': 130, 'test': 1000, 'val': 500}

    def retrieve_class_bucket(self, name, bucket):

        return {
            '_files': {'ILSVRC2012_val_00006619.JPEG': b'Hello world'},
            **self.parser.extract(b'metadata')
        }