from .container.list import StreamDatasetList

with open('/data/streamable/list.proto.bin', 'rb') as f:
  data = f.read()
  StreamDatasetList().parse(data)