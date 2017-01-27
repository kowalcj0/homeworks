package kowalcj0.page_objects;

import com.gargoylesoftware.htmlunit.javascript.background.JavaScriptExecutor;
import org.apache.log4j.Logger;
import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.List;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertThat;

/**
 * Created by JK on 25/01/17.
 */
public class Ramowka {

    static Logger log = Logger.getLogger(Ramowka.class);
    private By title = By.className("title");
    private By movies = By.cssSelector("#channel_contents > dl");
    private WebDriver driver;
    private WebDriverWait wait;

    public Ramowka(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(this.driver, 10);
    }

    public void go(){
        this.driver.get("http://www.comedycentral.pl/ramowka");
        WebElement pageTitle = driver.findElement(title);
        this.wait.until(ExpectedConditions.visibilityOf(pageTitle));
        WebElement channelContents = driver.findElement(movies);
        this.wait.until(ExpectedConditions.visibilityOf(channelContents));
        assertThat("Page title 'Ramówka' is not visible!!!", pageTitle.getText().toLowerCase(), is("ramowka"));
    }

    public void everyMovieHasAnDescriptionIndicator() {
        List<WebElement> items = driver.findElements(movies);
        for(WebElement item : items) {
            WebElement dd = item.findElement(By.cssSelector("dd"));
            String movieTitle = dd.findElement(By.xpath("a:nth-child(1) > div.text > h3")).getText();
            assertThat(
                    "Movie " + movieTitle + " does not have a description!",
                    dd.findElement(By.cssSelector("a.open")).isDisplayed(),
                    is(true));
        }
    }

    public void openAndCloseMovieDescriptions() {
        List<WebElement> items = driver.findElement(movies).findElements(By.cssSelector("dd"));
        log.info("Number of movies: " + items.size());
        for(WebElement item : items) {
            String movieTitle = item.getText();
            WebElement descriptionIndicator = item.findElement(By.cssSelector("a.open"));
            By description = By.cssSelector("a:nth-child(1) > p.description");
            // Scroll the page to the description indicator
            JavascriptExecutor jse = (JavascriptExecutor) driver;
            jse.executeScript("arguments[0].scrollIntoView();", descriptionIndicator);

            // open movie description
            descriptionIndicator.click();
            assertThat(
                    "Movie " + movieTitle + " does not have a description!",
                    item.findElement(description).isDisplayed(),
                    is(true));
            assertThat(
                    "Movie " + movieTitle + " not have a description!",
                    item.findElement(description).getText().isEmpty(),
                    is(false));

            // close movie description
            descriptionIndicator.click();
            assertThat(
                    "Movie " + movieTitle + " does not have a description!",
                    item.findElement(By.cssSelector("a:nth-child(1) > p.description")).isDisplayed(),
                    is(false));
        }
    }

    public void allMovieDescriptionsShouldBeHidden() {
        List<WebElement> descriptions = driver.findElements(By.cssSelector("p.description"));
        log.info("Number of movie descriptions to check: " + descriptions.size());
        for(WebElement description : descriptions) {
            assertThat(
                    "Movie description: " + description.getText() + " is still displayed!",
                    description.isDisplayed(),
                    is(false));
        }
    }
}
