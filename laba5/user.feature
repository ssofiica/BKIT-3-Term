Feature: Unique list

    Scenario: Making unique list
        Given I have list [1, 3, 1, 2, 5, 2]
        When Delete repeating numbers
        Then List is [1, 3, 2, 5]
