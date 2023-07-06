import time
import pages.extension_page as ep
import pages.sigaa_pages as sp 
import database_generator.database_generator as dg

from selenium import webdriver # pip install selenium
from dotenv import dotenv_values # pip install python-dotenv
from output_format import *

class MiniCrawler:
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
                        centralize("Nenhum navegador encontrado")
                        navegador = None
                        exit(1)

        self.env = dotenv_values(".env")
    
    def instance_login(self):
        sp._login_into_sigaa(self.driver, self.env)
        
        if self.driver.current_url in pages_valid['discente']:
            perfil = "discente"    
            sp.go_into_extension_page(self.driver, self.env) # Navegar para a página de extensão
            input("===")
        elif self.driver.current_url in pages_valid['docente']: 
            perfil = "docente"
            input(("Ao chegar na pagina de extensao aperte enter").center(SIZE_TERMINAL))

        return perfil
    
    def navigate_to_extension_page(self, perfil):
        if perfil == 'discente':
            sp.go_into_extension_page(self.driver, self.env) # Navegar para a página de extensão
        elif perfil == 'docente':
            pass

    def run(self):
        self.driver.get("https://sigaa.unb.br/sigaa/")
        perfil = self.instance_login()
        self.navigate_to_extension_page(perfil)

        dg.get_every_extension_activity_from_years(self.year, self.year, self.driver, self.perfil)

        self.driver.quit()

class Crawler:
    def __init__(self):
        # try: 
        #     self.driver = webdriver.Safari()
        #     navegador = "safari"    
        # except Exception as e:
        #     try:
        #         self.driver = webdriver.Chrome()
        #         navegador = "chrome"
        #     except Exception as e:
        #         try: 
        #             self.driver = webdriver.Edge()
        #             navegador = "edge"
        #         except Exception as e:
        #             try: 
        #                 self.driver = webdriver.Firefox()
        #                 navegador = "firefox"
        #             except Exception as e:
        #                 centralize("Nenhum navegador encontrado")
        #                 navegador = None
        #                 exit(1)

        self.env = dotenv_values(".env")

        # centralize(f'Navegador Usado: {RIGHT_ARROW} {navegador.capitalize()} {LEFT_ARROW}')
    
   
    def run(self):
        centralize(f'{RIGHT_ARROW} Running Crawler {LEFT_ARROW}')

        driver_2020 = MiniCrawler()
        driver_2020.year = 2020
        driver_2020.run()

        # self.driver.get("https://sigaa.unb.br/sigaa/")
        
        # perfil = "discente"

        # print(SEPARATOR)
        # input("Aperte enter para continuar".center(SIZE_TERMINAL))
        # start_year = 2020
        # end_year = 2020

        # driver_2020 = webdriver.Chrome()
        # driver_2020.get("https://sigaa.unb.br/sigaa/extensao/Atividade/lista.jsf")
        # driver_2020.execute_cdp_cmd('Network.setCookies', {'cookies': self.driver.get_cookies()})

        # self.driver.quit()
        centralize(f'{RIGHT_ARROW} Ending Crawler {LEFT_ARROW}')