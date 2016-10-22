import unittest
from Pablo.Settings.Driver import *
from Pablo.Settings.Environment import *
from Pablo.Settings.DriverExtender import *
from Pablo.Pages.HomePage import *
from Pablo.Pages.SignOnPage import *

class TestCases(unittest.TestCase):

    def setUp(self):
        self.myDriver = Driver().getdriver()
        environment = Environment()
        self.myDriver.get(environment.url)

    def test_incorrectlogin(self):
        home = Home(self.myDriver)
        signOn = SignOn(self.myDriver)
        home.setpassword("xxxxxx")
        home.clicklogin()
        self.assertTrue(signOn.verifyLogOnImage())

    def tearDown(self):
        driverExtender = DriverExtender(self.myDriver)
        driverExtender.closeDriver()

if __name__ == "__main__":
    unittest.main()