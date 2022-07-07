from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import Request, urlopen
import re

links_list=[]

req= Request('https://www.itaq.nl/vacant-vacatures.html')
result=urlopen(req).read()
doc=BeautifulSoup(result,'html.parser')

link = doc.find_all('a')

#"\n"
for links in link:
    try:
        x= links.get('href')
        links_list.append(x)
        
    except:
        pass
for i in links_list:
    try:
        req= Request(i)
        result=urlopen(req).read()
        doc_link=BeautifulSoup(result,'html.parser')
        title= doc_link.find(attrs={'class':'hookItemTitle fhlItemTitle chlItemTitle'})
        email= doc_link.find(attrs={'class':'hookItemWord fhlItemWord chlItemWord chlEmail'})
        job_des= doc_link.find(attrs={'class':'text jbdText'})
        #print(job_des.text)
        #print(title.text)
        #print(email.text)
    except:
        pass
    




