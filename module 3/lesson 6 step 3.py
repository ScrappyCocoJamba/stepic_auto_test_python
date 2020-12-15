import time
import math
import pytest
from selenium import webdriver


expected_feedback = "Correct!"

@pytest.fixture(scope="class")  # scopes: "class", "function", "session", "module"
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class Test_parametrize():

    @pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1","https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1","https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])
    def test_send_answer(self, browser, url):
        link = f"{url}"
        browser.get(link)
        browser.implicitly_wait(15)
        textarea = browser.find_element_by_css_selector(".string-quiz__textarea")
        textarea.click()
        answer = str(math.log(int(time.time() + 0.02)))
        textarea.send_keys(answer)
        browser.implicitly_wait(3)
        button = browser.find_element_by_css_selector(".submit-submission")
        button.click()
        browser.implicitly_wait(6)
        assert_text = browser.find_element_by_css_selector(".smart-hints__feedback")
        actual_feedback = assert_text.text
        assert actual_feedback == expected_feedback, f"Error, got {actual_feedback}, but expected {expected_feedback}"
