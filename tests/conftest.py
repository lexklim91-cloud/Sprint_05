import pytest
import random
import tests.data as data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(data.url)
    yield driver
    driver.quit()


@pytest.fixture()
def generate_email():
    first_names = ["alex", "maria", "alex", "anna"]
    last_names = ["smith", "ivanov", "doe", "petrov"]
    domains = ["gmail.com", "mail.ru", "yandex.ru"]

    email = f"{random.choice(first_names)}.{random.choice(last_names)}@{random.choice(domains)}"
    return email