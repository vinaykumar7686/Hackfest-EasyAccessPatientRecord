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


class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.email = self.driver.find_element_by_xpath(Login.email)
        self.password = self.driver.find_element_by_xpath(Login.password)
        self.submit_button = self.driver.find_element_by_xpath(Login.submit_button)

    
    def get_email(self):
        return self.email

    def get_password(self):
        return self.password
   
    def get_submit(self):
        return self.submit_button

        