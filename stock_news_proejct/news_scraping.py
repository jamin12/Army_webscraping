import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def into_request(url):
#requests로 접속하는 방법
# 사이트 url에 접속 후 Beautifulsoup 객체에 lxml로 저장
    #유저 에이전트
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.107.16 Safari/537.36"}
    res = requests.get(url,headers = headers)
    res.raise_for_status() # 위에 코드가 이상이 있을 경우 아래 코드 실행 안됨
    soup = BeautifulSoup(res.text,"lxml")
    return soup

def into_selenium(url):
#selenium으로 접속하는 방법
#브라우져 옵션 설정
    options = webdriver.ChromeOptions()
#화면 안뜨게
    options.headless = True
#유저 에이전트 설정
    options.add_argument('user agent')
#화면 사이즈 설정
    options.add_argument('window-size=1920x1080')
    broswer = webdriver.Chrome(options = options)
    broswer.maximize_window()
#브라우저 연결
    broswer.get(url)
    soup = BeautifulSoup(broswer.page_source,'lxml')
    return soup

def samsung_news():
    url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&nso=so%3Ar%2Cp%3Aall%2Ca%3Aall"
    soup = into_request(url)
    all_news = soup.find("div", attrs = {"class" : "news mynews section _prs_nws"})
    pick_news = all_news.find("ul", attrs = {"class":"type01"})
    pick = pi
if __name__ == "__main__":
    samsung_news()

