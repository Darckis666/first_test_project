from .pages.product_page import ProductPage
import time
import pytest

link2="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
 pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_add_bascket_product(browser, link):
    page=ProductPage(browser, link)
    page.open()
    page.add_product_button()
    page.solve_quiz_and_get_code()
    page.should_be_message_adding_bascket()
    page.should_be_message_price_basket()

@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", marks=pytest.mark.smoke)])
def test_guest_cant_see_success_message(browser, link):
    page=ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", marks=pytest.mark.smoke)])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page=ProductPage(browser, link)
    page.open()
    page.add_product_button()
    page.solve_quiz_and_get_code()
    page.disappearing_success_message()

@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", marks=pytest.mark.smoke)])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page=ProductPage(browser, link)
    page.open()
    page.add_product_button()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
