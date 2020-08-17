#%%
from selenium import webdriver
#셀레니움에 키입력 하기위한 설정
from selenium.webdriver.common.keys import Keys
# 크롬 드라이버 설정
browser = webdriver.Chrome()
#%%
#사이트 들어가기
browser.get("http://naver.com")
# %%
#클래스 이름으로 원하는 값 찾기
elem = browser.find_element_by_class_name("link_login")
# %%
# elem.click() # 클릭
# browser.back() # 뒤로 가기
# browser.forward() # 앞으로 가기
# browser.refresh() # 새로고침
 
 # id로 원하는 값 찾기
elem = browser.find_element_by_id("query")
#%%
elem.send_keys("나도코딩")
#%%
elem.send_keys(Keys.ENTER)
# %%
#테그 이름으로 원하는 값 찾기
elem = browser.find_elements_by_tag_name("a")
for e in elem:
    e.get_attribute("href")

#%%
elem = browser.find_element_by_xpath("//*[@id='nx_search_form']/fieldset/button")
elem.click()
# %%
browser.quit()
# %%
