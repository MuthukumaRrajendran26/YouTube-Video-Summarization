## CSCI 4152/6509 Natural Language Processing (Winter 2020)
# P-09: Generating Short Description of Videos

### Project members

| CSID:          | Name:                            | Course:   | Email:          |
|----------------|----------------------------------|-----------|-----------------|
| mani           | Karthikk Tamil Mani              | CSCI 6509 | kr630601@dal.ca |
| sasidharan     | Srikrishna Sasidharan            | CSCI 6509 | sr950863@dal.ca |
| tshanmugam     | Thanigaiselvan Senthil Shanmugam | CSCI 6509 | th876217@dal.ca |
| mrajendran     | Rajendran Muthukumar             | CSCI 6509 | mt911642@dal.ca |

  
### Prerequisites

* Download the Glove pretrained model from [Stanford Glove](http://nlp.stanford.edu/data/glove.840B.300d.zip).
* Replace this line `gloveFile = file_path+'glove.840B.300d.txt'` accrodingly in the [NLP_Project.ipynb](https://git.cs.dal.ca/courses/2020-winter/nlp/p-09/-/blob/master/Code/NLP_Project.ipynb) file.
* Download the FastText pretrained model from [FastText](https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.en.zip).
* Replace this line `model = FastText.load_fasttext_format(file_path+'wiki.en.bin')` accrodingly in the [NLP_Project.ipynb](https://git.cs.dal.ca/courses/2020-winter/nlp/p-09/-/blob/master/Code/NLP_Project.ipynb) file.
* Download and add [BBC News Dataset](https://git.cs.dal.ca/courses/2020-winter/nlp/p-09/-/blob/master/Code/bbc_dataset.csv) to your storage and replace `file_path = '/content/drive/My Drive/NLP_DATA/'` according to your specifications in the [NLP_Project.ipynb](https://git.cs.dal.ca/courses/2020-winter/nlp/p-09/-/blob/master/Code/NLP_Project.ipynb) file.
  
### How to run the code

* Run `git clone https://git.cs.dal.ca/courses/2020-winter/nlp/p-09.git` command from shell.
* Navigate to Code directory.
* Run NLP_Project.ipynb using Jupyter notebook or Google Colab.
* From current directory, navigate to skipThought folder.
* Execute the command `python skipTextSummarization.py`. Refer this [file](https://git.cs.dal.ca/courses/2020-winter/nlp/p-09/-/blob/master/Code/skipThought/README.txt) to do the required environment setup.

### Project Structure

* Code for TF-IDF SentenceRanking, Glove / Fasttext and Universal sentence encoder techniques is available in the single file [NLP_Project.ipynb](https://git.cs.dal.ca/courses/2020-winter/nlp/p-09/-/blob/master/Code/NLP_Project.ipynb).
* Code for Skip-thought vector model and respective Readme are available in [Skip-thought vectors](https://git.cs.dal.ca/courses/2020-winter/nlp/p-09/-/tree/master/Code%2FskipThought).