import requests
from bs4 import BeautifulSoup  
import os 
from urllib.parse import urlparse

ERROR_BAD_URL = -1
ERROR_BAD_FILE_PATH = -2

def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
def getImgs(websiteURL, save_path):
    try:
        htmldata = getdata(websiteURL)
    except Exception as e:
        return ERROR_BAD_URL

    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')
    for index, item in enumerate(images):
        print(item['src'])
        imageurl = item['src']
        path = urlparse(imageurl).path
        ext = os.path.splitext(path)[1]
        completeFilePath = os.path.join(save_path, f"img{index}{ext}")
        r = requests.get(item['src'], allow_redirects=True)
        try:
            open(completeFilePath, 'wb').write(r.content)
        except:
            return ERROR_BAD_FILE_PATH
    return len(images)
        
# getImgs("https://www.facebook.com", "../") #local testing purposes