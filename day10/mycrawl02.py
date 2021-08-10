import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5000/emp"

response = requests.get(url)
arr = []



if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    
else : 
    print(response.status_code)