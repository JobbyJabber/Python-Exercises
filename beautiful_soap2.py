import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
response = requests.get(url)
soup = BeautifulSoup(response.text) 
headers = soup.select("div.parbase.cn_text > div.body > p")
for header in headers:
    print(header.text)