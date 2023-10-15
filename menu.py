import database_generator.json_generator as jg
from dotenv import dotenv_values # pip install python-dotenv
from crawlers.crawler_auth import CrawlerAuth
from crawlers.crawler_config import CrawlerConfig
from crawlers.type_search import TypeSearch
from calculate_indicators.calculate_all import calculate_all_indicators
from database_generator.load_database import load_indicators_database, generate_indicators_database
from config.date_descryption import START_YEAR, END_YEAR
from config.output_format import *
from config.display_descryption import *
from config.crawler_descryption import SCHEDULE
import time
from datetime import datetime

class RunCrawler:
    def __init__(self):
        clear_screen()
        self.username = ''
        self.password = ''
        self.offset = 0
        self.env = dotenv_values(".env")
        clear_log()
        
        print(SEPARATOR)
        centralize(f'{RIGHT_ARROW} Script start {LEFT_ARROW}')
        print(SEPARATOR)
    
    def run_timer(self):
        self.timer = Timer()
        self.timer.set_start_time()

    def end_timer(self):
        self.timer.print_elapsed_ctime()
        self.timer.create_timer_log()
        if SCHEDULE == True:
            time.sleep(SLEEP_TIME)
        else:
            input("Press enter to continue...")

    def run_crawler_auth(self):
        username = self.env['SIGAA_USER']
        password = self.env['SIGAA_PASS']
        
        if username != '' and password != '':
            self.username = username
            self.password = password
        else:    
            self.crawler_auth = CrawlerAuth()
            self.username, self.password = self.crawler_auth.run()

    def run_crawler_config(self):
        # self.crawler_config = CrawlerConfig()
        # self.offset = self.crawler_config.run(self.username, self.password)
        # centralize(f'Offset: {self.offset}')
        # if SCHEDULE == True:
        #     time.sleep(SLEEP_TIME)
        # else:
        #     input("Press enter to continue...")
        self.offset = 55

    def run_crawler_data(self):
        self.crawler_data = TypeSearch(self.username, self.password, self.offset)
        self.crawler_data.run()

    def generate_crawler_output(self):
        jg.generate_crawler_json(START_YEAR, END_YEAR)

    def begin(self):
        self.run_timer()
        self.run_crawler_auth()
        self.run_crawler_config()
        self.run_crawler_data()
        self.generate_crawler_output()
        self.end_timer()

class RunCalculateIndicators:
    def __init__(self):
        clear_screen()
        self.database = load_indicators_database()

    def output(self):
        centralize("Indicators calculated.")
        centralize("Verifique a pasta databases/indicators/")
        if SCHEDULE == True:
            time.sleep(SLEEP_TIME)
        else:
            input("Press enter to continue...")

    def begin(self):
        calculate_all_indicators(self.database)
        generate_indicators_database()
        self.output()

class Menu:
    def __init__(self):
        self.options = {
            '1': 'Run crawler',
            '2': 'Calculate indicators',
            '3': 'Exit'
        }

    def print_menu(self):
        clear_screen()
        print(SEPARATOR)
        for option, text in self.options.items():
            centralize(option + " - " + text)
        print(SEPARATOR)
    
    def get_option(self):
        option = input("Option: ")
        return option
    
    def run_option(self, option):
        if option == '1':
            run_crawler = RunCrawler()
            run_crawler.begin()
        elif option == '2':
            run_calculate_indicators = RunCalculateIndicators()
            run_calculate_indicators.begin()
        elif option == '3':
            exit()
        else:
            centralize("Invalid option.")

    def begin(self):
        if SCHEDULE == True:
            self.run_option('1')
            self.run_option('2')
            self.run_option('3')
        else:
            while True:
                self.print_menu()
                option = self.get_option()
                self.run_option(option)