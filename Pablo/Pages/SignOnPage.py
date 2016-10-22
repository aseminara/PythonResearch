from selenium import webdriver
from selenium.webdriver.common.by import By
from Pablo.Settings.DriverExtender import *
class SignOn:
    def __init__(self,driver):
        self.signOnXpath = '//img[@src="/images/masts/mast_signon.gif"]'
        self.myDriver = driver
    def verifyLogOnImage(self):
        driverExtender = DriverExtender(self.myDriver)
        return driverExtender.verifyElementExistence("xpath",self.signOnXpath)
