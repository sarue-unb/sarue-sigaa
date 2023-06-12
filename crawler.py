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
            self.driver = webdriver.Safari()
            navegador = "safari"    
        except Exception as e:
            try:
                self.driver = webdriver.Chrome()
                navegador = "chrome"
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

        print("NAVEGADOR USADO:" + RIGHT_ARROW + navegador.capitalize() + LEFT_ARROW)                
    
    def run(self):
        print(HASH + "Running Crawler" + HASH)

        self.driver.get("https://sigaa.unb.br/sigaa/")
      
        ### LOGIN     
        self.driver.implicitly_wait(20) # Espera 20 segundos para o usuário se autenticar.

        ### Aqui, posso ver qual o perfil do usuário
        while (self.driver.current_url not in pages_valid['discente'] and self.driver.current_url not in pages_valid['docente']):
            print(RIGHT_ARROW + "Not logged in yet" + LEFT_ARROW) 
            time.sleep(5) # Usado para não poluir o console com mensagens de "Not logged in yet"
        
        if self.driver.current_url in pages_valid['discente']:
            print(RIGHT_ARROW + "Logged in as discente"  + LEFT_ARROW)
            perfil = "discente"
            ### Navegar para a página de extensão
            sp.go_into_extension_page(self.driver, self.env)
            ### 
        elif self.driver.current_url in pages_valid['docente']: 
            print(RIGHT_ARROW + "Logged in as docente" + LEFT_ARROW)
            perfil = "docente"
        ###

        # input("Ao chegar na pagina de extensao aperte enter")
        
        dg.get_every_extension_activity_from_years(2020,2023,self.driver)
        
        time.sleep(20)
        # self.driver.quit()
        print(RIGHT_ARROW + "Ending Crawler")