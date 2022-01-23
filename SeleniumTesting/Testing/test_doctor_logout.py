from audioop import add
from lib2to3.pgen2 import driver
from re import sub
import sys

sys.path.append("/home/manish/Desktop/seleniumPython/Manish")

from SeleniumTesting.page_object.pages.Doctor_HomePage import Doctor_HomePage
from SeleniumTesting.page_object.locator import Homepage

from SeleniumTesting.page_object.pages.Doctor_Register import Doctor_Register

from SeleniumTesting.page_object.pages.HomePage import HomePage



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


class TestDoctorLogout(unittest.TestCase):
    driver = setUp()

    def test_doctor_logout(self):
        data = {'name':'cook','email':'cook1@gmail.com','phone':2132980870,'password':'Cook123','re_password':'Cook123'}
        self.driver.get(Config.PROJECT_BASE_URL)
        hp = HomePage(self.driver)
        time.sleep(2)
        doctor = hp.get_doctor()
        doctor.click()
        time.sleep(2)
        doctor_sign_up = hp.get_doctor_sign_up_dropdown()
        doctor_sign_up.click()

        dr = Doctor_Register(self.driver)

        name = dr.get_name_query_box()
        email = dr.get_email_query_box()
        phone = dr.get_phone_query_box()
        password = dr.get_password_query_box()
        re_password = dr.get_re_password_query_box()
        submit = dr.get_submit_button()


        name.send_keys(data['name'])

        email.send_keys(data['email'])

        phone.send_keys(data['phone'])

        password.send_keys(data['password'])

        re_password.send_keys(data['re_password'])

        time.sleep(2)

        submit.send_keys(Keys.RETURN)

        time.sleep(2)


        self.assertEqual(Config.Doctor_Home_Page_URL,self.driver.current_url)

        time.sleep(2)

        dhp = Doctor_HomePage(self.driver)

        icon = dhp.get_icon()
        icon.click()
        time.sleep(3)
        logout = dhp.get_logout()
        logout.click()
        self.assertEqual(Config.PROJECT_BASE_URL,self.driver.current_url)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="testing_output"))