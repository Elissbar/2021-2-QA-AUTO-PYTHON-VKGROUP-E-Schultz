from selenium.webdriver.common.by import By


class BasePageLocators:
    segments = (By.XPATH, '//a[@href="/segments"]')


class LoginPageLocators(BasePageLocators):
    log_in = {
        "log_in": (By.XPATH, '//div[contains(@class, "responseHead-module-button")]'),
        "email": (By.XPATH, '//input[@name="email"]'),
        "password": (By.XPATH, '//input[@name="password"]'),
        "submit": (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
    }
