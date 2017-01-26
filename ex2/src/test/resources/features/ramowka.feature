@functional
@ramowka
Feature: Ramowka

  Scenario: Every movie should have a description that can be opened and closed
    Given I am on the ramowka page
    And every movie in the list has an description indicator

    When I open the description for every movie in the list

    Then no movie description should be visible
