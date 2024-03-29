from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BaseLocators
from .login_page import LoginPage
from .card_page import CardPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_card_page(self):
        card_link = self.browser.find_element(*BaseLocators.BASKET_LINK)
        card_link.click()
        return CardPage(browser=self.browser, url=self.browser.current_url)
