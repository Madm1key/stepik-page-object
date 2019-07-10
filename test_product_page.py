import pytest
import time
from pages.product_page import ProductPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


@pytest.mark.need_review
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        reg_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        e_mail = str(time.time()) + '@fakemail.org'
        psw = 'GaGaWa123'
        login_page = LoginPage(browser, reg_link)
        login_page.open()
        login_page.register_new_user(e_mail, psw)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.not_should_be_succes_message_elem_present()

    @pytest.mark.parametrize('number', (str(i) for i in range(2)))
    def test_user_can_add_product_to_cart(self, browser, number):
        total_link = link + number
        page = ProductPage(browser, total_link)
        page.open()
        page.click_to_basket_button()
        page.check_basket_product()


def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_to_basket_button()
    page.not_should_be_succes_message_elem_present()


def test_message_disappeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_to_basket_button()
    page.not_should_be_succes_message_is_disappeared()


def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    card_page = page.go_to_card_page()
    card_page.check_to_be()
