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


@pytest.fixture()
def user_dog():
    return data.User(name=data.name_user[0], surname=data.surname_user[0], address=data.address_user[0],
                     phone_number=data.phone_number_user[0], comment=data.comments[0])


@pytest.fixture()
def user_cat():
    return data.User(name=data.name_user[1], surname=data.surname_user[1], address=data.address_user[1],
                     phone_number=data.phone_number_user[1], comment=data.comments[1])
