from selenium import webdriver
from pytest import fixture
@fixture
def _driver():
    driver = webdriver.Chrome()
    driver.get(r"https://www.flipkart.com")
    driver.maximize_window()
    yield driver
