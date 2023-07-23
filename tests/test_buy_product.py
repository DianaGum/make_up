import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.login_page import Login
from pages.main_page import MainPage


def test_select_product():
    s = Service('C:\\Python\\Selenium_stepik\\drivers\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    print("Test start")

    login = Login(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.choose_product()

    cp = CartPage(driver)
    cp.click_checkout_button()

    cip = ClientInformationPage(driver)
    cip.fill_order_information()



