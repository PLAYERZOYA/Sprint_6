from selenium.webdriver.common.by import By

class OrderScooterLocators:

    order_button_in_header = [By.CLASS_NAME, 'Button_Button__ra12g']
    order_button =[By.CLASS_NAME, 'Button_Button__ra12g']

    first_name_field = [By.XPATH, "//input[@placeholder='* Имя']"]
    last_name_field = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address_field = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]

    metro_station_field = [By.XPATH, "//input[@placeholder='* Станция метро']"]


    phone_number_field = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]

    next_button = [By.XPATH, "//button[text()='Далее']"]

    date_field = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    lease_field = [By.CLASS_NAME, "Dropdown-arrow"]

    color_locators = {
    'black': [By.XPATH, '//label[@for="black"]'],
    'grey': [By.XPATH, '//label[@for="grey"]']
    }

    comment_field = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    order_button_2 = [By.CSS_SELECTOR, ".Order_Buttons__1xGrp button:last-child"]

    confirm_button = [By.XPATH, '//button[text()="Да"]']

    order_created_window = [By.CLASS_NAME, "Order_Text__2broi"]
    status_button = [By.XPATH, '//button[text()="Посмотреть статус"]']
    track_order_info = [By.CLASS_NAME, 'Track_OrderInfo__2fpDL']


    logo_scooter = [By.XPATH, "//img[@alt='Scooter']"]
    logo_yandex = [By.XPATH, "//img[@alt='Yandex']"]