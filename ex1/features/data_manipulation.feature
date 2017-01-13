Feature: Response data manipulation

    Background: Stack Exchange API should be reachable
        Given that Stack Exchange API is reachable


    @duplicates
    @tags
    @copy
    @list
    @manipulation
    Scenario: Retrieve all tags and save them to a list (duplicates should be removed
        When we get the activity feed for the term "perl"
        And we save the tags from the response to a list and remove the duplicates

        Then we should have a list of tags without duplicates


    @copy
    @tags
    @compare
    @manipulation
    Scenario: Compare 2 JSON structures except for title and last_activity_date values
        When we get the activity feed for the term "perl"
        And we create a copy of the response
        And we replace the value of field "title" in every item of the response copy with "Creating new JSON"
        And we remove the field "last_activity_date" from every item of the response copy

        Then the original response and the copy should be identical except for title and last_activity_date values
