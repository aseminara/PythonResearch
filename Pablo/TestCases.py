import unittest
from Pablo.Settings.Driver import *
from Pablo.Settings.Environment import *
from Pablo.Settings.DriverExtender import *
from Pablo.Pages.HomePage import *
from Pablo.Pages.SignOnPage import *
from Pablo.Pages.FlightFinderPage import *
from Pablo.Pages.SelectFlightPage import *
from Pablo.Pages.ReservationPage import *
from Pablo.Pages.RegistrationPage import *
from Pablo.Pages.CommonPage import *

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

    def test_validateRoundTrip(self):
        home = Home(self.myDriver)
        reservation = Reservation(self.myDriver)
        flightFinder = FlightFinder(self.myDriver)
        home.setusername("demo")
        home.setpassword("demo")
        home.clicklogin()
        flightFinder.selectdepartingFromOption('New York')
        flightFinder.clickFindFlight()
        reservation.continueButtonName()

    def test_register(self):
        common = Common(self.myDriver)
        register = Register(self.myDriver)
        common.clickRegister()
        register.addUserName("Pepe") #TODO: QUit hardcode here

    def tearDown(self):
        driverExtender = DriverExtender(self.myDriver)
        driverExtender.closeDriver()

if __name__ == "__main__":
    unittest.main()