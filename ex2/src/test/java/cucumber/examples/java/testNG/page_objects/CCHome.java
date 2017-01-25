package cucumber.examples.java.testNG.page_objects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.List;

/**
 * Created by JK on 25/01/17.
 */
public class CCHome {

    private By search_box = By.id("query");
    private By search_results = By.cssSelector("search_results");
    private WebDriver driver;
    private WebDriverWait wait;

    public CCHome(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(this.driver, 10);
    }

    public void go(){
        this.driver.get("http://www.comedycentral.pl/");
        this.wait.until(ExpectedConditions.visibilityOfElementLocated(search_box));
    }

    public void searchFor(String keywords){
        this.driver.findElement(search_box).clear();
        this.driver.findElement(search_box).sendKeys(keywords);
        this.driver.findElement(search_box).submit();
        this.wait.until(ExpectedConditions.visibilityOfElementLocated(search_results));
    }

    public List<WebElement> getTheSearchResults() {
        return this.driver.findElements(search_results);
    }
}
