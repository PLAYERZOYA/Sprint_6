
from locators.important_questions_locators import ImportantQuestionLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class ImportantQuestions:

    def __init__(self, driver):
        self.driver = driver

    def click_price_and_payment_question(self):
        heading_1 = self.driver.find_element(*ImportantQuestionLocators.price_and_payment)
        self.driver.execute_script("arguments[0].scrollIntoView();", heading_1)

        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(ImportantQuestionLocators.price_and_payment))
        heading_1.click()
    

        actually_result = self.driver.find_element(*ImportantQuestionLocators.price_and_payment_text).text
        expected_result = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

        return actually_result, expected_result


    def click_multiple_scooters_question(self):
        heading_2 = self.driver.find_element(*ImportantQuestionLocators.multiple_scooters)
        self.driver.execute_script("arguments[0].scrollIntoView();", heading_2)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(ImportantQuestionLocators.multiple_scooters))
        heading_2.click()

        actually_result = self.driver.find_element(*ImportantQuestionLocators.multiple_scooters_text).text
        expected_result = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        
        return actually_result, expected_result

    def click_rental_time_question(self):
        heading_3 = self.driver.find_element(*ImportantQuestionLocators.rental_time)
        self.driver.execute_script("arguments[0].scrollIntoView();", heading_3)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(ImportantQuestionLocators.rental_time))
        heading_3.click()

        actually_result = self.driver.find_element(*ImportantQuestionLocators.rental_time_text).text
        expected_result = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        
        return actually_result, expected_result
        
    def click_order_today_question(self):
        heading_4 = self.driver.find_element(*ImportantQuestionLocators.order_today)
        self.driver.execute_script("arguments[0].scrollIntoView();", heading_4)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(ImportantQuestionLocators.order_today))
        heading_4.click()

        actually_result = self.driver.find_element(*ImportantQuestionLocators.order_today_text).text
        expected_result = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        
        return actually_result, expected_result

    def click_extend_and_return_question(self):
        heading_5 = self.driver.find_element(*ImportantQuestionLocators.extend_and_return)
        self.driver.execute_script("arguments[0].scrollIntoView();", heading_5)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(ImportantQuestionLocators.extend_and_return))
        heading_5.click()

        actually_result = self.driver.find_element(*ImportantQuestionLocators.extend_and_return_text).text
        expected_result = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        
        return actually_result, expected_result


    def click_charging_question(self):
        heading_6 = self.driver.find_element(*ImportantQuestionLocators.charging)
        self.driver.execute_script("arguments[0].scrollIntoView();", heading_6)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(ImportantQuestionLocators.charging))
        heading_6.click()

        actually_result = self.driver.find_element(*ImportantQuestionLocators.charging_text).text
        expected_result = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        
        return actually_result, expected_result



    def click_order_cancellation_question(self):
        heading_7 = self.driver.find_element(*ImportantQuestionLocators.order_cancellation)
        self.driver.execute_script("arguments[0].scrollIntoView();", heading_7)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(ImportantQuestionLocators.order_cancellation))
        heading_7.click()

        actually_result = self.driver.find_element(*ImportantQuestionLocators.order_cancellation_text).text
        expected_result = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        
        return actually_result, expected_result


    def click_delivery_area_question(self):
        heading_8 = self.driver.find_element(*ImportantQuestionLocators.delivery_area)
        self.driver.execute_script("arguments[0].scrollIntoView();", heading_8)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(ImportantQuestionLocators.delivery_area))
        heading_8.click()

        actually_result = self.driver.find_element(*ImportantQuestionLocators.delivery_area_text).text
        expected_result = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        
        return actually_result, expected_result




   