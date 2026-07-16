
from selenium.webdriver.common.by import By
from user_locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 


class TestsCreatingAnAd:
    
    def test_create_ad_unauthorized_no_loginuser_error(self, driver):
        driver.find_element(*Locators.post_an_ad).click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((Locators.error_create_ad_unauthorized)))
        text_error = driver.find_element(*Locators.error_create_ad_unauthorized).text
        assert "Чтобы разместить объявление, авторизуйтесь" == text_error
        
    
    def test_create_ad_authorized_loginuser_goodtest(self, driver):

      driver.find_element(*Locators.LOGIN_REGISTER_BUTTON).click()    
      email = "klmn@mail.ru"
      password = "klmkn"

      WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((Locators.input_email)))
      driver.find_element(*Locators.input_email).send_keys(email) 
      driver.find_element(*Locators.input_password).send_keys(password)                 
        
      driver.find_element(*Locators.login_button).click()

      WebDriverWait(driver, 1).until(expected_conditions.element_to_be_clickable((Locators.user_name_and_avatar)))
      driver.find_element(*Locators.post_an_ad).click()
      
      driver.find_element(*Locators.ad_name_input).send_keys("Mercedes-Benz sprinter classic 311 cdi 2003 г.в.")
      driver.find_element(*Locators.ad_description_input).send_keys("Продам Mercedes-Benz sprinter")
      driver.find_element(*Locators.price).send_keys(500000)

      driver.find_element(*Locators.ad_condition_radio).click()

      driver.find_element(*Locators.ad_category_dropdown).click()
      driver.find_element(*Locators.category).click() 
 
      driver.find_element(*Locators.ad_city_dropdown).click()
      city = driver.find_element(*Locators.city).click()
        
      driver.find_element(*Locators.publish_buttom).click()

      WebDriverWait(driver, 2).until(expected_conditions.invisibility_of_element_located((Locators.publish_buttom)))
      driver.find_element(By.CSS_SELECTOR, "button.circleSmall").click()
      assert driver.find_elements(By.CLASS_NAME, "card") != 0
      driver.quit()
