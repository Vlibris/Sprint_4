import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX


class BasePage:
    @allure.step('Открываем браузер Mozilla Firefox')
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Открываем страницу')
    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EX.visibility_of_element_located(locator))

    def find_elements(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EX.presence_of_all_elements_located(locator),
                                                         message=f"Can't find elements by locator {locator}")

    def scroll_to_element(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

