import database_generator.json_generator as jg
from dotenv import dotenv_values # pip install python-dotenv
from crawlers.crawler_auth import CrawlerAuth
from crawlers.type_search import TypeSearch
from config.output_format import *
from config.date_descryption import START_YEAR, END_YEAR

class Main:
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

    def generate_output(self):
        jg.generate_json(START_YEAR, END_YEAR)

    def begin(self):
        self.run_timer()
        self.run_crawler_auth()
        self.run_crawler_data()
        self.generate_output()
        self.end_timer()

if __name__ == "__main__":
    main_obj = Main()
    main_obj.begin()