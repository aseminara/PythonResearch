import unittest
from Pablo.Settings.Driver import *
from Pablo.Settings.Environment import *
from Pablo.Settings.DriverExtender import *
from Pablo.Pages.HomePage import *
from Pablo.Pages.SignOnPage import *
from Pablo.Pages.FlightFinderPage import *
from Pablo.Pages.SelectFlightPage import *

class TestCases(unittest.TestCase):

    def setUp(self):
        self.myDriver = Driver().getdriver()
        environment = Environment()
        self.myDriver.get(environment.url)

    def test_incorrectLogin(self):
        home = Home(self.myDriver)
        signOn = SignOn(self.myDriver)
        home.setpassword("xxxxxx")
        home.clicklogin()
        self.assertTrue(signOn.verifyLogOnImage())

    def test_oneWayFlight(self):
        home = Home(self.myDriver)
        flightFinder = FlightFinder(self.myDriver)
        selectFlight = SelectFlight(self.myDriver)
        home.setusername("demo")
        home.setpassword("demo")
        home.clicklogin()
        flightFinder.selectOneWay()
        flightFinder.clickFindFlight()
        selectFlight.verifySelectFlightBanner()

    def tearDown(self):
        driverExtender = DriverExtender(self.myDriver)
        driverExtender.closeDriver()

if __name__ == "__main__":
    unittest.main()