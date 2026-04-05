
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators.order_scooter_locators import OrderScooterLocators

import allure

class RentalInformationOrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Выбор даты в поле Когда привезти самокат')
    def fill_date_field(self, date):
        self.driver.find_element(*OrderScooterLocators.date_field).send_keys(date)

    @allure.step('Выбор срока аренды')
    @allure.description('На странице ищем выпадающий список, нажимаем на него и выбираем количество дней аренды')
    def fill_lease_field(self, lease):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((OrderScooterLocators.lease_field)))

        self.driver.find_element(*OrderScooterLocators.lease_field).click()
  
        lease_field = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, f"//div[@class='Dropdown-option' and text()='{lease}']")))
        lease_field.click()

    @allure.step('Выбор цвета самоката')
    @allure.description('Выбираем цвет и ставим галочку в нужном чекбоксе')
    def select_color(self, color_name):
        color_checkbox = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(OrderScooterLocators.color_locators[color_name]))
        color_checkbox.click()

    @allure.step('Опциональный комментарий')
    def fill_comment_field(self, comment=''):
        self.driver.find_element(*OrderScooterLocators.comment_field).send_keys(comment)

    @allure.step('Клик по кнопке Заказать')
    def click_order_button_2(self):
        self.driver.find_element(*OrderScooterLocators.order_button_2).click()

    @allure.step('Клик по кнопке согласия с заказом')
    def click_confirm_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(OrderScooterLocators.confirm_button)).click()

    @allure.step('Проверка окна создания заказа')
    def check_order_created_window(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderScooterLocators.order_created_window))
        self.driver.find_element(*OrderScooterLocators.status_button).click()

        
    @allure.title('Заполнение формы данных по аренде при заказе самоката')
    def fill_rental_information(self, date, lease, color_name, comment):
        self.fill_date_field(date)
        self.fill_lease_field(lease)
        self.select_color(color_name)
        self.fill_comment_field(comment)
        self.click_order_button_2()
        self.click_confirm_button()


    