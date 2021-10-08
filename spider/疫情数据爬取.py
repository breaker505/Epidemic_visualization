# 疫情数据网址    https://news.qq.com/zt2020/page/feiyan.htm#/global
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)
# driver.get("https://news.qq.com/zt2020/page/feiyan.htm#/global")
# input_str = driver.find_element_by_class_name('number')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

r = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia', headers=headers)
print(r.status_code)
print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
context = soup.find_all('p',class_="subBlock6___3JMrs")
#<p class="subBlock6___3JMrs">43,619,754</p>
print(context)
