from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
   def not_product(self):
        assert self.is_not_element_present(*BasketPageLocators.CONTENT_PRODUCT)

  
   def message_null_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_TEXT), "No message about empty basket "
