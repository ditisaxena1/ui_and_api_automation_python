from behave import step

from features.page_objects.cartpage import CartPage


@step("I click on add to cart button")
def step_impl(context):
    cartpage = CartPage(context.driver)
    cartpage.switch_to_book_page()
    cartpage.click_add_to_cart()
    
    
@step('Verify that {no_of_product} product has been added to the cart')
def step_impl(context, no_of_product):
    cartpage = CartPage(context.driver)
    actual_products = cartpage.no_of_products_in_cart()
    assert int(actual_products) == int(no_of_product)




