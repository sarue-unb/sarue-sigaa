from crawler import Crawler

class Main:
    def __init__(self):
        pass
    
    def begin(self):
        print("Script start")
        crawler = Crawler()
        crawler.run()
        print("Script end")

if __name__ == "__main__":
    main_obj = Main()
    main_obj.begin()