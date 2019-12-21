from base.base_driver import init_driver
from page.network_page import NetworkPage


class TestNetWork:

    def setup(self):
        self.driver = init_driver()
        self.network_page = NetworkPage(self.driver)

    def test_network_2g(self):
        self.driver.implicitly_wait(30)
        self.network_page.click_two_card()
        self.network_page.click_mobile_card()
        self.network_page.click_choose_net()
        self.network_page.click_choose_2g()
        # self.driver.implicitly_wait(30)
        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="双卡与移动网络"]').click()
        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="中国移动"]').click()
        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="网络类型选择"]').click()
        # self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="仅使用2G网络(更省电)"]').click()
        # self.driver.quit()

    def test_network_3g(self):
        self.driver.implicitly_wait(30)
        self.network_page.click_two_card()
        self.network_page.click_mobile_card()
        self.network_page.click_choose_net()
        self.network_page.click_choose_3g()
        # self.driver.implicitly_wait(30)
        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="双卡与移动网络"]').click()
        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="中国移动"]').click()
        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="网络类型选择"]').click()
        # self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="3G网络优先"]').click()
