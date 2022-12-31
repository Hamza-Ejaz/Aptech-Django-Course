import requests
from bs4 import BeautifulSoup
page = requests.get('https://www.olx.com.pk/')
contents = page.content
soup = BeautifulSoup(contents,'html.parser')
for link in soup.find_all('div'):
    print(link.get('_1075525d d059c029 _858a64cf'))