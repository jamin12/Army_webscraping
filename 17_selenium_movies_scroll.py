# #%%
# import requests
# from bs4 import BeautifulSoup
# #%%
# url = "https://play.google.com/store/movies/top"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.22 Safari/537.36",
#     "Accept-Language":"ko-KR,ko"
# }
# res = requests.get(url, headers = headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")
# # %%
# movies = soup.find_all("div", attrs = {"class": "ImZGtf mpg5gc"})
# print(len(movies))
# # %%
# # with open("movie.html", "w",encoding="utf-8") as f:
# #     f.write(soup.prettify())

# for movie in movies:
#     print(movie.find("div",attrs = {"class":"WsMG1c nnK0zc"}).get_text())



#%%
from selenium import webdriver
import time
#%%
broswer = webdriver.Chrome()
#페이지 이동
url = "https://play.google.com/store/movies/top"
broswer.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# broswer.execute_script("window.scrollTo(0,1080)")

#%%
# 화면 가장 아래로 스크롤 내리기
# broswer.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# %%
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = broswer.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    broswer.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = broswer.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height
print("스크롤 완료")

