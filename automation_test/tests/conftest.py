import pytest
from selenium import webdriver

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