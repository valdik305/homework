from time import sleep

import pytest
from selenium import webdriver
import time

from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options


# @pytest.fixture(scope="function")
# def browser():
#     """ФИКСТУРА: открывает браузер перед тестом и закрывает после"""
#     browser = webdriver.Chrome()
#     yield browser  # Здесь тест берет управление и выполняется
#     sleep(5)
#     browser.quit()
#
#
# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default=chrome,
#                      help="Choose browser: chrome or firefox")
#

def pytest_addoption(parser):
    # Регистрируем параметр browser_name (он у вас, скорее всего, уже есть)
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    # РЕГИСТРИРУЕМ ПАРАМЕТР language (ЭТОГО НЕ ХВАТАЛО!)
    parser.addoption('--language', action='store', default="en",
                     help="Choose language, e.g., ru, en, es")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
