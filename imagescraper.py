import requests
import html
from requests_html import HTMLSession
from bs4 import BeautifulSoup  
import os 
from urllib.parse import urlparse

ERROR_BAD_URL = -1
ERROR_BAD_FILE_PATH = -2

def getdata(url): 
    # r = requests.get(url)
    session = HTMLSession()
    response = session.get(url) 
    response.html.render(timeout=40)
    return response.html.find('img')
    # return response.html.absolute_links
    # return html.unescape(r.text) 
    
def getImgs(websiteURL, save_path):
    print("============================imagescraper htmldata====================")
    try:
        htmldata = getdata(websiteURL)
    except Exception as e:
        print(e)
        return ERROR_BAD_URL
    print(htmldata)
    htmldata = [x.html for x in htmldata]
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(htmldata)
    soup = BeautifulSoup(' '.join(htmldata), 'html.parser')
    images = soup.find_all('img')
    print("============================imagescraper images====================")
    print(images)
    print("before for loop________________________++++++++++++++++++_________________")
    for index, item in enumerate(images):
        print(item['src'])
        imageurl = item['src']
        path = urlparse(imageurl).path
        print(path)
        ext = os.path.splitext(path)[1]
        completeFilePath = os.path.join(save_path, f"img{index}{ext}")
        r = requests.get("https://www.nasa.gov" + item['src'], allow_redirects=True)
        try:
            open(completeFilePath, 'wb').write(r.content)
        except:
            return ERROR_BAD_FILE_PATH
    return len(images)
        
# getImgs("https://www.facebook.com", "../") #local testing purposes