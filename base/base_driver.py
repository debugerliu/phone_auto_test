from appium import webdriver


def init_driver():
    caps = {"platformName": "Android", "deviceName": "7137c7d0", "appPackage": "com.android.settings",
            "appActivity": ".MainSettings", "unicodeKeyboard": "True",
            "resetKeyboard": "True",
            "noReset": "True"}
    return webdriver.Remote("http://localhost:4723/wd/hub", caps)

