import time
import pages.extension_page as ep
import pages.sigaa_pages as sp 
import components.selection_components as dc
from selenium import webdriver # pip install selenium
from dotenv import dotenv_values # pip install python-dotenv


class Crawler:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.env = dotenv_values(".env")
    
    def run(self):
        print("Running Crawler")
        self.driver.get("https://sigaa.unb.br/sigaa/")
        
        sp.go_into_extension_page(self.driver, self.env)
        
        result = ep.get_action_by_year_indicator(2023, 4, self.driver)
        
        print(result)
        
        
        time.sleep(5)
        self.driver.quit()
        print("Ending Crawler")