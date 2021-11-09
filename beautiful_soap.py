import requests
from bs4 import BeautifulSoup

url = 'https://www.wp.pl/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
headers = soup.find_all('h3')
for header in headers:
    print(header.text)