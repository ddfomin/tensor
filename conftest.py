import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    preferences = {
        "download.default_directory": os.path.join(os.getcwd()),
        'safebrowsing.enabled': True
    }
    options.add_experimental_option("prefs", preferences)

    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
