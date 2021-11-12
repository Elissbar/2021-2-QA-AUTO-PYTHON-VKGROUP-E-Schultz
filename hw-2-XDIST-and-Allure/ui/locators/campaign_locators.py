from selenium.webdriver.common.by import By


class CampaignPageLocators:
    # First creating
    FIRST_CREATE = (By.XPATH, '//a[@href="/campaign/new"]')
    # Next creating
    NEXT_CREATE = (By.XPATH, '//div[contains(@class, "button-module-blue")]')

    TRAFFIC = (By.XPATH, '//div[contains(@class, "_traffic")]')
    IPNUT_URL = (By.XPATH, '//input[contains(@class, "mainUrl-module-searchInput")]')
    NAME_CAMPAIGN = (By.XPATH, '//div[contains(@class, "input_campaign-name")]//input')
    BANNER = (By.XPATH, '//div[contains(@id, "patterns_banner")]/span')

    WRAP_UPLOAD = (By.XPATH, '//div[contains(@class, "button-module-textWrapper") and .="240 × 400"]')
    UPLOAD_FILE = (By.XPATH, '//input[@data-test="image_240x400"]')
    REMOVE_FILE = (By.XPATH, '//div[contains(@class, "mediaLibrary-module-removeAllButtonText")]')
    CONFIRM_REMOVE = (By.XPATH, '//div[contains(@class, "mediaLibrary-module-removeAllButton")]//div')

    SAVE_IMAGE = (By.XPATH, '//input[@type="submit"]')
    CREATE_A_CAMPAIGN = (By.XPATH, '//button[@data-service-readonly="true"]')

    SELECT_STATUS_CAMPAIGN = (By.XPATH, '//div[contains(@class, "statusFilter-module-filterButtonWrapper")]//div[contains(@class, "select-module-item")]')
    ACTIVE_CAMPAIGNS = (By.XPATH, '//li[@data-test="0"]')

    CAMPAIGN_LINK = lambda self, name: (By.XPATH, f'//a[@title="{name}"]')
    CHECKBOX_TO_DELETE = lambda self, id: (By.XPATH, f'//div[contains(@data-test, "name-{id}")]//input[contains(@class, "nameCell-module-checkbox")]')

    SELECT_ACTION = (By.XPATH, '//div[contains(@class, "tableControls-module-selectItem")]')
    DELETE_ACTION = (By.XPATH, '//li[@data-test="8"]')
