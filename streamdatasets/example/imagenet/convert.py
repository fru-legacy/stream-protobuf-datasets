import csv
from os import listdir
from os.path import isfile, isdir, join
from bs4 import BeautifulSoup

from .model import Imagenet
from ...generator import Generator

out_dir = '/data/streamable'
in_dir = '/data/ILSVRC'
in_dir_kaggle = '/data'

generator = Generator(out_dir)

train_folder = join(in_dir, '/Annotations/CLS-LOC/train')
# contains e.g: ./n02606052/n02606052_188.xml
train_folder_data = join(in_dir, '/data/ILSVRC/Data/CLS-LOC/train')
# contains e.g: ./n02606052/n02606052_188.JPEG

val_folder = join(in_dir, '/data/ILSVRC/Annotations/CLS-LOC/val')
# contains e.g: ./ILSVRC2012_val_00024102.xml
val_folder_data = join(in_dir, '/data/ILSVRC/Data/CLS-LOC/val')
# contains e.g: ./ILSVRC2012_val_00024102.JPEG

test_file = join(in_dir_kaggle, '/LOC_train_solution.csv')
# format: n02017213_4263,n02017213 355 155 430 273 n02017213 178 123 290 332
test_folder_data = join(in_dir, '/data/ILSVRC/Data/CLS-LOC/test')
# contains e.g: ./ILSVRC2012_test_00064102.JPEG

item_label_file = join(in_dir_kaggle, '/LOC_synset_mapping.txt')

def _read_item_label_file(file):
  with open(file, 'r') as f:
    lines = [l.split(',') for l in file.readlines()]
  print(lines[0][0])

def _read_csv_solution_file(file):
  with open(file, 'r') as f:
    lines = [l.split(',') for l in file.readlines()]
  print(lines[0][0])


_read_item_label_file(item_label_file)
_read_csv_solution_file(test_file)

exit()

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
