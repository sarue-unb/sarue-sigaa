import pages.sigaa_pages as sp 
import database_generator.database_generator as dg
from selenium import webdriver
from config.display_descryption import *
from config.url_descryption import *
from config.crawler_descryption import TYPE_SEARCH, TYPE_PERIOD, INVISIBLE

class MiniCrawlerParallel:
    def __init__(self):
        try:
            self.chrome_service = webdriver.ChromeService()
            self.chrome_options = webdriver.ChromeOptions()

            # self.chrome_options.page_load_strategy = "normal"

            # self.chrome_options.add_argument("--log-level=OFF")

            self.chrome_options.add_argument('--headless=new') if INVISIBLE == True else self.chrome_options.add_argument('start-maximized')
            # self.chrome_options.add_argument('disable-gpu')
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
                self.edge_options.add_argument('--headless=new') if INVISIBLE == True else self.chrome_options.add_argument('start-maximized')
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
                    
    def navigate_to_login_page(self):
        self.driver.get(LOGIN_PAGE)

    def navigate_to_extension_page(self):
        self.driver.get(EXTENSION_PAGE)

    def accept_cookies(self):
        sp.accept_cookies(self.driver)
        
    def instance_login(self, username:str, password:str):
        sp.login_into_sigaa(self.driver, username, password)
            
    def get_year(self, offset:int, year:int):
        dg.get_every_extension_activity_from_months(1, 12, year, offset, self.driver)

    def get_year_semester(self, offset:int, year:int, semester:int):
        if semester == 1:
            dg.get_every_extension_activity_from_months(1, 6, year, offset, self.driver)
        elif semester == 2:
            dg.get_every_extension_activity_from_months(7, 12, year, offset, self.driver)

    def get_year_quarter(self, offset:int, year:int, quarter:int):
        if quarter == 1:
            dg.get_every_extension_activity_from_months(1, 4, year, offset, self.driver)
        elif quarter == 2:
            dg.get_every_extension_activity_from_months(5, 8, year, offset, self.driver)
        elif quarter == 3:
            dg.get_every_extension_activity_from_months(9, 12, year, offset, self.driver)

    def get_year_trimester(self, offset:int, year:int, trimester:int):
        if trimester == 1:
            dg.get_every_extension_activity_from_months(1, 3, year, offset, self.driver)
        elif trimester == 2:
            dg.get_every_extension_activity_from_months(4, 6, year, offset, self.driver)
        elif trimester == 3:
            dg.get_every_extension_activity_from_months(7, 9, year, offset, self.driver)
        elif trimester == 4:
            dg.get_every_extension_activity_from_months(10, 12, year, offset, self.driver)

    def run(self, username:str, password:str, offset:int, year:int, semester:int=None, quarter:int=None, trimester:int=None):
        self.navigate_to_login_page()
        self.instance_login(username, password)
        self.navigate_to_extension_page()
        self.accept_cookies()
        
        if TYPE_SEARCH == "PARALLEL":
            if TYPE_PERIOD == "YEAR":
                self.get_year(offset, year)
            elif TYPE_PERIOD == "SEMESTER":
                self.get_year_semester(offset, year, semester)
            elif TYPE_PERIOD == "QUARTER":
                self.get_year_quarter(offset, year, quarter)
            elif TYPE_PERIOD == "TRIMESTER":
                self.get_year_trimester(offset, year, trimester)
        elif TYPE_SEARCH == "LINEAR":
            self.get_year(offset, year)

        self.driver.quit()

class MiniCrawlerConcurrent:
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

    def quit(self):
        self.driver.quit()
    
    def instance_login(self, username:str, password:str):
        sp.login_into_sigaa(self.driver, username, password)
        
    def navigate_to_extension_page(self):
        self.driver.get(EXTENSION_PAGE)
            
    def accept_cookies(self):
        sp.accept_cookies(self.driver)

    def get_year_month(self, offset:int, year:int, month:int, cnpq:str):
        if cnpq == None:
            dg.get_every_extension_activity_from_month_years(month, year, offset, self.driver)
        else:
            dg.get_every_extension_activity_from_month_years_passing_cnpq(month, year, cnpq, offset, self.driver)

    def run(self, offset:int, year:int, month:int, cnpq:str):
        self.get_year_month(offset, year, month, cnpq)