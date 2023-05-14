from locators.locators_question_page import LocatorsQuestionPage
from pages.base_page import BasePage


class PageQuestions(BasePage):
    def question_price(self):
        return self.driver.find_element(*LocatorsQuestionPage.PRICE)

    def question_multiple_scooter(self):
        return self.driver.find_element(*LocatorsQuestionPage.MULTIPLE_SCOOTER)

    def question_rental_time(self):
        return self.driver.find_element(*LocatorsQuestionPage.RENTAL_TIME)

    def question_order_today(self):
        return self.driver.find_element(*LocatorsQuestionPage.ORDER_TODAY)

    def question_renew_order(self):
        return self.driver.find_element(*LocatorsQuestionPage.RENEW_ORDER)

    def question_charger(self):
        return self.driver.find_element(*LocatorsQuestionPage.CHARGER)

    def question_cancel_order(self):
        return self.driver.find_element(*LocatorsQuestionPage.CANCEL_ORDER)

    def question_delivery_area(self):
        return self.driver.find_element(*LocatorsQuestionPage.DELIVERY_AREA)

    def click_question_price(self):
        self.question_price().click()

    def click_question_multiple_scooter(self):
        self.question_multiple_scooter().click()

    def click_question_rental_time(self):
        self.question_rental_time().click()

    def click_question_order_today(self):
        self.question_order_today().click()

    def click_question_renew_order(self):
        self.question_renew_order().click()

    def click_question_charger(self):
        self.question_charger().click()

    def click_question_cancel_order(self):
        self.question_cancel_order().click()

    def click_question_delivery_area(self):
        self.question_delivery_area().click()

    def scroll_to_element(self):
        element = self.driver.find_element(*LocatorsQuestionPage.PRICE)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def open_question_price_get_an_answer(self):
        self.open()
        self.scroll_to_element()
        self.element_is_visible(LocatorsQuestionPage.TEXT_PRICE)
        self.click_question_price()
        self.element_is_visible(LocatorsQuestionPage.PRICE_DROP_LIST)
        element = self.driver.find_element(*LocatorsQuestionPage.TEXT_PRICE_DROP_LIST)
        assert element.text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    def open_question_multiple_scooter_get_an_answer(self):
        self.open()
        self.scroll_to_element()
        self.element_is_visible(LocatorsQuestionPage.TEXT_PRICE)
        self.click_question_multiple_scooter()
        self.element_is_visible(LocatorsQuestionPage.MULTIPLE_SCOOTER_DROP_LIST)
        element = self.driver.find_element(*LocatorsQuestionPage.TEXT_MULTIPLE_SCOOTER_DROP_LIST)
        assert element.text == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, " \
                               "можете просто сделать несколько заказов — один за другим."

    def open_question_rental_time_get_an_answer(self):
        self.open()
        self.scroll_to_element()
        self.element_is_visible(LocatorsQuestionPage.TEXT_PRICE)
        self.click_question_rental_time()
        self.element_is_visible(LocatorsQuestionPage.RENTAL_TIME_DROP_LIST)
        element = self.driver.find_element(*LocatorsQuestionPage.TEXT_RENTAL_TIME_DROP_LIST)
        assert element.text == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. " \
                               "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы " \
                               "привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    def open_question_order_today_get_an_answer(self):
        self.open()
        self.scroll_to_element()
        self.element_is_visible(LocatorsQuestionPage.TEXT_PRICE)
        self.click_question_order_today()
        self.element_is_visible(LocatorsQuestionPage.ORDER_TODAY_DROP_LIST)
        element = self.driver.find_element(*LocatorsQuestionPage.TEXT_ORDER_TODAY_DROP_LIST)
        assert element.text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    def open_question_renew_order_get_an_answer(self):
        self.open()
        self.scroll_to_element()
        self.element_is_visible(LocatorsQuestionPage.TEXT_PRICE)
        self.click_question_renew_order()
        self.element_is_visible(LocatorsQuestionPage.RENEW_ORDER_DROP_LIST)
        element = self.driver.find_element(*LocatorsQuestionPage.TEXT_RENEW_ORDER_DROP_LIST)
        assert element.text == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по " \
                               "красивому номеру 1010."

    def open_question_charger_get_an_answer(self):
        self.open()
        self.scroll_to_element()
        self.element_is_visible(LocatorsQuestionPage.TEXT_PRICE)
        self.click_question_charger()
        self.element_is_visible(LocatorsQuestionPage.CHARGER_DROP_LIST)
        element = self.driver.find_element(*LocatorsQuestionPage.TEXT_CHARGER_DROP_LIST)
        assert element.text == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если " \
                               "будете кататься без передышек и во сне. Зарядка не понадобится."

    def open_question_cancel_order_get_an_answer(self):
        self.open()
        self.scroll_to_element()
        self.element_is_visible(LocatorsQuestionPage.TEXT_PRICE)
        self.click_question_cancel_order()
        self.element_is_visible(LocatorsQuestionPage.CANCEL_ORDER_DROP_LIST)
        element = self.driver.find_element(*LocatorsQuestionPage.TEXT_CANCEL_ORDER_DROP_LIST)
        assert element.text == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не " \
                               "попросим. Все же свои."

    def open_question_delivery_area_get_an_answer(self):
        self.open()
        self.scroll_to_element()
        self.element_is_visible(LocatorsQuestionPage.TEXT_PRICE)
        self.click_question_delivery_area()
        self.element_is_visible(LocatorsQuestionPage.DELIVERY_AREA_DROP_LIST)
        element = self.driver.find_element(*LocatorsQuestionPage.TEXT_DELIVERY_AREA_DROP_LIST)
        assert element.text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
