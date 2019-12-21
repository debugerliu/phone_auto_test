from appium import webdriver


class TestSetting:


    def setup(self):
        caps = {"platformName": "Android", "deviceName": "7137c7d0", "appPackage": "com.android.settings",
                "appActivity": ".MainSettings", "unicodeKeyboard": "True",
                "resetKeyboard": "True", 'noSign': 'True',
                "noReset": "True"}
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        print('setup')

    def test_network_2g(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="双卡与移动网络"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="中国移动"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="网络类型选择"]').click()
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="仅使用2G网络(更省电)"]').click()
        self.driver.quit()

    def test_network_3g(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="双卡与移动网络"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="中国移动"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="网络类型选择"]').click()
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="3G网络优先"]').click()

