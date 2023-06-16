from components.database_formatter import format_special_char
from crawler import Crawler
import time
class Main:
    def __init__(self):
        pass
    
    def begin(self):
        start_time = time.time()
        print("Script start", start_time)
        crawler = Crawler()
        crawler.run()

        end_time = time.time()
        print("Script end", end_time)
        execution_time = end_time - start_time

        print(f"Execution time: {execution_time} seconds")
        print("Formatting file:")

        format_special_char()

if __name__ == "__main__":
    main_obj = Main()
    main_obj.begin()