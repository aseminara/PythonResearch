from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from Settings.Driver import *
from Settings.Environment import *
from selenium.webdriver.common.by import By
from Pages.HomePage import *
from Pages.ContactPage import *

myDriver = Driver()
environment = Environment()
myDriver.driver.get(environment.url)

homePage = Home(myDriver.driver)
contactPage = Contact(myDriver.driver)


assert "Use Java Version" in myDriver.driver.page_source

homePage.clickcontact()

try:
    element = WebDriverWait(myDriver.driver,10)
    element.until(expected_conditions.presence_of_element_located((By.XPATH,"//a[@href='mercurywelcome.php']")))
except:
    print("There was a problem loading page")

contactPage.clickbackbutton()

homePage.verifyjavaversiontext()

myDriver.driver.quit()