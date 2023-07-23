import time
from pyclbr import Class

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    advertising = "//button[@class='button']"
    select_category = "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[2]"
    checkbox_brand = "//li[@id='popularinput-checkbox-2243-28669']"
    checkbox_linia = "//li[@id='input-checkbox-2245-123023']"
    checkbox_sex = "//li[@id='input-checkbox-2259-270479']"
    select_product_1 = "//a[@data-default-name='Versace Bright Crystal - Woda toaletowa']"
    add_to_cart = "//div[@class='button buy']"
    filter_brand = "//label[@for='input-checkbox-2243-28669']"
    filter_linia = "//label[@for='input-checkbox-2245-123023']"
    filter_sex = "//label[@for='input-checkbox-2259-270479']"
    product_name = "//span[@class='product-item__name']"
    product_price = "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]/div/span[2]"
    product_currency = "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]/div/span[3]"
    product_short_info = "//ul[@class='product-item-tabs__content tabs-content scrolling']"
    button_info_desc = "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[3]/ul[1]/li[2]"
    full_desc = "//li[@class='product-info__description']"

    # Getters

    def get_advertising(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.advertising)))

    def get_select_category(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_category)))

    def get_checkbox_brand(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_brand)))

    def get_filter_brand(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand)))

    def get_filter_linia(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_linia)))

    def get_checkbox_linia(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_linia)))

    def get_checkbox_sex(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_sex)))

    def get_filter_sex(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_sex)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    """Information about product"""


    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.product_price)))



    def get_product_currency(self):
        return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.product_currency)))

    #def get_product_price_value(self):
    # value_product_price = product_price.text
    # value_product_currency = product_currency.text
    # summary_product_price = value_product_price + " " + value_product_currency
    # print("++++++++++++++++++++++")
    # print(summary_product_price)


    def get_full_desc(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.full_desc)))


    def get_product_short_info(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_short_info)))

    """End information about product"""


    def get_button_info_desc(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_info_desc)))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    # Actions

    def click_advertising(self):
        self.get_advertising().click()
        print("Cloose advertising")

    def click_select_category(self):
        self.get_select_category().click()
        print("Choose select_category")

    def click_checkbox_brand(self):
        self.get_checkbox_brand().click()
        print("Click checkbox brand")

    def click_checkbox_linia(self):
        self.get_checkbox_linia().click()
        print("Click checkbox_linia")

    def click_checkbox_sex(self):
        self.get_checkbox_sex().click()
        print("Click checkbox sex")

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click select product1")

    def click_button_info_desc(self):
        self.get_button_info_desc().click()
        print("Click button info desc")

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print("Add product to cart")

    # Methods
    def choose_product(self):
        self.get_current_url()
        self.click_advertising()
        self.click_select_category()

        self.click_checkbox_brand()
        self.click_checkbox_linia()
        self.click_checkbox_sex()

        self.assert_word(self.get_filter_brand(), 'Versace')
        self.assert_word(self.get_filter_linia(), 'Bright Crystal')
        self.assert_word(self.get_filter_sex(), 'Kobieta')
        time.sleep(10)
        self.click_select_product_1()
        self.information_output(self.get_product_name())
        self.information_output(self.get_product_price())
        self.information_output(self.get_product_currency())
        self.information_output(self.get_product_short_info())
        self.click_button_info_desc()
        self.information_output(self.get_full_desc())
        self.click_add_to_cart()
        time.sleep(10)
