from pages.question_page import PageQuestions


class TestQuestionsPage:
    def test_open_question_price_get_an_answer(self, driver, url_home_page):
        page = PageQuestions(driver, url_home_page)
        page.open_question_price_get_an_answer()

    def test_open_question_multiple_scooter_get_an_answer(self, driver, url_home_page):
        page = PageQuestions(driver, url_home_page)
        page.open_question_multiple_scooter_get_an_answer()

    def test_open_question_rental_time_get_an_answer(self, driver, url_home_page):
        page = PageQuestions(driver, url_home_page)
        page.open_question_rental_time_get_an_answer()

    def test_open_question_order_today_get_an_answer(self, driver, url_home_page):
        page = PageQuestions(driver, url_home_page)
        page.open_question_order_today_get_an_answer()

    def test_open_question_renew_order_get_an_answer(self, driver, url_home_page):
        page = PageQuestions(driver, url_home_page)
        page.open_question_renew_order_get_an_answer()

    def test_open_question_charger_get_an_answer(self, driver, url_home_page):
        page = PageQuestions(driver, url_home_page)
        page.open_question_charger_get_an_answer()

    def test_open_question_cancel_order_get_an_answer(self, driver, url_home_page):
        page = PageQuestions(driver, url_home_page)
        page.open_question_cancel_order_get_an_answer()

    def test_open_question_delivery_area_get_an_answer(self, driver, url_home_page):
        page = PageQuestions(driver, url_home_page)
        page.open_question_delivery_area_get_an_answer()
