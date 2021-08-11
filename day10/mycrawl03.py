import requests
from bs4 import BeautifulSoup

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    trs = soup.select("tr")
    
    for i in enumerate(trs):
        print(i)
else : 
    print(response.status_code)