import components.selection_components as dc
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def go_into_extension_page(driver, env):
    # _login_into_sigaa(driver, env)
    _skip_welcome_screen(driver)
    _go_into_extension_actions(driver)

def _go_into_extension_actions(driver):
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/form/div/table/tbody/tr/td[3]/span[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/form/div/div[15]/table/tbody/tr[1]/td[1]").click()
    
def _skip_welcome_screen(driver):
    try:
        driver.find_element(By.XPATH, "//input[@value='Continuar >>']").click()
    except NoSuchElementException:  
        pass

# not used anymore
def _login_into_sigaa(driver, env_var):
    dc.use_input_by_name("user.login", env_var['SIGAA_USER'], driver)
    dc.use_input_by_name("user.senha", env_var['SIGAA_PASS'], driver)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    