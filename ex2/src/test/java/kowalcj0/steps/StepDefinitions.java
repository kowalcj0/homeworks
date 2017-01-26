package kowalcj0.steps;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import org.apache.log4j.Logger;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.WebDriverWait;

import kowalcj0.DriverManager;
import kowalcj0.page_objects.CCHome;
import kowalcj0.page_objects.BlokEkipaHome;

/**
 * Contains step definitions for two feature files: first.feature & blok_ekipa.feature
 * @author jk
 */
public class StepDefinitions {

    static Logger log = Logger.getLogger(StepDefinitions.class);
    WebDriver driver = DriverManager.getDriver();
    WebElement webElement;
    WebDriverWait wait = new WebDriverWait(driver, 10);

    @Given("^I am on the home page")
    public void iAmOnTheHomePage() {
        log.info("Given I'm on the homepage <br/>");
        CCHome page = new CCHome(driver);
        page.go();
    }

    @When("^I search for (.*)$")
    public void iSeachFor(String keywords) {
        log.info("When I go to the " + keywords + " result in the Programs section");
        CCHome page = new CCHome(driver);
        page.searchFor(keywords);
        page.goToProgram(keywords);
    }
    @When("^I go to the (.*) result in the Programy section")
    public void goToProgram(String keywords) {
        log.info("When I go to the " + keywords + " result in the Programs section");
        CCHome page = new CCHome(driver);
        page.goToProgram(keywords);
    }

    @Then("^I should see be on blok ekipa's page$")
    public void iAmOnBlokEkipasPage() {
        log.info("Then I should be on Blok Ekipa's page");
        BlokEkipaHome page = new BlokEkipaHome(driver);
        page.checkIfAllImportantElementAreVisible();
    }

    @Then("^Facebook like button should be visible")
    public void facebookLikButtonIsVisible() {
        log.info("Then Facebook Like button should be visible");
        BlokEkipaHome page = new BlokEkipaHome(driver);
        page.checkIfFacebookLikeButtonIsVisible();
    }

    @Then("^comedy central, mtv, viva and nickelodeon logos should be visible in the page footer")
    public void logosAreVisibleInTheFooter() {
        log.info("Then all logs are visible in the page footer");
        BlokEkipaHome page = new BlokEkipaHome(driver);
        page.checkIfAllLogosAreVisibleInTheFooter();
    }



}
