from locators.locators_base_page import LocatorsBasePage
from locators.locators_order_form_page import LocatorsOrderForm
from pages.base_page import BasePage
import allure


class PageForm(BasePage):
    @allure.step('Находим кнопку Заказать внизу страницы и кликаем')
    def click_order_button_bottom(self):
        self.driver.find_element(*LocatorsBasePage.ORDER_BUTTON_BOTTOM_PAGE).click()

    @allure.step('Находим кнопку Заказать вверху страницы и кликаем')
    def click_order_button_top(self):
        self.driver.find_element(*LocatorsBasePage.ORDER_BUTTON_TOP_PAGE).click()

    @allure.step('Находим логотип Самокат и кликаем')
    def click_logo_scooter(self):
        return self.driver.find_element(*LocatorsBasePage.LOGO_SCOOTER).click()

    @allure.step('Находим логотип Яндекс и кликаем')
    def click_logo_yandex(self):
        return self.driver.find_element(*LocatorsBasePage.LOGO_YANDEX).click()

    @allure.step('Находим поле Имя и кликаем')
    def click_field_name(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_NAME).click()

    @allure.step('Находим поле Фамилия и кликаем')
    def click_field_surname(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_SURNAME).click()

    @allure.step('Находим поле Адрес и кликаем')
    def click_field_address(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_ADDRESS).click()

    @allure.step('Находим поле Станция метро и кликаем')
    def click_field_metro_station(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_METRO_STATION).click()

    @allure.step('Находим выпадающий список поля Станция метро и кликаем на станцию')
    def click_list_metro_station_1(self):
        return self.driver.find_element(*LocatorsOrderForm.LIST_METRO_STATION_1).click()

    @allure.step('Находим выпадающий список поля Станция метро и кликаем на станцию')
    def click_list_metro_station_2(self):
        return self.driver.find_element(*LocatorsOrderForm.LIST_METRO_STATION_2).click()

    @allure.step('Находим поле Номер телефона и кликаем')
    def click_field_phone_number(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_PHONE_NUMBER).click()

    @allure.step('Находим кнопку Далее и кликаем')
    def click_next_button(self):
        return self.driver.find_element(*LocatorsOrderForm.NEXT_BUTTON).click()

    @allure.step('Находим поле Когда привезти самокат и кликаем')
    def click_field_date(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_DATE).click()

    @allure.step('Находим выпадающий календарь поля Срок аренды и кликаем на 4-е июня 2023 г.')
    def click_day_calendar_june(self):
        return self.driver.find_element(*LocatorsOrderForm.DAY_CALENDAR_JUNE).click()

    @allure.step('Находим выпадающий календарь поля Срок аренды и кликаем на 30-е мая 2023 г.')
    def click_day_calendar_may(self):
        return self.driver.find_element(*LocatorsOrderForm.DAY_CALENDAR_MAY).click()

    @allure.step('Находим поле Срок аренды и кликаем')
    def click_field_rental_period(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_RENTAL_PERIOD).click()

    @allure.step('Находим выпадающий список и кликаем на Одни сутки')
    def click_list_field_rental_period_one(self):
        return self.driver.find_element(*LocatorsOrderForm.LIST_RENTAL_PERIOD_ONE).click()

    @allure.step('Находим выпадающий список и кликаем на Семь суток')
    def click_list_field_rental_period_seven(self):
        return self.driver.find_element(*LocatorsOrderForm.LIST_RENTAL_PERIOD_SEVEN).click()

    @allure.step('Находим чербокс поля Цвет самоката и кликаем на черный жемчуг')
    def click_checkbox_black_color(self):
        return self.driver.find_element(*LocatorsOrderForm.CHECKBOX_COLOR_BLACK).click()

    @allure.step('Находим чербокс поля Цвет самоката и кликаем на серую безысходность')
    def click_checkbox_gray_color(self):
        return self.driver.find_element(*LocatorsOrderForm.CHECKBOX_COLOR_GRAY).click()

    @allure.step('Находим поле Комментарий и кликаем')
    def click_field_comment(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_COMMENT).click()

    @allure.step('Находим кнопку Заказать и кликаем')
    def click_order_button(self):
        return self.driver.find_element(*LocatorsOrderForm.BUTTON_ORDER).click()

    @allure.step('Находим кнопку Да в окне с вопросом и кликаем по ней')
    def click_button_yes(self):
        return self.driver.find_element(*LocatorsOrderForm.BUTTON_YES).click()

    @allure.description('Открываем форму бронирования через кнопку Заказать вверху страницы')
    def open_form_button_order_top(self):
        self.open()
        self.element_is_visible(LocatorsBasePage.ORDER_BUTTON_TOP_PAGE)
        self.click_order_button_top()
        self.element_is_visible(LocatorsOrderForm.TEXT_FOR_WHOM_THE_SCOOTER)

    @allure.description('Открываем форму бронирования через кнопку Заказать внизу страницы')
    def open_form_button_order_bottom(self):
        self.open()
        self.element_is_visible(LocatorsBasePage.ORDER_BUTTON_TOP_PAGE)
        self.click_order_button_top()
        self.element_is_visible(LocatorsOrderForm.TEXT_FOR_WHOM_THE_SCOOTER)

    @allure.description('Заполняем форму, Для кого самокат, данными собачки')
    def fill_form_fields_for_whom_scooter_data_one_positive_result(self, user_dog):
        self.click_field_name()
        self.driver.find_element(*LocatorsOrderForm.FIELD_NAME).send_keys(user_dog.name)
        self.click_field_surname()
        self.driver.find_element(*LocatorsOrderForm.FIELD_SURNAME).send_keys(user_dog.surname)
        self.click_field_address()
        self.driver.find_element(*LocatorsOrderForm.FIELD_ADDRESS).send_keys(user_dog.address)
        self.click_field_metro_station()
        self.element_is_visible(LocatorsOrderForm.LIST_METRO_STATION_1)
        self.click_list_metro_station_1()
        self.click_field_phone_number()
        self.driver.find_element(*LocatorsOrderForm.FIELD_PHONE_NUMBER).send_keys(user_dog.phone_number)
        self.click_next_button()
        self.element_is_visible(LocatorsOrderForm.TEXT_ABOUT_RENT)

    @allure.description('Заполняем форму, Для кого самокат, данными котика')
    def fill_form_fields_for_whom_scooter_data_two_positive_result(self, user_cat):
        self.click_field_name()
        self.driver.find_element(*LocatorsOrderForm.FIELD_NAME).send_keys(user_cat.name)
        self.click_field_surname()
        self.driver.find_element(*LocatorsOrderForm.FIELD_SURNAME).send_keys(user_cat.surname)
        self.click_field_address()
        self.driver.find_element(*LocatorsOrderForm.FIELD_ADDRESS).send_keys(user_cat.address)
        self.click_field_metro_station()
        self.element_is_visible(LocatorsOrderForm.LIST_METRO_STATION_2)
        self.click_list_metro_station_2()
        self.click_field_phone_number()
        self.driver.find_element(*LocatorsOrderForm.FIELD_PHONE_NUMBER).send_keys(user_cat.phone_number)
        self.click_next_button()
        self.element_is_visible(LocatorsOrderForm.TEXT_ABOUT_RENT)

    @allure.description('Заполняем форму, Про аренду, данными собачки')
    def fill_rental_form_data_one_positive_result(self, user_dog):
        self.click_field_date()
        self.element_is_visible(LocatorsOrderForm.CALENDAR)
        self.click_day_calendar_may()
        self.click_field_rental_period()
        self.element_is_visible(LocatorsOrderForm.LIST_RENTAL_PERIOD_ONE)
        self.click_list_field_rental_period_one()
        self.click_checkbox_black_color()
        self.click_field_comment()
        self.driver.find_element(*LocatorsOrderForm.FIELD_COMMENT).send_keys(user_dog.comment)

    @allure.description('Заполняем форму, Про аренду, данными котика')
    def fill_rental_form_data_two_positive_result(self, user_cat):
        self.click_field_date()
        self.element_is_visible(LocatorsOrderForm.CALENDAR)
        self.click_day_calendar_june()
        self.click_field_rental_period()
        self.element_is_visible(LocatorsOrderForm.LIST_RENTAL_PERIOD_ONE)
        self.click_list_field_rental_period_seven()
        self.click_checkbox_black_color()
        self.click_checkbox_gray_color()
        self.driver.find_element(*LocatorsOrderForm.FIELD_COMMENT).send_keys(user_cat.comment)

    @allure.description('Завершаем оформление заказа')
    def checkout(self):
        self.click_order_button()
        self.element_is_visible(LocatorsOrderForm.QUESTION_WINDOW)
        self.click_button_yes()
        self.element_is_visible(LocatorsOrderForm.WINDOW_ORDER_IS_PLACED)

    def transition_logo_scooter(self):
        self.open()
        self.click_logo_scooter()
        self.element_is_visible(LocatorsBasePage.TEXT_SCOOTER)

    def transition_logo_yandex(self):
        self.open()
        self.click_logo_yandex()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.element_is_visible(LocatorsBasePage.YANDEX)
