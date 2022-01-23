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


class Update_Medical_Details():
    def __init__(self,driver):
        self.driver = driver
        self.medical_history = self.driver.find_element_by_xpath(Update_medical_details.medical_history)
        self.submit = self.driver.find_element_by_xpath(Update_medical_details.submit)

    
    def get_medical_history(self):
        return self.medical_history

    def get_submit(self):
        return self.submit

    

        