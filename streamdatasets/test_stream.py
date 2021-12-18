from streamdatasets.container.data import StreamDatasetData
from .container.list import StreamDatasetItem, StreamDatasetList

with open('/data/streamable3/list.proto.bin', 'rb') as f:
  list_data = f.read()
list = StreamDatasetList().parse(list_data)
print(len(list.lookup))
print(len(list.items))
item = StreamDatasetItem().parse(list.items[10])
print(len(item.buckets))
bucket = item.buckets[1]

with open('/data/streamable3/data.proto.bin', 'rb') as f:
  f.seek(bucket.start_byte)
  data_data = f.read(bucket.end_byte - bucket.start_byte)
data = StreamDatasetData().parse(data_data)
print(data.metadata)
print([f.name for f in data.files])

with open('/data/test123.JPEG', 'wb') as f:
  f.write(data.files[0].data)