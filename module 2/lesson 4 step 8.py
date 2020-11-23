from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

'''
Используемые правила для ожиданий в библиотеке selenium.webdriver.support

https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
'''
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()

    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет 100$
    text = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    # Если в переменную text попало искомое значение - забронировать дом
    if text:
        button = browser.find_element_by_id("book")
        button.click()

    # вытаскиваю значение X из текста и произвожу математическое вычисление.
    x_value = browser.find_element_by_css_selector('#input_value')
    x = x_value.text
    y = calc(x)

    # Получаю данные для заполнения формы с ответом
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)

    # Отправляю решение
    submit = browser.find_element_by_id("solve")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
