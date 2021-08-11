import os
import sys
import urllib.request
from bs4 import BeautifulSoup
from day10 import dao_naver
from day10.dao_naver import DaoNaver
client_id = "Im5DAailWxE9nwo4U82W"
client_secret = "ihYKqNfB9S"
encText = urllib.parse.quote("주식")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)

rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    soup = BeautifulSoup(response_body.decode('utf-8'), 'xml.parser') 
    items = soup.select("item")
    
    for idx, item in enumerate(items) :
        title = item.title.text        
        link = item.link.text        
        description = item.description.text        
        bloggername = item.bloggername.text        
        bloggerlink = item.bloggerlink.text        
        postdate = item.postdate.text        

        dao=DaoNaver()
        count = dao.insert(title, link, description, bloggername, bloggerlink, postdate)
        print(count)
        
else:
    print("Error Code:" + rescode)

