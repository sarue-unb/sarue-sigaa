from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from database_generator.constants import *
from config.filter_descryption import *

def get_error_message(driver):
    try:
        return driver.find_element(By.XPATH, XPATH_ERROR_MESSAGE).text
    except:
        return None
    
def clear_input_name(name:str, driver):
    input_field = driver.find_element(By.NAME, name)
    input_field.clear()
    
def uncheck_checkbox_name(name:str, driver):
    checkbox = driver.find_element(By.NAME, name)
    if checkbox.is_selected():
        checkbox.click()
        
def use_input_by_name(name:str, input:str, driver):
    input_field = driver.find_element(By.NAME, name)
    input_field.click()
    input_field.send_keys(input)
    
def use_element_by_id(id:str, driver):
    driver.find_element(By.ID, id).click()

def use_element_by_xpath(value:int, driver):
    driver.find_element(By.XPATH, value).click()

def use_element_by_class(class_name:str, driver):
    driver.find_element(By.CLASS_NAME, class_name).click()

def get_element_by_id(id:str, driver):
    return driver.find_element(By.ID, id)

def get_element_by_xpath(value:int, driver):
    return driver.find_element(By.XPATH, value)

def get_element_by_class(class_name:str, driver):
    return driver.find_element(By.CLASS_NAME, class_name)

def get_element_by_select(name:str, option:str, driver):
    select = Select(driver.find_element_by_name(name))
    select.select_by_visible_text(option)

def get_rows_len(result_table):
    return len(result_table.find_elements(By.XPATH, ".//tr"))

def get_rows_from_table(driver):
    return driver.find_element(By.ID, "listagem")

def count_listing(driver):
    try:
        # This is being done directly through XPATH
        # But we could also do it by using the table Id
        rows = driver.find_elements(By.XPATH, XPATH_ROWS)
        return len(rows)
    except:
        return 0

def add_date_to_item(item, month, year):
     item['data_inicio'] = {'mes':month, 'ano':year}
     return item

def get_info_try_except(xpath, driver):
    try:
        return get_element_by_xpath(xpath, driver).text
    except:
        return "N/A"
    
def get_info_direct(xpath, driver):
    return get_element_by_xpath(xpath, driver).text

def get_qtd_tables_by_xpath(xpath, driver):
    form = driver.find_element(By.XPATH, xpath)

    return len(form.find_elements(By.XPATH, "table"))

def get_qtd_tables_by_xpath_relatorio(xpath, driver):
    form = driver.find_element(By.XPATH, xpath)

    return len(form.find_elements(By.XPATH, ".//tr"))