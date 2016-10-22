from selenium import webdriver
from selenium.webdriver.common.by import By

class Home:
    def __init__(self,driver):
        self.myDriver = driver
        self.contactElemLink="CONTACT"
        self.javatextXpath="//u[contains(text(),'Use Java Version')]"
        self.userNameName = "userName"
        self.passwordName = "password"
        self.loginButtonName = "login"

    def clickcontact(self):
        self.myDriver.find_element(By.LINK_TEXT,self.contactElemLink).click()


    def verifyjavaversiontext(self):
        try:
            self.myDriver.find_element(By.XPATH,self.javatextXpath)
            assert True
        except:
            assert False

    def setusername(self,text):
        self.myDriver.find_element(By.NAME,self.userNameName).send_keys(text)

    def setpassword(self,text):
        self.myDriver.find_element(By.NAME, self.passwordName).send_keys(text)

    def clicklogin(self):
        self.myDriver.find_element(By.NAME,self.loginButtonName).click()