import pages.sigaa_pages as sp 
import components.selection_components as sc
from dotenv import dotenv_values # pip install python-dotenv
from selenium import webdriver # pip install selenium
from config.output_format import *
from config.url_descryption import *
from selenium.common.exceptions import StaleElementReferenceException

class CrawlerAuth:
    def __init__(self):
        try:
            self.chrome_options = webdriver.ChromeOptions()
            self.chrome_options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
            self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

            self.driver = webdriver.Chrome(options=self.chrome_options)
            self.navegador = "chrome"
        except Exception:
            try:
                self.driver = webdriver.Edge()
                self.navegador = "edge"
            except Exception:
                try:
                    self.driver = webdriver.Firefox()
                    self.navegador = "firefox"
                except Exception:
                    try:
                        self.driver = webdriver.Safari()
                        self.navegador = "safari"
                    except Exception:
                        centralize("Nenhum navegador encontrado")
                        self.navegador = None
                        exit(1)

        centralize(f'Navegador Usado: {RIGHT_ARROW} {self.navegador.capitalize()} {LEFT_ARROW}')

    def instance_login(self):
        self.driver.implicitly_wait(20)

        username = sc.get_element_by_xpath(sp.USERNAME_XPATH, self.driver)
        password = sc.get_element_by_xpath(sp.PASSWORD_XPATH, self.driver)
        
        while (self.driver.current_url not in pages_valid['discente'] and self.driver.current_url not in pages_valid['docente']):
            username = sc.get_element_by_xpath(sp.USERNAME_XPATH, self.driver)
            password = sc.get_element_by_xpath(sp.PASSWORD_XPATH, self.driver)
            
            try:
                username = username.get_attribute("value")
                password = password.get_attribute("value")
            except StaleElementReferenceException:
                time.sleep(0.2)
                pass
            
            time.sleep(0.2)

        return username, password

    def run(self) -> tuple[str, str, str]:
        self.driver.get(LOGIN_PAGE)
        username, password = self.instance_login()
        self.driver.quit()
        return username, password