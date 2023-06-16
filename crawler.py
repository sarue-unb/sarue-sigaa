import time
import pages.extension_page as ep
import pages.sigaa_pages as sp 
import database_generator.database_generator as dg

from selenium import webdriver # pip install selenium
from dotenv import dotenv_values # pip install python-dotenv
from output_format import *

class Crawler:
    def __init__(self):
        try:
            self.driver = webdriver.Chrome()
            navegador = "chrome"
        except Exception as e:
            try: 
                self.driver = webdriver.Safari()
                navegador = "safari"    
            except Exception as e:
                try: 
                    self.driver = webdriver.Edge()
                    navegador = "edge"
                except Exception as e:
                    try: 
                        self.driver = webdriver.Firefox()
                        navegador = "firefox"
                    except Exception as e:
                        print("Nenhum navegador padrão encontrado.")
                        navegador = None
                        exit(1)
        
        self.env = dotenv_values(".env")
        
        print("NAVEGADOR USADO:" + RIGHT_ARROW + navegador + LEFT_ARROW)                 
    
    def run(self):
        print(HASH + "Running Crawler" + HASH)

        self.driver.get("https://sigaa.unb.br/sigaa/")
      
        input("Ao chegar na pagina de extensao aperte enter")

        dg.get_every_extension_activity_from_years(2023,2023,self.driver)
        
        # self.driver.quit()
        print(RIGHT_ARROW + "Ending Crawler")