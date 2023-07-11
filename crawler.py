import pages.extension_page as ep
import pages.sigaa_pages as sp 
import database_generator.database_generator as dg
import database_generator.json_generator as jg
import components.selection_components as sc

from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.options import Options
from dotenv import dotenv_values # pip install python-dotenv
from output_format import *
from selenium.common.exceptions import StaleElementReferenceException
from concurrent.futures import ThreadPoolExecutor

START_YEAR = 2020
END_YEAR = 2023
MAX_THREADS = 8

class MiniCrawler:
    def __init__(self):
        try:
            self.chrome_options = webdriver.ChromeOptions()
            self.chrome_options.add_argument("--headless=new")

            self.driver = webdriver.Chrome(options=self.chrome_options)
            self.driver = webdriver.Chrome()
            navegador = "chrome"
        except Exception as e:
            try: 
                self.firefox_options = Options()
                self.firefox_options.headless = True    

                self.driver = webdriver.Firefox(options=self.firefox_options)
                navegador = "firefox"
            except Exception as e:
                try: 
                    self.driver = webdriver.Edge()
                    navegador = "edge"
                except Exception as e:
                    centralize("Nenhum navegador encontrado")
                    navegador = None
                    exit(1)
    
    def instance_login(self, username, password):
        sp.login_into_sigaa(self.driver, username, password)
        
    def navigate_to_extension_page(self):
        self.driver.get(sp.EXTENSION_PAGE)
            
    def get_year(self, year, perfil):
        dg.get_every_extension_activity_from_months(1, 12, year, self.driver, perfil)

    def get_year_semester(self, year, perfil, semester):
        if semester == 1:
            dg.get_every_extension_activity_from_months(1, 6, year, self.driver, perfil)
        elif semester == 2:
            dg.get_every_extension_activity_from_months(7, 12, year, self.driver, perfil)

    def get_year_quarter(self, year, perfil, quarter):
        if quarter == 1:
            dg.get_every_extension_activity_from_months(1, 4, year, self.driver, perfil)
        elif quarter == 2:
            dg.get_every_extension_activity_from_months(5, 8, year, self.driver, perfil)
        elif quarter == 3:
            dg.get_every_extension_activity_from_months(9, 12, year, self.driver, perfil)

    def get_year_trimester(self, year, perfil, trimester):
        if trimester == 1:
            dg.get_every_extension_activity_from_months(1, 3, year, self.driver, perfil)
        elif trimester == 2:
            dg.get_every_extension_activity_from_months(4, 6, year, self.driver, perfil)
        elif trimester == 3:
            dg.get_every_extension_activity_from_months(7, 9, year, self.driver, perfil)
        elif trimester == 4:
            dg.get_every_extension_activity_from_months(10, 12, year, self.driver, perfil)

    def run(self, perfil, username, password, type_search, year, semester=None, quarter=None, trimester=None, group=None):
        self.driver.get(sp.LOGIN_PAGE)

        self.instance_login(username, password)
      
        self.navigate_to_extension_page()
        
        if type_search == "year":
            self.get_year(year, perfil)
        elif type_search == "semester":
            self.get_year_semester(year, perfil, semester)
        elif type_search == "quarter":
            self.get_year_quarter(year, perfil, quarter)
        elif type_search == "trimester":
            self.get_year_trimester(year, perfil, trimester)
        elif type_search == "linear":
            self.get_year(year, perfil)

        self.driver.quit()

class Crawler:
    def __init__(self):
        try:
            self.driver = webdriver.Chrome()
            self.navegador = "chrome"
        except Exception as e:
            try:
                self.driver = webdriver.Edge()
                self.navegador = "edge"
            except Exception as e:
                try:
                    self.driver = webdriver.Firefox()
                    self.navegador = "firefox"
                except Exception as e:
                    try:
                        self.driver = webdriver.Safari()
                        self.navegador = "safari"
                    except Exception as e:
                        centralize("Nenhum navegador encontrado")
                        self.navegador = None
                        exit(1)

        self.env = dotenv_values(".env")

        centralize(f'Navegador Usado: {RIGHT_ARROW} {self.navegador.capitalize()} {LEFT_ARROW}')

    def instance_login(self):
        self.driver.implicitly_wait(20)

        sp.insert_credencials_into_sigaa_env(self.driver, self.env)
        
        username = sc.get_element_by_xpath(sp.USERNAME_XPATH, self.driver)
        password = sc.get_element_by_xpath(sp.PASSWORD_XPATH, self.driver)
        
        sp.click_submit_button(self.driver)

        while (self.driver.current_url not in pages_valid['discente'] and self.driver.current_url not in pages_valid['docente']):
            username = sc.get_element_by_xpath(sp.USERNAME_XPATH, self.driver)
            password = sc.get_element_by_xpath(sp.PASSWORD_XPATH, self.driver)
            
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

    def search(self, type_search, username, password):
        if type_search == 'year':
            year_list = {}
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                for year in range(START_YEAR, END_YEAR+1):
                    year_instance = MiniCrawler()
                    year_list[year] = year_instance
                    executor.submit(year_instance.run, self.perfil, username, password, type_search, year)
        
        elif type_search == 'semester':
            semester = {}
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                for year in range(START_YEAR, END_YEAR+1):
                    for i in range(2):
                        semester_instance = MiniCrawler()
                        semester[str(year)+"_"+str(i)] = semester_instance
                        executor.submit(semester[str(year)+"_"+str(i)].run, self.perfil, username, password, type_search, year, i+1)
        
        elif type_search == 'quarter':
            quarter = {}
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                for year in range(START_YEAR, END_YEAR+1):
                    for i in range(2):
                        quarter_instance = MiniCrawler()
                        quarter[str(year)+"_"+str(i)] = quarter_instance
                        executor.submit(quarter[str(year)+"_"+str(i)].run, self.perfil, username, password, type_search, year, None, i+1)
        

        elif type_search == 'trimester':                
            trimester = {}
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                for year in range(START_YEAR, END_YEAR+1):
                    for i in range(4):
                        trimester_instance = MiniCrawler()
                        trimester[str(year)+"_"+str(i)] = trimester_instance
                        executor.submit(trimester[str(year)+"_"+str(i)].run, self.perfil, username, password, type_search, year, None, None, i+1)

        elif type_search == 'linear':
            for year in range(START_YEAR, END_YEAR+1):
                instance = MiniCrawler()
                instance.run(self.perfil, username, password, type_search, year)

    def run(self):
        self.driver.get(sp.LOGIN_PAGE)

        self.perfil, username, password = self.instance_login()
       
        self.driver.quit()

        self.search("year", username, password)
        # self.search("semester", username, password)
        # self.search("quarter", username, password)
        # self.search("trimester", username, password)
        # self.search("linear", username, password)

        jg.generate_json(START_YEAR, END_YEAR)

