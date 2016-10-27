/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Resources;

/**
 *
 * @author ericm
 */
public class InitialValues {
    private static String url = "http://newtours.demoaut.com/";
    private static String user = "tutorial";
    private static String password = "tutorial";
    private static String wrongPassword = "manzana";

    /**
     * @return the url
     */
    public static String getUrl() {
        return url;
    }

    /**
     * @param aUrl the url to set
     */
    public static void setUrl(String aUrl) {
        url = aUrl;
    }

    /**
     * @return the user
     */
    public static String getUser() {
        return user;
    }

    /**
     * @return the password
     */
    public static String getPassword() {
        return password;
    }

    /**
     * @return the wrongPassword
     */
    public static String getWrongPassword() {
        return wrongPassword;
    }
}
