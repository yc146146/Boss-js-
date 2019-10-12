import requests

import re

import time
import lxml
import lxml.etree

import datetime
import json
import os

import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions

from selenium.webdriver.support.ui import WebDriverWait #等待一个元素加载完成

#boss直聘
#无法使用无界面模式
chrome_options = ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = selenium.webdriver.Chrome(options=chrome_options)

print("开始")
driver.get("https://www.zhipin.com/c101010100/?query=Php&page=1&ka=page-1")
time.sleep(1)
print(driver.page_source)
print("完成")
#print(driver.get_cookies())

for cookie in driver.get_cookies():
	if cookie["name"] == "__zp_stoken__":
		print(cookie["value"])
