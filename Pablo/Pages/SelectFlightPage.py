from selenium.webdriver.common.by import By
from Pablo.Settings.DriverExtender import *

class SelectFlight:
    def __init__(self,driver):
        self.myDriver = driver
        self.selectFlightBannerXpath = '//img[@src="/images/masts/mast_selectflight.gif"]'

    def verifySelectFlightBanner(self):
        driverExtender = DriverExtender(self.myDriver)
        return driverExtender.verifyElementExistence("xpath", self.selectFlightBannerXpath)