import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Получаю данные для заполнения форм с email, firstname, lastname
    firstname = browser.find_element_by_css_selector('[name="firstname"]')
    firstname.send_keys('Konstantin')

    lastname = browser.find_element_by_css_selector('[name="lastname"]')
    lastname.send_keys('Nice')

    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('konstantin.nice@google.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'short_bio.txt')           # добавляем к этому пути имя файла
    element = browser.find_element_by_css_selector('#file')     # добавляем файл на веб страницу
    element.send_keys(file_path)

    submit = browser.find_element_by_css_selector(".btn")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций.
    browser.quit()

