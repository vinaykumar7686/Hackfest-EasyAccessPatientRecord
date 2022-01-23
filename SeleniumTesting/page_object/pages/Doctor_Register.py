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


class Doctor_Register():
    def __init__(self,driver):
        self.driver = driver
        self.name_query_box = self.driver.find_element_by_xpath(Doctor_register.name_box)
        self.email_query_box = self.driver.find_element_by_xpath(Doctor_register.email_box)
        self.phone_query_box = self.driver.find_element_by_xpath(Doctor_register.phone_box)
        self.password_query_box = self.driver.find_element_by_xpath(Doctor_register.password_box)
        self.re_password_query_box = self.driver.find_element_by_xpath(Doctor_register.re_password_box)
        self.submit_button = self.driver.find_element_by_xpath(Doctor_register.submit_button)

    
    def get_name_query_box(self):
        return self.name_query_box

    def get_email_query_box(self):
        return self.email_query_box
    
    def get_phone_query_box(self):
        return self.phone_query_box
    
    def get_password_query_box(self):
        return self.password_query_box

    def get_re_password_query_box(self):
        return self.re_password_query_box

    def get_submit_button(self):
        return self.submit_button

        