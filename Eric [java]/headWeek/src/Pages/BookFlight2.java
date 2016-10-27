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
public class BookFlight2 {

    private static WebElement element = null;
 
    public static WebElement passFirst0(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='passFirst0']"));
        return element;
    }

    public static WebElement passLast0(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='passLast0']"));
        return element;
    }

    public static WebElement pass0meal(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='pass.0.meal']"));
        return element;
    }
     
     public static WebElement creditCard(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='creditCard']"));
        return element;
    }

    public static WebElement creditnumber(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='creditnumber']"));
        return element;
    }
     
    public static WebElement cc_exp_dt_mn(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='cc_exp_dt_mn']"));
        return element;
    }
     
    public static WebElement cc_exp_dt_yr(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='cc_exp_dt_yr']"));
        return element;
    }
     
    public static WebElement cc_frst_name(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='cc_frst_name']"));
        return element;
    }

    public static WebElement cc_mid_name(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='cc_mid_name']"));
        return element;
    }

    public static WebElement cc_last_name(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='cc_last_name']"));
        return element;
    }

    public static WebElement ticketLess(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='ticketLess']"));
        return element;
    }

    public static WebElement billAddress1(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='billAddress1']"));
        return element;
    }

    public static WebElement billAddress2(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='billAddress2']"));
        return element;
    }

    public static WebElement billCity(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='billCity']"));
        return element;
    }

    public static WebElement billState(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='billState']"));
        return element;
    }

    public static WebElement billZip(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='billZip']"));
        return element;
    }

    public static WebElement billCountry(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='billCountry']"));
        return element;
    }
     
    public static WebElement ticketLessB(WebDriver driver){
        element = driver.findElement(By.xpath("(//input[@name='ticketLess'])[2]"));
        return element;
    }

    public static WebElement delAddress1(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='delAddress1']"));
        return element;
    }

    public static WebElement delAddress2(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='delAddress2']"));
        return element;
    }

    public static WebElement delCity(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='delCity']"));
        return element;
    }

    public static WebElement delState(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='delState']"));
        return element;
    }

    public static WebElement delZip(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='delZip']"));
        return element;
    }
    
    public static WebElement delCountry(WebDriver driver){
        element = driver.findElement(By.xpath("//select[@name='delCountry']"));
        return element;
    }
     
    public static WebElement buyFlights(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='buyFlights']"));
        return element;
    }


    
}
