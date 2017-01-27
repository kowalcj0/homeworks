package kowalcj0.page_objects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.List;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertThat;

/**
 * Created by JK on 25/01/17.
 */
public class BlokEkipaHome {

    private By search_box = By.id("query");
    private By title = By.cssSelector("title");
    private By facebook_like = By.id("u_0_1");

    private By logo_comedycentral = By.cssSelector("#comedycentral > a");
    private By logo_mtv = By.cssSelector("#mtv > a");
    private By logo_viva = By.cssSelector("#viva > a");
    private By logo_nickelodeon = By.cssSelector("#nickelodeon > a");

    private WebDriver driver;
    private WebDriverWait wait;

    public BlokEkipaHome(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(this.driver, 10);
    }

    public void go(){
        this.driver.get("http://www.comedycentral.pl/programy/2699-blok-ekipa");
        WebElement webElement = driver.findElement(title);
        this.wait.until(ExpectedConditions.visibilityOf(webElement));
        assertThat("Element is not visible!!!", webElement.isDisplayed(), is(true));
    }

    public void checkIfAllImportantElementAreVisible() {
        // if need be, we could also assert that other elements that are specific to this page are visible
        assertThat("Search box is not visible!!!", driver.findElement(search_box).isDisplayed(), is(true));
        assertThat("Page title is not visible!!!", driver.findElement(title).isDisplayed(), is(true));
    }

    public void checkIfFacebookLikeButtonIsVisible() {
        assertThat("Facebook Like button is not visible!!!", driver.findElement(facebook_like).isDisplayed(), is(true));
    }

    public void checkIfAllLogosAreVisibleInTheFooter() {
        assertThat("Comedy Central logo is not visible!!!", driver.findElement(logo_comedycentral).isDisplayed(), is(true));
        assertThat("MTV logo is not visible!!!", driver.findElement(logo_mtv).isDisplayed(), is(true));
        assertThat("Viva logo is not visible!!!", driver.findElement(logo_viva).isDisplayed(), is(true));
        assertThat("Nickelodeon logo is not visible!!!", driver.findElement(logo_nickelodeon).isDisplayed(), is(true));
    }
}
