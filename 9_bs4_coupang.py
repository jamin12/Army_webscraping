import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.22 Safari/537.36"}
res = requests.get(url,headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")


items = soup.find_all("li", attrs = {"class" : re.compile("^search-product")})
# print(items[0].find("div",attrs = {"class" : "name"}).get_text())

for item in items:
    name = item.find("div",attrs = {"class" : "name"}).get_text() # 제품 이름 가져오기
    price = item.find("strong", attrs = {"class":"price-value"}).get_text() # 제품 가격 가져오기
    rate = item.find("em", attrs = {"class":"rating"}) # 제품 평점 가져오기
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
    count = item.find("span", attrs = {"class":"rating-total-count"}) # 제품 평점 수 가져오기
    if count:
        count = count.get_text()
    else:
        count = "평점 수 없음"

    print(name,price,rate,count)

print("hihi")
