from selenium.webdriver.common.by import By


class SegmentsPageLocator:
    # First creating
    FIRST_BUTTON = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    # Next creating
    CREATE_SEGMENT = (By.XPATH, '//div[contains(@class, "js-create")]//div')

    APPS_AND_GAMES = (By.XPATH, '//div[@data-class-name="TypeItemView"][8]') # Не нашел более лучшего локатора
    CHECKBOX = (By.XPATH, "//input[contains(@class, 'adding-segments-source')]")
    ADD_SEGMENT = (By.XPATH, '//div[contains(@class, "adding-segments-modal__btn-wrap")]//*[contains(@class, "button_submit")]')
    NAME_SEGMENT = (By.XPATH, '//div[@class="js-segment-name"]//input')

    SEGMENT_LINK = lambda self, name: (By.XPATH, f'//a[@title="{name}"]')
    DELETE_SEGMENT = lambda self, segment_id: (By.XPATH, f'//div[contains(@data-test, "remove-{segment_id}")]//span')

    CONFIRM_REMOVE = (By.XPATH, '//button[contains(@class, "button_confirm-remove")]/div')
