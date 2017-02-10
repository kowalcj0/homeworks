@search
Feature: Document Search

    Background: Springer Link should be reachable
        Given that Springer Link is reachable


    @search
    @content-type
    Scenario Outline: Users should be able to do a full text search without specifying the content type
        When an unauthenticated user searches for any content type with "<keywords>"

        Then the results should contain all kinds of content types

        Examples:
            |keywords               |
            |Constructing backbone  |
            |International Trade    |
            |Medicago sativa        |


    @search
    @<contentype>
    @content-type
    Scenario Outline: Users should be able to do a full text search without specifying the content type
        When an unauthenticated user searches for "<contenttype>" with "<keywords>"

        Then the results should only contain "<contenttype>" content-type

        Examples:
            |keywords               |contenttype        |
            |Frontiers of Physics   |Chapter            |
            |Constructing backbone  |Article            |
            |International Trade    |ReferenceWorkEntry |
            |Medicago sativa        |Book               |
            |Chromosome Condensation|Protocol           |
            |Language and Education |BookSeries         |
            |Somnologie             |Journal            |
            |Wetland book           |ReferenceWork      |
