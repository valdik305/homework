import math
import re
import time
import os
import pytest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome()
# browser.get(link)
# button = browser.find_element(By.ID, "submit_button")
# button.click()
#
# # закрываем браузер после всех манипуляций
# browser.quit()
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# link = "http://suninjuly.github.io/find_link_text"
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     l = str(math.ceil(math.pow(math.pi, math.e)*10000))
#     browser.find_element(By.LINK_TEXT,l).click()
#     sleep(2)
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#     sleep(4)
#
# finally:
#     browser.quit()

# В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html).
# С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях своего продукта.
# В награду за заполнение формы становится доступен код на скидку. Но маркетологи явно переусердствовали,
# добавив в форму 100 обязательных полей и ограничив время на ее заполнение.
# Теперь эта задача под силу только роботам.
# Используйте WebDriver, метод find_elements, нужные локатор и его значение.
# Введите полученный код в качестве ответа к этой задаче.
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.CSS_SELECTOR, "input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# не забываем оставить пустую строку в конце файла


# link = " http://suninjuly.github.io/find_xpath_form"
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# не забываем оставить пустую строку в конце файла




# try:
#     link = "http://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
#     input3.send_keys("Smolensk")
#     sleep(2)
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     link = "https://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#
#     x_element = browser.find_element(By.CSS_SELECTOR, '[valuex]')
#     sleep(2)
#     x = x_element.get_attribute('valuex')
#     y = calc(x)
#     inp= browser.find_element(By.ID, 'answer')
#     sleep(2)
#     inp.send_keys(y)
#     ch_b= browser.find_element(By.ID, 'robotCheckbox')
#     ch_b.click()
#     rad_b= browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
#     rad_b.click()
#     bat_sab= browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]')
#     bat_sab.click()
#     sleep(2)
#
# finally:
#     time.sleep(10)
#         # закрываем браузер после всех манипуляций
#     browser.quit()




# try:
#     def calc(a, b):
#         return str(int(a) + int(b))
#     link = " https://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     a_element = browser.find_element(By.CSS_SELECTOR, '[id="num1"]')
#     a = a_element.text
#     b_element = browser.find_element(By.CSS_SELECTOR , '[id="num2"]')
#     b = b_element.text
#     y = calc(a,b)
#     inp= browser.find_element(By.CSS_SELECTOR, '[class="custom-select"]')
#     inp.click()
#     inp.send_keys(y)
#     subm= browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]')
#     subm.click()
#
# finally:
#     time.sleep(10)
#         # закрываем браузер после всех манипуляций
#     browser.quit()


# try:
#     browser = webdriver.Chrome()
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser.get(link)
#     button = browser.find_element(By.TAG_NAME, "button")
#     # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     browser.execute_script("window.scrollBy(0, 100);")
#     button.click()
#     sleep(3)
#
# finally:
#     browser.quit()
#
# def calc(x):
#      return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser.get(link)
#     p_elm = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
#     x = p_elm.text
#     y = calc(x)
#     # browser.execute_script("return arguments[0].scrollIntoView(true); btn btn-primary")
#     browser.execute_script("window.scrollBy(0, 100);")
#     inp = browser.find_element(By.ID, 'answer')
#     inp.send_keys(y)
#     chk_b = browser.find_element(By.ID, 'robotCheckbox')
#     chk_b.click()
#     rad_b = browser.find_element(By.ID, 'robotsRule')
#     rad_b.click()
#     btn = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
#     btn.click()
#     sleep(5)
# finally:
#     browser.quit()





# current_dir = os.path.abspath(os.path.dirname(__file__))
# file_path = os.path.join(current_dir, 'file.txt')
#
# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/file_input.html"
#     browser.get(link)
#     f_name = browser.find_element(By.TAG_NAME ,'input')
#     f_name.send_keys("lol")
#     l_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
#     l_name.send_keys("lolo")
#     emale= browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
#     emale.send_keys("sdf@mail.com")
#     file_z = browser.find_element(By.CSS_SELECTOR, '#file')
#     file_z.send_keys(file_path)
#     sleep(2)
#     subm= browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
#     subm.click()
#     sleep(4)
# finally:
#     browser.quit()


# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser.get(link)
#     knopka = browser.find_element(By.CSS_SELECTOR ,'[class="btn btn-primary"]')
#     knopka.click()
#     alert = browser.switch_to.alert
#     alert.accept()
#     n = browser.find_element(By.CSS_SELECTOR ,'[id="input_value"]')
#     x = n.text
#     y = calc(x)
#     inp=browser.find_element(By.CSS_SELECTOR ,'[id="answer"]')
#     inp.send_keys(str(y))
#     sub = browser.find_element(By.CSS_SELECTOR ,'[class="btn btn-primary"]')
#     sub.click()
#     sleep(4)
#
#
# finally:
#     browser.quit()


# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     link = "https://suninjuly.github.io/redirect_accept.html"
#     browser.get(link)
#     knopka = browser.find_element(By.TAG_NAME ,'button')
#     knopka.click()
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#     n = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
#     x = n.text
#     y = calc(x)
#     inp=browser.find_element(By.CSS_SELECTOR ,'[id="answer"]')
#     inp.send_keys(str(y))
#     sleep(1)
#     sub = browser.find_element(By.CSS_SELECTOR ,'[class="btn btn-primary"]')
#     sub.click()
#     sleep(4)
# finally:
#     browser.quit()

# def calc(x):
#      return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     link = "https://suninjuly.github.io/explicit_wait2.html"
#     browser.get(link)
#     price = WebDriverWait(browser, 12).until(
#         EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[id="price"]',), "100"))
#     knopka = browser.find_element(By.CSS_SELECTOR, '[id="book"]')
#     knopka.click()
#     sleep(2)
#     num = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
#     x = num.text
#     y = calc(x)
#     inp=browser.find_element(By.CSS_SELECTOR ,'[id="answer"]')
#     browser.execute_script("window.scrollBy(0, 100);")
#     inp.send_keys(str(y))
#     sub = browser.find_element(By.ID ,'solve')
#     sub.click()
#     sleep(5)
# finally:
#     browser.quit()