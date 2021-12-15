from os import listdir
from os.path import isfile, isdir, join
from bs4 import BeautifulSoup

#data/ILSVRC/Annotations/CLS-LOC/train/n02606052/n02606052_188.xml
folder = "/data/ILSVRC/Annotations/CLS-LOC/train"
train_folders = [join(folder, f) for f in listdir(folder) if isdir(join(folder, f))]

values = {'difficult': []}

for train_folder in train_folders[0:1]:
  files = [f for f in listdir(train_folder) if isfile(join(train_folder, f))]
  for file in files:
    with open(join(train_folder, file), 'r') as f:
      data = f.read()
    BsData = BeautifulSoup(data, "xml")
    b_folder = ''.join(child for child in BsData.find_all('difficult')[0].children)
    if b_folder not in values['difficult']:
      values['difficult'].append(b_folder)
    #print(b_folder)

print(values)
