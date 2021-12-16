sudo apt install transmission-cli
pip install kaggle

cd /data

# Visit https://academictorrents.com/browse.php?search=imagenet&sort_field=seeders&sort_dir=DESC
# Get ILSVRC2017_CLS-LOC.tar.gz (Size 166.02GB) torrent url
transmission-cli https://academictorrents.com/download/943977d8c96892d24237638335e481f3ccd54cfb.torrent

# Get all processes with: ps -aux
# Reconnect to process $pid with: sudo strace -ewrite -p $pid

tar -xvzf /data/ILSVRC2017_CLS-LOC.tar.gz
# Get progress with: ls ./Downloads/ILSVRC/Data/CLS-LOC/train/ | wc -l

# Under Kaggle > Your Profile > Account > Create New API Token
kaggle competitions download -c imagenet-object-localization-challenge -f LOC_synset_mapping.txt

# Validate hash: 
pv /data/ILSVRC2017_CLS-LOC.tar.gz | sha1sum

pip3 install git+https://github.com/fru/stream-protobuf-datasets
python -m streamdatasets.example.imagenet.convert

# Upload to webserver e.g: gdrive and rclone serve