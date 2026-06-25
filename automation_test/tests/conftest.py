import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
from allure_commons.types import AttachmentType
from utils.config_reader import ConfigReader


@pytest.fixture
def driver():
    # Khởi tạo Chrome driver với tùy chọn
    chrome_options = Options()
    if ConfigReader.get_headless():
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)

    # Phóng to cửa sổ
    driver.maximize_window()

    # Implicit wait
    driver.implicitly_wait(10)

    # Mở website
    driver.get("https://opensource-demo.orangehrmlive.com/")
    #driver.get("https://demo.guru99.com/test/drag_drop.html")
    yield driver

    # Đóng browser
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="Failure Screenshot",
                    attachment_type=AttachmentType.PNG,
                )
            except Exception:
                pass
