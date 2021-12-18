from typing import Any, List
from os.path import join
from pathlib import Path

from .container.data import StreamDatasetData, StreamDatasetFile, StreamDatasetMetadata
from .container.list import StreamDatasetKeyValue, StreamDatasetList, StreamDatasetBucket, StreamDatasetItem

class Generator():
  def __init__(self, out_path: str):
    Path(out_path).mkdir(parents=True, exist_ok=True)
    self.out_path = out_path
    self.list = StreamDatasetList()
    self.file_data = open(join(out_path, 'data.proto.bin'), 'wb')
    self.file_list = open(join(out_path, 'list.proto.bin'), 'wb')
    self.current_position = 0
    self.item_current = None

  def __add_bucket(self, length: int):
    bucket = StreamDatasetBucket()
    bucket.start_byte = self.current_position
    bucket.end_byte = self.current_position + length
    self.item_current.buckets.append(bucket)
    self.current_position += length

  def start_item(self, name: str, description: str = ''):
    item = StreamDatasetItem()
    item.name = name
    item.description = description
    if self.item_current is not None:
      self.list.items.append(bytes(self.item_current))
    self.item_current = item

  def append_bucket(self, path: str, files: List[str], extension: str, metadata: List[Any]):
    data = StreamDatasetData()
    for file in files:
      with open(join(path, file + extension), 'rb') as f:
        file_container = StreamDatasetFile()
        file_container.name = file
        file_container.data = f.read()
        data.files.append(file_container)
    for meta in metadata:
      data.metadata.append(StreamDatasetMetadata())
      data.metadata[-1].data = bytes(meta)
    data_bytes = bytes(data)
    self.__add_bucket(len(data_bytes))
    self.file_data.write(data_bytes)
    self.file_data.flush()

  def add_key_value(self, key: str, value: str):
    self.list.lookup.append(StreamDatasetKeyValue(key, value))

  def save_list(self):
    self.file_data.close()
    self.list.items.append(bytes(self.item_current))
    self.item_current = None
    print('Data done!')
    print(len(self.list.items))
    raw_list = bytes(self.list)
    print(f'List serialized {len(raw_list)}')
    self.file_list.write(raw_list)
    self.file_list.close()