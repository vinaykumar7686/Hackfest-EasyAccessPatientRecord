import sys
sys.path.append("/home/manish/Desktop/seleniumPython/Manish") 
from SeleniumTesting.page_object.locator import Homepage

from selenium import webdriver
import unittest
from SeleniumTesting.Testing.test_config import *
from SeleniumTesting.Config.config import *
# from SeleniumTesting.page_object.pages.login import Login
import HtmlTestRunner
from selenium import webdriver


def setUp():
    return webdriver.Chrome(executable_path=Config.CHROME_EXECUTABLE_PATH)

# def getDriver():
#     driver = setUp()
#     driver.get(Config.PROJECT_BASE_URL)
