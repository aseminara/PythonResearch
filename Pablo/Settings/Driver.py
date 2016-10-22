from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Driver:
    def __init__(self):
        caps = DesiredCapabilities.FIREFOX
        caps["marionette"] = True
        caps["binary"] = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
        self.driver = webdriver.Firefox(capabilities=caps)

    def getdriver(self):
        return self.driver

    def closedriver(self):
        self.driver.quit()
