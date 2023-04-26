from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def use_input_by_name(name: str, input: str, driver):
    input_field = driver.find_element(By.NAME, name)
    input_field.click()
    input_field.send_keys(input)
    
def use_element_by_id(id: str, driver):
    driver.find_element(By.ID, id).click()

def use_element_by_value(value: int, driver):
    return driver.find_element(By.XPATH, value).click()

def get_element_by_value(value: int, driver):
    return driver.find_element(By.XPATH, value)

def get_element_by_id(id: str, driver):
    return driver.find_element(By.ID, id)

def get_element_by_select(name: str, option: str, driver):
    select = Select(driver.find_element_by_name(name))
    select.select_by_visible_text(option)

def count_listing(driver):
    # This is being done directly through XPATH
    # But we could also do it by using the table Id
    rows = driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/form[2]/table/tbody/tr')
    return len(rows)