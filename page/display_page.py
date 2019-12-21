from selenium.webdriver.common.by import By


class DisplayPage(object):

    display_button = By.XPATH, '//android.widget.TextView[@text="蓝牙"]'
    name_button = By.ID, 'miui:id/value_right'
    send_name_button = By.ID, 'com.android.settings:id/device_name'

    def __init__(self, driver):
        self.driver = driver

    def click_blue_tooth(self):
        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="蓝牙"]').click()
        # self.driver.find_element(self.display_button[0], self.display_button[0]).click()
        self.find_element(self.display_button).click()

    def click_name(self):
        # self.driver.find_element_by_id('miui:id/value_right').click()
        self.driver.find_element(By.ID, 'miui:id/value_right').click()

    def send_keys_name(self, text):
        # self.driver.find_element_by_id('com.android.settings:id/device_name').send_keys(text)
        self.driver.find_element(By.ID, 'com.android.settings:id/device_name').send_keys(text)

    def find_element(self, ele):
        return self.driver.find_element(ele[0], ele[1])
