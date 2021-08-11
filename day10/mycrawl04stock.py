import requests
from bs4 import BeautifulSoup

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

response = requests.get(url)

if response.status_code == 200:
    html = response.content.decode("euc-kr", "replace")
    soup = BeautifulSoup(html, 'html.parser')
    
    tds = soup.select(".st2")
    prices = soup.select("table > .st2 ~ td")
    print(prices)
    #
    # for idx, td in enumerate(tds):
    #     codes = tds[idx].select("a")
    #     for idx, code in enumerate(codes):
    #         s_code = code['title']
    #         s_name = code.text
    #
    # for idx, price in enumerate(prices):
        # print(idx, price)

else : 
    print(response.status_code)