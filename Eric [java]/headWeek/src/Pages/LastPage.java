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
public class LastPage {

    private static WebElement element = null;
 
    public static WebElement results(WebDriver driver){
        element = driver.findElement(By.xpath("//font[2]"));
        return (element);
    }

}
