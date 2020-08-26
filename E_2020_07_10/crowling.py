import requests
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/movies/"
requests = requests.get(url)
requests = requests.content
# print(requests)


html = BeautifulSoup(requests, "html.parser")
ol = html.find('ol')
# print(ol)

li = ol.find_all("li")
# print(li)

for i in li :
    div = i.find("div",{"class" : "box-contentss"})
    strong = div.find('strong').text
    print(strong)


