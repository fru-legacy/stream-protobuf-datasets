from os import listdir
from os.path import isfile, isdir, join
from bs4 import BeautifulSoup
from .model import Imagenet

#data/ILSVRC/Annotations/CLS-LOC/train/n02606052/n02606052_188.xml
folder = "/data/ILSVRC/Annotations/CLS-LOC/train"
folder_data = "/data/ILSVRC/Data/CLS-LOC/train"

train_folders = [join(folder, f) for f in listdir(folder) if isdir(join(folder, f))]

values = {'difficult': [], 'truncated': [], 'database': [], 'depth': [], 'segmented': [], 'pose': []}
step = 1
for train_folder in train_folders[0:1]:
  print(step)
  step += 1
  files = [f for f in listdir(train_folder) if isfile(join(train_folder, f))]
  for file in files[0:1]:
    with open(join(train_folder, file), 'r') as f:
      data = f.read()
    BsData = BeautifulSoup(data, "xml")
    def get_value(name):
      return ''.join(child for child in BsData.find_all(name)[0].children)
    model = Imagenet().from_dict({
      'folder': get_value('folder'),
      'filename': get_value('filename'),
      'size_width': int(get_value('width')),
      'size_height': int(get_value('height')),
      'object_name': get_value('name'),
      'object_bndbox_xmin': int(get_value('xmin')),
      'object_bndbox_ymin': int(get_value('ymin')),
      'object_bndbox_xmax': int(get_value('xmax')),
      'object_bndbox_ymax': int(get_value('ymax'))
    })
    ser = bytes(model)
    print(ser)
    restored = Imagenet().parse(ser)
    print(restored)
    with open(join(folder_data, model.folder, model.filename + '.JPEG'), 'rb') as f:
      print(type(f.read()))

print(values)
