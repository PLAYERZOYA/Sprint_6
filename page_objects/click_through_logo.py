from selenium.webdriver.common.by import By
import allure
from page_objects.base_page import BasePage
from data.urls import Urls


logo_scooter = [By.XPATH, "//img[@alt='Scooter']"]
logo_yandex = [By.XPATH, "//img[@alt='Yandex']"]

class ClickThroughLogo(BasePage):

    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Проверка перехода на главную страницу при нажатии на лого Самокат')
    def check_click_logo_scooter_open_home_page(self):

        self.wait_for_url_contains(Urls.main_page_url) 
        self.click_element(logo_scooter)
        
        current_url = self.get_current_url()
        expected_url = Urls.main_page_url 

        return current_url, expected_url 
    
    @allure.step('Проверка открытия нового окна с Дзеном при нажатии на лого Яндекс')
    @allure.description('Нажимаем на логотип Яндекс, получаем все открытые вкладки и переключаемся на последнюю, сравниваем ожидаемый url с текущим')
    def check_click_logo_yandex_open_dzen_home_page(self):

        self.click_element_with_wait_clickable(logo_yandex)

        self.switch_window()

        self.wait_for_url_contains('yredirect=true') 

        current_url = self.get_current_url()
        expected_url = Urls.dzen_url

        return current_url, expected_url 
    
