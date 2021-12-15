from os import listdir
from os.path import isfile, isdir, join
from bs4 import BeautifulSoup

#data/ILSVRC/Annotations/CLS-LOC/train/n02606052/n02606052_188.xml
folder = "/data/ILSVRC/Annotations/CLS-LOC/train"
train_folders = [join(folder, f) for f in listdir(folder) if isdir(join(folder, f))]

values = {'difficult': [], 'truncated': [], 'database': [], 'depth': [], 'segmented': [], 'pose': []}

for train_folder in train_folders:
  files = [f for f in listdir(train_folder) if isfile(join(train_folder, f))]
  for file in files:
    with open(join(train_folder, file), 'r') as f:
      data = f.read()
    BsData = BeautifulSoup(data, "xml")
    def add_value(name):
      print(join(train_folder, file), name)
      b_value = ''.join(child for child in BsData.find_all(name)[0].children)
      if b_value not in values[name]:
        values[name].append(b_value)
    add_value('difficult')
    add_value('truncated')
    add_value('database')
    add_value('depth')
    add_value('segmented')
    add_value('pose')

print(values)
