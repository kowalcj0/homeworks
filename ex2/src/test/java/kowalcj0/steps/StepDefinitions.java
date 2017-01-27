package kowalcj0.steps;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import kowalcj0.page_objects.Ramowka;
import org.apache.log4j.Logger;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.WebDriverWait;

import kowalcj0.DriverManager;
import kowalcj0.page_objects.Home;
import kowalcj0.page_objects.BlokEkipa;

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
        log.info("Given I'm on the home page");
        Home page = new Home(driver);
        page.go();
    }

    @Given("^I am on the ramowka page")
    public void iAmOnTheRamowkaPage() {
        log.info("Given I'm on the ramowka page");
        Ramowka page = new Ramowka(driver);
        page.go();
    }

    @When("^I search for (.*)$")
    public void iSeachFor(String keywords) {
        log.info("When I go to the " + keywords + " result in the Programs section");
        Home page = new Home(driver);
        page.searchFor(keywords);
        page.goToProgram(keywords);
    }
    @When("^I go to the (.*) result in the Programy section")
    public void goToProgram(String keywords) {
        log.info("When I go to the " + keywords + " result in the Programs section");
        Home page = new Home(driver);
        page.goToProgram(keywords);
    }

    @Then("^I should see be on blok ekipa's page$")
    public void iAmOnBlokEkipasPage() {
        log.info("Then I should be on Blok Ekipa's page");
        BlokEkipa page = new BlokEkipa(driver);
        page.checkIfAllImportantElementAreVisible();
    }

    @Then("^Facebook like button should be visible")
    public void facebookLikButtonIsVisible() {
        log.info("Then Facebook Like button should be visible");
        BlokEkipa page = new BlokEkipa(driver);
        page.checkIfFacebookLikeButtonIsVisible();
    }

    @Then("^comedy central, mtv, viva and nickelodeon logos should be visible in the page footer")
    public void logosAreVisibleInTheFooter() {
        log.info("Then all logs are visible in the page footer");
        BlokEkipa page = new BlokEkipa(driver);
        page.checkIfAllLogosAreVisibleInTheFooter();
    }


    @Then("^every movie in the list has an description indicator")
    public void everyMovieHasDescriptionIndicator() {
        Ramowka page = new Ramowka(driver);
        page.everyMovieHasAnDescriptionIndicator();
    }

    @When("^I open and close all movie descriptions in the list")
    public void openAndCloseMovieDescriptions() {
        Ramowka page = new Ramowka(driver);
        page.openAndCloseMovieDescriptions();
    }

    @Then("^no movie description should be visible")
    public void allMovieDescriptionsShouldBeHidden() {
        Ramowka page = new Ramowka(driver);
        page.allMovieDescriptionsShouldBeHidden();
    }

}
