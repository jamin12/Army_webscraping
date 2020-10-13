from bs4 import BeautifulSoup
import requests
import re

def into_request(url):
    #requests로 접속하는 방법
    # 사이트 url에 접속 후 Beautifulsoup 객체에 lxml로 저장
    res = requests.get(url)
    res.raise_for_status() # 위에 코드가 이상이 있을 경우 아래 코드 실행 안됨
    soup = BeautifulSoup(res.text,"lxml")
    return soup

#vscode 단축키
#https://dayjms.tistory.com/entry/%EB%B9%84%EC%A3%BC%EC%96%BC-%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4-%EC%BD%94%EB%93%9C%EC%9D%98-11%EA%B0%80%EC%A7%80-%EC%9C%A0%EC%9A%A9%ED%95%9C-%EA%B8%B0%EB%8A%A5-1-%EB%A9%80%ED%8B%B0%EC%BB%A4%EC%84%9C-%EC%97%90%EB%94%94%ED%8C%85MultiCursor-Editing

#정규식 사이트(좀 잘나와 있음)
def regular_expression():
    url = "https://greeksharifa.github.io/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D(re)/2018/08/04/regex-usage-05-intermediate/"
    soup = into_request(url)
    menu = soup.find("div",attrs = {"class":"post"})
    chapters = menu.find_all("p")[1]
    chapter_url = chapters.find_all("a")
    for churl in chapter_url:
        print(churl.get_text())
        print(churl["href"]+"\n")
        
if __name__ == "__main__":
    regular_expression()

