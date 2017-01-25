@functional_test
@other_meta_tag
Feature: Users can search for Blok Ekipa

  Scenario Outline: Open various websites
    Given I am on <URL>
    When I search for element <element_id>
    Then I should see this element

  Examples:
    | URL                         | element_id  |
    | http://www.comedycentral.pl | query       |
