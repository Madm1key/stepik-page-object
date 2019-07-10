from .base_page import BasePage
from .locators import CardPageLocators


class CardPage(BasePage):
    def check_to_be(self):
        self.should_not_be_product()
        self.should_be_basket_empty_text()

    def should_not_be_product(self):
        self.is_not_element_present(*CardPageLocators.PRODUCT_TEXT)

    def should_be_basket_empty_text(self):
        self.is_element_present(*CardPageLocators.NOT_PRODUCT_TEXT)
