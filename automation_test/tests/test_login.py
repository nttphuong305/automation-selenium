import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_login():

    # Declare the driver to help interacting with the Chrome
    driver = webdriver.Chrome()

    # Open the SUT (system under test)
    driver.get('https://opensource-demo.orangehrmlive.com/')

    # maximize the Chrome browser
    driver.maximize_window()
    sleep(10)

    username_field = (By.NAME, 'username')
    password_field = (By.NAME, 'password')
    click_btn = (By.XPATH, '//button[@type="submit"]')
    upgrade_btn = (By.XPATH, '//button[@class="oxd-glass-button orangehrm-upgrade-button"]')

    driver.find_element(*username_field).send_keys('Admin')

    driver.find_element(*password_field).send_keys('admin123')
    driver.find_element(*click_btn).click()

    sleep(3)
    upgrade_btn = WebDriverWait(driver, 10).until(lambda d: d.find_element(*upgrade_btn))

    assert upgrade_btn.is_displayed()