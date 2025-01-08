from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from features.page_objects.base import BasePage


class HomePage:

    category_map = {
        'Skincare': 3
    }

    category = "//*[@id='category_id']"

    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(driver)

    def search_product(self, product_name):
        search_box = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@aria-label='Search for anything']")))

        search_box.clear()
        search_box.send_keys(product_name)

    def click_on_search(self):
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def select_product(self, book_index):
        index = int(book_index)
        book = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,f"(//div[@id='srp-river-results']/ul/li[{index}])//span[@role='heading']")))
        book.click()












