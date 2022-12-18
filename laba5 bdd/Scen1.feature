Feature: Unique list

Scenario: Making unique list
Given I have list [1, 2, 2, 3, 2, 5, 4, 3]
When Delete repeating numbers
Then List is unique [1, 2, 3, 5, 4]