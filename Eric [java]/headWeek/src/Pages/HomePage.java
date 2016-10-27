/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Pages;

import Resources.InitialValues;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

/**
 *
 * @author ericm
 */
public class HomePage {

    private static WebElement element = null;
 
    public static void page(WebDriver driver){
        driver.get(InitialValues.getUrl());
    }
    
    public static WebElement user(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='userName']"));
        return element;
    }
    
    public static WebElement password(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='password']"));
        return element;
    }
 
    public static WebElement login(WebDriver driver){
        element = driver.findElement(By.xpath("//input[@name='login']"));
        return element;
    }

}
