class NetworkPage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_two_card(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="双卡与移动网络"]').click()

    def click_mobile_card(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="中国移动"]').click()

    def click_choose_net(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="网络类型选择"]').click()

    def click_choose_2g(self):
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="仅使用2G网络(更省电)"]').click()

    def click_choose_3g(self):
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="3G网络优先"]').click()
