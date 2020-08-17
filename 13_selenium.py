#%%
# 크롬 드라이버 설정
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
#%%
#네이버 들어가기
browser.get("http://naver.com")
# %%
elem = browser.find_element_by_class_name("link_login")
# %%
# elem.click() # 클릭
# browser.back() # 뒤로 가기
# browser.forward() # 앞으로 가기
# browser.refresh() # 새로고침
 
elem = browser.find_element_by_id("query")
#%%
elem.send_keys("나도코딩")
#%%
elem.send_keys(Keys.ENTER)
# %%
