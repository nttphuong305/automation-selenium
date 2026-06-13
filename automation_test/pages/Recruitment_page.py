import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

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
    hiring_manager = (By.XPATH,"//input[@placeholder='Type for hints...']")
    user_profile = (By.XPATH,"//p[@class='oxd-userdropdown-name']")
    logout = (By.XPATH,"//a[text()='Logout']")
    number_of_position = (By.XPATH,"//label[text()='Number of Positions']/../following-sibling::div//input")



    def open_vacancies(self):
        self.driver.find_element(*self.recruitment_menu).click()
        self.driver.find_element(*self.vacancies_tab).click()
    
    def click_add(self):
        self.driver.find_element(*self.add_button).click()

    def create_vacancy(self, vacancy_name, description):
        self.driver.find_element(*self.vacancy_name).send_keys(vacancy_name)
        self.driver.find_element(*self.description).send_keys(description)

    def get_current_user(self):
        return self.find_element(self.user_profile).text

    def select_job_title(self):
        self.wait.until(EC.element_to_be_clickable(self.job_title_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable(self.automation_tester_option)).click()

    def enter_hiring_manager(self, manager):

        element = self.driver.find_element(*self.hiring_manager)
        element.send_keys(manager)
        sleep(2)
        element.send_keys(Keys.DOWN)
        element.send_keys(Keys.ENTER)

    def enter_number_of_positions(self, number):
        self.send_keys(self.number_of_position,number)

        
    def click_save(self):
        self.driver.find_element(*self.save_button).click()

    def set_active_false(self):
        self.click(self.ACTIVE_SWITCH)

    def set_publish_rss_true(self):
        self.click(self.RSS_SWITCH)