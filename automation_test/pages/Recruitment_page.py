import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class RecruitmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    recruitment_menu = (By.XPATH, "//span[text()='Recruitment']")
    vacancies_tab = (By.XPATH, "//a[text()='Vacancies']")
    add_button = (By.XPATH, "//button[text()=' Add ']")
    vacancy_name = (By.XPATH, "//label[text()='Vacancy Name']/../following-sibling::div/input")
    description = (By.TAG_NAME, "textarea")
    save_button = (By.XPATH, "//button[@type='submit']")
    job_title_dropdown = (By.XPATH,"//label[text()='Job Title']/../following-sibling::div")
    automation_tester_option = (By.XPATH,"//span[text()='Automaton Tester']")
    active_switch = (By.XPATH, "(//div[contains(@class,'oxd-switch-wrapper')])[1]")
    rss_switch = (By.XPATH,"(//div[contains(@class,'oxd-switch-wrapper')])[2]")

    def open_vacancies(self):
        self.driver.find_element(*self.recruitment_menu).click()
        self.driver.find_element(*self.vacancies_tab).click()
    
    def click_add(self):
        self.driver.find_element(*self.add_button).click()

    def create_vacancy(self, vacancy_name, description):
        self.driver.find_element(*self.vacancy_name).send_keys(vacancy_name)
        self.driver.find_element(*self.description).send_keys(description)

    def select_job_title(self):
        self.wait.until(EC.element_to_be_clickable(self.job_title_dropdown)).click()

        self.wait.until(EC.element_to_be_clickable(self.automation_tester_option)).click()

    def enter_hiring_manager(self, manager):

        element = self.driver.find_element(*self.hiring_manager)
        element.send_keys("AtAZc")
        sleep(2)
        element.send_keys(Keys.DOWN)
        element.send_keys(Keys.ENTER)

    def click_save(self):
        self.driver.find_element(*self.save_button).click()
