import unittest
from Pablo.Settings.Driver import *
from Pablo.Settings.Environment import *
from Pablo.Pages.HomePage import *
from Pablo.Pages.SignOnPage import *

class TestCases(unittest.TestCase):

    def setUp(self):
        self.myDriver = Driver()
        environment = Environment()
        self.myDriver.driver.get(environment.url)

    def test_incorrectlogin(self):
        home = Home(self.myDriver)
        signOn = SignOn(self.myDriver)
        home.setpassword("xxxxxx")
        home.clicklogin()
        self.assertTrue(signOn.verifyLogOnImage())

    def tearDown(self):
        self.myDriver.closedriver()

if __name__ == "__main__":
    unittest.main()