from selenium.webdriver.common.by import By


class CampaignPageLocators:
    # First creating
    first_create = (By.XPATH, '//a[@href="/campaign/new"]')
    # Next creating
    next_create = (By.XPATH, '//div[contains(@class, "button-module-blue")]')

    traffic = (By.XPATH, '//div[contains(@class, "_traffic")]')
    input_url = (By.XPATH, '//input[contains(@class, "mainUrl-module-searchInput")]')
    name_campaign = (By.XPATH, '//div[contains(@class, "input_campaign-name")]//input')
    banner = (By.XPATH, '//div[contains(@id, "patterns_banner")]/span')

    wrap_upload = (By.XPATH, '//div[contains(@class, "button-module-textWrapper") and .="240 × 400"]')
    upload_file = (By.XPATH, '//input[@data-test="image_240x400"]')
    remove_all = (By.XPATH, '//div[contains(@class, "mediaLibrary-module-removeAllButtonText")]')
    confirm_remove = (By.XPATH, '//div[contains(@class, "mediaLibrary-module-removeAllButton")]//div')

    save_image = (By.XPATH, '//input[@type="submit"]')
    create_a_campaign = (By.XPATH, '//button[@data-service-readonly="true"]')

    select_status_campaign = (By.XPATH, '//span[.="Active campaigns"]')
    active_campaigns = (By.XPATH, '//li[@data-test="0"]')

    campaign_link = lambda self, name: (By.XPATH, f'//a[@title="{name}"]')
    checkbox_to_delete = lambda self, id: (By.XPATH, f'//div[contains(@data-test, "name-{id}")]//input[contains(@class, "nameCell-module-checkbox")]')

    select_action = (By.XPATH, '//div[contains(@class, "tableControls-module-selectItem")]')
    delete_action = (By.XPATH, '//li[@data-test="8"]')

