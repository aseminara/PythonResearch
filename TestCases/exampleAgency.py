from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from Settings.Environment import *

environment = Environment()
caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
driver = webdriver.Firefox(capabilities=caps)

driver.get(environment.url)
assert "Use Java Version" in driver.page_source
contactElem = driver.find_element_by_link_text("CONTACT")
contactElem.click()

try:
    element = WebDriverWait(driver,10)
    element.until(expected_conditions.alert_is_present())
    #element.until(expected_conditions.presence_of_element_located("//a[@href='mercurywelcome.php']"))
except:
    print("There was a problem loading page")
#driver.implicitly_wait(10)
#assert 'Sorry' in driver.page_source
backButton = driver.find_element_by_xpath("//a[@href='mercurywelcome.php']")
backButton.click()

try:
    javaU = driver.find_element_by_xpath("//u[contains(text(),'Use Java Version')]")
    assert True
except:
    assert False


driver.close()