from punctuator import Punctuator
import os
import re


#Pre trained model to punctuate the subtiles
p = Punctuator('Demo-Europarl-EN.pcl')

i=0;
#punctuate each files in the directory
for file in os.listdir("/mnt/c/Users/tselv/Downloads/summary/subtitles/esubtitles/set3"):
    try:
        if file.endswith(".txt"):
            #print(file);
            if "(1)" in file:
                print("");
            else:
                f = open("/mnt/c/Users/tselv/Downloads/summary/subtitles/esubtitles/set3/"+file, "r")
                temp=""
                for x in f:
                    if(x != "\n"):
                        temp+=x;
                temp=re.sub(r'\[\w+]','',temp)
                x=file.split(".txt")
                #print(x[0])
                x[0]=re.sub(r'\[.*?]','',x[0])
                x[0]=re.sub(r'\W+','',x[0])



                temp=p.punctuate(temp);
                f = open("./subtitle_output/sreylap/"+x[0]+".txt", "w+")
                f.write(temp);
                f.close();
                print(i);
                i=i+1;
    except Exception as e:
        print(e);
        continue;
print("done")