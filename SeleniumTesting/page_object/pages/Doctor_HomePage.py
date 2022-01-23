import doctest
import sys
from audioop import add
from lib2to3.pgen2 import driver
from re import sub
import sys
sys.path.append('/home/manish/Desktop/seleniumPython/Manish') 
from SeleniumTesting.page_object.locator import Doctor_homepage

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


class Doctor_HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.add_prescription = self.driver.find_element_by_xpath(Doctor_homepage.add_prescription)
        self.icon = self.driver.find_element_by_xpath(Doctor_homepage.icon)
        self.logout = self.driver.find_element_by_xpath(Doctor_homepage.logout)
        self.personal_profile = self.driver.find_element_by_xpath(Doctor_homepage.personal_profile)
        self.prescribe_patient = self.driver.find_element_by_xpath(Doctor_homepage.prescribe_patient)
        self.medicines = self.driver.find_element_by_xpath(Doctor_homepage.medicines)
        self.registered_patients = self.driver.find_element_by_xpath(Doctor_homepage.registered_patients)

    
    def get_add_prescription(self):
        return self.add_prescription

    def get_icon(self):
        return self.icon

    def get_logout(self):
        return self.logout

    def get_personal_profile(self):
        return self.personal_profile

    def get_prescribe_patient(self):
        return self.prescribe_patient

    def get_medicines(self):
        return self.medicines

    def get_registered_patients(self):
        return self.registered_patients
    