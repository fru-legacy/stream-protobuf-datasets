from os import listdir
from os.path import isfile, isdir, join
from bs4 import BeautifulSoup

#data/ILSVRC/Annotations/CLS-LOC/train/n02606052/n02606052_188.xml
folder = "/data/ILSVRC/Annotations/CLS-LOC/train"
train_folders = [join(folder, f) for f in listdir(folder) if isdir(join(folder, f))]

for train_folder in train_folders[0:1]:
  files = [f for f in listdir(train_folder) if isfile(join(train_folder, f))]
  for file in files:
    with open(join(train_folder, file), 'r') as f:
      data = f.read()
    BsData = BeautifulSoup(data, "xml")
    b_folder = BsData.find_all('folder')
    print(b_folder)

