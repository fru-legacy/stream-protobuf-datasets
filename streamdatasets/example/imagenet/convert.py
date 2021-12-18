import io
from os import listdir
from os.path import isfile, isdir, join
from typing import List
from bs4 import BeautifulSoup

from .model import Imagenet, Imagenet_Object
from ...generator import Generator
from ...helper import grouper

## Configure paths

out_dir = '/data/streamable3'
in_dir = '/data/ILSVRC'
in_dir_kaggle = '/data'

max_bucket_size = 25
generator = Generator(out_dir)
folder_img = join(in_dir, 'Data/CLS-LOC')

def _read_label_file_as_key_values(file):
  with open(file, 'r') as f:
    lines = [l.split(' ', 1) for l in f.readlines()]
  for line in lines:
    generator.add_key_value(line[0], line[1].strip())

def _read_xml(file):
  def get_value(node, name):
      return ''.join(child for child in node.find_all(name)[0].children)
  with open(file, 'r') as f:
    data = f.read()
  root = BeautifulSoup(data, "xml")
  net = Imagenet()
  net.folder = get_value(root,'folder')
  net.filename = get_value(root,'filename')
  net.size_width = int(get_value(root,'width'))
  net.size_height = int(get_value(root,'height'))
  for object in root.find_all('object'):
    net.objects.append(Imagenet_Object())
    net.objects[-1].name = get_value(object, 'name')
    net.objects[-1].bndbox_xmin = int(get_value(object, 'xmin'))
    net.objects[-1].bndbox_ymin = int(get_value(object, 'ymin'))
    net.objects[-1].bndbox_xmax = int(get_value(object, 'xmax'))
    net.objects[-1].bndbox_ymax = int(get_value(object, 'ymax'))
  return net

def _get_path_and_files(group: List[Imagenet], clean_foldername):
  return (clean_foldername(group[0].folder), [f.filename for f in group])

def _read_metadata_as_bucket(metadata, image_root_folder, clean_foldername):
  for group in grouper(metadata, max_bucket_size):
    group = [g for g in group if g is not None]
    sub_folder, files = _get_path_and_files(group, clean_foldername)
    print(f'Bucket: {sub_folder} {generator.get_bucket_count()}')
    image_folder = join(image_root_folder, sub_folder)
    generator.append_bucket(image_folder, files, '.JPEG', group)

def _read_xml_dir_as_buckets(folder, image_root_folder, clean_foldername = lambda x: x):
  all = [_read_xml(join(folder, f)) for f in listdir(folder) if isfile(join(folder, f))]
  return _read_metadata_as_bucket(all, image_root_folder, clean_foldername)

def _read_jpeg_dir_as_buckets(image_root_folder, sub_folder, clean_foldername = lambda x: x):
  folder = join(image_root_folder, sub_folder)
  all = [f for f in listdir(folder) if isfile(join(folder, f))]
  net = [Imagenet(sub_folder, f.removesuffix('.JPEG')) for f in all]
  return _read_metadata_as_bucket(net, image_root_folder, clean_foldername)

## Read kaggle csv and txt files

label_file = join(in_dir_kaggle, 'LOC_synset_mapping.txt')
_read_label_file_as_key_values(label_file)

## Read imagenet xml & jpgs

# Test

train_folder = join(in_dir, 'Annotations/CLS-LOC/train') # ./n02606052/n02606052_188.xml
train_folder_img = join(in_dir, 'Data/CLS-LOC/train') # ./n02606052/n02606052_188.JPEG

clean_train_foldername = lambda f: f if f.startswith('n') else 'n' + f
for idx, f in enumerate(listdir(train_folder)):
    if isdir(join(train_folder, f)):
      generator.start_item('train/' + f)
      _read_xml_dir_as_buckets(join(train_folder, f), train_folder_img, clean_train_foldername)

# Var

generator.start_item('val')
val_folder = join(in_dir, 'Annotations/CLS-LOC/val') # ./ILSVRC2012_val_00024102.xml
_read_xml_dir_as_buckets(val_folder, folder_img)

# Test

generator.start_item('test')
_read_jpeg_dir_as_buckets(folder_img, 'test')

generator.save_list()

# Imagenet().parse(ser)