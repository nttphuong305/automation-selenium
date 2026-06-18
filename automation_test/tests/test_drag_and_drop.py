from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://demo.guru99.com/test/drag_drop.html"


def drag_and_drop(driver, source_text, target_id):
    wait = WebDriverWait(driver, 10)

    source = wait.until(
        EC.visibility_of_element_located((By.XPATH, f"//*[normalize-space()='{source_text}']")))
    target = wait.until(EC.visibility_of_element_located((By.ID, target_id)))

    ActionChains(driver).drag_and_drop(source, target).perform()
    wait.until(EC.text_to_be_present_in_element((By.ID, target_id), source_text))

def test_drag_and_drop_demo(driver):
    driver.get(URL)

    drag_and_drop(driver, "BANK", "bank")
    drag_and_drop(driver, "5000", "amt7")

    assert "BANK" in driver.find_element(By.ID, "bank").text
    assert "5000" in driver.find_element(By.ID, "amt7").text