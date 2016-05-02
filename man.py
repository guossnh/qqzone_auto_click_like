#by tlk
#utf-8
#  madan   jingran1   buzhichi1   zhongwen   
#jiu zhe yang ba shishi  linux 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
assert "百度一下，你就知道" in driver.title
time.sleep(5)
driver.close()