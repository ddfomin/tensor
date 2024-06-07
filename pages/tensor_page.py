import os
import time
import requests

from locators.tensor_page_locators import FirstScenarioPageLocators, SecondScenarioPageLocators, \
    ThirdScenarioPageLocators
from pages.base_page import BasePage


class FirstScenarioPage(BasePage):
    locators = FirstScenarioPageLocators()

    def go_to_page(self):
        self.element_is_visible(self.locators.CONTACTS).click()
        self.element_is_visible(self.locators.BANNER_TENSOR).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        strength_is_in_people = self.element_is_present(self.locators.STRENGTH).text
        about = self.element_is_visible(self.locators.ABOUT)
        self.go_to_element(about)
        about.click()
        current_url = self.driver.current_url
        return strength_is_in_people, current_url

    def check_height_width(self):
        work = self.element_is_visible(self.locators.WE_ARE_WORKING)
        self.go_to_element(work)
        work_img = self.elements_are_present(self.locators.IMAGES)
        amount_work_img = len(work_img)
        first_img_height = work_img[0].get_attribute("height")
        first_img_width = work_img[0].get_attribute("width")
        count = 0
        for img in work_img[1:]:
            height_value = img.get_attribute("height")
            width_value = img.get_attribute("width")
            if height_value != first_img_height and width_value != first_img_width:
                break
            else:
                count = count + 1
        return amount_work_img, count


class SecondScenarioPage(BasePage):
    locators = SecondScenarioPageLocators()

    def check_ekb_region(self):
        self.element_is_visible(self.locators.CONTACTS).click()
        sverdlovsk_region = self.element_is_present(self.locators.SVERDLOVSK_REGION).text
        ekb_list_partners = len(self.elements_are_present(self.locators.EKB_PARTNERS))
        ekb_number_partners = self.element_is_present(self.locators.EKB_NUMBER_PARTNERS).text
        return sverdlovsk_region, str(ekb_list_partners), ekb_number_partners

    def check_kamchatka_region(self):
        self.element_is_visible(self.locators.SVERDLOVSK_REGION).click()
        self.element_is_visible(self.locators.KAMCHATKA_BUTTON).click()
        time.sleep(2)
        kamchatka_region = self.element_is_present(self.locators.KAMCHATKA_REGION).text
        kamchatka_list_partners = len(self.elements_are_present(self.locators.KAMCHATKA_PARTNERS))
        kamchatka_number_partners = self.element_is_present(self.locators.KAMCHATKA_NUMBER_PARTNERS).text
        title = self.driver.title
        current_url = self.driver.current_url
        return kamchatka_region, str(kamchatka_list_partners), kamchatka_number_partners, title, current_url


class ThirdScenarioPage(BasePage):
    locators = ThirdScenarioPageLocators()

    def go_to_page(self):
        local_version = self.element_is_visible(self.locators.DOWNLOAD_LOCAL_VERSION)
        self.go_to_element(local_version)
        local_version.click()
        self.element_is_visible(self.locators.SBIS_PLUGIN).click()

    def download_installer(self):
        file_url = self.element_is_present(self.locators.WEB_INSTALLER).get_attribute("href")
        response = requests.get(file_url)
        downloaded_file_path = "SBIS_Plugin_WebInstaller.exe"
        with open(downloaded_file_path, 'wb') as file:
            file.write(response.content)

    def check_installer(self):
        downloaded_file_path = "SBIS_Plugin_WebInstaller.exe"
        check_file = os.path.exists(downloaded_file_path)
        file_size_bytes = os.path.getsize(downloaded_file_path)
        file_size_mb = round(file_size_bytes / (1024 * 1024), 2)
        expected_file_size_mb = 7.22
        return check_file, file_size_mb, expected_file_size_mb

    def remove_installer(self):
        downloaded_file_path = "SBIS_Plugin_WebInstaller.exe"
        os.remove(downloaded_file_path)
