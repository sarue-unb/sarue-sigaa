import unittest
from dotenv import dotenv_values
from config.date_descryption import HAS_DATA_MONTH
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from config.url_descryption import *
import pages.sigaa_pages as sp
import components.selection_components as sc
from components.info_printer import get_row_data_printer
import crawlers.crawler_config as cc

from config.filter_descryption import *
from config.date_descryption import *

class TestData(unittest.TestCase):
    def setUp(self):
        self.chrome_service = Service()
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--headless=new")
        self.chrome_options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(service=self.chrome_service, options=self.chrome_options)
        self.env = dotenv_values(".env")
        self.username = self.env['SIGAA_USER']
        self.password = self.env['SIGAA_PASS']
        self.offset = 63 # baseado no perfil de coordenadora de extensão

    def testGetOffset(self):
        instance = cc.CrawlerConfig()
        offset = instance.run(self.username, self.password)

        self.assertEqual(offset, self.offset)

    def testLoginInstance(self):
        def _monthly_date_generator(month:int, year:int, monthEnd:bool) -> str:
            expetected_day = FIRST_DAY_OF_MONTH

            if monthEnd:
                expetected_day = MONTHS_LAST_DAY[month]

            # Sigaa does not accept single digit months
            if month < 10:
                month = '0' + str(month)

            #Sigaa automatically fills the slashes in the date
            return f'{expetected_day}{month}{year}'
        
        def _get_activities_from_list_printer(driver, month:int, year:int, cnpq:str=None):
            dictionary = {}
            activities_info = get_row_data_printer(driver, month, year, cnpq)
            for row in activities_info:
                dictionary[row["codigo"]] = row
            return dictionary
        
        self.driver.get(LOGIN_PAGE)
        sp.login_into_sigaa(self.driver, self.username, self.password)
        self.driver.get(EXTENSION_PAGE)
        
        month, year = HAS_DATA_MONTH.split('/')

        sc.clear_input_name(NAME_DATA_INICIO_EXECUCAO, self.driver)
        sc.clear_input_name(NAME_DATA_FIM_EXECUCAO, self.driver)

        start_date = _monthly_date_generator(int(month), int(year), False)
        end_date = _monthly_date_generator(int(month), int(year), True)

        sc.use_element_by_id(NAME_SELECT_BUSCAR_PERIODO, self.driver)
        sc.use_input_by_name(NAME_DATA_INICIO_EXECUCAO, start_date, self.driver)
        sc.use_input_by_name(NAME_DATA_FIM_EXECUCAO, end_date, self.driver)

        sc.make_search(self.driver)

        qtd = sc.get_rows_len(self.driver) 

        if (qtd > self.offset): # maior que a quantidade quando não tem ações para discentes
            output = _get_activities_from_list_printer(self.driver, int(month), int(year))
            # _get_activities_from_list_view(driver, month, year)

        self.assertEqual(len(output), 94)        

    def tearDown(self):
        pass