from selenium import webdriver
from selenium.webdriver.common.by import By
from Pablo.Settings.DriverExtender import *
from selenium.webdriver.support.ui import Select
class FlightFinder:
    def __init__(self, driver):
        self.onewayXPath = '//input[@value="oneway"]'
        self.findFlightButtonName= 'findFlights'
        self.departingFromName = 'fromPort'
        self.myDriver = driver
        self.driverExtender = DriverExtender(self.myDriver)

    def selectOneWay(self):
        self.myDriver.find_element(By.XPATH,self.onewayXPath).click()

    def clickFindFlight(self):
        self.myDriver.find_element(By.NAME,self.findFlightButtonName).click()
        self.driverExtender.waitForDom()

    def selectdepartingFromOption(self,option):
        #Option is the value in this case
        #select = Select(self.myDriver.find_element(By.NAME,self.departingFromName))
        select = Select(self.myDriver.find_element_by_name(self.departingFromName))
        select.select_by_value(option)