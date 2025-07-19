import pytest
import allure
import time
import os
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Antisleep UI Tests")
@allure.story("Devices Report Export Flow")
def test_export_devices_report(browser):
    short_wait = WebDriverWait(browser, 10)
    long_wait = WebDriverWait(browser, 60)

    with allure.step("Authorization"):
        browser.get("https://stage-mgt.antisleep.ru/login")
        short_wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("demo@demo.ru")
        browser.find_element(By.ID, "password").send_keys("Demo1704@demo.ru")
        browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
        short_wait.until(EC.url_contains("/client-113"))

    with allure.step("Navigate to 'Devices' page"):
        browser.find_element(By.LINK_TEXT, "Устройства").click()
        short_wait.until(EC.url_contains("/client-113/device"))

    with allure.step("Toggle columns and close popup"):
        short_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mr-3 > .material-icons"))).click()
        short_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".close > span"))).click()

    with allure.step("Click 'Export Report' button"):
        browser.find_element(By.NAME, "export").click()

    with allure.step("Download report"):
        report_element = long_wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href, 'devices_report_')]")
            )
        )
        report_element.click()
        report_url = report_element.get_attribute("href")

    with allure.step("Verify report download"):
        report_filename = os.path.basename(urllib.parse.urlparse(report_url).path)
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        downloaded_path = os.path.join(downloads_folder, report_filename)

        for _ in range(10):
            if os.path.isfile(downloaded_path):
                return
            time.sleep(1)
        raise AssertionError(f"Report file not found: {downloaded_path}")

if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=allure-results"])
