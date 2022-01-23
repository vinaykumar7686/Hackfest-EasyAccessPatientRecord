import doctest
import sys
from audioop import add
from lib2to3.pgen2 import driver
from re import sub
import sys
sys.path.append('/home/manish/Desktop/seleniumPython/Manish') 
from SeleniumTesting.page_object.locator import *

from selenium import webdriver
import unittest
# from SeleniumTesting.Testing.test_config import setUp
from SeleniumTesting.Config.config import *
# from SeleniumTesting.page_object.pages.login import Login
import HtmlTestRunner
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


class HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.app_logo = self.driver.find_element_by_xpath(Homepage.XPATH_APP_LOGO)
        self.home_link = self.driver.find_element_by_xpath(Homepage.XPATH_HOME_LINK)
        self.view_doctors = self.driver.find_element_by_xpath(Homepage.XPATH_VIEW_DOCTORS_BUTTON)
        self.sign_in = self.driver.find_element_by_xpath(Homepage.XPATH_SIGN_IN)
        self.doctor = self.driver.find_element_by_xpath(Homepage.XPATH_DOCTOR)
        self.doctor_sign_up_dropdown = self.driver.find_element_by_xpath(Homepage.XPATH_DOCTOR_SIGN_UP_DROPDOWN)
        self.patient = self.driver.find_element_by_id(Homepage.patient_id)
        self.patient_sign_up_dropdown = self.driver.find_element_by_xpath(Homepage.patient_sign_up_dropdown)

    
    def get_app_logo(self):
        return self.app_logo

    def get_home_link(self):
        return self.home_link
    
    def get_view_doctors(self):
        return self.view_doctors
    
    def get_sign_in(self):
        return self.sign_in

    def get_doctor(self):
        return self.doctor

    def get_doctor_sign_up_dropdown(self):
        return self.doctor_sign_up_dropdown

    def get_patient(self):
        return self.patient

    def get_patient_sign_up_dropdown(self):
        return self.patient_sign_up_dropdown

        