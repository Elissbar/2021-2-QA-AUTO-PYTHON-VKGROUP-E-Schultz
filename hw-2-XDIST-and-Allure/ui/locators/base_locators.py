from selenium.webdriver.common.by import By


class BasePageLocators:
    log_in = {
        "log_in": (By.XPATH, '//div[contains(@class, "responseHead-module-button")]'),
        "email": (By.XPATH, '//input[@name="email"]'),
        "password": (By.XPATH, '//input[@name="password"]'),
        "submit": (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
    }
    right_menu = (By.XPATH, '//div[contains(@class, "right-module-rightButton")]')
    log_out = (By.XPATH, '//a[@href="/logout"]/..')
    tabs = {
        "dashboard": (By.XPATH, '//a[@href="/dashboard"]'),
        'segments': (By.XPATH, '//a[@href="/segments"]'),
        "billing": (By.XPATH, '//a[@href="/billing"]'),
        "statistics": (By.XPATH, '//a[@href="/statistics"]'),
        'pro': (By.XPATH, '//a[@href="/pro/en"]'),
        "profile": (By.XPATH, '//a[@href="/profile"]'),
        "tools": (By.XPATH, '//a[@href="/tools"]'),
        'help': (By.XPATH, '//a[@href="//target.my.com/help/advertisers/en"]')
    }

    invalid_login_page = {
        'error_message': (By.XPATH, '//div[contains(@class, "js_form_msg")]'),
        'error_title': (By.XPATH, '//div[contains(@class, "title")]'),
        'error_text': (By.XPATH, '//div[contains(@class, "text")]')
    }

    invalid_password = (By.XPATH, '//div[contains(@class, "notify-module-content")]')