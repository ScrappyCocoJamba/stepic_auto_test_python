import math
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_link_text')
    # расшифровка кода из цифр "224592" для нахождения текста ссылки
    search_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    # поиск ссылки по тексту "224592" и переход по ней
    link = browser.find_element_by_link_text(search_text)
    link.click()
    # заполение формы
    input1 = browser.find_element_by_tag_name("Input")
    input1.send_keys("Konstantin")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Martyashkov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Novosibirsk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    # получение кода.
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(20)

finally:
    browser.quit()
