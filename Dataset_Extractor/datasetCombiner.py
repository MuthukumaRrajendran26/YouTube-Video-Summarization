import os
import re
import csv

i=0;

with open('./bbc_dataset.csv', 'a+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ARTICLE", "SUMMARY"])
    #list all the article in the folder tech_sum
    for sub1 in os.listdir("./BBC/tech_sum/"):
        try:
            #list all the article in the folder tech_summary
            for sum in os.listdir("./BBC/tech_summary/"):
                row=list()
                if sum == sub1:
                    f = open("./BBC/tech_sum/"+sub1, "r")
                    temp_sub=""
                    for x in f:
                        if(x!= "\n"):
                            temp_sub+=x;
                    row.append(temp_sub);
                    g = open("./BBC/tech_summary/"+sum, "r")
                    temp_sum=""
                    for y in g:
                        temp_sum+=y;
                    row.append(temp_sum)
                    #write it to the dataset file named bbc_dataset
                    writer.writerow(row);
                    i=i+1;
                    print(i,"file matched");
        except Exception as e:
            print(e);

            
            
        
        
