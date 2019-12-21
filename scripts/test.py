from appium import webdriver

caps = {"platformName": "Android", "deviceName": "7137c7d0", "appPackage": "com.android.settings",
        "appActivity": "com.android.settings.MainSettings", "unicodeKeyboard": True,
        "resetKeyboard": True,
        "noReset": "True"}
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.find_element_by_xpath('//android.widget.TextView[@text="双卡与移动网络"]').click()
