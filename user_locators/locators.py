from selenium.webdriver.common.by import By

class Locators:

    # Кнопки
    LOGIN_REGISTER_BUTTON = (By.CSS_SELECTOR, "button.buttonSecondary")# кнопка "Вход и регистрация" 
    no_account_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/form/div[3]/button[2]")# кнопка "Нет аккаунта"
    create_account_button = (By.CSS_SELECTOR, "form .buttonPrimary")# кнопка "Создать аккаунт" 
    login_button = (By.CSS_SELECTOR, "form .buttonPrimary")# кнопка "Войти" 
    logout_button = (By.CSS_SELECTOR, ".btnSmall")# кнопка "Выйти" 
    post_an_ad = (By.CSS_SELECTOR, "button.buttonPrimary") # кнопка "Разместить объявление" 
    publish_buttom = (By.CSS_SELECTOR, "form .buttonPrimary") # кнопка "Опублиуовать" 


    # Поля формы регистрации
    input_email = (By.NAME, "email") 
    input_password = (By.NAME, "password")
    input_submitpassword = (By.NAME, "submitPassword")

    
    user_name_and_avatar = (By.CSS_SELECTOR, ".circleSmall")
    name_user = (By.XPATH, "//*[@id='root']/div/div[1]/div/div[1]/div/h3")
    
    
    # Сообщения об ошибках
    red_border_input = (By.CSS_SELECTOR, "form .input_inputError__fLUP9")# "Красный бордюр" 
    error_input_registration = (By.CSS_SELECTOR, ".input_span__yWPqB") # "Ошибка ввода"
    error_create_ad_unauthorized = (By.CSS_SELECTOR, '.h1') # "Чтобы разместить объявление, авторизуйтесь"


    form_add_post = (By.CSS_SELECTOR, ".createListing")
    
    ad_name_input = (By.NAME, "name") #«Название»
    ad_description_input = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/textarea") # "Описание товара" 
    price = (By.NAME, "price") #«Стоимость» 
    ad_category_dropdown  =  (By.XPATH, "/html/body/div/div/div[2]/div/form/div[2]/div[2]/div[1]/button") # "Категорию" 
    ad_city_dropdown = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div[2]/button[1]") # "Город"
    ad_condition_radio = (By.CSS_SELECTOR, ".radioUnput_inputRegular__FbVbr")
    
    
    category = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[3]/div[1]/button")
    city = (By.XPATH, f"//*[@id='root']/div/div[2]/div/form/div[3]/div[2]/button[5]")
  