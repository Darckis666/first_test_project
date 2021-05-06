from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
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
@pytest.mark.need_review
def test_guest_add_bascket_product(browser, link):
    page=ProductPage(browser, link)
    page.open()
    page.add_product_button()
    page.solve_quiz_and_get_code()
    page.should_be_message_adding_bascket()
    page.should_be_message_price_basket()

@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", marks=pytest.mark.regress)])
def test_guest_cant_see_success_message(browser, link):
    page=ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", marks=pytest.mark.xfail)])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page=ProductPage(browser, link)
    page.open()
    page.add_product_button()
    page.solve_quiz_and_get_code()
    page.disappearing_success_message()

@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", marks=pytest.mark.xfail)])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page=ProductPage(browser, link)
    page.open()
    page.add_product_button()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.regress
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page=BasketPage(browser, browser.current_url)
    basket_page.not_product()
    basket_page.message_null_basket()

@pytest.mark.add_basket_from_user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page=LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = str(time.time())+"@test.com"
        page.register_new_user(email, 'Qwertyu1!')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page=ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page=ProductPage(browser, link)
        page.open()
        page.add_product_button()
        page.solve_quiz_and_get_code()
        page.should_be_message_adding_bascket()
        page.should_be_message_price_basket()

