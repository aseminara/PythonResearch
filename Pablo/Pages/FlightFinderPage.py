from selenium.webdriver.common.by import By
class FlightFinder:
    def __init__(self, driver):
        self.onewayXPath = '//input[@value="oneway"]'
        self.myDriver = driver
    def selectOneWay(self):
        self.myDriver.find_element(By.XPATH,self.onewayXPath).click()