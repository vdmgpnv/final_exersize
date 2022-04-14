from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        
    def should_be_button_all_products(self):
        assert self.is_element_present(*MainPageLocators.ALL_PRODUCTS_BUTTON), "All products button is not presented"
        
    def go_to_all_products(self):
        self.browser.find_element(*MainPageLocators.ALL_PRODUCTS_BUTTON).click()
        
    def open_product_page(self):
        self.browser.find_element(*MainPageLocators.FIRST_BOOK_ELEMENT).click()
        
    