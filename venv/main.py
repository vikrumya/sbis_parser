from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# путь к драйверу chrome
browser = webdriver.Chrome('chromedriver.exe')
# browser = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
# Переход на страницу входа
agent = browser.execute_script("return navigator.userAgent")
print(agent)
#browser.set_preference("general.useragent.override", useragent)
browser.get('https://online.saby.ru/auth/?ret=%2F&tab=demo')
time.sleep(3)
begin = browser.find_element_by_xpath('//*[@id="wasaby-content"]/div[1]/div[2]/div/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[3]/div[2]/div[1]')
begin.click()
time.sleep(15)
search = browser.find_element_by_xpath('//*[@id="wasaby-content"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/input')
search.send_keys('7802112110')
time.sleep(3)
company = browser.find_element_by_xpath('//*[@id="wasaby-content"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/span')
company.click()
time.sleep(3)
director_name = browser.find_element_by_xpath('//*[@id="popup"]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div').text
post = browser.find_element_by_xpath('//*[@id="popup"]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[1]').text
print(director_name)
print(post)

# Поиск тегов по имени
# email = browser.find_element_by_name('ctl00$MainContent$ctlLogin$_UserName')
# password = browser.find_element_by_name('ctl00$MainContent$ctlLogin$_Password')
# login = browser.find_element_by_name('ctl00$MainContent$ctlLogin$BtnSubmit')