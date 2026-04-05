from selenium import webdriver
from page_objects.important_questions_page import ImportantQuestions



class TestImportantQuestions:
    driver = None 


    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        cls.important_questions = ImportantQuestions(cls.driver) 

    def test_price_and_payment_text_match(self):     
        actual_result, expected_result = self.important_questions.click_price_and_payment_question()

        assert actual_result == expected_result


    def test_multiple_scooters_text_match(self):       
        actual_result, expected_result = self.important_questions.click_multiple_scooters_question()

        assert actual_result == expected_result

    def test_rental_time_text_match(self):
        actual_result, expected_result = self.important_questions.click_rental_time_question()

        assert actual_result == expected_result

    def test_order_today_text_match(self):
        actual_result, expected_result = self.important_questions.click_order_today_question()

        assert actual_result == expected_result

    def test_extend_and_return_text_match(self):
        actual_result, expected_result = self.important_questions.click_extend_and_return_question()

        assert actual_result == expected_result


    def test_charging_text_match(self):
        actual_result, expected_result = self.important_questions.click_charging_question()

        assert actual_result == expected_result



    def test_order_cancellation_text_match(self):
        actual_result, expected_result = self.important_questions.click_order_cancellation_question()

        assert actual_result == expected_result


    def test_delivery_area_text_match(self):
        actual_result, expected_result = self.important_questions.click_delivery_area_question()

        assert actual_result == expected_result


    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 