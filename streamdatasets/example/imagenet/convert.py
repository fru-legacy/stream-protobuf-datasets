from os import listdir
from os.path import isfile, isdir, join

folder = "/data/ILSVRC2017_CLS-LOC"
onlyfolder = [f for f in listdir(folder) if isdir(join(folder, f))]

print('Test123', len(onlyfolder))

