from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import Request, urlopen



def extract(page):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    url= f'https://pk.indeed.com/jobs?l=Karachi&start={page}'
    req=requests.get(url,headers)
    doc= BeautifulSoup(req.content,'html.parser')
    return doc

def trans(doc):
    divs = doc.find_all('div',class_='job_seen_beacon')
    for item in divs:
        title= item.find('a').text
        company_name= item.find('span',class_='companyName').text
        company_location= item.find('div',class_='companyLocation').text.strip()
        job={
            'title':title,
            'company_name':company_name,
            'company_location':company_location
            }
        joblist.append(job)
    return


joblist=[]

c= extract(0)
trans(c)
print(joblist)    
    
    
