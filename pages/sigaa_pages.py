import components.selection_components as sc
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

MAIN_PAGE = "https://sigaa.unb.br/sigaa"
LOGIN_PAGE = "https://sigaa.unb.br/sigaa/verTelaLogin"
EXTENSION_PAGE = "https://sigaa.unb.br/sigaa/extensao/Atividade/lista.jsf"

# LOGIN_USER = "user.login"
# LOGIN_PASS = "user.senha"
# USERNAME_XPATH = "/html/body/div[2]/div[2]/div[4]/form/table/tbody/tr[1]/td/input"
# PASSWORD_XPATH = "/html/body/div[2]/div[2]/div[4]/form/table/tbody/tr[2]/td/input"
SUBMIT_BUTTON = "/html/body/div[3]/div/div[1]/form/button"

LOGIN_USER = "username"
LOGIN_PASS = "password"
USERNAME_XPATH = "/html/body/div[3]/div/div[1]/form/div[1]/input"
PASSWORD_XPATH = "/html/body/div[3]/div/div[1]/form/div[2]/input"

def insert_credencials_into_sigaa(driver, USERNAME, PASSWORD):
    sc.use_input_by_name(LOGIN_USER, USERNAME, driver)
    sc.use_input_by_name(LOGIN_PASS, PASSWORD, driver)

def insert_credencials_into_sigaa_env(driver, env_var):
    sc.use_input_by_name(LOGIN_USER, env_var['SIGAA_USER'], driver)
    sc.use_input_by_name(LOGIN_PASS, env_var['SIGAA_PASS'], driver)

def click_submit_button(driver):
    # driver.find_element(By.XPATH, "//input[@type='submit']").click()
    driver.find_element(By.XPATH, "//button[contains(text(), 'ENTRAR')]")
    # sc.use_element_by_xpath(SUBMIT_BUTTON, driver)

def login_into_sigaa(driver, USERNAME, PASSWORD):
    insert_credencials_into_sigaa(driver, USERNAME, PASSWORD)
    click_submit_button(driver)

def login_into_sigaa_env(driver, env_var):
    insert_credencials_into_sigaa_env(driver, env_var)
    click_submit_button(driver)