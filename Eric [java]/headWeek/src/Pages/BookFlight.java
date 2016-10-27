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
public class BookFlight {

    private static WebElement element = null;
 
    public static WebElement outFlightA(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='outFlight']"));
        return element;
    }

    public static WebElement outFlightB(WebDriver driver){
        element = driver.findElement(By.xpath("(//input[@name='outFlight'])[2]"));
        return element;
    }

    public static WebElement outFlightC(WebDriver driver){
        element = driver.findElement(By.xpath("(//input[@name='outFlight'])[3]"));
        return element;
    }

    public static WebElement outFlightD(WebDriver driver){
        element = driver.findElement(By.xpath("(//input[@name='outFlight'])[4]"));
        return element;
    }

    public static WebElement inFlightA(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='inFlight']"));
        return element;
    }

    public static WebElement inFlightB(WebDriver driver){
        element = driver.findElement(By.xpath("(//input[@name='inFlight'])[2]"));
        return element;
    }

    public static WebElement inFlightC(WebDriver driver){
        element = driver.findElement(By.xpath("(//input[@name='inFlight'])[3]"));
        return element;
    }

    public static WebElement inFlightD(WebDriver driver){
        element = driver.findElement(By.xpath("(//input[@name='inFlight'])[4]"));
        return element;
    }

    public static WebElement reserveFlights(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='reserveFlights']"));
        return element;
    }

}
