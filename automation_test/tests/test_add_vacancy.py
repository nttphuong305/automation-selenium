import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from pages.recruitment_page import RecruitmentPage

class TestAddVacancy:

    def test_add_vacancy(self, driver):

        login_page = LoginPage(driver)
        login_page.login(ConfigReader.get_username(), ConfigReader.get_password())
        login_page.is_upgrade_button_displayed()

    recruitment_page = RecruitmentPage(driver)
    recruitment_page.click_recruitment()
    recruitment_page.click_add()
    recruitment_page.enter_name("Automation test")
    recruitment_page.select_job_title("Automaton Tester")
    recruitment_page.enter_description("Created by Selenium")

    recruitment_page.enter_hiring_manager(current_user.split()[0])

    recruitment_page.enter_number_of_positions("1")

    recruitment_page.set_active_false()


    recruitment_page.set_publish_rss_true()

    recruitment_page.click_save()

        # Verify Edit Vacancy page
    assert recruitment_page.is_edit_vacancy_page_displayed()

        # Cancel
    recruitment_page.click_cancel()

        # Verify Vacancies page
    assert recruitment_page.is_vacancies_page_displayed()

        # Search
    recruitment_page.click_search()

        # Verify có ít nhất 1 record
    assert recruitment_page.has_records()

        # Verify vacancy vừa tạo
    assert recruitment_page.is_vacancy_exist(vacancy_name)

        # LogoutF
    recruitment_page.logout()