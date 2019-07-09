import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('link', (str(i) for i in range(10)))
def test_guest_can_add_product_to_cart(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + link
    page = ProductPage(browser, link)
    page.open()
    page.click_to_basket_button()
    page.check_basket_product()
