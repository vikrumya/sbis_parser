from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import openpyxl
import re
from openpyxl import load_workbook

# путь к драйверу chrome
browser = webdriver.Chrome('chromedriver.exe')
# browser = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
# Переход на страницу входа
"""Полкючение базы для парсинга"""
wb = load_workbook('putin_data.xlsx')
"""Организации"""
print('загрузка данных')
sheet_ranges = wb['Лист1']
column_a = sheet_ranges['A']
org = []
for i in range(len(column_a)):
    print(column_a[i].value)
    org.append(column_a[i].value)
print(org)
"""ИНН"""
column_b = sheet_ranges['B']
inn = []
for i in range(len(column_b)):
    print(column_b[i].value)
    inn.append(column_b[i].value)
print(inn)
print('Данные загружены')
org.pop(0)
inn.pop(0)
agent = browser.execute_script("return navigator.userAgent")
print(agent)
print('User-agent правильный')
print('Логинимся')
# browser.set_preference("general.useragent.override", useragent)
browser.get('https://online.sbis.ru/page/company')
time.sleep(3)
"""Логинимся"""
login = browser.find_element_by_xpath('//*[@id="auth-loginForm_login"]/div/div/input')
login.send_keys('********')
password = browser.find_element_by_xpath('//*[@id="auth-loginForm_password"]/div/div/input')
password.send_keys('********')
begin = browser.find_element_by_xpath(
    '//*[@id="wasaby-content"]/div[1]/div[2]/div/div[3]/div[2]/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/button')
begin.click()
print('ЗАЛОГИНИЛИСЬ')
time.sleep(7)
print('Начинаем парсить')
search = browser.find_element_by_xpath(
    '//*[@id="wasaby-content"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/input')
email = []
director_name = []
post = []
telephone = []
adress = []
keepers = []
site = []
for item in inn:
    print('Парсим ', item)
    search.send_keys(item)
    time.sleep(5)
    company = browser.find_element_by_xpath(
        '//*[@id="wasaby-content"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/span')
    company.click()
    time.sleep(10)
    try:
        temp = browser.find_element_by_xpath(
        '//*[@id="popup"]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[3]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]').text
        director_name.append(temp)
        print(director_name)
    except:
        temp = ''
        director_name.append(temp)
        print('ФИО директора не найдено')
    try:
        temp = browser.find_element_by_xpath(
        '//*[@id="popup"]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[3]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[1]').text
        post.append(temp)
        print(post)
    except:
        temp = ''
        post.append(temp)
        print('Должность не найдена')
    try:
        temp = browser.find_element_by_xpath('//*[@id="popup"]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[3]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div[1]/div').text
        telephone.append(temp)
        print(telephone)
    except:
        temp = ''
        telephone.append(temp)
        print('Телефон не найден')
    try:
        temp = browser.find_element_by_xpath('//*[@id="popup"]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[3]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/div[3]/div[2]/div[1]').text
        email.append(temp)
        print(email)
    except:
        temp = ''
        email.append(temp)
        print('Email не найден')
    try:
        temp = browser.find_element_by_xpath('//*[@id="popup"]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[3]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[2]').text
        adress.append(temp)
        print(adress)
    except:
        temp = ''
        adress.append(temp)
        print('Адрес не найден')
    try:
        temp = browser.find_element_by_xpath('//*[@id="popup"]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[3]/div[2]/div[1]/div[3]/div/div/div/div[1]/div/div[1]/div[3]/div[2]/div[2]/div/div[1]/div/div').text
        summ = browser.find_element_by_xpath('//*[@id="popup"]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[3]/div[2]/div[1]/div[3]/div/div/div/div[1]/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div').text
        procent = browser.find_element_by_xpath('//*[@id="popup"]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[3]/div[2]/div[1]/div[3]/div/div/div/div[1]/div/div[1]/div[3]/div[2]/div[2]/div/div[3]/div/div/div').text
        tempus = temp + summ + procent
        keepers.append(tempus)
        print(keepers)
    except:
        temp = ''
        keepers.append(temp)
        print('Владельцы не найдены')
    try:
        temp = browser.find_element_by_xpath('//*[@id="popup"]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[3]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div[3]/div/div[3]/div[2]/div[1]/div/div/div').text
        site.append(temp)
        print(site)
    except:
        temp = ''
        site.append(temp)
        print('Сайт не найден')
    search.clear()

wb=load_workbook('putin_data.xlsx')
#wb.create_sheet(title = 'Первый лист', index = 0)
# получаем лист, с которым будем работать
sheet = wb['Лист1']
i = 2
j = 0
sheet.cell(row=1, column=3).value = 'ФИО'
sheet.cell(row=1, column=4).value = 'Должность'
sheet.cell(row=1, column=5).value = 'Телефон'
sheet.cell(row=1, column=6).value = 'email'
sheet.cell(row=1, column=7).value = 'Сайт'
sheet.cell(row=1, column=8).value = 'Адрес'
sheet.cell(row=1, column=9).value = 'Учредители'
for item in inn:
    sheet.cell(row=i, column=3).value = director_name[j]
    sheet.cell(row=i, column=4).value = post[j]
    sheet.cell(row=i, column=5).value = telephone[j]
    sheet.cell(row=i, column=6).value = email[j]
    sheet.cell(row=i, column=7).value = site[j]
    sheet.cell(row=i, column=8).value = adress[j]
    sheet.cell(row=i, column=9).value = keepers[j]
    i += 1
    j += 1
wb.save('putin_data.xlsx')
driver.quit()
# Поиск тегов по имени
# email = browser.find_element_by_name('ctl00$MainContent$ctlLogin$_UserName')
# password = browser.find_element_by_name('ctl00$MainContent$ctlLogin$_Password')
# login = browser.find_element_by_name('ctl00$MainContent$ctlLogin$BtnSubmit')
