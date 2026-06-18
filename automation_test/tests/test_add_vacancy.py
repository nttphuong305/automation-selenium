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
        # ensure login succeeded
        assert login_page.is_upgrade_button_displayed()

        recruitment_page = RecruitmentPage(driver)
        # open Recruitment -> Vacancies
        recruitment_page.open_vacancies()
        recruitment_page.click_add()

        vacancy_name = "Automation test"
        # fill vacancy form
        recruitment_page.create_vacancy(vacancy_name, "Created by Selenium")
        # select job title (method opens dropdown and chooses the preset option)
        recruitment_page.select_job_title()

        # get current user and enter as hiring manager (use first name token)
        current_user = recruitment_page.get_current_user()
        recruitment_page.enter_hiring_manager(current_user.split()[0])

        recruitment_page.enter_number_of_positions("1")
        recruitment_page.set_active_false()
        recruitment_page.set_publish_rss_true()
        recruitment_page.click_save()

        # Verify Edit Vacancy page
        assert recruitment_page.is_edit_vacancy_page_displayed()

        # Cancel back to vacancies list
        recruitment_page.click_cancel()

        # Verify Vacancies page
        assert recruitment_page.is_vacancies_page_displayed()

        # Search and verify results
        recruitment_page.click_search()
        assert recruitment_page.has_records()

        # Verify vacancy just created exists
        assert recruitment_page.is_vacancy_exist(vacancy_name)

        # Logout
        recruitment_page.logout()