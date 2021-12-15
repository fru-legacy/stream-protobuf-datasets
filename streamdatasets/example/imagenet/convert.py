from os import listdir
from os.path import isfile, isdir, join

#data/ILSVRC/Annotations/CLS-LOC/train/n02606052/n02606052_188.xml
folder = "/data/ILSVRC/Annotations/CLS-LOC/train"
onlyfolder = [f for f in listdir(folder) if isdir(join(folder, f))]

print('Test123', len(onlyfolder))

