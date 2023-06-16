from crawler import Crawler
from output_format import Timer

class Main:
    def __init__(self):
        pass
    
    def begin(self):
        print("Script start")
        timer = Timer()
        crawler = Crawler()
        timer.set_start_time()
        crawler.run()
        timer.print_elapsed_ctime()
        input("Press enter to exit")

if __name__ == "__main__":
    main_obj = Main()
    main_obj.begin()