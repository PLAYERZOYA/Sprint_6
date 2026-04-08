
from locators.important_questions_locators import ImportantQuestionLocators
from page_objects.base_page import BasePage
import allure


class ImportantQuestions(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def check_question_answer(self, question_locator, answer_locator, expected_text):

        self.scroll_into_view(question_locator)
        self.wait_for_element_visible(question_locator)
        self.click_element_with_wait_clickable(question_locator)
        actual_text = self.return_text_of_element(answer_locator)
        return actual_text, expected_text
    
    @allure.step('Клик по вопросу "Сколько это стоит? И как оплатить?" и проверка ответа')
    def click_price_and_payment_question(self):
        return self.check_question_answer(
            ImportantQuestionLocators.price_and_payment,
            ImportantQuestionLocators.price_and_payment_text,
            'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        )

    @allure.step('Клик по вопросу "Хочу сразу несколько самокатов! Так можно?" и проверка ответа')
    def click_multiple_scooters_question(self):
        return self.check_question_answer(
            ImportantQuestionLocators.multiple_scooters,
            ImportantQuestionLocators.multiple_scooters_text,
            'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        )

    @allure.step('Клик по вопросу "Как рассчитывается время аренды?" и проверка ответа')
    def click_rental_time_question(self):
        return self.check_question_answer(
            ImportantQuestionLocators.rental_time,
            ImportantQuestionLocators.rental_time_text,
            'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        )

    @allure.step('Клик по вопросу "Можно ли заказать самокат прямо сегодня?" и проверка ответа')
    def click_order_today_question(self):
        return self.check_question_answer(
            ImportantQuestionLocators.order_today,
            ImportantQuestionLocators.order_today_text,
            'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        )

    @allure.step('Клик по вопросу "Можно ли продлить заказ или вернуть самокат?" и проверка ответа')
    def click_extend_and_return_question(self):
        return self.check_question_answer(
            ImportantQuestionLocators.extend_and_return,
            ImportantQuestionLocators.extend_and_return_text,
            'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        )

    @allure.step('Клик по вопросу "А привезут ли самокат с полной зарядкой?" и проверка ответа')
    def click_charging_question(self):
        return self.check_question_answer(
            ImportantQuestionLocators.charging,
            ImportantQuestionLocators.charging_text,
            'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        )
    
    @allure.step('Клик по вопросу "Отменяют ли заказ, если на самокат приехать не успели?" и проверка ответа')
    def click_order_cancellation_question(self):
        return self.check_question_answer(
            ImportantQuestionLocators.order_cancellation,
            ImportantQuestionLocators.order_cancellation_text,
            'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        )

    @allure.step('Клик по вопросу "Привезут ли самокат за МКАД?" и проверка ответа')
    def click_delivery_area_question(self):
        return self.check_question_answer(
            ImportantQuestionLocators.delivery_area,
            ImportantQuestionLocators.delivery_area_text,
            'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        )




   