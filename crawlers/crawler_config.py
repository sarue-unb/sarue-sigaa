import pages.sigaa_pages as sp 
import database_generator.database_generator as dg
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from config.output_format import *
from config.url_descryption import *
from config.date_descryption import EMPTY_MONTH

class CrawlerConfig:
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

    def navigate_to_login_page(self):
        self.driver.get(LOGIN_PAGE)

    def navigate_to_extension_page(self):
        self.driver.get(EXTENSION_PAGE)
        
    def instance_login(self, username:str, password:str):
        sp.login_into_sigaa(self.driver, username, password)
            
    def get_offset(self):
        month, year = EMPTY_MONTH.split('/')
        return dg.get_offset(int(month), int(year), self.driver)
    
    def run(self, username:str, password:str):
        self.navigate_to_login_page()
        self.instance_login(username, password)
        self.navigate_to_extension_page()
        
        offset = self.get_offset()

        self.driver.quit()

        return offset