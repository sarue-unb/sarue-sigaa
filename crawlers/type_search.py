from concurrent.futures import ThreadPoolExecutor
from crawlers.crawler_data import MiniCrawlerParallel
from config.output_format import centralize
from config.date_descryption import START_YEAR, END_YEAR
from config.crawler_descryption import MAX_THREADS, TYPE_SEARCH, TYPE_PERIOD


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
        pass
        # lista = [str(year) + '/' + str(month) for year in range(END_YEAR, START_YEAR-1, -1) for month in range(12, -1, -1)]

        # def execute_instance(year_month):
        #     year, month = map(int, year_month.split('/'))
        #     instance = free_instances.get()  # Obtem uma instância da fila
        #     instance.run('discente', year, month)
        #     free_instances.put(instance)  # Devolve a instância para a fila

        # free_instances = queue.Queue()

        # # Preenche a fila com instâncias
        # for _ in range(MAX_THREADS):
        #     free_instances.put(MiniCrawlerK(username, password))

        # with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        #     executor.map(execute_instance, lista)

        # # lista = [str(year) + '/' + str(month) for year in range(END_YEAR, START_YEAR-1, -1) for month in range(12, -1, -1)]
        # # instances = [MiniCrawlerK(username, password) for i in range(MAX_THREADS)]

        # # def execute_instance(instance, year, month):
        # #     instance.run('discente', year, month)

        # # with ThreadPoolExecutor() as executor:
        # #     while len(lista) > 0:
        # #         year_month = lista.pop(0)
        # #         year, month = year_month.split('/')
        # #         year, month = int(year), int(month)

        # #         # Pegar a primeira instância que estiver livre e executar a função em uma nova thread
        # #         for instance in instances:
        # #             if instance not in executor._threads:  # Verifica se a thread está disponível
        # #                 executor.submit(execute_instance, instance, year, month)
        # #                 break
        # # lista = [str(year) + '/' + str(month) for month in range(1, 13) for year in range(START_YEAR, END_YEAR + 1)]
        # # lista.reverse()

        # # semaphore = threading.BoundedSemaphore(MAX_THREADS)

        # # with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        # #     instances = {MiniCrawler_keeped(username, password):True for _ in tqdm(range(MAX_THREADS), desc='Logging in', bar_format='{desc} - {elapsed} {bar} - {percentage:.0f}%', ncols=SIZE_TERMINAL)}

        # # while len(lista) > 0:
        # #     threads = []
        # #     for instance in instances:
        # #         if instances[instance]:
        # #             try:
        # #                 semaphore.acquire()
        # #                 month = lista.pop()
        # #                 thread = threading.Thread(target=instance.run, args=(self.perfil, username, password, type_search, START_YEAR, None, None, None, month))
        # #                 thread.start()
        # #                 threads.append(thread)
        # #             except IndexError:
        # #                 break
        # #             except Exception as e:
        # #                 print(e)
        # #             finally:
        # #                 semaphore.release()

        # # # Aguarda a finalização de todas as threads
        # # for thread in threads:
        # #     thread.join()

        # # time.sleep(1)
        # # clear_screen()

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