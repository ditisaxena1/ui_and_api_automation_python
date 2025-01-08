from behave import step

from features.page_objects.homepage import HomePage


@step("I search for product - '{product_name}'")
def step_impl(context, product_name):
    homepage = HomePage(context.driver)
    homepage.search_product(product_name)


@step("I click on search button")
def step_impl(context):
    homepage = HomePage(context.driver)
    homepage.click_on_search()


@step("I select the product '{product_name}'")
def step_impl(context, product_name):
    homepage = HomePage(context.driver)
    homepage.select_product(product_name)









