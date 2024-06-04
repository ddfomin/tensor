class FirstScenarioPageLocators:
    CONTACTS = ("xpath", "//a[text()='Контакты']")
    BANNER_TENSOR = ("xpath", "(//a[@title='tensor.ru'])[1]")
    STRENGTH = ("xpath", "//p[text()='Сила в людях']")
    ABOUT = ("xpath", "//a[@href='/about' and text()='Подробнее']")
    WE_ARE_WORKING = ("xpath", "//h2[text()='Работаем']")
    IMAGES = ("xpath", "//img[@class='tensor_ru-About__block3-image new_lazy loaded']")


class SecondScenarioPageLocators:
    CONTACTS = ("xpath", "//a[text()='Контакты']")

    # ekb locators
    SVERDLOVSK_REGION = ("xpath", "(//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link'])[1]")
    EKB_PARTNERS = ("xpath", "//div[@item-parent-key='-2']")
    EKB_NUMBER_PARTNERS = ("xpath", "(//div[@class='sbisru-Contacts-City__item-count sbisru-Contacts__text--md ws-flex-shrink-0'])[1]")

    # kamchatka locators
    KAMCHATKA_BUTTON = ("xpath", "//span[@title='Камчатский край']")
    KAMCHATKA_REGION = ("xpath", "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link'][1]")
    KAMCHATKA_PARTNERS = ("xpath", "//div[@item-parent-key='-2']")
    KAMCHATKA_NUMBER_PARTNERS = ("xpath", "(//div[@class='sbisru-Contacts-City__item-count sbisru-Contacts__text--md ws-flex-shrink-0'])[1]")


class ThirdScenarioPageLocators:
    DOWNLOAD_LOCAL_VERSION = ("xpath", "//a[@href='/download']")
    SBIS_PLUGIN = ("xpath", "//div[@data-id='plugin']")
    WEB_INSTALLER = ("xpath", "//a[@href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")
