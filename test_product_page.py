from .pages.product_page import ProductPage
import time
import pytest

#link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_add_bascket_product(browser, link):
    page=ProductPage(browser, link)
    page.open()
    page.add_product_button()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.should_be_message_adding_bascket()
    page.should_be_message_price_basket()

