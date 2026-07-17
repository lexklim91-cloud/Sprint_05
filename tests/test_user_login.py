
from selenium.webdriver.common.by import By
from user_locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 

class TestUserLogin:
        
    def test_login_account(self, driver):
 
        driver.get("https://qa-desk.education-services.ru")
        driver.find_element(*Locators.LOGIN_REGISTER_BUTTON).click()
    
        email = "klmn@mail.ru"
        password = "klmkn"
        
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((Locators.input_email)))
        driver.find_element(*Locators.input_email).send_keys(email) 
        driver.find_element(*Locators.input_password).send_keys(password) 
               
        driver.find_element(*Locators.login_button).click() # кнопка "Войти" 
        
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((Locators.user_name_and_avatar)))
        elements = driver.find_elements(*Locators.user_name_and_avatar)
        assert len(elements) == 1


