from pages.tensor_page import FirstScenarioPage, SecondScenarioPage, ThirdScenarioPage


class TestFirstScenario:
    def test_first_scenario(self, driver):
        first_scenario_page = FirstScenarioPage(driver, "https://sbis.ru/")
        first_scenario_page.open()
        strength_is_in_people, current_url = first_scenario_page.go_to_page()
        assert strength_is_in_people == "Сила в людях", "Отсутствует блок 'Сила в людях'"
        assert current_url == "https://tensor.ru/about", "Ссылка на страницу 'О компании' некорректная"
        amount_work_img, count = first_scenario_page.check_height_width()
        assert amount_work_img == 4, "Количество изображений меньше 4"
        assert count == 3, "Разная высота и ширина изображений"


class TestSecondScenario:
    def test_second_scenario(self, driver):
        second_scenario_page = SecondScenarioPage(driver, "https://sbis.ru/")
        second_scenario_page.open()
        sverdlovsk_region, ekb_list_partners, ekb_number_partners = second_scenario_page.check_ekb_region()
        assert sverdlovsk_region == "Свердловская обл.", "Выбран неверный регион"
        assert ekb_list_partners == ekb_number_partners, "Список партнеров отсутствует"
        kamchatka_region, kamchatka_list_partners, kamchatka_number_partners, title, current_url = second_scenario_page.check_kamchatka_region()
        assert kamchatka_region == "Камчатский край", "Выбран неверный регион"
        assert kamchatka_list_partners == kamchatka_number_partners, "Список партнеров отсутствует"
        assert title == "СБИС Контакты — Камчатский край", "Неверный title"
        assert current_url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients", "Неверный url"


class TestThirdScenario:
    def test_third_scenario(self, driver):
        third_scenario_page = ThirdScenarioPage(driver, "https://sbis.ru/")
        third_scenario_page.open()
        third_scenario_page.go_to_page()
        third_scenario_page.download_installer()
        check_file, file_size_mb, expected_file_size_mb = third_scenario_page.check_installer()
        assert check_file is True, "Ошибка при скачивании плагина"
        assert file_size_mb == expected_file_size_mb, "Размер скачанного файла не соответствует ожидаемому размеру"
        third_scenario_page.remove_installer()
