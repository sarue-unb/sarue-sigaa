# crawler_config.py

## @file
# Módulo para configuração do web crawler usando Selenium.

import pages.sigaa_pages as sp 
import database_generator.database_generator as dg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from config.display_descryption import *
from config.url_descryption import *
from config.date_descryption import EMPTY_MONTH

## Classe para configurar o web crawler e obter informações do usuário.
class CrawlerConfig:
    ## Método construtor da classe CrawlerConfig.
    def __init__(self):
        try:
            self.chrome_service = Service()
            self.chrome_options = webdriver.ChromeOptions()
            self.chrome_options.add_argument("--headless=new")
            self.chrome_options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
            self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

            self.driver = webdriver.Chrome(service=self.chrome_service, options=self.chrome_options)
            self.navegador = "chrome"
        except Exception as e:
            try: 
                self.firefox_options = Options()
                self.firefox_options.headless = True    

                self.driver = webdriver.Firefox(options=self.firefox_options)
                self.navegador = "firefox"
            except Exception as e:
                try: 
                    self.driver = webdriver.Edge()
                    self.navegador = "edge"
                except Exception as e:
                    centralize("Nenhum navegador encontrado")
                    self.navegador = None
                    exit(1)

    ## Método para navegar até a página de login.
    def navigate_to_login_page(self):
        self.driver.get(LOGIN_PAGE)

    ## Método para navegar até a página de extensão.
    def navigate_to_extension_page(self):
        self.driver.get(EXTENSION_PAGE)
        
    ## Método para realizar a instância de login com um nome de usuário e senha específicos.
    # @param username Nome de usuário para login.
    # @param password Senha para login.
    def instance_login(self, username:str, password:str):
        sp.login_into_sigaa(self.driver, username, password)
            
    ## Método para obter o deslocamento (offset) do web crawler.
    # @return O valor do offset.
    def get_offset(self):
        month, year = EMPTY_MONTH.split('/')
        return dg.get_offset(int(month), int(year), self.driver)
    
    ## Método principal para executar o processo de configuração do web crawler.
    # @param username Nome de usuário para login.
    # @param password Senha para login.
    # @return O valor do offset obtido durante a configuração.
    def run(self, username:str, password:str):
        self.navigate_to_login_page()
        self.instance_login(username, password)
        self.navigate_to_extension_page()
        
        offset = self.get_offset()

        self.driver.quit()

        return offset
