from selenium.webdriver.common.by import By
from Pablo.Settings.DriverExtender import *
class FlightFinder:
    def __init__(self, driver):
        self.onewayXPath = '//input[@value="oneway"]'
        self.findFlightButtonName= 'findFlights'
        self.myDriver = driver
        self.driverExtender = DriverExtender(self.myDriver)
    def selectOneWay(self):
        self.myDriver.find_element(By.XPATH,self.onewayXPath).click()
    def clickFindFlight(self):
        self.myDriver.find_element(By.NAME,self.findFlightButtonName).click()
        self.driverExtender.waitForDom()
