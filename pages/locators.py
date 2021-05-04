from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")
    BASKET_LINK=(By.CSS_SELECTOR,"div.basket-mini  a")

class BasketPageLocators():
    CONTENT_PRODUCT=(By.CSS_SELECTOR,"div.basket-items")
    MESSAGE_TEXT=(By.CSS_SELECTOR,"#messages")

class MainPageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    LOGIN_INPUT=(By.CSS_SELECTOR, "#id_login_username")
    PASSWORD_INPUT=(By.CSS_SELECTOR, "#id_login-password")
    PASSWORD_RESET_LINK=(By.CSS_SELECTOR, "p>a")
    BUTTON_LOGIN_IN=(By.NAME, "login_submit")
    
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT=(By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_INPUT=(By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_INPUT=(By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON=(By.NAME, "registration_submit")
    
class ProductPageLocators():
    ADD_PRODUCT_BUTTON=(By.CSS_SELECTOR,"button.btn-add-to-basket")
    MESSAGE_ADD_BOOK=(By.XPATH,"//*[@id='messages']/div[1]/div/strong")
    COST_BASCKET=(By.CSS_SELECTOR,"div.alertinner>p>strong")
    NAME_BOOK=(By.CSS_SELECTOR,"div.product_main>h1")
    COST_BOOK=(By.CSS_SELECTOR,"p.price_color")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,"")
