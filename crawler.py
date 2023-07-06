import pages.extension_page as ep
import pages.sigaa_pages as sp 
import database_generator.database_generator as dg
import components.selection_components as sc

from selenium import webdriver # pip install selenium
from dotenv import dotenv_values # pip install python-dotenv
from output_format import *
from selenium.common.exceptions import StaleElementReferenceException
from concurrent.futures import ThreadPoolExecutor

START_YEAR = 2020
END_YEAR = 2023

class MiniCrawler:
    def __init__(self):
        try: 
            self.driver = webdriver.Safari()
            navegador = "safari"    
        except Exception as e:
            try:
                self.driver = webdriver.Chrome()
                navegador = "chrome"
            except Exception as e:
                try: 
                    self.driver = webdriver.Edge()
                    navegador = "edge"
                except Exception as e:
                    try: 
                        self.driver = webdriver.Firefox()
                        navegador = "firefox"
                    except Exception as e:
                        centralize("Nenhum navegador encontrado")
                        navegador = None
                        exit(1)
    
    def instance_login(self, username, password):
        sp.login_into_sigaa(self.driver, username, password)

    def navigate_to_extension_page(self):
        self.driver.get("https://sigaa.unb.br/sigaa/extensao/Atividade/lista.jsf")
            
    def run(self, year, perfil, username, password):
        self.driver.get("https://sigaa.unb.br/sigaa/")
        
        self.instance_login(username, password)
        self.navigate_to_extension_page()
        
        dg.get_every_extension_activity_from_years(year, year, self.driver, perfil)

        self.driver.quit()

# TRY LATER: Get login and password from sigaa login page
class Crawler:
    def __init__(self):
        try:
            self.driver = webdriver.Safari()
            navegador = "safari"
        except Exception as e:
            try:
                self.driver = webdriver.Chrome()
                navegador = "chrome"
            except Exception as e:
                try:
                    self.driver = webdriver.Edge()
                    navegador = "edge"
                except Exception as e:
                    try:
                        self.driver = webdriver.Firefox()
                        navegador = "firefox"
                    except Exception as e:
                        centralize("Nenhum navegador encontrado")
                        navegador = None
                        exit(1)

        self.env = dotenv_values(".env")

        centralize(f'Navegador Usado: {RIGHT_ARROW} {navegador.capitalize()} {LEFT_ARROW}')

    def instance_login(self):
        self.driver.implicitly_wait(10)

        username_xpath = "/html/body/div[2]/div[2]/div[4]/form/table/tbody/tr[1]/td/input"
        password_xpath = "/html/body/div[2]/div[2]/div[4]/form/table/tbody/tr[2]/td/input"

        username = sc.get_element_by_xpath(username_xpath, self.driver)
        password = sc.get_element_by_xpath(password_xpath, self.driver)
        
        while (self.driver.current_url not in pages_valid['discente'] and self.driver.current_url not in pages_valid['docente']):
            username = sc.get_element_by_xpath(username_xpath, self.driver)
            password = sc.get_element_by_xpath(password_xpath, self.driver)
            
            try:
                username = username.get_attribute("value")
                password = password.get_attribute("value")
            except StaleElementReferenceException:
                time.sleep(0.2)
                pass
            
            time.sleep(0.2)

        if self.driver.current_url in pages_valid['discente']:
            perfil = "discente"
        elif self.driver.current_url in pages_valid['docente']:
            perfil = "docente"

        centralize(f'{RIGHT_ARROW} Logged in as {perfil} {LEFT_ARROW}')
        return perfil, username, password

    def run(self):
        self.driver.get("https://sigaa.unb.br/sigaa/")

        self.perfil, username, password = self.instance_login()

        self.driver.quit()

        year_list = {}
        with ThreadPoolExecutor(max_workers=(END_YEAR-START_YEAR)+1) as executor:
            for year in range(START_YEAR, END_YEAR+1):
                year_instance = MiniCrawler()
                year_list[year] = year_instance
                executor.submit(year_instance.run, year, self.perfil, username, password)

