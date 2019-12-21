from selenium import webdriver


class webinfo(object):

    def __init__(self):
        self.driver1 = webdriver.Chrome()

    def ww(self):
        self.driver1.get('http://www.baidu.com')

    def mm(self):
        self.driver1.find_element_by_xpath('//*[@id="kw"]').send_keys('点击了双卡')

    def mmm(self):
        self.driver1.find_element_by_xpath('//*[@id="kw"]').send_keys('点击了中国移动')

