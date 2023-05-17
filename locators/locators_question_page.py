from selenium.webdriver.common.by import By


class LocatorsQuestionPage:
    QUESTION = By.XPATH, ".//*[contains(@id, 'accordion__heading-')]"
    ANSWER = By.XPATH, ".//*[contains(@id, 'accordion__panel-')]/p"
    QUESTIONS = By.XPATH, ".//*[@class='accordion']"
