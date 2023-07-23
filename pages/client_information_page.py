import time
from pyclbr import Class

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class ClientInformationPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    next_button = "//label[@class='button']"
    adress = "//input[@id='select-city']"
    dropdown_adress = "//li[@data-id='774530']"
    delivery_dropdown = "//select[@id='order-delivery']"
    choose_delivery = "//option[@value='17']"
    street = "//input[@id='street']"
    home = "//input[@id='home']"
    flat = "//input[@id='register-flat']"
    zip = "//input[@id='order-zip']"

    # Getters

    def get_next_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.next_button)))

    def get_adress(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.adress)))

    def get_dropdown_adress(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.dropdown_adress)))

    def get_delivery_dropdown(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delivery_dropdown)))

    def get_choose_delivery(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.choose_delivery)))

    def get_street(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.street)))

    def get_home(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.home)))

    def get_flat(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.flat)))

    def get_zip(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.zip)))

    # Actions

    def click_next_button(self):
        self.get_next_button().click()
        print("Click next button")

    def input_adress(self, adress_text):
        self.get_adress().send_keys(adress_text)
        print("Input adress")

    def click_dropdown_adress(self):
        self.get_dropdown_adress().click()
        print("Click adress dropdown")

    def click_delivery_dropdown(self):
        self.get_delivery_dropdown().click()
        print("Click delivery dropdown")

    def click_choose_delivery(self):
        self.get_choose_delivery().click()
        print("Choose type delivery")

    def input_street(self, street_adress):
        self.get_street().send_keys(street_adress)
        print("Write street")

    def input_home(self, number_home):
        self.get_home().send_keys(number_home)
        print("Write home")

    def input_flat(self, number_flat):
        self.get_flat().send_keys(number_flat)
        print("Write flat")

    def input_zip(self, number_zip):
        self.get_zip().send_keys(number_zip)
        print("Write zip")

    # Methods
    def fill_order_information(self):
        self.get_current_url()
        self.click_next_button()
        self.input_adress("DDolice, Dolice, gmina wiejska, Stargardzki, ZACHODNIOPOMORSKIE")
        self.click_dropdown_adress()
        self.click_delivery_dropdown()
        self.click_choose_delivery()
        self.input_street("Stanislawa Drabika")
        self.input_home("11")
        self.input_flat("11")
        self.input_zip("50-367")
        time.sleep(10)
