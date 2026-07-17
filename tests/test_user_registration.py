
from user_locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 


class TestUserRegistration:
    
    def test_regiatration_account(self, generate_email, driver):

        driver.find_element(*Locators.LOGIN_REGISTER_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.no_account_button)))
        driver.find_element(*Locators.no_account_button).click()
        
        email = generate_email
        password = "klmkn"

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((Locators.input_email)))
        driver.find_element(*Locators.input_email).send_keys(email) 
        driver.find_element(*Locators.input_password).send_keys(password) 
        driver.find_element(*Locators.input_submitpassword).send_keys(password) 
        
        driver.find_element(*Locators.create_account_button).click()


        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((Locators.name_user)))
        name_user = driver.find_element(*Locators.name_user)
        assert "qa-desk.education-services.ru" in driver.current_url and "User." == name_user.text
        
    def test_bad_regiatration_account(self, driver):
        

        driver.find_element(*Locators.LOGIN_REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.no_account_button)))
        driver.find_element(*Locators.no_account_button).click()
    
        email = "Lex.Klimkin@ru"
        password = "123"

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((Locators.input_email)))
        driver.find_element(*Locators.input_email).send_keys(email) 
        driver.find_element(*Locators.input_password).send_keys(password) 
        driver.find_element(*Locators.input_submitpassword).send_keys(password) 

        driver.find_element(*Locators.create_account_button).click()
        

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((Locators.red_border_input)))
        red_border_input = driver.find_element(*Locators.red_border_input)
        error_input_registration = driver.find_element(*Locators.error_input_registration)
        assert "rgb(255, 105, 114)" in red_border_input.value_of_css_property("border") and "Ошибка"== error_input_registration.text
   