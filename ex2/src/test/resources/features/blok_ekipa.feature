@functional
@blok_ekipa
Feature: Users can search for Blok Ekipa

  Scenario Outline: Users can go to Blok Ekipa's page through search results
    Given I am on the home page

    When I search for <keywords>
    And I go to the <keywords> result in the Programy section

    Then I should be on the <key words>'s page
    And Facebook like button should be visible
    And comedy central, mtv, viva and nickelodeon logos should be visible in the page footer

  Examples:
    | keywords    |
    | blok ekipa  |

