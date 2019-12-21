class DisplayPage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_blue_tooth(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="蓝牙"]').click()

    def click_name(self):
        self.driver.find_element_by_id('miui:id/value_right').click()

    def send_keys_name(self, text):
        self.driver.find_element_by_id('com.android.settings:id/device_name').send_keys(text)





