import pytest
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com"


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()


    def test_guest_should_see_login_link(browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_can_go_to_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    card_page = page.go_to_card_page()
    card_page.check_to_be()
