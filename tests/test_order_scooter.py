import pytest


from page_objects.personal_information_form_order_page import PersonalInformationOrderPage
from page_objects.rental_information_form_order_page import RentalInformationOrderPage
from page_objects.click_through_logo import ClickThroughLogo

from data.order_data import OrderData


class TestOrderScooter:
    
    @pytest.mark.parametrize("test_data", OrderData.UPPER_BUTTON_DATA)
    def test_full_order_flow_with_upper_order_button(self, driver, test_data):

        personal_data = test_data["personal"]
        rental_data = test_data["rental"]
        
        first_name, last_name, address, metro, phone = personal_data
        date, lease, color_name, comment = rental_data

        #инициализация страниц 
        personal_info_page = PersonalInformationOrderPage(driver)
        rental_info_page = RentalInformationOrderPage(driver)

         # Нажатие кнопки Заказать в хедере страницы
        personal_info_page.click_order_button_in_header()
        
        # Шаг 1: Заполнение личной информации
        personal_info_page.fill_personal_information_form(first_name, last_name, address, metro, phone)
        
        # Шаг 2: Заполнение информации об аренде
        rental_info_page.fill_rental_information(date, lease, color_name, comment)

        
        # Проверка окна создания заказа
        rental_info_page.check_order_created_window()

        # Проверка успешного создания заказа
        rental_info_page.check_order_created_successful()
        

    @pytest.mark.parametrize("test_data", OrderData.LOWER_BUTTON_DATA)

    def test_full_order_flow_with_lower_order_button(self, driver, test_data):

        # Распаковываем личные данные
        personal_data = test_data["personal"]
        rental_data = test_data["rental"]
        first_name, last_name, address, metro, phone = personal_data
        date, lease, color_name, comment = rental_data

        #инициализация страниц с переданным драйвером
        personal_info_page = PersonalInformationOrderPage(driver)
        rental_info_page = RentalInformationOrderPage(driver)

         # Нажатие кнопки Заказать внизу страницы
        personal_info_page.click_order_button()
        
        # Шаг 1: Заполнение личной информации
        personal_info_page.fill_personal_information_form(first_name, last_name, address, metro, phone)
        
        # Шаг 2: Заполнение информации об аренде
        date, lease, color_name, comment = rental_data
        rental_info_page.fill_rental_information(date, lease, color_name, comment)
        
        # Проверка окна создания заказа
        rental_info_page.check_order_created_window()

        # Проверка успешного создания заказа
        rental_info_page.check_order_created_successful()


        
    # Проверка логотипа Самокат
def test_check_click_logo_scooter_open_home_page(driver):
    logo_page = ClickThroughLogo(driver)
    current_url, expected_url = logo_page.check_click_logo_scooter_open_home_page()
    assert current_url == expected_url

# Проверка логотипа Яндекс
def test_check_click_logo_yandex_open_dzen_home_page(driver):
    logo_page = ClickThroughLogo(driver)
    current_url, expected_url = logo_page.check_click_logo_yandex_open_dzen_home_page()
    assert current_url == expected_url