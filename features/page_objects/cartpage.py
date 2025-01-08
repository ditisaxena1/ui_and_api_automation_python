from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.page_objects.base import BasePage


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(driver)

    def switch_to_book_page(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])

    def click_add_to_cart(self):
        self.base.wait_and_click(By.XPATH, "//*[text()='Add to cart']", 40)

    def no_of_products_in_cart(self):
        no_of_products = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, f"//li[@id='gh-minicart-hover']//i")))
        return no_of_products.text

