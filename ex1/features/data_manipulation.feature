Feature: Response data manipulation

    Background: Stack Exchange API should be reachable
        Given that Stack Exchange API is reachable


    Scenario: Retrieve all tags and save them to a list (duplicates should be removed
        When we get the activity feed for the term "perl"

        Then save them to a list and remove the duplicates


    Scenario: Compare 2 JSON structures except for title and last_activity_date values
        When we get the activity feed for the term "perl"
        And we create a copy of the response
        And we replace the "title" value in every item of the response copy with "Creating new JSON"
        And we remove the "last_activity_date" value from every item of the response copy

        Then the original response and the copy should be identical except for title and last_activity_date values

