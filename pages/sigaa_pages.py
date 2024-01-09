# sigaa_pages.py
## @file
# Módulo com funções para interagir com a página da web do SIGAA.

import components.selection_components as sc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Nome dos campos de login
LOGIN_USER = "username"
LOGIN_PASS = "password"

# XPath dos campos de login e botões
USERNAME_XPATH = "/html/body/div[3]/div/div[1]/form/div[1]/input"
PASSWORD_XPATH = "/html/body/div[3]/div/div[1]/form/div[2]/input"
SUBMIT_BUTTON = "//button[contains(text(), 'ENTRAR')]"
COOKIES_BUTTON = "//button[contains(text(), 'Ciente')]"

def insert_credentials_into_sigaa(driver, USERNAME, PASSWORD):
    """
    Insere as credenciais (nome de usuário e senha) nos campos de login do SIGAA.

    @param driver: Instância do driver do Selenium.
    @param USERNAME: Nome de usuário para login.
    @param PASSWORD: Senha para login.
    """
    sc.use_input_by_name(LOGIN_USER, USERNAME, driver)
    sc.use_input_by_name(LOGIN_PASS, PASSWORD, driver)

def insert_credentials_into_sigaa_env(driver, env_var):
    """
    Insere as credenciais (nome de usuário e senha) nos campos de login do SIGAA usando variáveis de ambiente.

    @param driver: Instância do driver do Selenium.
    @param env_var: Dicionário contendo as variáveis de ambiente (SIGAA_USER e SIGAA_PASS).
    """
    sc.use_input_by_name(LOGIN_USER, env_var['SIGAA_USER'], driver)
    sc.use_input_by_name(LOGIN_PASS, env_var['SIGAA_PASS'], driver)

def click_submit_button(driver):
    """
    Clica no botão de envio (login) no SIGAA.

    @param driver: Instância do driver do Selenium.
    """
    driver.find_element(By.XPATH, SUBMIT_BUTTON).click()

def login_into_sigaa(driver, USERNAME, PASSWORD):
    """
    Realiza o login no SIGAA usando as credenciais fornecidas.

    @param driver: Instância do driver do Selenium.
    @param USERNAME: Nome de usuário para login.
    @param PASSWORD: Senha para login.
    """
    insert_credentials_into_sigaa(driver, USERNAME, PASSWORD)
    click_submit_button(driver)

def login_into_sigaa_env(driver, env_var):
    """
    Realiza o login no SIGAA usando as credenciais armazenadas nas variáveis de ambiente.

    @param driver: Instância do driver do Selenium.
    @param env_var: Dicionário contendo as variáveis de ambiente (SIGAA_USER e SIGAA_PASS).
    """
    insert_credentials_into_sigaa_env(driver, env_var)
    click_submit_button(driver)

def accept_cookies(driver):
    """
    Aceita os cookies no SIGAA clicando no botão "Ciente".

    @param driver: Instância do driver do Selenium.
    """
    wait = WebDriverWait(driver, 10)
    button_ciente = wait.until(EC.visibility_of_element_located((By.XPATH, COOKIES_BUTTON)))
    button_ciente.click()