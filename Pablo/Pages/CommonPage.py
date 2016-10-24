from selenium import webdriver
from selenium.webdriver.common.by import By
from Pablo.Settings.DriverExtender import *

class Common:
    def __init__(self,driver):

        self.registerLink = 'REGISTER'
        self.myDriver = driver
        self.extender = DriverExtender(self.myDriver)

    def clickRegister(self):
        self.myDriver.find_element(By.LINK_TEXT,self.registerLink).click()
        self.extender.waitForDom()