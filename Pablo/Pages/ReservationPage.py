from selenium.webdriver.common.by import By
from Pablo.Settings.DriverExtender import *

class Reservation:
    def __init__(self,driver):
        self.myDriver = driver
        self.continueButtonName = "reserveFlights"
    def clickContinue(self):
        self.myDriver.find_element(By.NAME,self.continueButtonName)