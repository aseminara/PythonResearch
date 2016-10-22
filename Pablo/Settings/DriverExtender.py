from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
class DriverExtender:
    def __init__(self,driver):
        self.myDriver = driver
    def closeDriver(self):
        self.myDriver.quit()
    def verifyElementExistence(self,typeofelement,element):
        switcher = {
            #TODO: Agregar los demás selectores
            "xpath": By.XPATH,
            "link": By.LINK_TEXT,
            "id": By.ID,
            "name":By.NAME,
            "css":By.CSS_SELECTOR,
        }
        #self.myDriver.implicitly_wait(10)
        try:
            WebDriverWait(self.myDriver, 10).until(expected_conditions.presence_of_element_located((switcher.get(typeofelement.lower()), element)))
            return True
        except:
            return False