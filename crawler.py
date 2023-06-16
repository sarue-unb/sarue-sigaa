import time
import pages.extension_page as ep
import pages.sigaa_pages as sp 
import database_generator.database_generator as dg

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
      
        input("Ao chegar na pagina de extensao aperte enter")

        dg.get_every_extension_activity_from_years(2023,2023,self.driver)
        
        # self.driver.quit()
        print(RIGHT_ARROW + "Ending Crawler")