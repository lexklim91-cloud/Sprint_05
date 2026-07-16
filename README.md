

Папка tests содержит 6 файлов:
conftest.py:

test_creating_an_ad.py - тесты на функциональность «Создание объявления»:
    test_create_ad_unauthorized_no_loginuser_error - создание обьявления без авторизации
    test_create_ad_authorized_loginuser_goodtest - создание обьявления с авторизации пользователя 

test_user_login.py - тесты на функциональность «Login пользователя»:
    test_login_account - авторизация Login пользователя


test_user_logout.py - тесты на функциональность «Login пользователя»:
    def test_logout_account - авторизация Login пользователя и выход

test_user_registration.py - тесты на функциональность «Регистрация пользователя»:
    test_regiatration_account - тестируеться регистрация пользователя
    
__init__.py - пустой файл используеться для превращения папки в модуль

Папка user_locators содержит 2 файла:

locators.py - локаторы элементов:
__init__.py - пустой файл используеться для превращения папки в модуль