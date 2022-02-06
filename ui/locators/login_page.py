from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOG_IN = {
        "username": (By.XPATH, '//*[@id="username"]'),
        "password": (By.XPATH, '//*[@id="password"]'),
        "submit": (By.XPATH, '//*[@id="submit"]'),
        "registration_page": (By.XPATH, '//*[@href="/reg"]'),
        "error_message": (By.XPATH, '')
    }

    REGISTRATION = {
        "username": (By.XPATH, '//*[@id="username"]'),
        "email": (By.XPATH, '//*[@id="email"]'),
        "password": (By.XPATH, '//*[@id="password"]'),
        "confirm": (By.XPATH, '//*[@id="confirm"]'),
        "checkbox": (By.XPATH, '//*[@id="term"]'),
        "submit": (By.XPATH, '//*[@id="submit"]'),
        "login_page": (By.XPATH, '//*[@href="/login"]'),
    }

    error_message = (By.XPATH, '//*[@id="flash"]')
