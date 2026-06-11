import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from homework.conftest import browser

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_1(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert button.is_displayed()
