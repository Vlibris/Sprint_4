from selenium.webdriver.common.by import By


class LocatorsOrderForm:
    TEXT_FOR_WHOM_THE_SCOOTER = By.XPATH, "//div[text()='Для кого самокат']"
    FIELD_NAME = By.XPATH, "//input[@placeholder='* Имя']"
    FIELD_SURNAME = By.XPATH, "//input[@placeholder='* Фамилия']"
    FIELD_ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    FIELD_METRO_STATION = By.XPATH, "//input[@placeholder='* Станция метро']"
    LIST_METRO_STATION_1 = By.XPATH, "//li[@data-index='1']"
    LIST_METRO_STATION_2 = By.XPATH, "//li[@data-index='5']"
    FIELD_PHONE_NUMBER = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, "//button[text()='Далее']"
    TEXT_ABOUT_RENT = By.XPATH, "//div[text()='Про аренду']"
    FIELD_DATE = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    CALENDAR = By.XPATH, "//div[@class='react-datepicker__header']"
    DAY_CALENDAR_JUNE = By.XPATH, "//div[@aria-label='Choose воскресенье, 4-е июня 2023 г.']"
    DAY_CALENDAR_MAY = By.XPATH, "//div[@aria-label='Choose вторник, 30-е мая 2023 г.']"
    FIELD_RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-control']"
    LIST_RENTAL_PERIOD_ONE = By.XPATH, "//div[text()='сутки']"
    LIST_RENTAL_PERIOD_SEVEN = By.XPATH, "//div[text()='семеро суток']"
    CHECKBOX_COLOR_BLACK = By.XPATH, "//input[@id='black']"
    CHECKBOX_COLOR_GRAY = By.XPATH, "//input[@id='grey']"
    FIELD_COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    BUTTON_ORDER = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    QUESTION_WINDOW = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"
    BUTTON_YES = By.XPATH, "//button[text()='Да']"
    WINDOW_ORDER_IS_PLACED = By.XPATH, "//div[text()='Заказ оформлен']"
    BUTTON_VIEW_STATUS = By.XPATH, "//button[text()='Посмотреть статус']"



