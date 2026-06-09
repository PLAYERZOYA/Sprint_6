import pytest
from selenium import webdriver
from data.urls import Urls



@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.main_page_url)
    yield driver
    driver.quit()