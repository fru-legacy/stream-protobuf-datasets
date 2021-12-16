from streamdatasets.container.data import StreamDatasetData
from .container.list import StreamDatasetList

with open('/data/streamable/list.proto.bin', 'rb') as f:
  list_data = f.read()
list = StreamDatasetList().parse(list_data)
print(len(list.lookup))
print(len(list.items))
print(len(list.items[10].buckets))
bucket = list.items[10].buckets[2]

with open('/data/streamable/data.proto.bin', 'rb') as f:
  f.seek(bucket.start_byte)
  data_data = f.read(bucket.end_byte - bucket.start_byte)
data = StreamDatasetData().parse(data_data)
print(data.metadata)
print([f.name for f in data.files])