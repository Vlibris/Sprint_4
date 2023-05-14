from selenium.webdriver.common.by import By


class LocatorsQuestionPage:
    TEXT_SCOOTER = By.XPATH, "//div[text()='Самокат']"
    PRICE = By.ID, 'accordion__heading-0'
    TEXT_PRICE = By.XPATH, "//div[text()='Сколько это стоит? И как оплатить?']"
    PRICE_DROP_LIST = By.ID, 'accordion__panel-0'
    TEXT_PRICE_DROP_LIST = By.XPATH, "//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"
    MULTIPLE_SCOOTER = By.ID, 'accordion__heading-1'
    MULTIPLE_SCOOTER_DROP_LIST = By.ID, 'accordion__panel-1'
    TEXT_MULTIPLE_SCOOTER_DROP_LIST = By.XPATH, "//p[text()='Пока что у нас так: один заказ — один самокат. Если " \
                                                "хотите покататься с друзьями, можете просто сделать несколько " \
                                                "заказов — один за другим.']"
    RENTAL_TIME = By.ID, 'accordion__heading-2'
    RENTAL_TIME_DROP_LIST = By.ID, 'accordion__panel-2'
    TEXT_RENTAL_TIME_DROP_LIST = By.XPATH, "//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 "\
                                           "мая в течение дня. Отсчёт времени аренды начинается с момента, " \
                                           "когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, " \
                                           "суточная аренда закончится 9 мая в 20:30.']"
    ORDER_TODAY = By.ID, 'accordion__heading-3'
    ORDER_TODAY_DROP_LIST = By.ID, 'accordion__panel-3'
    TEXT_ORDER_TODAY_DROP_LIST = By.XPATH, "//p[text()='Только начиная с завтрашнего дня. Но скоро станем " \
                                           "расторопнее.']"
    RENEW_ORDER = By.ID, 'accordion__heading-4'
    RENEW_ORDER_DROP_LIST = By.ID, 'accordion__panel-4'
    TEXT_RENEW_ORDER_DROP_LIST = By.XPATH, "//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить "\
                                           "в поддержку по красивому номеру 1010.']"
    CHARGER = By.ID, 'accordion__heading-5'
    CHARGER_DROP_LIST = By.ID, 'accordion__panel-5'
    TEXT_CHARGER_DROP_LIST = By.XPATH, "//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на " \
                                       "восемь суток — даже если будете кататься без передышек и во сне. Зарядка не " \
                                       "понадобится.']"
    CANCEL_ORDER = By.ID, 'accordion__heading-6'
    CANCEL_ORDER_DROP_LIST = By.ID, 'accordion__panel-6'
    TEXT_CANCEL_ORDER_DROP_LIST = By.XPATH, "//p[text()='Да, пока самокат не привезли. Штрафа не будет, " \
                                            "объяснительной записки тоже не попросим. Все же свои.']"
    DELIVERY_AREA = By.ID, 'accordion__heading-7'
    DELIVERY_AREA_DROP_LIST = By.ID, 'accordion__panel-7'
    TEXT_DELIVERY_AREA_DROP_LIST = By.XPATH, "//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской " \
                                             "области.']"
    TEXT_QUESTIONS_ABOUT_IMPORTANT = By.XPATH, "//div[text()='Вопросы о важном']"
