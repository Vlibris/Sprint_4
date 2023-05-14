from locators.locators_order_form_page import LocatorsOrderForm
from pages.order_form_page import PageForm


class TestOrderForms:
    def test_checkout_button_order_top_positive_result(self, driver, url_home_page):
        page = PageForm(driver, url_home_page)
        page.open_form_button_order_top()
        page.fill_form_fields_for_whom_scooter_data_one_positive_result()
        page.fill_rental_form_data_one_positive_result()
        page.checkout()
        assert driver.find_element(*LocatorsOrderForm.BUTTON_VIEW_STATUS).text == 'Посмотреть статус'

    def test_checkout_button_order_bottom_positive_result(self, driver, url_home_page):
        page = PageForm(driver, url_home_page)
        page.open_form_button_order_bottom()
        page.fill_form_fields_for_whom_scooter_data_two_positive_result()
        page.fill_rental_form_data_two_positive_result()
        page.checkout()
        assert driver.find_element(*LocatorsOrderForm.BUTTON_VIEW_STATUS).text == 'Посмотреть статус'

    def test_go_to_page_click_logo_scooter(self, driver, url_home_page, url_order_form):
        page = PageForm(driver, url_order_form)
        page.transition_logo_scooter()
        assert driver.current_url == url_home_page

    def test_go_to_page_click_logo_yandex(self, driver, url_home_page, url_yandex):
        page = PageForm(driver, url_home_page)
        page.transition_logo_yandex()
        assert driver.current_url == url_yandex
