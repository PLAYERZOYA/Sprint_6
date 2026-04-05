from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import allure


logo_scooter = [By.XPATH, "//img[@alt='Scooter']"]
logo_yandex = [By.XPATH, "//img[@alt='Yandex']"]

class ClickThroughLogo:

    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Проверка перехода на главную страницу при нажатии на лого Самокат')
    def check_click_logo_scooter_open_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_contains("https://qa-scooter.praktikum-services.ru/track"))
        self.driver.find_element(*logo_scooter).click()
        current_url = self.driver.current_url
        expected_url = "https://qa-scooter.praktikum-services.ru/"
        return current_url, expected_url 
    
    @allure.step('Проверка открытия нового окна с Дзеном при нажатии на лого Яндекс')
    @allure.description('Нажимаем на логотип Яндекс, получаем все открытые вкладки и переключаемся на последнюю, сравниваем ожидаемый url с текущим')
    def check_click_logo_yandex_open_dzen_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(logo_yandex))
        self.driver.find_element(*logo_yandex).click()

        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('yredirect=true'))
        current_url = self.driver.current_url
        expected_url = "https://dzen.ru/?yredirect=true"
        return current_url, expected_url 
    
