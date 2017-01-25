Functional tests powered by Selenium (WebDriver) and TestNG
-----------------------------------------------------------

This example project is based on few other projects:
* [Cucumber-JVM-Parallel](https://github.com/tristanmccarthy/Cucumber-JVM-Parallel)
* [java-parallel](https://github.com/cucumber/cucumber-jvm/tree/java-parallel-example/examples/java-parallel)
* [java-webbit-websockets-selenium](https://github.com/cucumber/cucumber-jvm/tree/java-parallel-example/examples/java-webbit-websockets-selenium)

It allows you to run Cucumber features (tests/scenarios) in multiple browsers simultaneously using Selenium (WebDriver) and TestNG.

# Requirements

* Maven
* Java 7+
* Firefox and Chrome WebDriver binaries

# Running features in IDE

Tested in IntelliJ Idea 2016.3.3

To run all scenarios from an IDE using just Firefox, simply right click on one of the files:
* cucumber.examples.java.testNG.runners.RunCukesTestInFirefox

And chose "Run ..."
(Unfortunately, at this point in time, choosing RunCukesTestInChrome will run tests also in FF!)


To run all stories simultaneously in both browsers (Chrome and Firefox) right click on one of the files:
* src/test/resources/TestNGRunTestsLocally.xml
* src/test/resources/TestNGRunTestsRemotely.xml

And chose "Run ..."

To run just one selected feature, change the feature name in the class below:

    cucumber.examples.java.testNG.runners.RunSingleFeature

And as in previous example, right click on this class and chose "Run ..."


# Running features from CLI
Run tests using local browsers:

    mvn clean install

Run tests using browsers running on remote nodes:

    mvn clean install -P runTestsRemotely


# Reports

Test reports in various formats [html, json, xml, js] are stored in: target/cucumber-report


# How to download WebDriver binaries automatically
This project is using Mark Collin's "selenium-standalone-server-plugin" which is a Maven plugin that can download
WebDriver binaries automatically.
Once you configure the plugin to your liking, then:

    mvn clean install -P downloadDriverBinaries

The pom.xml is currently configured to download only a Chrome driver binary for 64bit Linux OSes.
If you can't download desired driver binary, then check if its URL and checksum specified in:

    src/test/resources/RepositoryMap.xml

are correct. If not, then modify this file accordingly.

# How to download WebDriver binaries manually

If, for any reason, you can't download WebDriver binaries automatically, 
then you can download them here: [http://www.seleniumhq.org/download/](http://www.seleniumhq.org/download/)
 and extract to `binaries` dir 

```
${project.basedir}-|
                   |
                   \linux|
                         |
                         |\googlechrome|
                         |             |
                         |             \64bit
                         |
                         \marionette|   # dir for firefox driver
                                    \64bit
                   \windows|
                           |
                           |\googlechrome|
                           |             |
                           |             \64bit
                           |
                           \marionette|   # dir for firefox driver
                                      \64bit
```

## Paths to WebDriver binaries
In some rare cases you might also need to update paths to WebDriver binaries specified in `cucumber.examples.java.testNG.LocalDriverFactory`

