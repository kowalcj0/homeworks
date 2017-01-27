@functional
@ramowka
Feature: Ramowka

  @bug
  @jira_ticket_number_CC2143
  @fixme
  Scenario: Every movie should have a description
    Given I am on the ramowka page

    Then every movie in the list has an description indicator


  Scenario: User can open and close movie description
    Given I am on the ramowka page

    When I open and close all movie descriptions in the list

    Then no movie description should be visible
