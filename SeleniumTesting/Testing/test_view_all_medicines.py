from audioop import add
from lib2to3.pgen2 import driver
from re import sub
import sys

sys.path.append("/home/manish/Desktop/seleniumPython/Manish")

from SeleniumTesting.page_object.pages.HomePage import HomePage
from SeleniumTesting.page_object.pages.Doctor_Register import Doctor_Register
from SeleniumTesting.page_object.pages.Doctor_HomePage import Doctor_HomePage



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


class TestViewAllMedicines(unittest.TestCase):
    driver = setUp()

    def test_view_all_medicines(self):
        data = {'name':'rovit','relative_name':'tim','email':'rovits2@gmail.com','phone':3126543876,'ailments':'nothing','password':'rovit@123','re_password':'rovit@123','relative_phone':8465098324,'dob':'10/1/1993','address':'45-A Old Tower Dehradun 143820'}

        self.driver.get(Config.PROJECT_BASE_URL)

        hp = HomePage(self.driver)

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


        dhp = Doctor_HomePage(self.driver)


        medicines = dhp.get_medicines()
        medicines.click()

        self.assertEqual(Config.VIEW_ALL_MEDICINES_URL,self.driver.current_url)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="testing_output"))