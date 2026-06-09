
from selenium.webdriver.common.by import By
from locators.order_scooter_locators import OrderScooterLocators
import allure
from page_objects.base_page import BasePage
from data.urls import Urls


class PersonalInformationOrderPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        
    @allure.step('Клик по кнопке Заказать внизу страницы')
    def click_order_button(self):

        self.scroll_into_view(OrderScooterLocators.order_button)
        self.click_element(OrderScooterLocators.order_button)
        self.wait_for_url_contains(Urls.order_page_url)
     
    @allure.step('Клик по кнопке Заказать в хедере страницы')
    def click_order_button_in_header(self):
        self.click_element(OrderScooterLocators.order_button_in_header)
        self.wait_for_url_contains(Urls.order_page_url)

    @allure.step('Ввод имени в поле Имя')
    def fill_first_name_field(self, first_name):
        self.fill_field(OrderScooterLocators.first_name_field, first_name)

    @allure.step('Ввод фамилии в поле Фамилия')
    def fill_last_name_field(self, last_name):
        self.fill_field(OrderScooterLocators.last_name_field, last_name)

    @allure.step('Ввод адреса в поле Адрес')
    def fill_address_field(self, address):
        self.fill_field(OrderScooterLocators.address_field, address)

    @allure.step('Выбор станции метро')
    @allure.description('На странице ищем выпадающий список станций метро и из него выбираем нужное значение')
    def select_metro_station(self, station_name):
        self.click_element(OrderScooterLocators.metro_station_field)

        self.click_element_with_wait_clickable([By.XPATH, f"//div[text()='{station_name}']"])

    @allure.step('Ввод номера телефона в поле Телефон')
    def fill_phone_number_field(self, phone):

        self.fill_field(OrderScooterLocators.phone_number_field, phone)

    @allure.step('Клик по кнопке Далее')
    def click_next_button(self):
        self.click_element(OrderScooterLocators.next_button)

    @allure.title('Заполнение формы персональных данных при заказе самоката')
    def fill_personal_information_form(self, first_name, last_name, address, metro, phone):
        self.fill_first_name_field(first_name)
        self.fill_last_name_field(last_name)
        self.fill_address_field(address)
        self.select_metro_station(metro) 
        self.fill_phone_number_field(phone)
        self.click_next_button()
    