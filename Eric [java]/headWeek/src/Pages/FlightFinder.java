/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

/**
 *
 * @author ericm
 */
public class FlightFinder {

    private static WebElement element = null;
    
    public static WebElement roundTrip(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='tripType']"));
        return element;
    }
    
    public static WebElement oneWay(WebDriver driver){
        element = driver.findElement(By.xpath("(//input[@name='tripType'])[2]"));
        return element;
    }
 
    public static WebElement passCount(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='passCount']"));
        return element;
    }

    public static WebElement fromPort(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='fromPort']"));
        return element;
    }

    public static WebElement fromMonth(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='fromMonth']"));
        return element;
    }

    public static WebElement fromDay(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='fromDay']"));
        return element;
    }

    public static WebElement toPort(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='toPort']"));
        return element;
    }
    
    public static WebElement toMonth(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='toMonth']"));
        return element;
    }
    
    public static WebElement toDay(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='toDay']"));
        return element;
    }
    
    public static WebElement servClassA(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='servClass']"));
        return element;
    }
    
    public static WebElement servClassB(WebDriver driver){
        element = driver.findElement(By.xpath("(//input[@name='servClass'])[2]"));
        return element;
    }
    
    public static WebElement servClassC(WebDriver driver){
        element = driver.findElement(By.xpath("(//input[@name='servClass'])[3]"));
        return element;
    }

    public static WebElement airline(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='airline']"));
        return element;
    }

    public static WebElement findFlights(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='findFlights']"));
        return element;
    }

    public static WebElement signOff(WebDriver driver){
        element = driver.findElement(By.linkText("SIGN-OFF"));
        return element;
    }

}
