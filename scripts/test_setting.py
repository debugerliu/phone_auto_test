from appium import webdriver


class TestSetting:

    def setup(self):
        caps = {"platformName": "Android", "deviceName": "c3e0d4dd", "appPackage": "com.android.settings",
                "appActivity": ".HWSettings", "unicodeKeyboard": "True",
                "resetKeyboard": "True",
                "noReset": "True"}
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        print('setup')

    def test_login(self):
        print('成功')
