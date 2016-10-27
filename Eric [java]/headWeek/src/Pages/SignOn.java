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
public class SignOn {

    private static WebElement element = null;
 
    public static WebElement user(WebDriver driver){
        element = driver.findElement(By.name("userName"));
        return element;
    }
    
        public static WebElement password(WebDriver driver){
        element = driver.findElement(By.name("password"));
        return element;
    }

}
