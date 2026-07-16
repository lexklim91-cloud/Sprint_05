
from user_locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 


class TestUserLogout:

    def test_logout_account(self, driver):

        driver.find_element(*Locators.LOGIN_REGISTER_BUTTON).click()
        
        email = "klmn@mail.ru"
        password = "klmkn"
        
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((Locators.input_email)))
        driver.find_element(*Locators.input_email).send_keys(email) 
        driver.find_element(*Locators.input_password).send_keys(password) 
                
        driver.find_element(*Locators.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.logout_button)))
        driver.find_element(*Locators.logout_button).click()        
        
        WebDriverWait(driver, 2).until(expected_conditions.invisibility_of_element_located((Locators.user_name_and_avatar)))
        user_name_and_avatar = driver.find_elements(*Locators.user_name_and_avatar)
        assert len(user_name_and_avatar) == 0