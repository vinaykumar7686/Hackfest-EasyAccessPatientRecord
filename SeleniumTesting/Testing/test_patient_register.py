from audioop import add
from lib2to3.pgen2 import driver
from re import sub
import sys

sys.path.append("/home/manish/Desktop/seleniumPython/Manish")

from SeleniumTesting.page_object.pages.Patient_Register import Patient_Register


from SeleniumTesting.Config.config import Config
from selenium.webdriver.common.keys import Keys 
from SeleniumTesting.page_object.locator import Homepage
from SeleniumTesting.page_object.pages.HomePage import HomePage


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


class TestPatientRegister(unittest.TestCase):
    driver = setUp()

    def test_patient_register(self):
        data = {'name':'rovit','relative_name':'tim','email':'rovits@gmail.com','phone':3126543876,'ailments':'nothing','password':'rovit@123','re_password':'rovit@123','relative_phone':8465098324,'dob':'10/1/1993','address':'45-A Old Tower Dehradun 143820'}
        self.driver.get(Config.PROJECT_BASE_URL)

        hp = HomePage(self.driver)


        patient= hp.get_patient()
        patient.click()
        time.sleep(2)
        patient_sign_up = hp.get_patient_sign_up_dropdown()
        patient_sign_up.click()

        time.sleep(2)

        print(self.driver.current_url)

        pr = Patient_Register(self.driver)


        name = pr.get_name()
        relative_name = pr.get_relative_name()
        email = pr.get_email()
        phone = pr.get_phone()
        ailments = pr.get_ailments()
        password = pr.get_password()
        re_password = pr.get_re_password()
        relative_phone = pr.get_relative_phone()
        dob = pr.get_dob()
        address = pr.get_address()
        time.sleep(5)


        name.send_keys(data['name'])
        time.sleep(5)

        relative_name.send_keys(data['relative_name'])
        time.sleep(5)

        email.send_keys(data['email'])
        time.sleep(5)

        phone.send_keys(data['phone'])
        time.sleep(5)

        ailments.send_keys(data['ailments'])
        time.sleep(5)

        password.send_keys(data['password'])
        time.sleep(5)

        re_password.send_keys(data['re_password'])
        time.sleep(5)

        relative_phone.send_keys(data['relative_phone'])
        time.sleep(5)

        dob.send_keys(data['dob'])
        time.sleep(5)

        address.send_keys(data['address'])
        time.sleep(5)

        submit = pr.get_submit()
        submit.send_keys(Keys.RETURN)
        time.sleep(5)


        self.assertEqual(Config.PATIENT_MEDICAL_FORM_URL,self.driver.current_url)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="testing_output"))