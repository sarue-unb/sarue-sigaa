# menu.py

## @file
# Módulo que define classes para execução de operações do sistema.

import database_generator.json_generator as jg
from dotenv import dotenv_values  # pip install python-dotenv
from crawlers.crawler_auth import CrawlerAuth
from crawlers.crawler_config import CrawlerConfig
from crawlers.type_search import TypeSearch
from calculate_indicators.calculate_all import calculate_all_indicators
from database_generator.load_database import load_indicators_database, generate_indicators_database
from database_generator.excel_generator import generate_excel_database
from config.date_descryption import START_YEAR, END_YEAR
from config.output_format import *
from config.display_descryption import *
from config.crawler_descryption import SCHEDULE
import time
from datetime import datetime

## Classe para executar o Crawler.
class RunCrawler:
    ## Método construtor da classe RunCrawler.
    def __init__(self):
        clear_screen()
        self.username = ''
        self.password = ''
        self.offset = 0
        self.env = dotenv_values(".env")
        clear_log()

        print(SEPARATOR)
        centralize(f'{RIGHT_ARROW} Início do Script {LEFT_ARROW}')
        print(SEPARATOR)

    ## Método para iniciar o temporizador.
    def run_timer(self):
        self.timer = Timer()
        self.timer.set_start_time()

    ## Método para finalizar o temporizador e gerar logs.
    def end_timer(self):
        self.timer.print_elapsed_ctime()
        self.timer.create_timer_log()
        if SCHEDULE == True:
            time.sleep(SLEEP_TIME)
        else:
            input("Pressione Enter para continuar...")

    ## Método para autenticar o Crawler.
    def run_crawler_auth(self):
        username = self.env['SIGAA_USER']
        password = self.env['SIGAA_PASS']

        if username != '' and password != '':
            self.username = username
            self.password = password
        else:
            self.crawler_auth = CrawlerAuth()
            self.username, self.password = self.crawler_auth.run()

    ## Método para configurar o Crawler.
    def run_crawler_config(self):
        # self.crawler_config = CrawlerConfig()
        # self.offset = self.crawler_config.run(self.username, self.password)
        # centralize(f'Offset: {self.offset}')
        # if SCHEDULE == True:
        #     time.sleep(SLEEP_TIME)
        # else:
        #     input("Pressione Enter para continuar...")
        self.offset = 55

    ## Método para obter dados usando o Crawler.
    def run_crawler_data(self):
        self.crawler_data = TypeSearch(self.username, self.password, self.offset)
        self.crawler_data.run()

    ## Método para gerar a saída do Crawler em formato JSON.
    def generate_crawler_output(self):
        jg.generate_crawler_json(START_YEAR, END_YEAR)

    ## Método principal para iniciar o script do Crawler.
    def begin(self):
        self.run_timer()
        self.run_crawler_auth()
        self.run_crawler_config()
        self.run_crawler_data()
        self.generate_crawler_output()
        self.end_timer()

## Classe para executar o cálculo de indicadores.
class RunCalculateIndicators:
    ## Método construtor da classe RunCalculateIndicators.
    def __init__(self):
        clear_screen()
        self.database = load_indicators_database()

    ## Método para exibir a saída após o cálculo dos indicadores.
    def output(self):
        centralize("Indicadores calculados.")
        centralize("Verifique a pasta databases/indicators/")
        if SCHEDULE == True:
            time.sleep(SLEEP_TIME)
        else:
            input("Pressione Enter para continuar...")

    ## Método principal para iniciar o cálculo dos indicadores.
    def begin(self):
        calculate_all_indicators(self.database)
        generate_indicators_database()
        self.output()

## Classe para gerar um arquivo Excel a partir dos dados.
class RunGenerateExcel:
    ## Método construtor da classe RunGenerateExcel.
    def __init__(self):
        clear_screen()

    ## Método para exibir a saída após a geração do arquivo Excel.
    def output(self):
        centralize("Excel gerado.")
        centralize("Verifique a pasta databases/outputs/")
        if SCHEDULE == True:
            time.sleep(SLEEP_TIME)
        else:
            input("Pressione Enter para continuar...")

    ## Método principal para iniciar a geração do arquivo Excel.
    def begin(self):
        generate_excel_database()
        self.output()

## Classe para alterar configurações do sistema.
class RunChangeConfig:
    ## Método construtor da classe RunChangeConfig.
    def __init__(self):
        self.options = {
            '1': 'Alterar credenciais',
            '2': 'Sair',
        }

        self.username = ''
        self.password = ''
        self.env = dotenv_values(".env")

    ## Método para imprimir o menu de opções.
    def print_menu(self):
        clear_screen()
        print(SEPARATOR)
        for option, text in self.options.items():
            centralize(option + " - " + text)
        print(SEPARATOR)

    ## Método para obter a opção escolhida pelo usuário.
    def get_option(self):
        option = input("Opção: ")
        return option

    ## Método para executar a opção escolhida pelo usuário.
    def run_option(self, option):
        if option == '1':
            self.crawler_auth = CrawlerAuth()
            self.username, self.password = self.crawler_auth.run()
            with open('.env', 'w') as f:
                f.write(f'# NÃO FAÇA COMMIT DE SEU LOGIN E INFORMAÇÕES\n')
                f.write(f'SIGAA_USER = "{self.username}"\n')
                f.write(f'SIGAA_PASS = "{self.password}"\n')
        elif option == '2':
            exit()
        else:
            centralize("Opção inválida.")

    ## Método para autenticar o Crawler.
    def run_crawler_auth(self):
        username = self.env['SIGAA_USER']
        password = self.env['SIGAA_PASS']

        if username != '' and password != '':
            self.username = username
            self.password = password
        else:
            self.crawler_auth = CrawlerAuth()
            self.username, self.password = self.crawler_auth.run()

    ## Método principal para iniciar a alteração de configurações.
    def begin(self):
        while True:
            self.print_menu()
            option = self.get_option()
            self.run_option(option)

## Classe que define o menu principal do sistema.
class Menu:
    ## Método construtor da classe Menu.
    def __init__(self):
        self.options = {
            '1': 'Executar Crawler',
            '2': 'Calcular indicadores',
            '3': 'Gerar Excel',
            '4': 'Configurações',
            '5': 'Sair'
        }

    ## Método para imprimir o menu principal.
    def print_menu(self):
        clear_screen()
        print(SEPARATOR)
        for option, text in self.options.items():
            centralize(option + " - " + text)
        print(SEPARATOR)
    
    ## Método para obter a opção escolhida pelo usuário.
    def get_option(self):
        option = input("Opção: ")
        return option
    
    ## Método para executar a opção escolhida pelo usuário.
    def run_option(self, option):
        if option == '1':
            run_crawler = RunCrawler()
            run_crawler.begin()
        elif option == '2':
            run_calculate_indicators = RunCalculateIndicators()
            run_calculate_indicators.begin()
        elif option == '3':
            run_generate_excel = RunGenerateExcel()
            run_generate_excel.begin()
        elif option == '4':
            run_crawler = RunChangeConfig()
            run_crawler.begin()
        elif option == '5':
            exit()
        else:
            centralize("Opção inválida.")

    ## Método principal para iniciar o menu do sistema.
    def begin(self):
        if SCHEDULE == True:
            self.run_option('1')
            self.run_option('2')
            self.run_option('3')
            self.run_option('5')
        else:
            while True:
                self.print_menu()
                option = self.get_option()
                self.run_option(option)