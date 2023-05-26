import time
import pages.extension_page as ep
import pages.sigaa_pages as sp 
import components.selection_components as dc
from selenium import webdriver # pip install selenium
from dotenv import dotenv_values # pip install python-dotenv
from output_format import *

class Crawler:
    def __init__(self):
        # Aqui pode ser selecionado pelo usuário qual navegador ele que usar.
        # Importante: Usuarios MacOS normalmente só possuem Safari.
        # ou até mesmo verificar se o driver retorna algo.

        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox() 
        # self.driver = webdriver.Edge()
        # self.driver = webdriver.Safari()
        
        self.env = dotenv_values(".env")
    
    def run(self):
        print(HASH + "Running Crawler" + HASH)

        self.driver.get("https://sigaa.unb.br/sigaa/")
      
        self.driver.implicitly_wait(20) # Espera 20 segundos para o usuário se autenticar.

        while (self.driver.current_url not in pages_valid['discente']):
            print(RIGHT_ARROW + "Not logged in yet" + LEFT_ARROW) 
            time.sleep(5) # Usado para não poluir o console com mensagens de "Not logged in yet"
        
        print(RIGHT_ARROW + "Login successful" + LEFT_ARROW)
      
        # Adicionar pular tela de aviso

        sp.go_into_extension_page(self.driver, self.env)
        
        total_actions = ep.get_total_actions_indicator(self.driver)

        # result = ep.get_year_indicator(2023, self.driver)
        # result = ep.get_action_by_year_indicator(2023, 4, self.driver)
        
        print(total_actions)
        
        time.sleep(20)
        # self.driver.quit()
        print(RIGHT_ARROW + "Ending Crawler")