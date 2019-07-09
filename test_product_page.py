import pytest
from pages.product_page import ProductPage
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


@pytest.mark.parametrize('number', (str(i) for i in range(10)))
def test_guest_can_add_product_to_cart(browser, number):
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


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.not_should_be_succes_message_elem_present()


def test_message_disappeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_to_basket_button()
    page.not_should_be_succes_message_is_disappeared()
