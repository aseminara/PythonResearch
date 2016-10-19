from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from Settings.Driver import *
from Settings.Environment import *
from selenium.webdriver.common.by import By

myDriver = Driver()
environment = Environment()

myDriver.driver.get(environment.url)
assert "Use Java Version" in myDriver.driver.page_source
contactElem = myDriver.driver.find_element_by_link_text("CONTACT")
contactElem.click()

try:
    element = WebDriverWait(myDriver.driver,10)
    element.until(expected_conditions.presence_of_element_located((By.XPATH,"//a[@href='mercurywelcome.php']")))
except:
    print("There was a problem loading page")

backButton = myDriver.driver.find_element_by_xpath("//a[@href='mercurywelcome.php']")
backButton.click()

try:
    javaU = myDriver.driver.find_element_by_xpath("//u[contains(text(),'Use Java Version')]")
    assert True
except:
    assert False

myDriver.driver.quit()