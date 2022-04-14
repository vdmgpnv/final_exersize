from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ALL_PRODUCTS_BUTTON = (By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a')
    FIRST_BOOK_ELEMENT = (By.XPATH, '//*[@id="default"]/div[2]/div/div/div/section/div/ol/li[1]/article/h3/a')
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    
class ProductPageLocators():
    ADD_TO_BIN_BUTTON = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    