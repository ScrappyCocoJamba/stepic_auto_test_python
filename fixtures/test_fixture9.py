import pytest
from selenium import webdriver
import  time

link = "http://selenium1py.pythonanywhere.com/"

#  pytest -s -v -m "not smoke" test_fixture9.py -- if you won't use smoke mark

#  pytest -s -v -m "smoke or regression" test_fixture9.py  -- if you want run several tests with these marks

#  pytest -s -v -m "smoke and win10" test_fixture9.py  -- if you want run test with these marks

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        time.sleep(3)

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        time.sleep(3)