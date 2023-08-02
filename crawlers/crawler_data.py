import pages.sigaa_pages as sp 
import database_generator.database_generator as dg
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.options import Options
from config.output_format import *
from config.url_descryption import *
from config.crawler_descryption import TYPE_SEARCH, TYPE_PERIOD

class MiniCrawlerParallel:
    def __init__(self):
        try:
            self.chrome_options = webdriver.ChromeOptions()
            self.chrome_options.add_argument("--headless=new")
            self.chrome_options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
            self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

            self.driver = webdriver.Chrome(options=self.chrome_options)
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
            
    def get_year(self, profile:str, year:int):
        dg.get_every_extension_activity_from_months(1, 12, year, self.driver, profile)

    def get_year_semester(self, profile:str, year:int, semester:int):
        if semester == 1:
            dg.get_every_extension_activity_from_months(1, 6, year, self.driver, profile)
        elif semester == 2:
            dg.get_every_extension_activity_from_months(7, 12, year, self.driver, profile)

    def get_year_quarter(self, profile:str, year:int, quarter:int):
        if quarter == 1:
            dg.get_every_extension_activity_from_months(1, 4, year, self.driver, profile)
        elif quarter == 2:
            dg.get_every_extension_activity_from_months(5, 8, year, self.driver, profile)
        elif quarter == 3:
            dg.get_every_extension_activity_from_months(9, 12, year, self.driver, profile)

    def get_year_trimester(self, profile:str, year:int, trimester:int):
        if trimester == 1:
            dg.get_every_extension_activity_from_months(1, 3, year, self.driver, profile)
        elif trimester == 2:
            dg.get_every_extension_activity_from_months(4, 6, year, self.driver, profile)
        elif trimester == 3:
            dg.get_every_extension_activity_from_months(7, 9, year, self.driver, profile)
        elif trimester == 4:
            dg.get_every_extension_activity_from_months(10, 12, year, self.driver, profile)

    def run(self, username:str, password:str, profile:str, year:int, semester:int=None, quarter:int=None, trimester:int=None):
        self.navigate_to_login_page()
        self.instance_login(username, password)
        self.navigate_to_extension_page()
        
        if TYPE_SEARCH == "PARALLEL":
            if TYPE_PERIOD == "YEAR":
                self.get_year(profile, year)
            elif TYPE_PERIOD == "SEMESTER":
                self.get_year_semester(profile, year, semester)
            elif TYPE_PERIOD == "QUARTER":
                self.get_year_quarter(profile, year, quarter)
            elif TYPE_PERIOD == "TRIMESTER":
                self.get_year_trimester(profile, year, trimester)
        elif TYPE_SEARCH == "LINEAR":
            self.get_year(profile, year)

        self.driver.quit()

class MiniCrawlerConcurrent:
    def __init__(self, username, password):
        try:
            self.chrome_options = webdriver.ChromeOptions()
            self.chrome_options.add_argument("--headless=new")
            # self.chrome_options.add_argument("--start-minimized")
            self.chrome_options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
            self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

            self.driver = webdriver.Chrome(options=self.chrome_options)
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
                    
        self.driver.get(LOGIN_PAGE)
        self.instance_login(username, password)
        self.navigate_to_extension_page()

    def quit(self):
        self.driver.quit()
    
    def instance_login(self, username:str, password:str):
        sp.login_into_sigaa(self.driver, username, password)
        
    def navigate_to_extension_page(self):
        self.driver.get(EXTENSION_PAGE)
            
    def get_year(self, perfil:str, year:int):
        dg.get_every_extension_activity_from_months(1, 12, year, self.driver, perfil)

    def get_year_month(self, perfil:str, year:int, month:int):
        dg.get_every_extension_activity_from_months(month, month, year, self.driver, perfil)

    def run(self, perfil:str, year:int, month:int):
        self.get_year_month(perfil, year, month)