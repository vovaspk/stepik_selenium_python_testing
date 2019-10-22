from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math

class BasePage():
    
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)	
        
    def open(self):
        self.browser.get(self.url)	
	
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        return True
	
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
			
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
		
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((*ProductPageLocators.PRODUCT_ADDED)))
        except TimeoutException:
            return False
        return True
			
    def go_to_login_page(self):
        print("Find login link")
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        print("Clicked login link")
        login_link.click()
        
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
		
    def product_in_basket_opened(self):
        view_basket_button = self.browser.find_element(*BasePageLocators.VIEW_BASKET)
        view_basket_button.click()
		
    def should_not_be_product_in_bascet(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_ADDED), "Product in basket"	

    def should_be_emptay_basket_message(self):
        assert self.is_element_present(*BasePageLocators.CHECKING_TEXT), "Not \"Your basket is now empty\"message" 

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"
	
