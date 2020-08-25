#%%
#초기 설정
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#%%
def weather():
    #requests로 접속하는 방법
    # 사이트 url에 접속 후 Beautifulsoup 객체에 lxml로 저장
    url = "https://search.naver.com/search.naver?ie=UTF-8&sm=whl_hty&query=%EB%82%A0%EC%94%A8+"
    res = requests.get(url)
    res.raise_for_status() # 위에 코드가 이상이 있을 경우 아래 코드 실행 안됨
    soup = BeautifulSoup(res.text,"lxml")
    weathers = soup.find("div", attrs = {"class":"info_data"}) # 날씨의 종합적인 정보 가져오기
    weather = weathers.find("p",attrs = {"class":"cast_txt"}).get_text() # 오늘의 날씨 가져오기
    Temp = weathers.find("span",attrs = {"class":"todaytemp"}).get_text() # 현재 온도 
    Min_temp = weathers.find("span",attrs = {"class":"min"}).get_text() # 최소 온도
    Max_temp = weathers.find("span",attrs = {"class":"max"}).get_text() # 최대 온도
    Rain = soup.find("li",attrs = {"class":"date_info today"})# 오늘 날씨 강수량
    AM_rain_rate = Rain.find_all("span",attrs = {"class":"num"})[0].get_text() # 오전 강수량
    PM_rain_rate = Rain.find_all("span",attrs = {"class":"num"})[1].get_text() # 오후 강수량
    dusts = soup.find("div", attrs = {"class":"sub_info"})
    dust = dusts.find_all("dd",attrs = {"class":"lv1"})[0].get_text()
    undust = dusts.find_all("dd",attrs = {"class":"lv1"})[1].get_text()
    print(f"[오늘의 날씨]\n{weather}\n현재 {Temp} (최저{Min_temp} / 최대{Max_temp})")
    print(f"오전 강수확률 {AM_rain_rate}% / 오후 강수확률 {PM_rain_rate}%\n")
    print(f"미세먼지 {dust}\n초미세먼지 {undust}")
#%%
def news_headline():
    #selenium으로 접속하는 방법
    #브라우져 옵션 설정
    options = webdriver.ChromeOptions()
    #화면 안뜨게
    options.headless = True
    #유저 에이전트 설정
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
    #화면 사이즈 설정
    options.add_argument("window-size=1920x1080")

    broswer = webdriver.Chrome(options = options)
    broswer.maximize_window()
    #브라우저 연결
    url = "https://search.naver.com/search.naver?ie=UTF-8&sm=whl_hty&query=%EB%82%A0%EC%94%A8+"
    broswer.get(url)
    soup = BeautifulSoup(broswer.page_source,"lxml")
    #뉴스 헤드라인 정보 가저오기

#%%
if __name__ == "__main__":
    # weather()
# %%
