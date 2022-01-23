from audioop import add
from lib2to3.pgen2 import driver
from re import sub
import sys


sys.path.append("/home/manish/Desktop/seleniumPython/Manish")

from SeleniumTesting.page_object.pages.HomePage import HomePage
from SeleniumTesting.page_object.pages.LoginPage import LoginPage

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


class TestSignInValidData(unittest.TestCase):
    driver = setUp()

    def test_sign_in_valid_data(self):
        self.driver.get(Config.PROJECT_BASE_URL)

        hp = HomePage(self.driver)

        sign_in = hp.get_sign_in()
        sign_in.click()


        lp = LoginPage(self.driver)

        email = lp.get_email()
        email.send_keys('y@gmail.com')

        password = lp.get_password()
        password.send_keys('1')

        submit = lp.get_submit()
        submit.click()
        self.assertEqual(Config.patient_home_page,self.driver.current_url)
    

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="testing_output"))