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
    @<contenttype>
    @content-type
    Scenario Outline: Users should be able to do a full text search for a document of a specific type
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


    @wip
    @search
    @discipline
    @<discipline>
    Scenario Outline: Users should be able to narrow down the search results to "<discipline>" discipline
        When an unauthenticated user searches for a document within "<discipline>" discipline with "<keywords>"

        Then the results should only contain documents from "<discipline>" discipline

        Examples:
            |keywords               |discipline         |
            |Doctors without Borders|Medicine           |
            |Plasma                 |Life Sciences      |
            |Chromosome Condensation|Biomedical Sciences|
            |Medicago sativa        |Chemistry          |
            |Cryptography           |Computer Science   |



    @wip
    @search
    @language
    @<language>
    Scenario Outline: Users should be able to narrow down the search results to "<language>" language
        When an unauthenticated user searches for a document in "<language>" with "<keywords>"

        Then the results should only contain documents in "<language>"

        Examples:
            |keywords               |language|
            |Doctors without Borders|English |
            |Plasma                 |German  |
            |Chromosome Condensation|Dutch   |
            |Medicago sativa        |French  |
            |Cryptography           |Italian |


    @wip
    @csv
    @search
    @<contenttype>
    @content-type
    Scenario Outline: The response should be a valid CSV
        When an unauthenticated user searches for "<contenttype>" with "<keywords>"

        Then the response should contain a valid CSV file

        Examples:
            |keywords               |contenttype        |
            |Constructing backbone  |Article            |
            |International Trade    |ReferenceWorkEntry |


    @wip
    @search
    @empty
    @content-type
    Scenario: Empty query searches should return all documents
        When an unauthenticated user do a search without any keywords

        Then the results should contain all kinds of content types


    @wip
    @search
    @security
    @sqlinjection
    @content-type
    Scenario Outline: Empty query searches should return all documents
        When an unauthenticated user searches for any content type with "<sql>"

        Then search API should gracefully handle such a request

		Examples:
			|sql                            |
            |' OR '1'='1' --                |
		    |' OR '1'='1' ({                |
		    |' OR '1'='1' /*                |
            |);SELECT pg_sleep(25)--        |
            |)) OR SLEEP(25)=0 LIMIT 1--    |
