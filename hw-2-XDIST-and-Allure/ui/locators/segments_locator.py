from selenium.webdriver.common.by import By


class SegmentsPageLocator:
    # First create
    first_button = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    apps_and_games = (By.XPATH, '//div[.="Apps and games in social networks"]')
    checkbox = (By.XPATH, "//input[contains(@class, 'adding-segments-source')]")
    add_segment_button = (By.XPATH, '//div[contains(text(), "Add segment")]')

    name_segment = (By.XPATH, '//input[@maxlength="60"]')
    create_segment = (By.XPATH, '//div[contains(text(), "Create segment")]')

    delete_segment = (By.XPATH, '//span[contains(@class, "icon-cross")]')

    segments_list = (By.XPATH, '//div[@data-row-id and starts-with(@data-test, "name")]')
    segment = (By.XPATH, '//div[@data-row-id="central-{}" and starts-with(@data-test, "name")]')
    segment_link = (By.XPATH, f'//a[@title]')

    remove = (By.XPATH, '//div[@data-row-id="central-{}" and starts-with(@data-test, "remove")]')
    delete = (By.XPATH, '//div[.="Delete"]')


