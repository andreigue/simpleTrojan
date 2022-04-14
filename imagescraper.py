from tokenize import String
import requests
import html
from requests_html import HTMLSession
from bs4 import BeautifulSoup  
import os 
from urllib.parse import urlparse

ERROR_BAD_URL = -1
ERROR_BAD_FILE_PATH = -2

def getdata(url): 
    session = HTMLSession()
    response = session.get(url) 
    response.html.render(timeout=40)
    return response.html.find('img')
    
def getBaseURL(websiteURL:str):
    endPosition = websiteURL[8:].find('/') + 8 # add 8 for first 8 characters skipped ('http://')
    baseURL = websiteURL[:endPosition]
    return baseURL

def isRelativeURL(url):
        return url[0]=='/'

def getImgs(websiteURL, save_path):
    try:
        htmldata = getdata(websiteURL)
    except Exception as e:
        print(e)
        return ERROR_BAD_URL
    htmldata = [x.html for x in htmldata]
    soup = BeautifulSoup(' '.join(htmldata), 'html.parser')
    images = soup.find_all('img')
    baseURL = getBaseURL(websiteURL)
    for index, item in enumerate(images):
        imageurl = item['src']
        path = urlparse(imageurl).path
        ext = os.path.splitext(path)[1]
        completeFilePath = os.path.join(save_path, f"img{index}{ext}")
        if isRelativeURL(item['src']): 
            r = requests.get(baseURL + item['src'], allow_redirects=True)
        else:
            r = requests.get(item['src'], allow_redirects=True)
        try:
            open(completeFilePath, 'wb').write(r.content)
        except:
            return ERROR_BAD_FILE_PATH
    return len(images)
        
# getImgs("https://www.facebook.com", "../") #local testing purposes