import time
from pyclbr import Class

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.main_page import MainPage


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    checkout_button = "//div[@class='button']"
    name_product_in_cart = "//div[@class='product__header']"
    price_in_cart = "//div[@class='product__price']"

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_name_product_in_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name_product_in_cart)))

    def get_price_in_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_in_cart)))
    # value_price_in_cart = price_in_cart.text    # assert summary_product_price == value_price_in_cart

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout")

    # Methods

    def product_confirmation(self):
        self.get_current_url()
        self.information_output(self.get_price_in_cart())
        self.assert_text(self.get_name_product_in_cart(), MainPage.get_product_name())
        self.click_checkout_button()
        time.sleep(5)
