from locators.locators_base_page import LocatorsBasePage
from locators.locators_order_form_page import LocatorsOrderForm
from pages.base_page import BasePage


class PageForm(BasePage):
    def order_button_top(self):
        return self.driver.find_element(*LocatorsBasePage.ORDER_BUTTON_TOP_PAGE)

    def order_button_bottom(self):
        return self.driver.find_element(*LocatorsBasePage.ORDER_BUTTON_BOTTOM_PAGE)

    def logo_scooter(self):
        return self.driver.find_element(*LocatorsBasePage.LOGO_SCOOTER)

    def logo_yandex(self):
        return self.driver.find_element(*LocatorsBasePage.LOGO_YANDEX)

    def field_name(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_NAME)

    def field_surname(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_SURNAME)

    def field_address(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_ADDRESS)

    def field_metro_station(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_METRO_STATION)

    def list_metro_station_1(self):
        return self.driver.find_element(*LocatorsOrderForm.LIST_METRO_STATION_1)

    def list_metro_station_2(self):
        return self.driver.find_element(*LocatorsOrderForm.LIST_METRO_STATION_2)

    def field_phone_number(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_PHONE_NUMBER)

    def next_button(self):
        return self.driver.find_element(*LocatorsOrderForm.NEXT_BUTTON)

    def field_date(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_DATE)

    def day_calendar_june(self):
        return self.driver.find_element(*LocatorsOrderForm.DAY_CALENDAR_JUNE)

    def day_calendar_may(self):
        return self.driver.find_element(*LocatorsOrderForm.DAY_CALENDAR_MAY)

    def field_rental_period(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_RENTAL_PERIOD)

    def list_field_rental_period_seven(self):
        return self.driver.find_element(*LocatorsOrderForm.LIST_RENTAL_PERIOD_SEVEN)

    def list_field_rental_period_one(self):
        return self.driver.find_element(*LocatorsOrderForm.LIST_RENTAL_PERIOD_ONE)

    def checkbox_black_color(self):
        return self.driver.find_element(*LocatorsOrderForm.CHECKBOX_COLOR_BLACK)

    def checkbox_gray_color(self):
        return self.driver.find_element(*LocatorsOrderForm.CHECKBOX_COLOR_GRAY)

    def field_comment(self):
        return self.driver.find_element(*LocatorsOrderForm.FIELD_COMMENT)

    def order_button(self):
        return self.driver.find_element(*LocatorsOrderForm.BUTTON_ORDER)

    def button_yes(self):
        return self.driver.find_element(*LocatorsOrderForm.BUTTON_YES)

    def click_order_button_bottom(self):
        self.order_button_bottom().click()

    def click_order_button_top(self):
        self.order_button_top().click()

    def click_logo_scooter(self):
        self.logo_scooter().click()

    def click_logo_yandex(self):
        self.logo_yandex().click()

    def click_field_name(self):
        self.field_name().click()

    def click_field_surname(self):
        self.field_surname().click()

    def click_field_address(self):
        self.field_address().click()

    def click_field_metro_station(self):
        self.field_metro_station().click()

    def click_list_metro_station_1(self):
        self.list_metro_station_1().click()

    def click_list_metro_station_2(self):
        self.list_metro_station_2().click()

    def click_field_phone_number(self):
        self.field_phone_number().click()

    def click_next_button(self):
        self.next_button().click()

    def click_field_date(self):
        self.field_date().click()

    def click_day_calendar_june(self):
        self.day_calendar_june().click()

    def click_day_calendar_may(self):
        self.day_calendar_may().click()

    def click_field_rental_period(self):
        self.field_rental_period().click()

    def click_list_field_rental_period_one(self):
        self.list_field_rental_period_one().click()

    def click_list_field_rental_period_seven(self):
        self.list_field_rental_period_seven().click()

    def click_checkbox_black_color(self):
        self.checkbox_black_color().click()

    def click_checkbox_gray_color(self):
        self.checkbox_gray_color().click()

    def click_field_comment(self):
        self.field_comment().click()

    def click_order_button(self):
        self.order_button().click()

    def click_button_yes(self):
        self.button_yes().click()

    def open_form_button_order_top(self):
        self.open()
        self.element_is_visible(LocatorsBasePage.ORDER_BUTTON_TOP_PAGE)
        self.click_order_button_top()
        self.element_is_visible(LocatorsOrderForm.TEXT_FOR_WHOM_THE_SCOOTER)

    def open_form_button_order_bottom(self):
        self.open()
        self.element_is_visible(LocatorsBasePage.ORDER_BUTTON_TOP_PAGE)
        self.click_order_button_top()
        self.element_is_visible(LocatorsOrderForm.TEXT_FOR_WHOM_THE_SCOOTER)

    def fill_form_fields_for_whom_scooter_data_one_positive_result(self):
        self.click_field_name()
        self.field_name().send_keys('Песик')
        self.click_field_surname()
        self.field_surname().send_keys('Песиков')
        self.click_field_address()
        self.field_address().send_keys('ул.Песиков')
        self.click_field_metro_station()
        self.element_is_visible(LocatorsOrderForm.LIST_METRO_STATION_1)
        self.click_list_metro_station_1()
        self.click_field_phone_number()
        self.field_phone_number().send_keys('99999999999')
        self.click_next_button()
        self.element_is_visible(LocatorsOrderForm.TEXT_ABOUT_RENT)

    def fill_form_fields_for_whom_scooter_data_two_positive_result(self):
        self.click_field_name()
        self.field_name().send_keys('Котик')
        self.click_field_surname()
        self.field_surname().send_keys('Котиков')
        self.click_field_address()
        self.field_address().send_keys('ул.Котиков')
        self.click_field_metro_station()
        self.element_is_visible(LocatorsOrderForm.LIST_METRO_STATION_2)
        self.click_list_metro_station_2()
        self.click_field_phone_number()
        self.field_phone_number().send_keys('55555555555')
        self.click_next_button()
        self.element_is_visible(LocatorsOrderForm.TEXT_ABOUT_RENT)

    def fill_rental_form_data_one_positive_result(self):
        self.click_field_date()
        self.element_is_visible(LocatorsOrderForm.CALENDAR)
        self.click_day_calendar_may()
        self.click_field_rental_period()
        self.element_is_visible(LocatorsOrderForm.LIST_RENTAL_PERIOD_ONE)
        self.click_list_field_rental_period_one()
        self.click_checkbox_black_color()
        self.click_field_comment()
        self.field_comment().send_keys('Привет')

    def fill_rental_form_data_two_positive_result(self):
        self.click_field_date()
        self.element_is_visible(LocatorsOrderForm.CALENDAR)
        self.click_day_calendar_june()
        self.click_field_rental_period()
        self.element_is_visible(LocatorsOrderForm.LIST_RENTAL_PERIOD_ONE)
        self.click_list_field_rental_period_seven()
        self.click_checkbox_black_color()
        self.click_checkbox_gray_color()
        self.click_field_comment()
        self.field_comment().send_keys('Не могу определиться с цветом!')

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
