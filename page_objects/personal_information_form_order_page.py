
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators.order_scooter_locators import OrderScooterLocators
import allure


class PersonalInformationOrderPage:

    def __init__(self, driver):
        self.driver = driver
        
    @allure.step('Клик по кнопке Заказать внизу страницы')
    def click_order_button(self):

        button = self.driver.find_element(*OrderScooterLocators.order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/order"))

    @allure.step('Клик по кнопке Заказать в хедере страницы')
    def click_order_button_in_header(self):
        self.driver.find_element(*OrderScooterLocators.order_button_in_header).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/order"))

    @allure.step('Ввод имени в поле Имя')
    def fill_first_name_field(self, first_name):
        self.driver.find_element(*OrderScooterLocators.first_name_field).send_keys(first_name)

    @allure.step('Ввод фамилии в поле Фамилия')
    def fill_last_name_field(self, last_name):
        self.driver.find_element(*OrderScooterLocators.last_name_field).send_keys(last_name)

    @allure.step('Ввод адреса в поле Адрес')
    def fill_address_field(self, address):
        self.driver.find_element(*OrderScooterLocators.address_field).send_keys(address)

    @allure.step('Выбор станции метро')
    @allure.description('На странице ищем выпадающий список станций метро и из него выбираем нужное значение')
    def select_metro_station(self, station_name):
        self.driver.find_element(*OrderScooterLocators.metro_station_field).click()

        station = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, f"//div[text()='{station_name}']")))
        station.click()

    @allure.step('Ввод номера телефона в поле Телефон')
    def fill_phone_number_field(self, phone):
        self.driver.find_element(*OrderScooterLocators.phone_number_field).send_keys(phone)


    @allure.step('Клик по кнопке Далее')
    def click_next_button(self):
        self.driver.find_element(*OrderScooterLocators.next_button).click()

    @allure.title('Заполнение формы персональных данных при заказе самоката')
    def fill_personal_information_form(self, first_name, last_name, address, metro, phone):
        self.fill_first_name_field(first_name)
        self.fill_last_name_field(last_name)
        self.fill_address_field(address)
        self.select_metro_station(metro) 
        self.fill_phone_number_field(phone)
        self.click_next_button()
    