# type_search.py

## @file
# Módulo para realizar a busca de dados de extensão.

import time
from tqdm import tqdm
from crawlers.crawler_data import MiniCrawlerConcurrent
from config.output_format import *
from config.display_descryption import *
from config.date_descryption import *
from config.crawler_descryption import MAX_THREADS, TYPE_SEARCH
from config.filter_descryption import AREA_CNPq
from concurrent.futures import ThreadPoolExecutor, as_completed

## Classe para realizar a busca de dados de extensão.
class TypeSearch():
    ## Método construtor da classe TypeSearch.
    # @param username Nome de usuário para login.
    # @param password Senha para login.
    # @param offset Deslocamento temporal.
    def __init__(self, username, password, offset):
        self.username = username
        self.password = password
        self.offset = offset
        
    ## Método para realizar a busca de dados de extensão de forma concorrente.
    def concurrent_search(self):
        lista = []
        for year in range(START_YEAR, END_YEAR+1):
            for month in range(FIRST_MONTH_OF_YEAR, LAST_MONTH_OF_YEAR+1):
                year_month = str(year) + '/' + str(month)
                month_year = str(month) + '/' + str(year)
                if month_year in SPECIAL_DATE:
                    for cnpq in AREA_CNPq:
                        lista.append(year_month + '/' + cnpq)
                else:
                    lista.append(year_month)

        desc = 'Loggin in'
        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            instances = [MiniCrawlerConcurrent(self.username, self.password) for _ in tqdm(range(MAX_THREADS), desc=desc, bar_format='{desc} - {elapsed} {bar} {n_fmt}/{total_fmt} - {percentage:.0f}%', ncols=SIZE_TERMINAL)]
        
        def get_instance_with_wait():
            while len(instances) == 0:
                time.sleep(1)  # Aguarda 1 segundo antes de tentar novamente
            instance = instances.pop(0)
            return instance

        def run_instance(username, password, year_month_cnpq):
            lista_year_month_cnpq = year_month_cnpq.split('/')
            year, month = map(int, lista_year_month_cnpq[:2])
            cnpq = lista_year_month_cnpq[2] if len(lista_year_month_cnpq) == 3 else None

            instance = get_instance_with_wait()
            instance.run(self.offset, year, month, cnpq)
            instances.append(instance)
            return year_month_cnpq

        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            futures = {executor.submit(run_instance, self.username, self.password, year_month_cnpq): year_month_cnpq  for year_month_cnpq in lista}
           
            for future in as_completed(futures):
                year_month_cnpq = futures[future]
                try:
                    future.result()
                except Exception as exc:
                    add_item_to_log(f'{year_month_cnpq} - generated an exception: {exc}')
                else:
                    add_item_to_log(f'{year_month_cnpq} - ok')

            for instance in instances:
                instance.quit()

    ## Método para realizar a busca de dados de extensão.
    def search(self):
        if TYPE_SEARCH == 'CONCURRENT':
            self.concurrent_search()
        else:
            centralize("Invalid type search")
    
    ## Método principal para executar o processo de busca de dados.
    def run(self):
        self.search()
