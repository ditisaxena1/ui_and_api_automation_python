# Created by ditis at 23-10-2024
Feature: [UI] - Test Ebay website

  @web
  Scenario: Verify that user is able to interact with the ecommerce website
    When I search for product - 'book'
    And I click on search button
    And I select the product '1'
    And I click on add to cart button
    Then Verify that 1 product has been added to the cart