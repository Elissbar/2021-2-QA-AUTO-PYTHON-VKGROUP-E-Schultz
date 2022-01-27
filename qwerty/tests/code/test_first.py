from base import BaseCase
from selenium.webdriver.common.by import By


class TestFirst(BaseCase):

    # locators = {
    #     (By.XPATH, '//a[@href="/reg"]')
    # }

    def test_first(self):
        # time.sleep(10)
        # assert 1 == 1
        self.driver.find_element(By.XPATH, '//a[@href="/reg"]').click()
        self.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys('testtest1')
        self.driver.find_element(By.XPATH, '//input[@id="email"]').send_keys('code@code.ru')
        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('qwerty2')
        self.driver.find_element(By.XPATH, '//input[@id="confirm"]').send_keys('qwerty2')
        self.driver.find_element(By.XPATH, '//input[@id="term"]').click()
        self.driver.find_element(By.XPATH, '//input[@id="submit"]').click()
        resp = self.api_client.post_login()
        print(resp.content)
        print(resp.status_code)
        print(resp.cookies)
#         //input[@id="password"]
# //input[@id="confirm"]
# //input[@id="term"]
# //input[@id="submit"]
