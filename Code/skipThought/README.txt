This program is designed to run on the local instance. The following
libraries need to be installed before running the program.


# Libraries to be installed

* pip install skip-thoughts
* pip install pandas
* pip install nltk
* pip install pandas

#Please note: Program is designed to run only on Python 2.7 version.

#To download the pretrained skip-thoughts model:

Download and extract the unidirectional model.
wget "http://download.tensorflow.org/models/skip_thoughts_uni_2017_02_02.tar.gz"
tar -xvf skip_thoughts_uni_2017_02_02.tar.gz
rm skip_thoughts_uni_2017_02_02.tar.gz

The path need to be  re configured based on the download location

path = "/home/th876217/skip_thoughts_uni_2017_02_02"

The dataset_path need to be reconfigured when running locally

dataset_path = "/mnt/c/Users/tselv/Downloads/bbc_dataset.csv"