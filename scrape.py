import requests
import urllib.request
import time
import os
from bs4 import BeautifulSoup

url = 'http://www.dermnet.com/images/Warts-Common/photos/4'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

images = soup.findAll('img')

num = 48

for i in images:
    if i.get('alt', '') == "Warts Common":
        url = i.get('src', '')
        urllib.request.urlretrieve(url,'./training/warts/pic'+str(num)+'.jpg') 
        num += 1
        time.sleep(1)
