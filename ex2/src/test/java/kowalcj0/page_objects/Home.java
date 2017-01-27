package kowalcj0.page_objects;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

/**
 * Created by JK on 25/01/17.
 */
public class Home {

    private By search_box = By.id("query");
    private By search_results = By.className("search_results");
    private By programs = By.cssSelector("div.search_results > div:nth-child(1) > ul > li > a");
    private WebDriver driver;
    private WebDriverWait wait;

    public Home(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(this.driver, 10);
    }

    public void go(){
        this.driver.get("http://www.comedycentral.pl/");
        this.wait.until(ExpectedConditions.visibilityOfElementLocated(search_box));
    }

    public void searchFor(String keywords){
        WebElement se = driver.findElement(search_box);
        se.clear();
        se.sendKeys(keywords);
        this.wait.until(ExpectedConditions.visibilityOfElementLocated(search_results));
    }

    public void goToProgram(String keywords) {
        List<WebElement> links = driver.findElements(programs);
        for(WebElement link : links) {
            WebElement hdr = link.findElement(By.cssSelector("h3"));
            if (hdr.getText().toLowerCase().equals(keywords.toLowerCase())) {
                link.click();
            }
        }
    }

}
