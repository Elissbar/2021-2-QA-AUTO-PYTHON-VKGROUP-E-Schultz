from selenium.webdriver.common.by import By
from ui.locators.base_locators import BasePageLocators


class CommandPageLocators(BasePageLocators):
    suggests_list = (By.XPATH, '//android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView')
    population_button = (By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView')
    number_of_people = (By.XPATH, '//*[@resource-id="ru.mail.search.electroscope:id/item_dialog_fact_card_title"and contains(@text,"146 млн.")]')

    search_button = (By.ID, "ru.mail.search.electroscope:id/keyboard")
    search_input = (By.ID, 'ru.mail.search.electroscope:id/input_text')
    search_submit = (By.ID, 'ru.mail.search.electroscope:id/text_input_action')

    message = (By.XPATH, "//*[@resource-id='ru.mail.search.electroscope:id/dialog_item' and contains(@text,'{}')]")

    fm_news = (By.XPATH, '//*[contains(@text, "Включаю новости Вести FM.")]')