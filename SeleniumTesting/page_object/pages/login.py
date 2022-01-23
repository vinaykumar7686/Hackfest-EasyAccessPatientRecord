import sys
sys.path.append("/home/manish/Desktop/seleniumPython/Manish") 
from SeleniumTesting.page_object.locator import Homepage

from selenium import webdriver
import unittest
from SeleniumTesting.Testing.test_config import *
from SeleniumTesting.Config.config import *
from SeleniumTesting.page_object.pages.login import Login
import HtmlTestRunner
from SeleniumTesting.page_object.locator import Locator

class Login:
    def doLogin(self,driver):
        
        username = driver.find_element_by_xpath(Locator.XPATH_USERNAME)
        username.send_keys(Config.USER_NAME)
        password = driver.find_element_by_xpath(Locator.XPATH_PASSWORD)
        password.send_keys(Config.USER_PASSWORD)
        
        login = driver.find_element_by_xpath(Locator.XPATH_LOGIN)
        login.click()
        
        # return driver.current_url