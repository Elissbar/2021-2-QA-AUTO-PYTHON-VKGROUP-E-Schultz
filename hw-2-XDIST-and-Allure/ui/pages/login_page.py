from ui.pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    @allure.step('Login in page')
    def login(self, login, password):
        self.find(self.locators.log_in['log_in']).click()
        self.find(self.locators.log_in['email']).send_keys(login) # Решил как вариант не выносить
        self.find(self.locators.log_in['password']).send_keys(password)      # логин и пасс в отдельный файл
        self.find(self.locators.log_in['submit']).click()


