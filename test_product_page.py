#Tests for product page
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.locators import BasePageLocators
from .pages.base_page import BasePage
import pytest
import time


@pytest.mark.need_review
def test_add_product_and_solve_quiz(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

@pytest.mark.need_review							  
def test_guest_can_add_product_to_basket(browser):
    #The test of adding an item to the basket is not authorized by the user
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.should_be_added_to_basket_message()
	
@pytest.mark.skip(reason="no way of currently testing this")
def test_guest_should_see_login_link_on_product_page(browser):
    #Find Buttons "add to basket"
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.need_review	
def test_guest_can_go_to_login_page_from_product_page (browser):
    #Test of transition guest from product page to registration page
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    #Test of transition guest from product page to basket
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.product_in_basket_opened()
    page.should_not_be_product_in_bascet()
    page.should_be_emptay_basket_message()
    assert "empty" in browser.find_element(*BasePageLocators.CHECKING_TEXT).text, "No empty basket message"

@pytest.mark.usser_add_to_basket
class TestUserAddToBasketFromProductPage():
#Tests for authorized users
    @pytest.fixture(scope="function", autouse=True)
    
    def setup(self, browser):	
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = ProductPage(browser,link)
        page.open()
        email = str(int(time.time()))+"@hoolymail.org" #Generation email
        password = str(int(time.time()))+"qwerty" #Generation password
        LoginPage.register_new_user(browser, email, password) #Create new usser
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        yield
        page.deleted_usser(browser, password) #Deleted usser
		
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        #The test of adding an item to the basket is authorized by the user
        page = ProductPage(browser, self.link)
        page.open()
        page.add_product_to_basket()
        page.should_be_added_to_basket_message()
	
    def test_usser_cant_see_success_message(self, browser): 
        #We are looking for a message about the successful addition of the product to the basket
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

 
