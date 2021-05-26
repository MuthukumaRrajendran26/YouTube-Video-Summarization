from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import os, time
import re

totalLink = 0;
targetUrl='https://www.youtube.com/watch?v=DZwi2fMxXbY&list=PLA0c-X5PdUCXWWJb8XFqdbpelQQFdBTk-'
totalUrl=set()
f = open("./Summary/links.txt", "w+")


#method to collect the youtube links for extracting the subtitle

def method(targetUrl):
    global totalLink;
    r = requests.get(targetUrl)
    page = r.text
    soup=bs(page,'html.parser')
    res=soup.find_all('a',{'class':'playlist-video'})
    i=0;
    print("i value",i);
    print("Link size",len(res))
    for l in res:
        url='https://www.youtube.com'+l.get("href");
        f.write(str(url)+",");
        totalUrl.add(url);
        
        print("Total links",totalLink);
        print("Current link increment",i);
        i=i+1;
        if( totalLink == 4000 ):
            print("going to break");
            break;
        if (i == len(res)):
            totalLink+= i;
            x = url.split("&index")
            targetUrl = x[0];
            print(targetUrl);
            method(targetUrl);
            print("hello");
        
method(targetUrl)
print(len(totalUrl));


f.close();

#extract the links stored in the file

f = open("./Summary/links.txt", "r+")
links=f.read()
link=links.split(",")

#Using selenium download the subtitles from the site

for l in link:
    try:
        rp=requests.get(l);
        descPage=rp.text
        soup1=bs(descPage,'html.parser')
        titletag=soup1.find('title');
        title=titletag.text.split("- YouTube");
        print(title[0]);
        resp=soup1.find('p',attrs={'id':'eow-description'})
        summary=resp.text.split("For more info")
        print(summary[0]);
        x = l.split("&index")
        url = x[0];
        print(url);
        CHROMEDRIVERPATH = os.path.join(os.getcwd(), "chromedriver.exe")
        options = Options()
        ##options.add_argument("--headless")
        driver = webdriver.Chrome(options=options, executable_path=CHROMEDRIVERPATH)
        driver.get('https://downsub.com/')
        username_input = driver.find_element_by_id("input-30")
        username_input.send_keys(url)
        driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[1]/div/div[2]/form/div/div[2]/button/span').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div/div/div[1]/div[2]/div[1]/a[2]/button/span/button').click()
        title[0] = re.sub(r'\W','',title[0])
        print(title[0])
        f = open("./Summary/"+title[0]+".txt", "w+")
        f.write(summary[0]);
        f.close();
        ##break;
    except Exception as e:
        print("Some exception",e);
        continue;
        
print("done")




