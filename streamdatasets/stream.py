# url
# url + '/data.proto.bin' + '/list.proto.bin' + '/model.py'

from abc import ABC, abstractmethod
from typing import Dict, Type, TypeVar, Generic
from importlib.machinery import SourceFileLoader
from .container.data import StreamDatasetData, StreamDatasetFile, StreamDatasetMetadata
from .container.list import StreamDatasetList
import requests
  
# imports the module from the given path

from abc import ABC, abstractmethod
class Parser(ABC):
    @abstractmethod
    def extract(self, bytes) -> Dict:
        pass

#test = StreamDatasetBucket()
#test.files.append(StreamDatasetFile())
#print(test)

#r=requests.get("http://www.example.com/", headers={"content-type":"text"})

#T = TypeVar('T')
#class Bucket(Generic[T], StreamDatasetBucket):
#    def parse_metadata(t: Type[T]) -> T:
#        return t()

#print(type(Bucket[Bucket].parse_metadata(Bucket)))
    
class Stream:
    def __init__(self, url, cache, model = "model.py"):
        self.endpoints = {
            'data': url + '/data.proto.bin',
            'list': url + '/list.proto.bin',
            'model': url + '/' + model
        }
        self.cache = cache
        # https://www.geeksforgeeks.org/how-to-import-a-python-module-given-the-full-path/
        #self.parser = SourceFileLoader("gfg","articles/gfg.py").load_module()

    def _download(self, url, cache_name, part_start=None, part_end=None):
        headers = {'Range': f"bytes={part_start}-{part_end}"}
        print(headers)
        return requests.get(url, headers=headers)
        #return b'Hello world'

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