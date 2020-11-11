from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time



try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # найти сумму двух числе из текста
    number1 = browser.find_element_by_css_selector('#num1')
    number1_value = number1.text
    number2 = browser.find_element_by_css_selector('#num2')
    number2_value = number2.text
    values_sum = int(number1_value) + int(number2_value)
    values_sum2 = str(values_sum)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(values_sum2)  # ищем элемент из списка со значением суммы

    button = browser.find_element_by_css_selector(".btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()