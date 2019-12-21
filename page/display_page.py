from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DisplayPage(BaseAction):

    display_button = By.XPATH, '//android.widget.TextView[@text="蓝牙"]'
    name_button = By.ID, 'miui:id/value_right'
    send_name_button = By.ID, 'com.android.settings:id/device_name'

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def click_blue_tooth(self):
        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="蓝牙"]').click()
        # self.driver.find_element(self.display_button[0], self.display_button[0]).click()
        # self.find_element(self.display_button).click()
        self.click(self.display_button)

    def click_name(self):
        # self.driver.find_element_by_id('miui:id/value_right').click()
        # self.driver.find_element(By.ID, 'miui:id/value_right').click()
        # self.driver.find_element(self.name_button).click()
        self.click(self.name_button)

    def send_keys_name(self, text):
        # self.driver.find_element_by_id('com.android.settings:id/device_name').send_keys(text)
        # self.driver.find_element(By.ID, 'com.android.settings:id/device_name').send_keys(text)
        self.input_text(self.send_name_button, text)
