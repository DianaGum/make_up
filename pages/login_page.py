import time
from pyclbr import Class

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login(Base):
    url = 'https://makeup.pl/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    auth_icon = "//div[@class='header-office']"
    user_name = "//input[@id='login']"
    password = "//input[@id='pw']"
    login_button = "//button[@class='button full-width']"
    #main_word =

    # Getters

    def get_auth_icon(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.auth_icon)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    # def get_main_word(self):
    #     return WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_auth_icon(self):
        self.get_auth_icon().click()
        print("Click Auth icon")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_auth_icon()
        self. input_user_name("test133d@gmail.com")
        self.input_password("12345Da!")
        self.click_login_button()
        #self.assert_word(self.get_main_word(), 'Products')
