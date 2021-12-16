from .container.list import StreamDatasetList

with open('/data/streamable/list.proto.bin', 'rb') as f:
  data = f.read()
print(len(data))
list = StreamDatasetList().parse(data)
print(len(list.lookup))
print(len(list.items))
print(len(list.items[10].buckets))
