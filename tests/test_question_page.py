import allure
import pytest
from locators.locators_question_page import LocatorsQuestionPage
from data import QuestionsAnswers
from pages.question_page import PageQuestions


class TestQuestionsPage:
    @allure.title('Проверяем, клик по вопросу, открывает ответ')
    @pytest.mark.parametrize('index', [i for i in range(8)])
    def test_click_on_question_and_check_answer(self, driver, url_home_page, index):
        page = PageQuestions(driver, url_home_page)
        page.open_question_get_an_answer(index)
        actual_result = page.find_elements(LocatorsQuestionPage.ANSWER)[index].text
        expected_result = QuestionsAnswers.questions_and_answers[page.find_elements(LocatorsQuestionPage.QUESTION)
                                                                 [index].text]
        assert actual_result == expected_result
