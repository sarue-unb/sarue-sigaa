import time
from tqdm import tqdm
from crawlers.crawler_data import MiniCrawlerParallel, MiniCrawlerConcurrent
from config.output_format import centralize, Timer
from config.date_descryption import START_YEAR, END_YEAR
from config.crawler_descryption import MAX_THREADS, TYPE_SEARCH, TYPE_PERIOD
from concurrent.futures import ThreadPoolExecutor

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
            # instances = {}
            # with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            #     for year in range(END_YEAR, START_YEAR-1, -1):
            #         for trimester in range(3,-1,-1):
            #             instance = MiniCrawlerParallel()
            #             instances[str(year)+"_"+str(trimester)] = instance
            #             executor.submit(instances[str(year)+"_"+str(trimester)].run, self.username, self.password, self.profile, year, None, None, trimester+1)    
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
        timer = self.timer = Timer()
        timer.set_start_time()
        # lista = [str(year) + '/' + str(month) for year in range(END_YEAR, START_YEAR-1, -1) for month in range(12, 0, -1)]
        lista = [str(year) + '/' + str(month) for year in range(START_YEAR, END_YEAR+1) for month in range(1, 12+1)]
        instances = [MiniCrawlerConcurrent(self.username, self.password) for _ in tqdm(range(MAX_THREADS))]
        timer.print_elapsed_ctime()

        def get_instance_with_wait():
            while len(instances) == 0:
                time.sleep(1)  # Aguarda 1 segundo antes de tentar novamente
            instance = instances.pop(0)
            return instance

        def run_instance(username, password, year_month):
            year, month = map(int, year_month.split('/'))
            
            instance = get_instance_with_wait()
            instance.run('discente', year, month)
            instances.append(instance)
            return year_month

        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            futures = [executor.submit(run_instance, self.username, self.password, year_month) for year_month in tqdm(lista)]

            for instance in instances:
                instance.quit()

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