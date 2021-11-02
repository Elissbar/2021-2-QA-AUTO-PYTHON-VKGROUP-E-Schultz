from selenium.webdriver.common.by import By


class BasePageLocators:
    TABS = {
        "segments": (By.XPATH, '//a[@href="/segments"]')
    }


class LoginPageLocators(BasePageLocators):
    LOG_IN = {
        "log_in": (By.XPATH, '//div[contains(@class, "responseHead-module-button")]'),
        "email": (By.XPATH, '//input[@name="email"]'),
        "password": (By.XPATH, '//input[@name="password"]'),
        "submit": (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
    }
