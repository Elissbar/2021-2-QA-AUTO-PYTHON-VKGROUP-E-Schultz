from ui.pages.base_page import BasePage
from ui.locators.base_locators import LoginPageLocators
import allure


class LoginPage(BasePage):
    locators = LoginPageLocators()

    @allure.step('Login in page')
    def login(self, login, password):
        self.find(self.locators.LOG_IN['log_in']).click()
        self.find(self.locators.LOG_IN['email']).send_keys(login)
        self.find(self.locators.LOG_IN['password']).send_keys(password)
        self.find(self.locators.LOG_IN['submit']).click()