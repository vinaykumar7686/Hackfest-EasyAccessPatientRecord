import doctest
import sys
from audioop import add
from lib2to3.pgen2 import driver
from re import sub
import sys

from urllib3 import Retry
sys.path.append('/home/manish/Desktop/seleniumPython/Manish') 
from SeleniumTesting.page_object.locator import *
from SeleniumTesting.page_object.locator import Homepage
from SeleniumTesting.page_object.locator import Patient_homepage


from SeleniumTesting.page_object.locator import Login



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


class Patient_HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.icon = self.driver.find_element_by_xpath(Patient_homepage.icon)
        self.logout = self.driver.find_element_by_xpath(Patient_homepage.logout)
        self.update_medical_details = self.driver.find_element_by_xpath(Patient_homepage.update_medical_details)
        self.view_doctors = self.driver.find_element_by_xpath(Patient_homepage.view_doctors)
        self.view_profile = self.driver.find_element_by_xpath(Patient_homepage.view_profile)

    def get_icon(self):
        return self.icon

    def get_logout(self):
        return self.logout

    def get_update_medical_details(self):
        return self.update_medical_details

    def get_view_doctors(self):
        return self.view_doctors

    def get_view_profile(self):
        return self.view_profile


    
    

        