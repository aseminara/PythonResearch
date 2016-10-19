from selenium import webdriver
from selenium.webdriver.common.by import By
class Contact:
    def __init__(self,driver):
        self.myDriver = driver
        self.backButtonXpath = "//a[@href='mercurywelcome.php']"
    def clickbackbutton(self):
        self.myDriver.find_element(By.XPATH,self.backButtonXpath).click()
        #self.backButton.click()