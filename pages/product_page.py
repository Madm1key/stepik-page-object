from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_to_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def check_basket_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        basket_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME)
        assert basket_name.text == product_name.text, "Добавленный товар не соответсвует исходному"

    def check_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert basket_price.text == product_price.text, "Добавленная сумма не соответствует исходной"

    def not_should_be_succes_message_elem_present(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_NAME), "Инфомарция о товаре отображается"

    def not_should_be_succes_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_NAME), "Информация о товаре не исчезла"
