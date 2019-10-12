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

from selenium.webdriver.support.ui import WebDriverWait #等待一个元素加载完成



driver = selenium.webdriver.Chrome()

driver.get("https://www.zhipin.com")

driver.get("https://www.zhipin.com/c101010100/?query=Php&page=1&ka=page-1")
print(driver.page_source)


