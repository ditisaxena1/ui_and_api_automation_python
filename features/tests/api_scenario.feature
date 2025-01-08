# Created by dsaxena2 at 08/01/25
Feature: [API] - Coindesk API

  Scenario: Verify the response contains 3 BPIs (USD, GBP, EUR) and the GBP 'description' is 'British Pound Sterling'
    Given Send the get request
    Then Verify that status code is 200
    And Verify that the response contains 3 BPIs: USD, GBP, EUR
    And Verify that the GBP description' is 'British Pound Sterling'
