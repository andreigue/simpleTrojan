import requests
from bs4 import BeautifulSoup  
import os 
from urllib.parse import urlparse

def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
def getImgs(websiteURL, save_path):
    try:
        htmldata = getdata(websiteURL)
    except Exception as e:
        return False

    soup = BeautifulSoup(htmldata, 'html.parser')
    for index, item in enumerate(soup.find_all('img')):
        print(item['src'])
        imageurl = item['src']
        path = urlparse(imageurl).path
        ext = os.path.splitext(path)[1]
        completeFilePath = os.path.join(save_path, f"img{index}{ext}")
        r = requests.get(item['src'], allow_redirects=True)
        open(completeFilePath, 'wb').write(r.content)
    return True
        
# getImgs("https://www.facebook.com", "../") #local testing purposes