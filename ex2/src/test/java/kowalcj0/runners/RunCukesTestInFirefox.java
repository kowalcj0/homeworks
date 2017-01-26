package kowalcj0.runners;

import cucumber.api.CucumberOptions;
import cucumber.api.testng.AbstractTestNGCucumberTests;

/**
 * Please notice that BeforeAfterHooks class
 * is in the same package as the steps definitions.
 * It has two methods that are executed before or after scenario.
 * I'm using it to delete cookies and take a screen shot if scenario fails.
 */
@CucumberOptions(
        features = "target/test-classes/features",
        glue = {"kowalcj0.steps"},
        format = {"pretty",
                "html:target/cucumber-report/firefox",
                "json:target/cucumber-report/firefox/cucumber.json",
                "junit:target/cucumber-report/firefox/cucumber.xml"})
public class RunCukesTestInFirefox extends AbstractTestNGCucumberTests {
}