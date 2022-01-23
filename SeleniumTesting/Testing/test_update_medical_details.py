from audioop import add
from lib2to3.pgen2 import driver
from pydoc import doc
from re import sub
import sys


sys.path.append("/home/manish/Desktop/seleniumPython/Manish")

from SeleniumTesting.page_object.pages.HomePage import HomePage
from SeleniumTesting.page_object.pages.LoginPage import LoginPage
from SeleniumTesting.page_object.pages.Patient_HomePage import Patient_HomePage

from SeleniumTesting.page_object.pages.Update_Medical_Details import Update_Medical_Details

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


class TestUpdateMedicalDetails(unittest.TestCase):
    driver = setUp()

    def test_update_medical_details(self):
        self.driver.get(Config.PROJECT_BASE_URL)

        hp = HomePage(self.driver)

        sign_in = hp.get_sign_in()
        sign_in.click()

        self.assertEqual(Config.LOGIN_PAGE_URL,self.driver.current_url)

        lp = LoginPage(self.driver)

        email = lp.get_email()
        password = lp.get_password()

        email.send_keys('y@gmail.com')
        password.send_keys('1')

        sign_in = lp.get_submit()
        sign_in.click()


        self.assertEqual(Config.patient_home_page,self.driver.current_url)  


        php = Patient_HomePage(self.driver)


        icon = php.get_icon()

        icon.click()

        time.sleep(3)

        update_medical_details = php.get_update_medical_details()

        update_medical_details.click()

        self.assertEqual(Config.update_medical_details_url,self.driver.current_url)


        umd = Update_Medical_Details(self.driver)


        medical_history = umd.get_medical_history()

        medical_history.send_keys('Updated')

        submit = umd.get_submit()

        submit.click()

        self.assertEqual(Config.patient_home_page,self.driver.current_url)


    

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="testing_output"))
