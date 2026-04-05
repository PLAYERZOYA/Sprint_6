from selenium.webdriver.common.by import By

class ImportantQuestionLocators:

    price_and_payment = [By.CLASS_NAME, "accordion__heading-0"] # кнопка Сколько это стоит и как оплатить
    price_and_payment_text = [By.XPATH, "//p[contains(text(), '400 рублей')]"]

    multiple_scooters = [By.ID, "accordion__heading-1"] # кнопка Хочу сразу несколько самокатов
    multiple_scooters_text = [By.XPATH, "//p[contains(text(), 'один заказ — один самокат')]"]


    rental_time = [By.ID, 'accordion__heading-2'] # кнопка как рассчитывается время аренды
    rental_time_text = [By.XPATH, "//p[contains(text(), 'Допустим, вы оформляете заказ на 8 мая.')]"]


    order_today = [By.ID, 'accordion__heading-3'] # кнопка Можно ли заказать самокат на сегодня
    order_today_text = [By.XPATH, "//p[contains(text(), 'Только начиная с завтрашнего дня.')]"]


    extend_and_return = [By.ID, 'accordion__heading-4'] # кнопка Можно ли продлить заказ и вернуть самокат раньше
    extend_and_return_text = [By.XPATH, "//p[contains(text(), 'Пока что нет!')]"]


    charging = [By.ID, 'accordion__heading-5'] # кнопка Вы привозите зарядку вместе с самокатом
    charging_text = [By.XPATH, "//p[contains(text(), 'Зарядка не понадобится.')]"]


    order_cancellation = [By.ID, 'accordion__heading-6'] # кнопка Можно ли отменить заказ
    order_cancellation_text = [By.XPATH, "//p[contains(text(), 'Да, пока самокат не привезли.')]"]


    delivery_area = [By.ID, 'accordion__heading-7'] # кнопка Я живу за МКАДом
    delivery_area_text = [By.XPATH, "//p[contains(text(), 'Всем самокатов!')]"]
