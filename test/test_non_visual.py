import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


from pages.homepage import HomePage
from pages.product import Product


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product = Product(browser)
    product.check_title_is('Samsung galaxy s6')


def test_two_mon(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()

    # позорище, это для теста
    time.sleep(3)

    homepage.check_monitor_count(2)
