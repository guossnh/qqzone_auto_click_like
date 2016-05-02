#by tlk
#utf-8
#  madan   jingran1   buzhichi1   zhongwen   
#jiu zhe yang ba shishi  linux 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#
driver = webdriver.Firefox()
driver.get("http://user.qzone.qq.com/")
assert "QQ空间-分享生活，留住感动" in driver.title
time.sleep(3)
#driver.execute_script("document.getElementById('switcher_plogin').click()")
driver.find_element_by_id("switcher_plogin").click()
driver.close()