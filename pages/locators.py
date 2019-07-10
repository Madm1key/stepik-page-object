from selenium.webdriver.common.by import By


class BaseLocators(object):
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")


class BasePageLocators(object):
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CLASS_NAME, "login_form")
    REGISTER_FORM = (By.CLASS_NAME, "register_form")
    E_MAIL = (By.ID, 'id_registration-email')
    PWD = (By.ID, 'id_registration-password1')
    RE_PWD = (By.ID, 'id_registration-password2')
    REG_BUTTON = (By.CSS_SELECTOR, '#register_form button')


class ProductPageLocators(object):
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .price_color")
    BASKET_NAME = (By.CSS_SELECTOR, "#messages > .alert-safe:nth-child(1) strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > .alert-safe:nth-child(3) strong")


class CardPageLocators(object):
    PRODUCT_TEXT = (By.CSS_SELECTOR, "#content_inner .basket-title  h2")
    NOT_PRODUCT_TEXT = (By.CSS_SELECTOR, "#content_inner p")
