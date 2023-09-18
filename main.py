import database_generator.json_generator as jg
from dotenv import dotenv_values # pip install python-dotenv
from crawlers.crawler_auth import CrawlerAuth
from crawlers.type_search import TypeSearch
from calculate_indicators.calculate_all import calculate_all_indicators
from database_generator.load_database import load_indicators_database, generate_indicators_database
from config.output_format import *
from config.date_descryption import START_YEAR, END_YEAR

class RunCrawler:
    def __init__(self):
        clear_screen()
        self.username = ''
        self.password = ''
        self.profile = ''
        self.env = dotenv_values(".env")

        print(SEPARATOR)
        centralize(f'{RIGHT_ARROW} Script start {LEFT_ARROW}')
        print(SEPARATOR)
    
    def run_timer(self):
        self.timer = Timer()
        self.timer.set_start_time()

    def end_timer(self):
        self.timer.print_elapsed_ctime()
        input("Press enter to continue...")

    def run_crawler_auth(self):
        username = self.env['SIGAA_USER']
        password = self.env['SIGAA_PASS']
        profile = self.env['SIGAA_PROFILE']

        if username != '' and password != '':
            self.username = username
            self.password = password
            self.profile = profile
        else:    
            self.crawler_auth = CrawlerAuth()
            self.username, self.password, self.profile = self.crawler_auth.run()

    def run_crawler_data(self):
        self.crawler_data = TypeSearch(self.username, self.password, self.profile)
        self.crawler_data.run()

    def generate_crawler_output(self):
        jg.generate_crawler_json(START_YEAR, END_YEAR)

    def begin(self):
        self.run_timer()
        self.run_crawler_auth()
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
        input("Press enter to continue...")

    def begin(self):
        calculate_all_indicators(self.database)
        generate_indicators_database()
        self.output()

class Main:
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
        while True:
            self.print_menu()
            option = self.get_option()
            self.run_option(option)

if __name__ == "__main__":
    main_obj = Main()
    main_obj.begin()