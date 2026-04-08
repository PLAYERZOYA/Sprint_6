import pytest
from page_objects.important_questions_page import ImportantQuestions



class TestImportantQuestions:

    @pytest.mark.parametrize("method", [
        ImportantQuestions.click_price_and_payment_question,
        ImportantQuestions.click_multiple_scooters_question,
        ImportantQuestions.click_rental_time_question,
        ImportantQuestions.click_order_today_question,
        ImportantQuestions.click_extend_and_return_question,
        ImportantQuestions.click_charging_question,
        ImportantQuestions.click_order_cancellation_question,
        ImportantQuestions.click_delivery_area_question,
    ])
    def test_question_text_match(self, driver, method):
        important_questions = ImportantQuestions(driver)
        actual_result, expected_result = method(important_questions)  # передаем экземпляр
        assert actual_result == expected_result

   
