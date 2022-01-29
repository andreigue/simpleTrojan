import requests
from bs4 import BeautifulSoup   

def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
def getImgs():
    
    htmldata = getdata("http://www.facebook.com") 
    soup = BeautifulSoup(htmldata, 'html.parser') 
    for index, item in enumerate(soup.find_all('img')):
        print(item['src'])
        r = requests.get(item['src'], allow_redirects=True)
        print(r)
        open('img'+str(index), 'wb').write(r.content)
        
getImgs()