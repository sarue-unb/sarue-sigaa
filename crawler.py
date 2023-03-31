from selenium import webdriver
import time
import components.selection_components as dc
import pages.sigaa_pages as sp
import pages.extension_page as ep
from dotenv import dotenv_values


class Crawler:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.env = dotenv_values(".env")
        
    
    def run(self):
        print("Running Crawler")
        self.driver.get("https://sigaa.unb.br/sigaa/")
        
        sp.go_into_extension_page(self.driver, self.env)
        
        result = ep.get_year_indicator(2023, self.driver)
        
        print(result)
        time.sleep(5)
        self.driver.quit()
        print("Ending Crawler")
        
