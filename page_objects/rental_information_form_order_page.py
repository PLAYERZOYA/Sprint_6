

from selenium.webdriver.common.by import By
from locators.order_scooter_locators import OrderScooterLocators

import allure
from page_objects.base_page import BasePage
from data.urls import Urls


class RentalInformationOrderPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Выбор даты в поле Когда привезти самокат')
    def fill_date_field(self, date):
        self.fill_field(OrderScooterLocators.date_field, date)

    @allure.step('Выбор срока аренды')
    @allure.description('На странице ищем выпадающий список, нажимаем на него и выбираем количество дней аренды')
    def fill_lease_field(self, lease):
        self.click_element_with_wait_clickable(OrderScooterLocators.lease_field)
        self.click_element_with_wait_clickable([By.XPATH, f"//div[@class='Dropdown-option' and text()='{lease}']"])
  

    @allure.step('Выбор цвета самоката')
    @allure.description('Выбираем цвет и ставим галочку в нужном чекбоксе')
    def select_color(self, color_name):
        self.click_element_with_wait_clickable(OrderScooterLocators.color_locators[color_name])


    @allure.step('Опциональный комментарий')
    def fill_comment_field(self, comment=''):
        self.fill_field(OrderScooterLocators.comment_field, comment)


    @allure.step('Клик по кнопке Заказать')
    def click_order_button_2(self):
        self.click_element(OrderScooterLocators.order_button_2)

    @allure.step('Клик по кнопке согласия с заказом')
    def click_confirm_button(self):
        self.click_element_with_wait_clickable(OrderScooterLocators.confirm_button)


    @allure.step('Проверка успешного создания заказа')
    def check_order_created_window(self):
        self.wait_for_element_visible(OrderScooterLocators.order_created_window)
        self.wait_for_element_clickable(OrderScooterLocators.status_button)
        self.click_element(OrderScooterLocators.status_button)



    @allure.step('Проверка успешного создания заказа')
    def check_order_created_successful(self):
        self.wait_for_url_contains(Urls.url_track)
        self.wait_for_element_visible(OrderScooterLocators.track_order_info)


        
    @allure.title('Заполнение формы данных по аренде при заказе самоката')
    def fill_rental_information(self, date, lease, color_name, comment):
        self.fill_date_field(date)
        self.fill_lease_field(lease)
        self.select_color(color_name)
        self.fill_comment_field(comment)
        self.click_order_button_2()
        self.click_confirm_button()
  

    