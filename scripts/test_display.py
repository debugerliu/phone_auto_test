from base.base_driver import init_driver


class TestDisplay:

    def setup(self):
        self.driver = init_driver()

    def test_mobile_display_input(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="WLAN"]').click()

