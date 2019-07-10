from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Is not login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, e_mail, pwd):
        e_mail_field = self.browser.find_element(*LoginPageLocators.E_MAIL)
        pwd_field = self.browser.find_element(*LoginPageLocators.PWD)
        re_pwd_field = self.browser.find_element(*LoginPageLocators.RE_PWD)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        e_mail_field.send_keys(e_mail)
        pwd_field.send_keys(pwd)
        re_pwd_field.send_keys(pwd)
        reg_button.click()
