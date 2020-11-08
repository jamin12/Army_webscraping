#%%
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#%%
# 크롬 드라이버 설정
browser = webdriver.Chrome()
#네이버 이동
browser.get("http://daum.net")
#%%
#로그인 버튼 클릭
browser.find_element_by_class_name("link_login").click()
# %%
#자동 로그인 기능

# id, pw 입력
browser.find_element_by_id("id").send_keys("user-id")
browser.find_element_by_id("inputPwd").send_keys("password")

# 로그인 버튼 클릭
browser.find_element_by_xpath("//*[@id='loginBtn']").click()

#%%
# id 를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")
# %%
# html 정보 출력
print(browser.page_source)

browser.quit() # 전체 브라우저 종료
# %%
