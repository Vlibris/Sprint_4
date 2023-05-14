import pytest
from selenium import webdriver
import data


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture()
def url_home_page():
    return data.home_page()


@pytest.fixture()
def url_order_form():
    return data.order_form()


@pytest.fixture()
def url_yandex():
    return data.yandex()
