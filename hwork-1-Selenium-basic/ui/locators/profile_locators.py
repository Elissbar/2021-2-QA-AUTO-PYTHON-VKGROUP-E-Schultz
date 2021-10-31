from selenium.webdriver.common.by import By


class ProfilePageLocators:
    full_name = (By.XPATH, '//div[@data-name="fio"]//input')
    phone_number = (By.XPATH, '//div[@data-name="phone"]//input')
    save_change_btn = (By.XPATH, '//button[@data-class-name="Submit"]')
