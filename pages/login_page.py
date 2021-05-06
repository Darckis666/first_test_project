from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        text_link=self.browser.current_url
        assert "login" in str(text_link), "Text link in not 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not see page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not see page"

    def register_new_user(self, email, password):
          self.fill_email_input(email)
          self.fill_password_input(password)
          self.fill_repeat_password_input(password)
          self.button_register_submint_click()

    def fill_email_input(self, email):
        email_input=self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

    def fill_password_input(self, password):
        password_input=self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

    def fill_repeat_password_input(self, password):
        repeat_password_input=self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT)
        repeat_password_input.send_keys(password)

    def button_register_submint_click(self):
        button_register=self.browser.find_element(*LoginPageLocators.REGISTR_BUTTON)
        button_register.click()
