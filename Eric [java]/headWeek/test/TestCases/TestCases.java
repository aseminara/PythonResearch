package TestCases;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import Pages.BookFlight;
import Pages.BookFlight2;
import Pages.FlightFinder;
import Pages.HomePage;
import Pages.LastPage;
import Pages.SignOn;
import Resources.InitialValues;
import java.util.concurrent.TimeUnit;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Assert;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

/**
 *
 * @author ericm
 */
public class TestCases {
    
    private static WebDriver driver = new FirefoxDriver();
    
    public TestCases() {
    }
    
    @BeforeClass
    public static void setUpClass() {
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS); //waits up to 10 seconds to find any element
    }
    
    @AfterClass
    public static void tearDownClass() {
        driver.quit();
    }
    
    @Before
    public void setUp() {
    }
    
    @After
    public void tearDown() {
    }

    @Test
    public void logInFailure_WrongPassword() throws Exception {
        try{
            HomePage.page(driver);
            HomePage.user(driver).sendKeys(InitialValues.getUser());
            HomePage.password(driver).sendKeys(InitialValues.getWrongPassword());
            HomePage.login(driver).click();
            Assert.assertEquals(true, SignOn.password(driver).isDisplayed());
        } catch (Exception e) {
            Assert.fail(e.toString());
        }
    }

    @Test
    public void selectFlightRoundTrip() throws Exception {
        try{
            HomePage.page(driver);
            HomePage.user(driver).sendKeys(InitialValues.getUser());
            HomePage.password(driver).sendKeys(InitialValues.getPassword());
            HomePage.login(driver).click();
            FlightFinder.roundTrip(driver).click();
            FlightFinder.findFlights(driver).click();
            Assert.assertEquals(true, BookFlight.reserveFlights(driver).isDisplayed());
        } catch (Exception e) {
            Assert.fail(e.toString());
        }
    }
    
    @Test
    public void BookAFlight_NumberFieldEmpty() throws Exception {
        try{
            HomePage.page(driver);
            HomePage.user(driver).sendKeys(InitialValues.getUser());
            HomePage.password(driver).sendKeys(InitialValues.getPassword());
            HomePage.login(driver).click();
            FlightFinder.findFlights(driver).click();
            BookFlight.reserveFlights(driver).click();
            BookFlight2.creditnumber(driver).sendKeys("");
            BookFlight2.buyFlights(driver).click();
            Assert.assertEquals("Your itinerary has been booked!",LastPage.results(driver).getText());
        } catch (Exception e) {
            Assert.fail(e.toString());
        }
    }

        @Test
    public void signOff() throws Exception {
        try{
            HomePage.page(driver);
            HomePage.user(driver).sendKeys(InitialValues.getUser());
            HomePage.password(driver).sendKeys(InitialValues.getPassword());
            HomePage.login(driver).click();
            FlightFinder.signOff(driver).click();
            Assert.assertEquals(true, SignOn.password(driver).isDisplayed());
        } catch (Exception e) {
            Assert.fail(e.toString());
        }
    }

}
