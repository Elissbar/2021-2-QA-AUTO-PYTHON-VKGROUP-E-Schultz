from selenium.webdriver.common.by import By


class MainPageLocators:

    username = (By.XPATH, '//*[@id="login-controls"]//ul/li[1]')
    vk_id = (By.XPATH, '//*[@id="login-controls"]//ul/li[2]')

    icons = {
        'api': (By.XPATH, '//a[contains(@href, "Application_programming_interface")]'),
        'foi': (By.XPATH, '//a[contains(@href, "future-of-the-internet")]'),
        'smtp': (By.XPATH, '//a[contains(@href, "SMTP")]')
    }

    navbar = {
        "home": (By.XPATH, "//a[contains(text(), 'HOME')]"),
        "python": (By.XPATH, "//a[contains(@href, 'https://www.python.org/')]"),
        "linux": (By.XPATH, "//a[contains(text(), 'Linux')]"),
        "network": (By.XPATH, "//a[contains(text(), 'Network')]")
    }


