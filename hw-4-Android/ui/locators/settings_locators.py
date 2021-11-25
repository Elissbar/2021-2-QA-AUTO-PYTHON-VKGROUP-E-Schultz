from ui.locators.base_locators import BasePageLocators
from selenium.webdriver.common.by import By


class SettingsPageLocators(BasePageLocators):
    above_app = (By.ID, 'ru.mail.search.electroscope:id/user_settings_about')

    version = (By.ID, 'ru.mail.search.electroscope:id/about_version')
    about_copyright = (By.ID, 'ru.mail.search.electroscope:id/about_copyright')

    source_news = (By.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    news_fm = (By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]')
    news_selected = (By.ID, 'ru.mail.search.electroscope:id/news_sources_item_selected')

    prev_page = (By.XPATH, '//android.widget.ImageButton')

    close_settings = (By.XPATH, '//android.widget.ImageButton')