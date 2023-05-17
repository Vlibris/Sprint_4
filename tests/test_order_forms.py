import allure

from locators.locators_order_form_page import LocatorsOrderForm
from pages.order_form_page import PageForm


class TestOrderForms:
    @allure.description('Проверяем, что заказ оформлен с данными собачки')
    @allure.title('Проверка, клик по кнопке "Заказать" вверху страницы, '
                  'ввод данных user_dog в форму бронирования самоката')
    def test_checkout_button_order_top_positive_result(self, driver, url_home_page, user_dog):
        page = PageForm(driver, url_home_page)
        page.open_form_button_order_top()
        page.fill_form_fields_for_whom_scooter_data_one_positive_result(user_dog)
        page.fill_rental_form_data_one_positive_result(user_dog)
        page.checkout()
        assert driver.find_element(*LocatorsOrderForm.BUTTON_VIEW_STATUS).text == 'Посмотреть статус'

    @allure.description('Проверяем, что заказ оформлен с данными котика')
    @allure.title('Проверка, клик по кнопке "Заказать" внизу страницы, '
                  'ввод данных user_cat в форму бронирования самоката')
    def test_checkout_button_order_bottom_positive_result(self, driver, url_home_page, user_cat):
        page = PageForm(driver, url_home_page)
        page.open_form_button_order_bottom()
        page.fill_form_fields_for_whom_scooter_data_two_positive_result(user_cat)
        page.fill_rental_form_data_two_positive_result(user_cat)
        page.checkout()
        assert driver.find_element(*LocatorsOrderForm.BUTTON_VIEW_STATUS).text == 'Посмотреть статус'

    @allure.title('Проверяем, клик по логотипу Самокат, ведет на главную страницу Самоката')
    def test_go_to_page_click_logo_scooter(self, driver, url_home_page, url_order_form):
        page = PageForm(driver, url_order_form)
        page.transition_logo_scooter()
        assert driver.current_url == url_home_page

    @allure.title('Проверяем, клик по логотипу Яндекс, ведет на главную страницу Яндекса')
    def test_go_to_page_click_logo_yandex(self, driver, url_home_page, url_yandex):
        page = PageForm(driver, url_home_page)
        page.transition_logo_yandex()
        assert driver.current_url == url_yandex
