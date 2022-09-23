import logging
from selenium import webdriver


class Initializer():

    test_suit_name = ""
    driver = ""

    def initialize_chrome(self, suite_name):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome("../Drivers/chromedriver.exe", 0, options)
        self.driver = driver
        self.test_suit_name = suite_name
        return driver

    @classmethod
    def initialize_test_suite_name(cls):
        return cls.test_suit_name

    def close_chrome(self):
        self.driver.close()
