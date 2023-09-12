import time
from tqdm import tqdm
from crawlers.crawler_data import MiniCrawlerParallel, MiniCrawlerConcurrent
from config.output_format import add_item_to_log, centralize, SIZE_TERMINAL
from config.date_descryption import *
from config.crawler_descryption import MAX_THREADS, TYPE_SEARCH, TYPE_PERIOD
from config.filter_descryption import AREA_CNPq
from concurrent.futures import ThreadPoolExecutor, as_completed

class TypeSearch():
    def __init__(self, username, password, profile):
        self.username = username
        self.password = password
        self.profile = profile

    def linear_search(self):
        instance = MiniCrawlerParallel()
        for year in range(START_YEAR, END_YEAR+1):
            instance.run(self.username, self.password, self.profile, year)

    def parallel_search(self):
        if TYPE_PERIOD == 'YEAR':
            instances = {}
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                for year in range(START_YEAR, END_YEAR+1):
                    instance = MiniCrawlerParallel()
                    instances[year] = instance
                    executor.submit(instances[year].run, self.username, self.password, self.profile, year)
        
        elif TYPE_PERIOD == 'SEMESTER':
            instances = {}
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                for year in range(START_YEAR, END_YEAR+1):
                    for semester in range(2):
                        instance = MiniCrawlerParallel()
                        instances[str(year)+"_"+str(semester)] = instance
                        executor.submit(instances[str(year)+"_"+str(semester)].run, self.username, self.password, self.profile, year, semester+1)
    
        elif TYPE_PERIOD == 'QUARTER':
            instances = {}
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                for year in range(START_YEAR, END_YEAR+1):
                    for quarter in range(3):
                        instance = MiniCrawlerParallel()
                        instances[str(year)+"_"+str(quarter)] = instance
                        executor.submit(instances[str(year)+"_"+str(quarter)].run, self.username, self.password, self.profile, year, None, quarter+1)    

        elif TYPE_PERIOD == 'TRIMESTER':
            instances = {}
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                for year in range(START_YEAR, END_YEAR+1):
                    for trimester in range(4):
                        instance = MiniCrawlerParallel()
                        instances[str(year)+"_"+str(trimester)] = instance
                        executor.submit(instances[str(year)+"_"+str(trimester)].run, self.username, self.password, self.profile, year, None, None, trimester+1)    

        else:
            centralize("Invalid type period")

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

        lista_errors = []
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
            if len(lista_year_month_cnpq) == 3:
                cnpq = lista_year_month_cnpq[2]
            else:
                cnpq = None

            instance = get_instance_with_wait()
            instance.run(self.profile, year, month, cnpq)
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
                    lista_errors.append(year_month_cnpq)
                else:
                    add_item_to_log(f'{year_month_cnpq} - ok')

            for instance in instances:
                instance.quit()

        if len(lista_errors) > 0:
            new_instance = MiniCrawlerConcurrent(self.username, self.password)
            for year_month_cnpq in lista_errors:
                centralize(f'Trying again: {year_month_cnpq}')
                lista_year_month_cnpq = year_month_cnpq.split('/')
                year, month = map(int, lista_year_month_cnpq[:2])
                if len(lista_year_month_cnpq) == 3:
                    cnpq = lista_year_month_cnpq[2]
                else:
                    cnpq = None

                new_instance.run(self.profile, year, month, cnpq)
            new_instance.quit()

    def search(self):
        if TYPE_SEARCH == 'PARALLEL':
            self.parallel_search()
        elif TYPE_SEARCH == 'CONCURRENT':
            self.concurrent_search()
        elif TYPE_SEARCH == 'LINEAR':
            self.linear_search()
        else:
            centralize("Invalid type search")
    
    def run(self):
        self.search()