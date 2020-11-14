import requests
from bs4 import BeautifulSoup

#requests로 접속하는 방법
def into_request(url):
    #유저 에이전트
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.15 Safari/537.36"}
    # 사이트 url에 접속 후 Beautifulsoup 객체에 lxml로 저장
    res = requests.get(url,headers = headers)
    res.raise_for_status() # 위에 코드가 이상이 있을 경우 아래 코드 실행 안됨
    soup = BeautifulSoup(res.text,"lxml")
    return soup


def get_keyword_number(keyword):
    url = f"https://www.google.com/search?q={keyword}&aqs=chrome..69i57j69i64l2j69i60j0l4&sourceid=chrome&ie=UTF-8"
    soup = into_request(url)

    number = soup.find("div",attrs = {"id" : "result-stats"}).get_text()
    number = int(number[number.find("약") + 2:number.rfind("개")].replace(',',''))
    print(number)
    return number
if __name__ == "__main__":
    pass