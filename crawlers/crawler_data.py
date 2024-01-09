# crawler_data.py

## @file
# Módulo para a execução do web crawler de coleta de dados usando Selenium.

import pages.sigaa_pages as sp 
import database_generator.database_generator as dg
from selenium import webdriver
from config.display_descryption import *
from config.url_descryption import *
from config.crawler_descryption import INVISIBLE

## Classe para a execução do web crawler de coleta de dados.
class MiniCrawlerConcurrent:
    ## Método construtor da classe MiniCrawlerConcurrent.
    # @param username Nome de usuário para login.
    # @param password Senha para login.
    def __init__(self, username, password):
        try:
            self.chrome_service = webdriver.ChromeService()
            self.chrome_options = webdriver.ChromeOptions()

            self.chrome_service = webdriver.ChromeService(service_args=['--disable-build-check'])

            self.chrome_options.page_load_strategy = "normal"

            self.chrome_options.add_argument("--log-level=OFF")

            self.chrome_options.add_argument('headless') if INVISIBLE == True else self.chrome_options.add_argument('start-maximized')
            self.chrome_options.add_argument('disable-gpu')
            self.chrome_options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
            self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

            self.driver = webdriver.Chrome(service=self.chrome_service, options=self.chrome_options)

            self.navegador = "chrome"
        except Exception as e:
            try: 
                self.edge_options = webdriver.EdgeOptions()
                self.edge_service = webdriver.EdgeService()

                self.edge_options.page_load_strategy = "normal"

                self.edge_options.add_argument("--log-level=OFF")

                self.edge_options.use_chromium = True
                self.edge_options.add_argument('headless')
                self.edge_options.add_argument('disable-gpu')

                self.edge_options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
                self.edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
                self.driver = webdriver.Edge(service=self.edge_service, options=self.edge_options)

                self.navegador = "edge"
            except Exception as e:
                try: 
                    self.firefox_service = webdriver.FirefoxService()
                    self.firefox_options = webdriver.FirefoxOptions()

                    self.firefox_options.page_load_strategy = "normal"

                    self.firefox_options.add_argument("--log-level=OFF")

                    self.firefox_options.add_argument('-headless') if INVISIBLE == True else self.firefox_options.add_argument('start-maximized')

                    self.driver = webdriver.Firefox(service=self.firefox_service, options=self.firefox_options)
                    self.navegador = "firefox"
                except Exception as e:
                    centralize("Nenhum navegador encontrado")
                    self.navegador = None
                    exit(1)
                    
        self.driver.get(LOGIN_PAGE)
        self.instance_login(username, password)
        self.navigate_to_extension_page()
        self.accept_cookies()

    ## Método para encerrar a execução do web crawler.
    def quit(self):
        self.driver.quit()
    
    ## Método para realizar a instância de login com um nome de usuário e senha específicos.
    # @param username Nome de usuário para login.
    # @param password Senha para login.
    def instance_login(self, username:str, password:str):
        sp.login_into_sigaa(self.driver, username, password)
        
    ## Método para navegar até a página de extensão.
    def navigate_to_extension_page(self):
        self.driver.get(EXTENSION_PAGE)
            
    ## Método para aceitar os cookies na página web.
    def accept_cookies(self):
        sp.accept_cookies(self.driver)

    ## Método para obter os dados de atividades de extensão de um determinado mês e ano.
    # @param offset Deslocamento temporal.
    # @param year Ano desejado.
    # @param month Mês desejado.
    # @param cnpq Código CNPq (opcional).
    def get_year_month(self, offset:int, year:int, month:int, cnpq:str):
        if cnpq == None:
            dg.get_every_extension_activity_from_month_years(month, year, offset, self.driver)
        else:
            dg.get_every_extension_activity_from_month_years_passing_cnpq(month, year, cnpq, offset, self.driver)

    ## Método principal para executar o processo de coleta d
