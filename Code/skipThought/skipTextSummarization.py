import numpy as np
from skip_thoughts import configuration
from skip_thoughts import encoder_manager
import os
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from nltk.tokenize import sent_tokenize, word_tokenize
import csv
from tqdm import tqdm
import io
import codecs
import pandas as pd

import sys
reload(sys)
sys.setdefaultencoding('utf8')

path = "/home/th876217/skip_thoughts_uni_2017_02_02"

dataset_path = "/mnt/c/Users/tselv/Downloads/bbc_dataset.csv"

VOCAB_FILE = path + "/vocab.txt"
EMBEDDING_MATRIX_FILE = path + "/embeddings.npy"
CHECKPOINT_PATH = path + "/model.ckpt-501424"
encoder = encoder_manager.EncoderManager()
encoder.load_model(configuration.model_config(),vocabulary_file=VOCAB_FILE,embedding_matrix_file=EMBEDDING_MATRIX_FILE,checkpoint_path=CHECKPOINT_PATH)
check=0
bbc_summary=[]
bbc_article=[]
output_summary=list();
fileName=0;

#Dynamically decide the total number of sentence in the summary
def getOutputSent(totalSentence):
    if totalSentence/2 < 10:
        a = totalSentence/2;
        if a == 0:
            return int(1)
        else:
            return int(totalSentence/2)
    else:
        return int(10);

    
def wrtiteToFile(fileName,output_summary):
    writeFile='./bbc_output_temp'+str(fileName)+'.csv'
    with io.open(writeFile, 'wb') as filew:
        writer = csv.writer(filew,quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["INPUT_SUMMARY", "OUTPUT_SUMMARY"])
        for ik in output_summary:
            writer.writerow(ik)
        output_summary=list();

#reading dataset    
with open(dataset_path, 'r') as file:
        reader = csv.reader(file)
        t=0;
        for row in reader:
            if check == 0:
                print(row)
                check=check+1
            else:
                #if t > 2000:
                bbc_article.append(row[0]);
                bbc_summary.append(row[0]);
                t=t+1;

summary_iter=0;
for each_data in tqdm(bbc_article):
    try:
    #tokens = nlp(unicode(each_data))
        each_data= each_data.decode('utf-8').strip()
    #print(each_data)
        temp_s=list();
        temp_s.append(bbc_summary[summary_iter]);
        tokens= sent_tokenize(each_data)
        sentences = []
        average =[]

        for sent in tokens:
            sentences.append(sent)

        encodedSentences = encoder.encode(sentences)
        encodedSentences = np.nan_to_num(encodedSentences)
        totalSentence=getOutputSent(len(encodedSentences))
        totalClusters = int(np.ceil(totalSentence))
        kmeans = KMeans(n_clusters=totalClusters, random_state=0)
        kmeans = kmeans.fit(encodedSentences)

        for j in range(totalClusters):
            i = np.where(kmeans.labels_ == j)[0]
            average.append(np.mean(i))

    #Index of the sentence close to cluster center
        relatedSent, temp = pairwise_distances_argmin_min(kmeans.cluster_centers_,encodedSentences)
    #finding summary order
        summary_order = sorted(range(totalClusters), key=lambda k: average[k])
        summary = ' '.join([sentences[relatedSent[i]] for i in summary_order])
        #temp_s.append(summary);
        output_summary.append(summary);
        
        '''
        if summary_iter % 1000 == 0 or summary_iter == len(bbc_summary):
            wrtiteToFile(fileName,output_summary);
            fileName = fileName + 1;
            output_summary=list();
            #break;
            '''
    except Exception as e:
        print(e)
        output_summary.append("ERROR") 
        continue

    #if len(output_summary) == len(bbc_summary):

 
output_pd = pd.DataFrame()
output_pd["OUR_SUMMARY"] = output_summary
output_pd.to_csv("skipThoughtOutput.csv")
print("done")
