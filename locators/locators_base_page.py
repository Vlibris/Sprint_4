from selenium.webdriver.common.by import By


class LocatorsBasePage:
    ORDER_BUTTON_TOP_PAGE = By.XPATH, "//button[@class='Button_Button__ra12g']"
    ORDER_BUTTON_BOTTOM_PAGE = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    TEXT_SCOOTER = By.XPATH, "//div[@class='Home_Header__iJKdX']"
    LOGO_SCOOTER = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"
    LOGO_YANDEX = By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"
    YANDEX = By.XPATH, "//a[text()='Установить']"
