import sys
from audioop import add
from lib2to3.pgen2 import driver
from re import sub
import sys
sys.path.append('/home/manish/Desktop/seleniumPython/Manish') 

from SeleniumTesting.page_object.locator import Patient_register

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


class Patient_Register():
    def __init__(self,driver):
        self.driver = driver
        self.name = self.driver.find_element_by_xpath(Patient_register.name)
        self.relative_name = self.driver.find_element_by_xpath(Patient_register.relative_name)
        self.email = self.driver.find_element_by_xpath(Patient_register.email)
        self.phone = self.driver.find_element_by_xpath(Patient_register.phone)
        self.ailments = self.driver.find_element_by_xpath(Patient_register.ailments)
        self.password = self.driver.find_element_by_xpath(Patient_register.password)
        self.re_password = self.driver.find_element_by_xpath(Patient_register.re_password)
        self.relative_phone = self.driver.find_element_by_xpath(Patient_register.relative_phone)
        self.dob = self.driver.find_element_by_xpath(Patient_register.dob)
        self.address = self.driver.find_element_by_xpath(Patient_register.address)
        self.submit = self.driver.find_element_by_xpath(Patient_register.submit)

    
    def get_name(self):
        return self.name
    
    def get_relative_name(self):
        return self.relative_name
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_ailments(self):
        return self.ailments
    
    def get_password(self):
        return self.password
    
    def get_re_password(self):
        return self.re_password
    
    def get_relative_phone(self):
        return self.relative_phone
    
    def get_dob(self):
        return self.dob
    
    def get_address(self):
        return self.address

    def get_submit(self):
        return self.submit



        