from selenium.webdriver.common.by import By


class NetworkPage(object):

    two_card_button = By.XPATH, '//android.widget.TextView[@text="双卡与移动网络"]'
    china_mobile_button = By.XPATH, '//android.widget.TextView[@text="中国移动"]'
    choose_net_button = By.XPATH, '//android.widget.TextView[@text="网络类型选择"]'
    choose_2g_button = By.XPATH, '//android.widget.CheckedTextView[@text="仅使用2G网络(更省电)"]'
    choose_3g_button = By.XPATH, '//android.widget.CheckedTextView[@text="3G网络优先"]'

    def __init__(self, driver):
        self.driver = driver

    def click_two_card(self):
        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="双卡与移动网络"]').click()
        self.find_element(self.two_card_button).click()

    def click_mobile_card(self):
        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="中国移动"]').click()
        self.find_element(self.china_mobile_button).click()

    def click_choose_net(self):
        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="网络类型选择"]').click()
        self.find_element(self.choose_net_button).click()

    def click_choose_2g(self):
        # self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="仅使用2G网络(更省电)"]').click()
        self.find_element(self.choose_2g_button).click()

    def click_choose_3g(self):
        # self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="3G网络优先"]').click()
        self.find_element(self.choose_3g_button).click()

    def find_element(self, ele):
        return self.driver.find_element(ele[0], ele[1])
