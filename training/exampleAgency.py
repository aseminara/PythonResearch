from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
driver = webdriver.Firefox(capabilities=caps)

driver.get("http://newtours.demoaut.com")
assert "Use Java Version" in driver.page_source
contactElem = driver.find_element_by_link_text("CONTACT")
contactElem.click()

#Hasta aca vamos bien
try:
    element = WebDriverWait(driver,10)
    element.until(expected_conditions.alert_is_present())





#assert "Sorry         for any inconvienece." in driver.page_source
backButton = driver.find_element_by_xpath("html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/t[2]/table/tbody/tr[4]/td/a/img")
backButton.click()
assert "use Java Version" in driver.page_source
driver.close()