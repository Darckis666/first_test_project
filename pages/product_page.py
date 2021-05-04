from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .login_page import LoginPage

class ProductPage(BasePage):
    def add_product_button(self):
        button=self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        button.click()
        
    def should_be_message_adding_bascket(self):
        assert self.name_book() == self.name_book_in_message_adding_basket(), "Name book not contains message adding in basket"
    
    def should_be_message_price_basket(self):
        assert self.price_book() == self.coast_basket(), "Price book not equals caost bascket"
    
    def name_book(self):
        name_book_e=self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        return name_book_e.text
        
    def name_book_in_message_adding_basket(self):
        message_name_book=self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_BOOK)
        return message_name_book.text
        
    def price_book(self):
        price=self.browser.find_element(*ProductPageLocators.COST_BOOK)
        return price.text
        
    def coast_basket(self):
        coast_baske_message=self.browser.find_element(*ProductPageLocators.COST_BASCKET)
        return coast_baske_message.text
   
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_BOOK), "Success message is presented, but should not be"

    def disappearing_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_BOOK), "Success message is presented, but should not be"
