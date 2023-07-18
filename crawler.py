import queue
import threading
import pages.extension_page as ep
import pages.sigaa_pages as sp 
import database_generator.database_generator as dg
import database_generator.json_generator as jg
import components.selection_components as sc

from dotenv import dotenv_values # pip install python-dotenv
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.options import Options
from output_format import *
from selenium.common.exceptions import StaleElementReferenceException
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm # pip install tqdm

START_YEAR = 2020
END_YEAR = 2020
MAX_THREADS = 4

class MiniCrawler:
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

    def instance_login(self, username:str, password:str):
        sp.login_into_sigaa(self.driver, username, password)
        
    def navigate_to_extension_page(self):
        self.driver.get(sp.EXTENSION_PAGE)
            
    def get_year(self, perfil:str, year:int):
        dg.get_every_extension_activity_from_months(1, 12, year, self.driver, perfil)

    def get_year_semester(self, perfil:str, year:int, semester:int):
        if semester == 1:
            dg.get_every_extension_activity_from_months(1, 6, year, self.driver, perfil)
        elif semester == 2:
            dg.get_every_extension_activity_from_months(7, 12, year, self.driver, perfil)

    def get_year_quarter(self, perfil:str, year:int, quarter:int):
        if quarter == 1:
            dg.get_every_extension_activity_from_months(1, 4, year, self.driver, perfil)
        elif quarter == 2:
            dg.get_every_extension_activity_from_months(5, 8, year, self.driver, perfil)
        elif quarter == 3:
            dg.get_every_extension_activity_from_months(9, 12, year, self.driver, perfil)

    def get_year_trimester(self, perfil:str, year:int, trimester:int):
        if trimester == 1:
            dg.get_every_extension_activity_from_months(1, 3, year, self.driver, perfil)
        elif trimester == 2:
            dg.get_every_extension_activity_from_months(4, 6, year, self.driver, perfil)
        elif trimester == 3:
            dg.get_every_extension_activity_from_months(7, 9, year, self.driver, perfil)
        elif trimester == 4:
            dg.get_every_extension_activity_from_months(10, 12, year, self.driver, perfil)

    def run(self, perfil:str, username:str, password:str, type_search:str, year:int, semester:int=None, quarter:int=None, trimester:int=None, month:int=None):
        self.driver.get(sp.LOGIN_PAGE)
        self.instance_login(username, password)
        self.navigate_to_extension_page()
        
        if type_search == "year":
            self.get_year(perfil, year)
        elif type_search == "semester":
            self.get_year_semester(perfil, year, semester)
        elif type_search == "quarter":
            self.get_year_quarter(perfil, year, quarter)
        elif type_search == "trimester":
            self.get_year_trimester(perfil, year, trimester)
        elif type_search == "linear":
            self.get_year(perfil, year)

        self.driver.quit()

# This is a WIP, it's not working yet
# Trying to use threads to speed up the process
class MiniCrawler_keeped:
    def __init__(self, username, password):
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
        self.driver.get(sp.LOGIN_PAGE)
        self.instance_login(username, password)
        self.navigate_to_extension_page()

    def quit(self):
        self.driver.quit()
    
    def instance_login(self, username:str, password:str):
        sp.login_into_sigaa(self.driver, username, password)
        
    def navigate_to_extension_page(self):
        self.driver.get(sp.EXTENSION_PAGE)
            
    def get_year(self, perfil:str, year:int):
        dg.get_every_extension_activity_from_months(1, 12, year, self.driver, perfil)

    def get_year_month(self, perfil:str, year:int, month:int):
        dg.get_every_extension_activity_from_months(month, month, year, self.driver, perfil)

    def run(self, perfil:str, username:str, password:str, type_search:str, year:int, semester:int=None, quarter:int=None, trimester:int=None, month:int=None):
        if type_search == "linear":
            self.get_year(perfil, year)
        elif type_search == "group":
            self.get_year_month(perfil, year, month)

class Crawler:
    def __init__(self):
        try:
            self.chrome_options = webdriver.ChromeOptions()
            self.chrome_options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
            self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

            self.driver = webdriver.Chrome(options=self.chrome_options)
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

    # Only for testing
    def auto_login(self):
        username = self.env['SIGAA_USER']
        password = self.env['SIGAA_PASS']
        perfil = "discente"
        return perfil, username, password

    def search(self, type_search, username, password):
        if type_search == 'year':
            instances = {}
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                for year in range(START_YEAR, END_YEAR+1):
                    year_instance = MiniCrawler()
                    instances[year] = year_instance
                    executor.submit(year_instance.run, self.perfil, username, password, type_search, year)
        
        elif type_search == 'semester':
            instances = {}
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                for year in range(START_YEAR, END_YEAR+1):
                    for i in range(2):
                        semester_instance = MiniCrawler()
                        instances[str(year)+"_"+str(i)] = semester_instance
                        executor.submit(instances[str(year)+"_"+str(i)].run, self.perfil, username, password, type_search, year, i+1)
        
        elif type_search == 'quarter':
            instances = {}
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                for year in range(START_YEAR, END_YEAR+1):
                    for i in range(2):
                        quarter_instance = MiniCrawler()
                        instances[str(year)+"_"+str(i)] = quarter_instance
                        executor.submit(instances[str(year)+"_"+str(i)].run, self.perfil, username, password, type_search, year, None, i+1)    

        elif type_search == 'trimester':                
            instances = {}
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                for year in range(START_YEAR, END_YEAR+1):
                    for i in range(4):
                        trimester_instance = MiniCrawler()
                        instances[str(year)+"_"+str(i)] = trimester_instance
                        executor.submit(instances[str(year)+"_"+str(i)].run, self.perfil, username, password, type_search, year, None, None, i+1)

        elif type_search == 'linear':
            instance = MiniCrawler()
            for year in range(START_YEAR, END_YEAR+1):
                instance.run(self.perfil, username, password, type_search, year)
                
        elif type_search == 'group':
            lista = [str(year) + '/' + str(month) for month in range(1, 13) for year in range(START_YEAR, END_YEAR + 1)]
            lista.reverse()
            instances_status = [True] * MAX_THREADS
            semaphore = threading.BoundedSemaphore(MAX_THREADS)

            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                instances = [MiniCrawler_keeped(username, password) for _ in tqdm(range(MAX_THREADS), desc='Logging in', bar_format='{desc} - {elapsed} {bar} - {percentage:.0f}%', ncols=SIZE_TERMINAL)]

            def execute_task(year, month, index):
                instance = instances[index]
                instance.run(self.perfil, username, password, type_search, int(year), None, None, None, int(month))
                instances_status[index] = True
                semaphore.release()

            threads = []

            for year_month in lista:
                year, month = year_month.split('/')

                semaphore.acquire()
                index = next((index for index, status in enumerate(instances_status) if status), None)

                if index is not None:
                    instances_status[index] = False
                    thread = threading.Thread(target=execute_task, args=(year, month, index))
                    thread.start()
                    threads.append(thread)

            # Aguarda a finalização de todas as threads
            for thread in threads:
                thread.join()

            time.sleep(1)
            clear_screen()

    def run(self):
        # self.driver.get(sp.LOGIN_PAGE)
        # self.perfil, username, password = self.instance_login()
        self.driver.quit()

        self.perfil, username, password = self.auto_login()

        # self.search("year", username, password)
        # self.search("semester", username, password)
        # self.search("quarter", username, password) # 8 - 32:01 16 - 
        self.search("trimester", username, password) # 8 - 36:38 16 - 32:01
        # self.search("linear", username, password)
        # self.search("group", username, password)
        # self.search("test", username, password)

        jg.generate_json(START_YEAR, END_YEAR)

