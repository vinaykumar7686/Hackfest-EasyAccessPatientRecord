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

class TestLogin(unittest.TestCase):
    driver = setUp()
    
    # def test_valid_login(self):
    #     self.driver.get(Config.PROJECT_BASE_URL)
    #     Login.doLogin(self, self.driver)
    #     self.assertEqual(Config.INVENTRY_URL, self.driver.current_url, "Invalid Login")

    def test_homepage(self):
        self.driver.get(Config.PROJECT_BASE_URL)
        self.assertEqual(Config.PROJECT_BASE_URL,self.driver.current_url)
    
    def test_app_logo(self):
        self.driver.get(Config.PROJECT_BASE_URL)
        app_logo = self.driver.find_element_by_xpath(Homepage.XPATH_APP_LOGO)
        app_logo.click()
        self.assertEqual(Config.PROJECT_BASE_URL,self.driver.current_url)
        
    def test_home_link(self):
        self.driver.get(Config.PROJECT_BASE_URL)
        home_page = self.driver.find_element_by_xpath(Homepage.XPATH_HOME_LINK)
        home_page.click()
        self.assertEqual(Config.PROJECT_BASE_URL,self.driver.current_url)
    
    def test_login_page(self):
        self.driver.get(Config.PROJECT_BASE_URL)
        sign_in = self.driver.find_element_by_xpath(Homepage.XPATH_SIGN_IN)
        sign_in.click()
        self.assertEqual(Config.LOGIN_PAGE_URL,self.driver.current_url)
    

    def test_patient_register(self):
        data = {'name':'rovit','relative_name':'tim','email':'rovits@gmail.com','phone':3126543876,'ailments':'nothing','password':'rovit@123','re_password':'rovit@123','relative_phone':8465098324,'dob':'10/1/1993','address':'45-A Old Tower Dehradun 143820'}
        PATIENT_MEDICAL_FORM_URL = "http://127.0.0.1:8000/patient/medicalForm/"
        self.driver.get(Config.PROJECT_BASE_URL)
        patient= self.driver.find_element_by_id('dropdown02')
        patient.click()
        time.sleep(2)
        patient_sign_up = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[2]/ul/li[2]/a')
        patient_sign_up.click()

        time.sleep(2)

        print(self.driver.current_url)
        name = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[1]/div/input')
        relative_name = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[3]/div/input')
        email = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[7]/div/input')
        phone = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[2]/div/input')
        ailments = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[9]/div/input')
        password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[10]/div/input')
        re_password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[11]/div/input')
        relative_phone = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[4]/div/input')
        dob = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[6]/div/input')
        address = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[8]/div/input')
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

        submit = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[2]/input')
        submit.send_keys(Keys.RETURN)
        time.sleep(5)


        self.assertEqual(PATIENT_MEDICAL_FORM_URL,self.driver.current_url)

    def test_doctor_register(self):
        data = {'name':'cook','email':'cook206@gmail.com','phone':2132980870,'password':'Cook123','re_password':'Cook123'}
        Doctor_Home_Page_URL = 'http://127.0.0.1:8000/doctor/'
        self.driver.get(Config.PROJECT_BASE_URL)
        doctor = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[3]/a')
        doctor.click()
        time.sleep(2)
        doctor_sign_up = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[3]/ul/li[2]/a')
        doctor_sign_up.click()

        name = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[1]/div/input')
        email = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[2]/div/input')
        phone = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[3]/div/input')
        password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')
        re_password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[6]/div/input')
        submit = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')

        name.send_keys(data['name'])

        email.send_keys(data['email'])

        phone.send_keys(data['phone'])

        password.send_keys(data['password'])

        re_password.send_keys(data['re_password'])

        time.sleep(2)


        submit.send_keys(Keys.RETURN)

        time.sleep(2)

        self.assertEqual(Doctor_Home_Page_URL,self.driver.current_url)

    
    def test_view_registered_patients(self):
        VIEW_ALL_PATIENTS_URL = 'http://127.0.0.1:8000/allpatients/'
        data = {'name':'rovit','relative_name':'tim','email':'rovits1@gmail.com','phone':3126543876,'ailments':'nothing','password':'rovit@123','re_password':'rovit@123','relative_phone':8465098324,'dob':'10/1/1993','address':'45-A Old Tower Dehradun 143820'}
        Doctor_Home_Page_URL = 'http://127.0.0.1:8000/doctor/'
        self.driver.get(Config.PROJECT_BASE_URL)
        doctor = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[3]/a')
        doctor.click()
        time.sleep(2)
        doctor_sign_up = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[3]/ul/li[2]/a')
        doctor_sign_up.click()

        name = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[1]/div/input')
        email = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[2]/div/input')
        phone = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[3]/div/input')
        password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')
        re_password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[6]/div/input')
        submit = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')

        name.send_keys(data['name'])

        email.send_keys(data['email'])

        phone.send_keys(data['phone'])

        password.send_keys(data['password'])

        re_password.send_keys(data['re_password'])

        time.sleep(2)


        submit.send_keys(Keys.RETURN)

        time.sleep(2)


        self.assertEqual(Doctor_Home_Page_URL,self.driver.current_url)

        registered_patients = self.driver.find_element_by_xpath('/html/body/section[2]/div/div[2]/div/div[1]/input')
        registered_patients.click()
        self.assertEqual(VIEW_ALL_PATIENTS_URL,self.driver.current_url)

    def test_view_all_medicines(self):
        VIEW_ALL_MEDICINES_URL = 'http://127.0.0.1:8000/allmedicines/'
        data = {'name':'rovit','relative_name':'tim','email':'rovits2@gmail.com','phone':3126543876,'ailments':'nothing','password':'rovit@123','re_password':'rovit@123','relative_phone':8465098324,'dob':'10/1/1993','address':'45-A Old Tower Dehradun 143820'}

        Doctor_Home_Page_URL = 'http://127.0.0.1:8000/doctor/'
        self.driver.get(Config.PROJECT_BASE_URL)
        doctor = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[3]/a')
        doctor.click()
        time.sleep(2)
        doctor_sign_up = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[3]/ul/li[2]/a')
        doctor_sign_up.click()

        name = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[1]/div/input')
        email = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[2]/div/input')
        phone = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[3]/div/input')
        password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')
        re_password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[6]/div/input')
        submit = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')

        name.send_keys(data['name'])

        email.send_keys(data['email'])

        phone.send_keys(data['phone'])

        password.send_keys(data['password'])

        re_password.send_keys(data['re_password'])

        time.sleep(2)


        submit.send_keys(Keys.RETURN)

        time.sleep(2)


        self.assertEqual(Doctor_Home_Page_URL,self.driver.current_url)

        medicines = self.driver.find_element_by_xpath('/html/body/section[2]/div/div[2]/div/div[2]/input')
        medicines.click()
        self.assertEqual(VIEW_ALL_MEDICINES_URL,self.driver.current_url)

    def test_personal_profile(self):
        VIEW_DOCTOR_PERSONAL_PROFILE_URL = 'http://127.0.0.1:8000/doctor/info'
        data = {'name':'rovit','relative_name':'tim','email':'rovits3@gmail.com','phone':3126543876,'ailments':'nothing','password':'rovit@123','re_password':'rovit@123','relative_phone':8465098324,'dob':'10/1/1993','address':'45-A Old Tower Dehradun 143820'}
        Doctor_Home_Page_URL = 'http://127.0.0.1:8000/doctor/'
        self.driver.get(Config.PROJECT_BASE_URL)
        doctor = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[3]/a')
        doctor.click()
        time.sleep(2)
        doctor_sign_up = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[3]/ul/li[2]/a')
        doctor_sign_up.click()

        name = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[1]/div/input')
        email = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[2]/div/input')
        phone = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[3]/div/input')
        password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')
        re_password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[6]/div/input')
        submit = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')

        name.send_keys(data['name'])

        email.send_keys(data['email'])

        phone.send_keys(data['phone'])

        password.send_keys(data['password'])

        re_password.send_keys(data['re_password'])

        time.sleep(2)


        submit.send_keys(Keys.RETURN)

        time.sleep(2)


        self.assertEqual(Doctor_Home_Page_URL,self.driver.current_url)

        personal_profile = self.driver.find_element_by_xpath('/html/body/section[2]/div/div[2]/div/div[3]/form/input')
        personal_profile.click()
        self.assertEqual(VIEW_DOCTOR_PERSONAL_PROFILE_URL,self.driver.current_url)

    def test_add_prescription(self):
        ADD_PRESCRIPTION = 'http://127.0.0.1:8000/prescription/add/'
        data = {'name':'rovit','relative_name':'tim','email':'rovits4@gmail.com','phone':3126543876,'ailments':'nothing','password':'rovit@123','re_password':'rovit@123','relative_phone':8465098324,'dob':'10/1/1993','address':'45-A Old Tower Dehradun 143820'}
        Doctor_Home_Page_URL = 'http://127.0.0.1:8000/doctor/'
        self.driver.get(Config.PROJECT_BASE_URL)
        doctor = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[3]/a')
        doctor.click()
        time.sleep(2)
        doctor_sign_up = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[3]/ul/li[2]/a')
        doctor_sign_up.click()

        name = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[1]/div/input')
        email = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[2]/div/input')
        phone = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[3]/div/input')
        password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')
        re_password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[6]/div/input')
        submit = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')

        name.send_keys(data['name'])

        email.send_keys(data['email'])

        phone.send_keys(data['phone'])

        password.send_keys(data['password'])

        re_password.send_keys(data['re_password'])

        time.sleep(2)


        submit.send_keys(Keys.RETURN)

        time.sleep(2)


        self.assertEqual(Doctor_Home_Page_URL,self.driver.current_url)
        add_prescription = self.driver.find_element_by_xpath('/html/body/section[2]/div/div[2]/div/div[4]/form/input')
        add_prescription.click()
        self.assertEqual(ADD_PRESCRIPTION,self.driver.current_url)

    def test_doctor_logout(self):
        data = {'name':'cook','email':'cook1@gmail.com','phone':2132980870,'password':'Cook123','re_password':'Cook123'}
        Doctor_Home_Page_URL = 'http://127.0.0.1:8000/doctor/'
        self.driver.get(Config.PROJECT_BASE_URL)
        time.sleep(2)
        doctor = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[3]/a')
        doctor.click()
        time.sleep(2)
        doctor_sign_up = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[3]/ul/li[2]/a')
        doctor_sign_up.click()

        name = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[1]/div/input')
        email = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[2]/div/input')
        phone = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[3]/div/input')
        password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')
        re_password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[6]/div/input')
        submit = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')

        name.send_keys(data['name'])

        email.send_keys(data['email'])

        phone.send_keys(data['phone'])

        password.send_keys(data['password'])

        re_password.send_keys(data['re_password'])

        time.sleep(2)

        submit.send_keys(Keys.RETURN)

        time.sleep(2)


        self.assertEqual(Doctor_Home_Page_URL,self.driver.current_url)

        time.sleep(2)

        icon = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[2]/a')
        icon.click()
        time.sleep(3)
        logout = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[2]/ul/li[5]/a')
        logout.click()
        self.assertEqual(Config.PROJECT_BASE_URL,self.driver.current_url)

    def test_view_all_doctors(self):
        data = {'name':'rovit','relative_name':'tim','email':'rovits5@gmail.com','phone':3126543876,'ailments':'nothing','password':'rovit@123','re_password':'rovit@123','relative_phone':8465098324,'dob':'10/1/1993','address':'45-A Old Tower Dehradun 143820'}
        view_all_doctors = 'http://127.0.0.1:8000/alldoctors/'
        view_doctors = self.driver.find_element_by_xpath('/html/body/section[2]/div/div[2]/div/div[1]/input')
        view_doctors.click()
        self.assertEqual(view_all_doctors,self.driver.current_url)

    def test_personal_profile(self):
        data = {'name':'rovit','relative_name':'tim','email':'rovits6@gmail.com','phone':3126543876,'ailments':'nothing','password':'rovit@123','re_password':'rovit@123','relative_phone':8465098324,'dob':'10/1/1993','address':'45-A Old Tower Dehradun 143820'}
        self.test_patient_register(data)
        view_patient_personal_profile = 'http://127.0.0.1:8000/patient/info/'
        view_profile = self.driver.find_element_by_xpath('/html/body/section[2]/div/div[2]/div/div[2]/form/input')
        view_profile.click()
        self.assertEqual(view_patient_personal_profile,self.driver.current_url)
    
    def test_patient_logout(self):
        data = {'name':'rovit','relative_name':'tim','email':'rovits7@gmail.com','phone':3126543876,'ailments':'nothing','password':'rovit@123','re_password':'rovit@123','relative_phone':8465098324,'dob':'10/1/1993','address':'45-A Old Tower Dehradun 143820'}
        PATIENT_MEDICAL_FORM_URL = "http://127.0.0.1:8000/patient/medicalForm/"
        self.driver.get(Config.PROJECT_BASE_URL)
        patient= self.driver.find_element_by_id('dropdown02')
        patient.click()
        time.sleep(2)
        patient_sign_up = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[2]/ul/li[2]/a')
        patient_sign_up.click()

        print(self.driver.current_url)
        name = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[1]/div/input')
        relative_name = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[3]/div/input')
        email = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[7]/div/input')
        phone = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[2]/div/input')
        ailments = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[9]/div/input')
        password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[10]/div/input')
        re_password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[11]/div/input')
        relative_phone = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[4]/div/input')
        dob = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[6]/div/input')
        address = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[8]/div/input')
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

        submit = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[2]/input')
        submit.send_keys(Keys.RETURN)
        time.sleep(5)


        self.assertEqual(PATIENT_MEDICAL_FORM_URL,self.driver.current_url)


        patient_register = 'http://127.0.0.1:8000/patient/register/'
        icon = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[2]/a')
        icon.click()
        time.sleep(3)
        logout = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[2]/ul/li[5]/a')
        logout.click()
        self.assertEqual(patient_register,self.driver.current_url)

    def test_sign_in_valid_data(self):
        self.driver.get(Config.PROJECT_BASE_URL)
        patient_home_page = 'http://127.0.0.1:8000/patient/'
        sign_in = self.driver.find_element_by_xpath('/html/body/footer/div/div/div[3]/div/ul/li[1]/a')
        sign_in.click()
        email = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[2]/div/input')
        email.send_keys('y@gmail.com')
        password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')
        password.send_keys('1')
        self.assertEqual(patient_home_page,self.driver.current_url)
    
    def test_sign_in_invalid_data(self):
        self.driver.get(Config.PROJECT_BASE_URL)
        sign_in_url = 'http://127.0.0.1:8000/login/'
        sign_in = self.driver.find_element_by_xpath('/html/body/footer/div/div/div[3]/div/ul/li[1]/a')
        sign_in.click()
        email = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[2]/div/input')
        email.send_keys('random')
        password = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input')
        password.send_keys('1')
        self.assertEqual(sign_in_url,self.driver.current_url)


    

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="testing_output"))



