from base.base_driver import init_driver
from page.display_page import DisplayPage

class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def test_mobile_display_input(self):
        # 点击蓝牙
        # 点击手机名称
        # 输入文字
        # 点击返回
        self.driver.implicitly_wait(30)
        self.display_page.click_blue_tooth()
        self.display_page.click_name()
        self.display_page.send_keys_name(text=1)


        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="蓝牙"]').click()
        # self.driver.find_element_by_id('miui:id/value_right').click()
        # self.driver.find_element_by_id('com.android.settings:id/device_name').send_keys(1)


