import allure
from locators.locators_question_page import LocatorsQuestionPage
from pages.base_page import BasePage


class PageQuestions(BasePage):
    @allure.description('Кликаем на вопрос')
    def open_question_get_an_answer(self, index):
        self.open()
        self.scroll_to_element()
        self.element_is_visible(LocatorsQuestionPage.QUESTIONS)
        button_accordions = self.find_elements(LocatorsQuestionPage.QUESTION)[index]
        button_accordions.click()
        self.element_is_visible(LocatorsQuestionPage.QUESTIONS)
        self.element_is_visible(LocatorsQuestionPage.QUESTION)

