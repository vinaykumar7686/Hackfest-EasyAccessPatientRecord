from audioop import add
from lib2to3.pgen2 import driver
from re import sub
import sys


sys.path.append("/home/manish/Desktop/seleniumPython/Manish")

from SeleniumTesting.page_object.pages.Add_Prescription import Add_Prescription
from SeleniumTesting.page_object.pages.Doctor_HomePage import Doctor_HomePage
from SeleniumTesting.page_object.pages.HomePage import HomePage

from SeleniumTesting.Config.config import Config
from selenium.webdriver.common.keys import Keys 
from SeleniumTesting.page_object.locator import Homepage
from SeleniumTesting.page_object.pages.Doctor_Register import Doctor_Register


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


class TestPrescribePatient(unittest.TestCase):
    driver = setUp()

    def test_prescribe_patient(self):
        data = {'name':'rovit','relative_name':'tim','email':'rovits10@gmail.com','phone':3126543876,'ailments':'nothing','password':'rovit@123','re_password':'rovit@123','relative_phone':8465098324,'dob':'10/1/1993','address':'45-A Old Tower Dehradun 143820'}

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


        prescribe_patient = dhp.get_prescribe_patient()
        prescribe_patient.click()

        add_prescription_data = {'date':'23/6/2022','next_visit':'31/7/2022','reason':'nothing','doctor_notes':'dash'}

        ap = Add_Prescription(self.driver)

        date = ap.get_date()

        next_visit = ap.get_next_visit()

        reason = ap.get_reason()

        doctor_notes = ap.get_doctor_notes()

        submit = ap.get_submit()

        date.send_keys(add_prescription_data['date'])

        next_visit.send_keys(add_prescription_data['next_visit'])

        reason.send_keys(add_prescription_data['reason'])

        doctor_notes.send_keys(add_prescription_data['doctor_notes'])

        submit.send_keys(Keys.RETURN)
        
        self.assertEqual(Config.Doctor_Home_Page_URL,self.driver.current_url)
        

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="testing_output"))