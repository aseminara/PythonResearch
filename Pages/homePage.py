from selenium import webdriver
from selenium.webdriver.common.by import By
class Home:
    def __init__(self,driver):
        self.myDriver = driver
        self.contactElemLink="CONTACT"
        self.javatextXpath="//u[contains(text(),'Use Java Version')]"

    def clickcontact(self):
        self.myDriver.find_element(By.LINK_TEXT,self.contactElemLink).click()


    def verifyjavaversiontext(self):
        try:
            self.myDriver.find_element(By.XPATH,self.javatextXpath)
            assert True
        except:
            assert False
