from ast import Add
import doctest
from site import addpackage
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


class Add_Prescription():
    def __init__(self,driver):
        self.driver = driver

        self.date = self.driver.find_element_by_xpath(Add_prescription.date)

        self.next_visit = self.driver.find_element_by_xpath(Add_prescription.next_visit)

        self.reason = self.driver.find_element_by_xpath(Add_prescription.reason)

        self.doctor_notes = self.driver.find_element_by_xpath(Add_prescription.doctor_notes)

        self.submit = self.driver.find_element_by_xpath(Add_prescription.submit)

    def get_date(self):
        return self.date
    
    def get_next_visit(self):
        return self.next_visit
    
    def get_reason(self):
        return self.reason
    
    def get_doctor_notes(self):
        return self.doctor_notes
    
    def get_submit(self):
        return self.submit


    

    
    

        