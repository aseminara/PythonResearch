from selenium import webdriver
from selenium.webdriver.common.by import By
from Pablo.Settings.DriverExtender import *

class Register:
    def __init__(self,driver):
        self.myDriver = driver
        self.firstNameName='firstName'
        self.lastNameName='lastName'
        self.phoneName = 'phone'
        self.mailName = 'userName'
        self.userName = 'mail'
        self.passwordName = 'password'
        self.confirmPasswordName = 'confirmPassword'
        self.submitButtonName = 'register'
        self.extender = DriverExtender(self.myDriver)
    def addUserName(self,text):
        self.myDriver.find_element(By.NAME,self.userName).send_keys(text)

    def addPassword(self,password):
        self.myDriver.find_element(By.NAME, self.passwordName).send_keys(password)

    def addConfirmPassword(self,password):
        self.myDriver.find_element(By.NAME, self.confirmPasswordNameName).send_keys(password)

    def pressSubmit(self):
        self.myDriver.find_element(By.NAME,self.submitButtonName).click()
        self.extender.waitForDom()
