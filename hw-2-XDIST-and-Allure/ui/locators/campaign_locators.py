from selenium.webdriver.common.by import By


class CampaignPageLocators:

    create_campaign_btn = (By.XPATH, '//a[@href="/campaign/new"]')

    button_wrap = (By.XPATH, '//div[contains(@class, "dashboard-module-createButtonWrap")]')
    create_button_in_wrap = (By.XPATH, '//div[contains(@class, "button-module-textWrapper")]')

    traffic = (By.XPATH, '//div[contains(@class, "_traffic")]')
    input_url = (By.XPATH, '//input[contains(@class, "mainUrl-module-searchInput")]')
    name_campaign = (By.XPATH, '//input[@maxlength="255"]')
    banner = (By.XPATH, '//div[contains(@id, "patterns_banner")]/span')

    wrap_upload = (By.XPATH, '//div[contains(@class, "button-module-textWrapper") and .="240 × 400"]')
    upload_file = (By.XPATH, '//input[@data-test="image_240x400"]')

    remove_all = (By.XPATH, '//div[contains(@class, "mediaLibrary-module-removeAllButtonText")]')
    confirm_remove = (By.XPATH, '//div[contains(@class, "mediaLibrary-module-removeAllButton")]//div')

    edit_the_image_window = (By.XPATH, '//div[@class="image-cropper"]')
    save_image = (By.XPATH, '//input[@type="submit"]')

    create_a_campaign = (By.XPATH, '//button[@data-service-readonly="true"]')

    campaign_list = (By.XPATH, '//div[contains(@data-test, "name") and @data-row-id]')
    link_campaign = (By.XPATH, '//div[contains(@data-test, "name") and @data-row-id="central-{}"]//a')
    checkbox_campaign = (By.XPATH, '//div[contains(@data-test, "name") and @data-row-id="central-{}"]//input[contains(@class, "nameCell-module-checkbox")]')

    select_status_campaign = (By.XPATH, '//span[.="Active campaigns"]')
    active_campaigns = (By.XPATH, '//li[@data-test="0"]')

    select_action = (By.XPATH, '//div[contains(@class, "tableControls-module-selectItem")]')
    delete_action = (By.XPATH, '//li[@data-test="8"]')
