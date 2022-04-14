from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    
    def should_be_button_add_to_bin(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BIN_BUTTON), 'No button for adding to bin'
        
    def guest_can_add_product_to_bin(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BIN_BUTTON).click()
        self.solve_quiz_and_get_code()
        
    
             
        
   