#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#%%
broswer = webdriver.Chrome()
broswer.maximize_window() # 창 최대화

#%%
broswer.get("https://flight.naver.com/flights/?trip=RT&scity1=ICN&scity2=&ecity1=&ecity2=ICN&adult=1&child=0&infant=0&fareType=YC&airlineCode=&nxQuery=%ED%95%AD%EA%B3%B5%EA%B6%8C")

# %%
#가는날 선택
# broswer.find_element_by_link_text("가는날 선택").click() # 텍스트로 검색
broswer.find_element_by_xpath("//*[@id='l_8']/div[1]/div/div[1]/a").click()

# %%
# 이번달 20 25
# broswer.find_elements_by_link_text("20")[0].click() # [0] --> 이번달
# broswer.find_elements_by_link_text("25")[0].click() # [0] --> 이번달

# 다음달 20 25
# broswer.find_elements_by_link_text("20")[1].click() # [1] --> 다음달
# broswer.find_elements_by_link_text("25")[1].click() # [1] --> 다음달

broswer.find_elements_by_link_text("20")[0].click() # [0] --> 이번달
broswer.find_elements_by_link_text("25")[1].click() # [1] --> 다음달

#%%
#제주도 검색
broswer.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()
#항공권 검색 클릭
broswer.find_element_by_link_text("항공권 검색").click()
# %%
try:
    #로딩 시간 대기를 위한 코드
    elem = WebDriverWait(broswer,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)
except:
    broswer.quit()
#첫 번째 결과 출력
# elem = broswer.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# %%
