from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CLASS_NAME, "login_form")
    REGISTER_FORM = (By.CLASS_NAME, "register_form")


class ProductPageLocators(object):
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .price_color")
    BASKET_NAME = (By.CSS_SELECTOR, "#messages > .alert-safe:nth-child(1) strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > .alert-safe:nth-child(3) strong")

