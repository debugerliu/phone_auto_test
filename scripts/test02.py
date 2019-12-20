from time import sleep
from scripts import test03
from appium import webdriver

import time
import re

from selenium.common.exceptions import NoSuchElementException

# 配置信息
caps = {"platformName": "Android", "deviceName": "7137c7d0", "appPackage": "com.android.settings",
        "appActivity": ".MainSettings", "unicodeKeyboard": "True",
        "resetKeyboard": "True", 'noSign':'True',
        "noReset": "True"}
# 初始化driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(30)
c = test03.webinfo()
c.ww()
sleep(3)
driver.find_element_by_xpath('//android.widget.TextView[@text="双卡与移动网络"]').click()
sleep(3)
c.mm()
sleep(3)
driver.find_element_by_xpath('//android.widget.TextView[@text="中国移动"]').click()
sleep(3)
c.mmm()
print(111111111111111111)
