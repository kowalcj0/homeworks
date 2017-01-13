Feature: JSON data coming from Stack Exchange API should have correct structure

    Background: Stack Exchange API should be reachable
        Given that Stack Exchange API is reachable


    @<keyword>
    @array
    @structure
    Scenario Outline: Response should contain an array of items for a keyword "<keyword>"
        When we get the activity feed for the term "<keyword>"

        Then the response should contain an array of items called "items"

        Examples:
            |keyword    |
            |api        |
            |bdd        |
            |perl       |
            |python     |


    @<keyword>
    @meta
    @structure
    Scenario Outline: Response should contain meta data
        When we get the activity feed for the term "<keyword>"

        Then response should contain meta data

        Examples:
            |keyword    |
            |api        |
            |bdd        |
            |perl       |
            |python     |


    @<keyword>
    @tags
    @owner
    @values
    @structure
    Scenario Outline: Every item should contain an array of tags, an owner object and a list of json values
        When we get the activity feed for the term "<keyword>"

        Then every item should contain an array of tags
        And every item should contain an owner object
        And every item should contain a list of json values

        Examples:
            |keyword    |
            |api        |
            |bdd        |
            |perl       |
            |python     |


    @<keyword>
    @owner
    @profile
    @structure
    Scenario Outline: Every owner should have a valid link to its profile and profile image
        When we get the activity feed for the term "<keyword>"

        Then every existing owner should have a valid profile link
        And every existing owner should have a valid profile image link
        And every non-existing owner should not have a profile link
        And every non-existing owner should not have a valid profile image link

        Examples:
            |keyword    |
            |api        |
            |bdd        |
            |perl       |
            |python     |
