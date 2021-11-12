import pytest
from base import BaseCase
from random import randint


@pytest.mark.android
class TestAndroid(BaseCase):

    def test_window_command(self):
        self.command_page.get_chat_page(values='Russia')
        self.command_page.send_values(values='Russia')
        self.base_page.swipe_element_lo_left(self.command_page.locators.suggests_list)
        self.base_page.click(self.command_page.locators.population_button)
        people = self.base_page.find(self.command_page.locators.number_of_people)
        assert people.text == '146 млн.'

    def test_calculate(self):
        a, b = randint(5, 9), randint(5, 10)
        self.command_page.get_chat_page(values=f'{a} + {b}')
        self.base_page.click(self.command_page.locators.search_submit)
        message_text = self.base_page.find((self.command_page.locators.message[0],
                                            self.command_page.locators.message[1].format(a+b))).text
        assert message_text == str(a+b)

    def test_settings(self):
        self.base_page.click(self.base_page.locators.settings)
        self.base_page.swipe_to_element(self.settings_page.locators.above_app)
        self.base_page.click(self.settings_page.locators.above_app)
        assert '1.50.2' in self.base_page.find(self.settings_page.locators.version).text
        assert "Все права защищены" in self.base_page.find(self.settings_page.locators.about_copyright).text

    def test_news(self):
        self.base_page.click(self.base_page.locators.settings)
        self.base_page.swipe_to_element(self.settings_page.locators.source_news)
        self.base_page.click(self.settings_page.locators.source_news)
        self.base_page.click(self.settings_page.locators.news_fm)
        assert self.base_page.find(self.settings_page.locators.news_selected)
        self.base_page.click(self.settings_page.locators.prev_page)
        self.base_page.click(self.settings_page.locators.close_settings)
        self.command_page.get_chat_page(values='News')
        self.base_page.click(self.command_page.locators.search_submit)
        # Так и не разобрался почему тест зависает на этом моменте, но пока не остановить новости "Вести ФМ" тест вряд ли закончится раньше
        assert 'Вести FM' in self.base_page.find(self.command_page.locators.fm_news).text



