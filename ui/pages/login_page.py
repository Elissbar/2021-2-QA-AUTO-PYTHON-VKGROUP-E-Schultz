from ui.pages.base_page import BasePage
from ui.locators.login_page import LoginPageLocators
import allure


class LoginPage(BasePage):

    locators = LoginPageLocators()

    @allure.step('Authorization user')
    def authorization_user(self, username, password):
        self.find(self.locators.LOG_IN["username"]).send_keys(username)
        self.find(self.locators.LOG_IN["password"]).send_keys(password)
        self.click(self.locators.LOG_IN["submit"])

    @allure.step('Registration user')
    def registration_user(self, username, password, email):
        self.click(self.locators.LOG_IN["registration_page"])
        self.find(self.locators.REGISTRATION["username"]).send_keys(username)
        self.find(self.locators.REGISTRATION["email"]).send_keys(email)
        self.find(self.locators.REGISTRATION["password"]).send_keys(password)
        self.find(self.locators.REGISTRATION["confirm"]).send_keys(password)
        self.click(self.locators.REGISTRATION["checkbox"])
        self.click(self.locators.REGISTRATION["submit"])


