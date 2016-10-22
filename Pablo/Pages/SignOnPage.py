from selenium import webdriver
from selenium.webdriver.common.by import By

class SignOn:
    def __init__(self,driver):
        self.signOnXpath = "//img[@src='/img/logo/new_logo.jpg']"
        self.myDriver = driver
    def verifyLogOnImage(self):
        try:
            self.myDriver.find_element(By.XPATH, self.signOnXpath).click()
            return True
        except:
            return False
