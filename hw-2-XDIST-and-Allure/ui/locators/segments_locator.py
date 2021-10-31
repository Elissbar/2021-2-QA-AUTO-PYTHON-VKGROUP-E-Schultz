from selenium.webdriver.common.by import By


class SegmentsPageLocator:
    # First creating
    first_button = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    # Next creating
    create_segment = (By.XPATH, '//div[contains(@class, "js-create")]//div')

    apps_and_games = (By.XPATH, '//div[@data-class-name="TypeItemView"][8]') # Не нашел более лучшего локатора
    checkbox = (By.XPATH, "//input[contains(@class, 'adding-segments-source')]")
    add_segment = (By.XPATH, '//div[contains(@class, "adding-segments-modal__btn-wrap")]//*[contains(@class, "button_submit")]')
    name_segment = (By.XPATH, '//div[@class="js-segment-name"]//input')

    segment_link = lambda self, name: (By.XPATH, f'//a[@title="{name}"]')
    delete_segment = lambda self, segment_id: (By.XPATH, f'//div[contains(@data-test, "remove-{segment_id}")]//span')

    confirm_remove = (By.XPATH, '//button[contains(@class, "button_confirm-remove")]/div')


