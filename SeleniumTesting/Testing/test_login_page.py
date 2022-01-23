from audioop import add
from lib2to3.pgen2 import driver
from re import sub
import sys

sys.path.append("/home/manish/Desktop/seleniumPython/Manish")

from SeleniumTesting.Config.config import Config
from selenium.webdriver.common.keys import Keys 
from SeleniumTesting.page_object.locator import Homepage

import time
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
import unittest
from SeleniumTesting.Testing.test_config import setUp
from SeleniumTesting.Config.config import *
from SeleniumTesting.page_object.locator import *
import HtmlTestRunner
# import time


class TestLoginPage(unittest.TestCase):
    driver = setUp()

    def test_login_page(self):
        self.driver.get(Config.PROJECT_BASE_URL)
        sign_in = self.driver.find_element_by_xpath(Homepage.XPATH_SIGN_IN)
        sign_in.click()
        self.assertEqual(Config.LOGIN_PAGE_URL,self.driver.current_url)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="testing_output"))