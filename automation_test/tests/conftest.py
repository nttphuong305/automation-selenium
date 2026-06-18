import pytest
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType


@pytest.fixture
def driver():
    # Khởi tạo Chrome driver
    driver = webdriver.Chrome()

    # Phóng to cửa sổ
    driver.maximize_window()

    # Implicit wait
    driver.implicitly_wait(10)

    # Mở website
    driver.get("https://opensource-demo.orangehrmlive.com/")

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
